#!/usr/bin/env python3
"""Collect and verify runtime-reality attestations for DAIOF deployments."""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import time
import urllib.error
import urllib.request
from urllib.parse import urlparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Mapping

SCHEMA_VERSION = "1.0.0"
DEFAULT_CONFIG = Path("governance/runtime_adapters.json")
DEFAULT_TOPOLOGY = Path("governance/runtime_topology.json")
DEFAULT_OUTPUT = Path(".runtime/runtime_attestation.json")
EXTERNAL_EVIDENCE_STATE = "external_evidence_required"


class EvidenceError(ValueError):
    """Raised when runtime evidence cannot be trusted."""


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def isoformat(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def parse_timestamp(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise EvidenceError(f"{field} must be an ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise EvidenceError(f"{field} is not valid ISO-8601: {value}") from exc
    if parsed.tzinfo is None:
        raise EvidenceError(f"{field} must include a timezone")
    return parsed.astimezone(timezone.utc)


def load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise EvidenceError(f"missing JSON artifact: {path}") from exc
    except json.JSONDecodeError as exc:
        raise EvidenceError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise EvidenceError(f"JSON artifact must be an object: {path}")
    return payload


def canonical_digest(payload: Mapping[str, Any]) -> str:
    content = {
        key: value for key, value in payload.items() if key != "attestation_sha256"
    }
    if isinstance(content.get("signing"), dict):
        content["signing"] = {
            key: value
            for key, value in content["signing"].items()
            if key != "signature"
        }
    canonical = json.dumps(
        content, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def nested_value(payload: Any, dotted_path: str) -> Any:
    current = payload
    for part in dotted_path.split("."):
        if not isinstance(current, dict) or part not in current:
            raise EvidenceError(f"response field not found: {dotted_path}")
        current = current[part]
    return current


def resolve_env(name: Any, environ: Mapping[str, str]) -> str:
    if not isinstance(name, str) or not name:
        raise EvidenceError("adapter environment variable name is missing")
    value = environ.get(name, "").strip()
    if not value:
        raise EvidenceError(f"required environment variable is not set: {name}")
    return value


def fetch_http_json(
    adapter: dict[str, Any], timeout: float, environ: Mapping[str, str]
) -> tuple[dict[str, Any], dict[str, Any]]:
    url = resolve_env(adapter.get("url_env"), environ)
    parsed_url = urlparse(url)
    loopback = parsed_url.hostname in {"127.0.0.1", "::1", "localhost"}
    if parsed_url.scheme != "https" and not (parsed_url.scheme == "http" and loopback):
        raise EvidenceError(
            "HTTP runtime probes require HTTPS except for loopback testing"
        )
    headers = {"Accept": "application/json", "User-Agent": "DAIOF-Runtime-Evidence/1.0"}
    token_env = adapter.get("bearer_token_env")
    if token_env and environ.get(str(token_env), "").strip():
        headers["Authorization"] = f"Bearer {environ[str(token_env)].strip()}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
            status = int(response.status)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise EvidenceError(f"HTTP probe failed: {exc}") from exc
    if status < 200 or status >= 300:
        raise EvidenceError(f"HTTP probe returned status {status}")
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise EvidenceError("HTTP probe did not return valid UTF-8 JSON") from exc
    if not isinstance(payload, dict):
        raise EvidenceError("HTTP probe JSON must be an object")
    return payload, {
        "transport": "https" if url.startswith("https://") else "http",
        "http_status": status,
    }


def read_file_json(
    adapter: dict[str, Any], _timeout: float, environ: Mapping[str, str]
) -> tuple[dict[str, Any], dict[str, Any]]:
    path = Path(resolve_env(adapter.get("path_env"), environ)).expanduser().resolve()
    payload = load_json(path)
    return payload, {"transport": "file", "source_sha256": file_digest(path)}


ADAPTERS = {
    "http_json": fetch_http_json,
    "file_json": read_file_json,
}


def probe_component(
    component: dict[str, Any],
    timeout: float,
    environ: Mapping[str, str],
    observed_time: datetime | None = None,
) -> dict[str, Any]:
    started = time.monotonic()
    observed_at = isoformat(observed_time or utc_now())
    component_id = str(component.get("id") or "")
    adapter = component.get("adapter") or {}
    expected_identity = adapter.get("expected_identity")
    result: dict[str, Any] = {
        "id": component_id,
        "required": component.get("required") is True,
        "adapter_type": adapter.get("type"),
        "observed_at": observed_at,
        "status": "unavailable",
        "reachable": False,
        "identity": {"expected": expected_identity, "observed": None, "matches": False},
        "version": {"observed": None},
        "health": {
            "observed": None,
            "healthy_values": adapter.get("healthy_values", []),
            "matches": False,
        },
        "evidence": {},
        "error": None,
    }
    try:
        adapter_type = adapter.get("type")
        if adapter_type not in ADAPTERS:
            raise EvidenceError(f"unsupported adapter type: {adapter_type}")
        payload, transport = ADAPTERS[adapter_type](adapter, timeout, environ)
        identity = nested_value(payload, str(adapter.get("identity_path")))
        version = nested_value(payload, str(adapter.get("version_path")))
        health = nested_value(payload, str(adapter.get("health_path")))
        healthy_values = {
            str(item).lower() for item in adapter.get("healthy_values", [])
        }
        identity_matches = str(identity) == str(expected_identity)
        health_matches = str(health).lower() in healthy_values
        version_present = bool(str(version).strip())
        result.update(
            {
                "reachable": True,
                "identity": {
                    "expected": expected_identity,
                    "observed": identity,
                    "matches": identity_matches,
                },
                "version": {"observed": version},
                "health": {
                    "observed": health,
                    "healthy_values": adapter.get("healthy_values", []),
                    "matches": health_matches,
                },
                "evidence": transport,
                "status": (
                    "healthy"
                    if identity_matches and health_matches and version_present
                    else "unverified"
                ),
            }
        )
        if not identity_matches:
            result["error"] = "identity mismatch"
        elif not version_present:
            result["error"] = "version evidence is empty"
        elif not health_matches:
            result["error"] = "health value is not accepted"
    except EvidenceError as exc:
        result["error"] = str(exc)
    result["latency_ms"] = round((time.monotonic() - started) * 1000, 3)
    return result


def external_component_ids(topology: dict[str, Any]) -> set[str]:
    return {
        str(component.get("id"))
        for component in topology.get("components", [])
        if isinstance(component, dict)
        and component.get("evidence_state") == EXTERNAL_EVIDENCE_STATE
    }


def build_attestation(
    config_path: Path,
    topology_path: Path,
    environment: str,
    environ: Mapping[str, str] | None = None,
    now: datetime | None = None,
) -> dict[str, Any]:
    config = load_json(config_path)
    topology = load_json(topology_path)
    if config.get("schema_version") != SCHEMA_VERSION:
        raise EvidenceError("runtime adapter config schema_version mismatch")
    if topology.get("schema_version") != SCHEMA_VERSION:
        raise EvidenceError("runtime topology schema_version mismatch")
    if not environment.strip():
        raise EvidenceError("environment must not be empty")

    topology_external = external_component_ids(topology)
    configured = {
        str(item.get("id"))
        for item in config.get("components", [])
        if isinstance(item, dict)
    }
    missing_adapters = sorted(topology_external - configured)
    if missing_adapters:
        raise EvidenceError(
            f"external runtime components lack adapters: {', '.join(missing_adapters)}"
        )

    timeout = float(config.get("default_timeout_seconds", 3.0))
    ttl = int(config.get("ttl_seconds", 300))
    generated_at = now or utc_now()
    env = environ if environ is not None else os.environ
    signing_key = resolve_env(config.get("attestation_hmac_key_env"), env)
    signing_key_id = resolve_env(config.get("attestation_key_id_env"), env)
    observations = [
        probe_component(item, timeout, env, observed_time=generated_at)
        for item in config.get("components", [])
    ]
    required = [item for item in observations if item["required"]]
    verified = bool(required) and all(item["status"] == "healthy" for item in required)
    attestation: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "attestation_type": "runtime_reality",
        "environment": environment,
        "generated_at": isoformat(generated_at),
        "expires_at": isoformat(generated_at + timedelta(seconds=ttl)),
        "topology_sha256": file_digest(topology_path),
        "adapter_config_sha256": file_digest(config_path),
        "components": observations,
        "summary": {
            "required_count": len(required),
            "healthy_count": sum(item["status"] == "healthy" for item in required),
            "verified": verified,
        },
    }
    attestation["signing"] = {
        "algorithm": "HMAC-SHA256",
        "key_id": signing_key_id,
    }
    attestation["attestation_sha256"] = canonical_digest(attestation)
    attestation["signing"]["signature"] = hmac.new(
        signing_key.encode("utf-8"),
        attestation["attestation_sha256"].encode("ascii"),
        hashlib.sha256,
    ).hexdigest()
    return attestation


def deployment_path(topology: dict[str, Any], workflow: str) -> dict[str, Any]:
    for path in topology.get("deployment_paths", []):
        if isinstance(path, dict) and path.get("workflow") == workflow:
            return path
    raise EvidenceError(f"workflow is not mapped in runtime topology: {workflow}")


def verify_attestation(
    attestation: dict[str, Any],
    topology_path: Path,
    workflow: str,
    environment: str,
    now: datetime | None = None,
    signing_key: str | None = None,
    signing_key_id: str | None = None,
    config_path: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    topology = load_json(topology_path)
    if attestation.get("schema_version") != SCHEMA_VERSION:
        errors.append("runtime attestation schema_version mismatch")
    if attestation.get("attestation_type") != "runtime_reality":
        errors.append("runtime attestation type mismatch")
    if attestation.get("attestation_sha256") != canonical_digest(attestation):
        errors.append("runtime attestation digest mismatch")
    signing = attestation.get("signing") or {}
    if signing.get("algorithm") != "HMAC-SHA256":
        errors.append("runtime attestation signing algorithm mismatch")
    if signing_key_id and signing.get("key_id") != signing_key_id:
        errors.append("runtime attestation signing key identity mismatch")
    if not signing_key:
        errors.append("runtime attestation signing key is unavailable")
    else:
        expected_signature = hmac.new(
            signing_key.encode("utf-8"),
            str(attestation.get("attestation_sha256") or "").encode("ascii"),
            hashlib.sha256,
        ).hexdigest()
        if not hmac.compare_digest(
            str(signing.get("signature") or ""), expected_signature
        ):
            errors.append("runtime attestation signature mismatch")
    if attestation.get("topology_sha256") != file_digest(topology_path):
        errors.append("runtime attestation topology binding mismatch")
    if config_path is not None and attestation.get(
        "adapter_config_sha256"
    ) != file_digest(config_path):
        errors.append("runtime attestation adapter configuration binding mismatch")
    if attestation.get("environment") != environment:
        errors.append("runtime attestation environment mismatch")

    current = now or utc_now()
    generated_at: datetime | None = None
    try:
        generated_at = parse_timestamp(attestation.get("generated_at"), "generated_at")
        expires_at = parse_timestamp(attestation.get("expires_at"), "expires_at")
        if generated_at > current + timedelta(seconds=30):
            errors.append("runtime attestation was generated in the future")
        if expires_at <= current:
            errors.append("runtime attestation is stale")
        if expires_at <= generated_at:
            errors.append("runtime attestation expiry must be after generation")
    except EvidenceError as exc:
        errors.append(str(exc))

    try:
        path = deployment_path(topology, workflow)
    except EvidenceError as exc:
        errors.append(str(exc))
        return errors
    external = external_component_ids(topology)
    required_external = set(path.get("required_components", [])) & external
    observations = {
        str(item.get("id")): item
        for item in attestation.get("components", [])
        if isinstance(item, dict) and item.get("id")
    }
    for component_id in sorted(required_external):
        observation = observations.get(component_id)
        if observation is None:
            errors.append(
                f"runtime evidence missing for required component: {component_id}"
            )
            continue
        try:
            observed_at = parse_timestamp(
                observation.get("observed_at"), f"{component_id}.observed_at"
            )
            if generated_at is not None and not (
                generated_at - timedelta(seconds=30)
                <= observed_at
                <= generated_at + timedelta(seconds=30)
            ):
                errors.append(
                    f"runtime observation timestamp is not bound to attestation: {component_id}"
                )
        except EvidenceError as exc:
            errors.append(str(exc))
        if observation.get("status") != "healthy":
            errors.append(f"runtime component is not verified healthy: {component_id}")
        if observation.get("reachable") is not True:
            errors.append(f"runtime component is not reachable: {component_id}")
        if (observation.get("identity") or {}).get("matches") is not True:
            errors.append(f"runtime identity is not verified: {component_id}")
        if not str((observation.get("version") or {}).get("observed") or "").strip():
            errors.append(f"runtime version evidence is missing: {component_id}")
        if (observation.get("health") or {}).get("matches") is not True:
            errors.append(f"runtime health evidence is not accepted: {component_id}")

    if (
        path.get("missing_evidence_policy") == "block"
        and required_external
        and not required_external.issubset(observations)
    ):
        errors.append(
            "deployment path blocks because required runtime evidence is incomplete"
        )
    if (attestation.get("summary") or {}).get("verified") is not True:
        errors.append("runtime attestation summary is not verified")
    return errors


def write_attestation(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    probe = subparsers.add_parser(
        "probe", help="Probe configured runtimes and create an attestation"
    )
    probe.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    probe.add_argument("--topology", type=Path, default=DEFAULT_TOPOLOGY)
    probe.add_argument("--environment", required=True)
    probe.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)

    verify = subparsers.add_parser(
        "verify", help="Verify an attestation for one deployment workflow"
    )
    verify.add_argument("--attestation", type=Path, required=True)
    verify.add_argument("--topology", type=Path, default=DEFAULT_TOPOLOGY)
    verify.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    verify.add_argument("--workflow", required=True)
    verify.add_argument("--environment", required=True)
    verify.add_argument("--signing-key-env", default="RUNTIME_ATTESTATION_HMAC_KEY")
    verify.add_argument("--signing-key-id-env", default="RUNTIME_ATTESTATION_KEY_ID")

    args = parser.parse_args()
    try:
        if args.command == "probe":
            payload = build_attestation(args.config, args.topology, args.environment)
            write_attestation(args.output, payload)
            print(json.dumps(payload["summary"], sort_keys=True))
            return 0 if payload["summary"]["verified"] else 1
        payload = load_json(args.attestation)
        errors = verify_attestation(
            payload,
            args.topology,
            args.workflow,
            args.environment,
            signing_key=os.environ.get(args.signing_key_env),
            signing_key_id=os.environ.get(args.signing_key_id_env),
            config_path=args.config,
        )
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("Runtime attestation verified")
        return 0
    except EvidenceError as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
