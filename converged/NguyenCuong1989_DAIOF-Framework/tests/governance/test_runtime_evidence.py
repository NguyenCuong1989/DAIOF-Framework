import json
import threading
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from tools.governance.runtime_evidence import (
    build_attestation,
    canonical_digest,
    verify_attestation,
)


@contextmanager
def health_server(payload):
    encoded = json.dumps(payload).encode("utf-8")

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

        def log_message(self, _format, *_args):
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/health"
    finally:
        server.shutdown()
        thread.join(timeout=2)
        server.server_close()


def write_contract(tmp_path: Path, adapter_type="http_json"):
    topology = {
        "schema_version": "1.0.0",
        "components": [
            {"id": "service", "evidence_state": "external_evidence_required"}
        ],
        "deployment_paths": [
            {
                "workflow": ".github/workflows/release.yml",
                "required_components": ["service"],
                "missing_evidence_policy": "block",
            }
        ],
    }
    adapter = {
        "type": adapter_type,
        "identity_path": "identity",
        "expected_identity": "service",
        "version_path": "version",
        "health_path": "status",
        "healthy_values": ["healthy"],
    }
    if adapter_type == "http_json":
        adapter["url_env"] = "SERVICE_URL"
        adapter["bearer_token_env"] = "SERVICE_TOKEN"
    else:
        adapter["path_env"] = "SERVICE_FILE"
    config = {
        "schema_version": "1.0.0",
        "default_timeout_seconds": 1.0,
        "ttl_seconds": 60,
        "attestation_hmac_key_env": "ATTESTATION_KEY",
        "attestation_key_id_env": "ATTESTATION_KEY_ID",
        "components": [{"id": "service", "required": True, "adapter": adapter}],
    }
    topology_path = tmp_path / "topology.json"
    config_path = tmp_path / "adapters.json"
    topology_path.write_text(json.dumps(topology))
    config_path.write_text(json.dumps(config))
    return config_path, topology_path


def test_http_probe_creates_verifiable_runtime_reality_attestation(tmp_path):
    config, topology = write_contract(tmp_path)
    now = datetime(2026, 6, 8, 12, 0, tzinfo=timezone.utc)
    with health_server(
        {"identity": "service", "version": "2.4.1", "status": "healthy"}
    ) as url:
        attestation = build_attestation(
            config,
            topology,
            "production",
            environ={
                "SERVICE_URL": url,
                "SERVICE_TOKEN": "not-emitted",
                "ATTESTATION_KEY": "test-signing-secret",
                "ATTESTATION_KEY_ID": "test-key",
            },
            now=now,
        )

    assert attestation["summary"] == {
        "required_count": 1,
        "healthy_count": 1,
        "verified": True,
    }
    assert attestation["components"][0]["identity"]["observed"] == "service"
    assert attestation["components"][0]["version"]["observed"] == "2.4.1"
    assert "not-emitted" not in json.dumps(attestation)
    assert (
        verify_attestation(
            attestation,
            topology,
            ".github/workflows/release.yml",
            "production",
            now=now + timedelta(seconds=30),
            signing_key="test-signing-secret",
            signing_key_id="test-key",
            config_path=config,
        )
        == []
    )


def test_identity_mismatch_is_observed_but_not_verified(tmp_path):
    config, topology = write_contract(tmp_path)
    with health_server(
        {"identity": "impostor", "version": "1.0", "status": "healthy"}
    ) as url:
        attestation = build_attestation(
            config,
            topology,
            "production",
            environ={
                "SERVICE_URL": url,
                "ATTESTATION_KEY": "test-signing-secret",
                "ATTESTATION_KEY_ID": "test-key",
            },
        )

    observation = attestation["components"][0]
    assert observation["reachable"] is True
    assert observation["status"] == "unverified"
    assert observation["identity"]["matches"] is False
    errors = verify_attestation(
        attestation,
        topology,
        ".github/workflows/release.yml",
        "production",
        signing_key="test-signing-secret",
        signing_key_id="test-key",
        config_path=config,
    )
    assert any("identity is not verified" in error for error in errors)


def test_missing_endpoint_is_unavailable_not_healthy(tmp_path):
    config, topology = write_contract(tmp_path)
    attestation = build_attestation(
        config,
        topology,
        "production",
        environ={
            "ATTESTATION_KEY": "test-signing-secret",
            "ATTESTATION_KEY_ID": "test-key",
        },
    )
    observation = attestation["components"][0]
    assert observation["status"] == "unavailable"
    assert observation["reachable"] is False
    assert "SERVICE_URL" in observation["error"]
    assert attestation["summary"]["verified"] is False


def test_file_adapter_records_source_digest(tmp_path):
    config, topology = write_contract(tmp_path, adapter_type="file_json")
    evidence_file = tmp_path / "runtime.json"
    evidence_file.write_text(
        json.dumps({"identity": "service", "version": "7", "status": "healthy"})
    )
    attestation = build_attestation(
        config,
        topology,
        "local",
        environ={
            "SERVICE_FILE": str(evidence_file),
            "ATTESTATION_KEY": "test-signing-secret",
            "ATTESTATION_KEY_ID": "test-key",
        },
    )
    observation = attestation["components"][0]
    assert observation["status"] == "healthy"
    assert len(observation["evidence"]["source_sha256"]) == 64


def test_stale_attestation_is_rejected(tmp_path):
    config, topology = write_contract(tmp_path)
    generated = datetime(2026, 6, 8, 12, 0, tzinfo=timezone.utc)
    with health_server(
        {"identity": "service", "version": "1", "status": "healthy"}
    ) as url:
        attestation = build_attestation(
            config,
            topology,
            "production",
            environ={
                "SERVICE_URL": url,
                "ATTESTATION_KEY": "test-signing-secret",
                "ATTESTATION_KEY_ID": "test-key",
            },
            now=generated,
        )
    errors = verify_attestation(
        attestation,
        topology,
        ".github/workflows/release.yml",
        "production",
        now=generated + timedelta(seconds=61),
        signing_key="test-signing-secret",
        signing_key_id="test-key",
        config_path=config,
    )
    assert "runtime attestation is stale" in errors


def test_tampering_and_topology_drift_are_rejected(tmp_path):
    config, topology = write_contract(tmp_path)
    with health_server(
        {"identity": "service", "version": "1", "status": "healthy"}
    ) as url:
        attestation = build_attestation(
            config,
            topology,
            "production",
            environ={
                "SERVICE_URL": url,
                "ATTESTATION_KEY": "test-signing-secret",
                "ATTESTATION_KEY_ID": "test-key",
            },
        )
    attestation["components"][0]["version"]["observed"] = "tampered"
    assert any(
        "digest mismatch" in error
        for error in verify_attestation(
            attestation,
            topology,
            ".github/workflows/release.yml",
            "production",
            signing_key="test-signing-secret",
            signing_key_id="test-key",
            config_path=config,
        )
    )

    attestation["attestation_sha256"] = canonical_digest(attestation)
    topology.write_text(topology.read_text() + "\n")
    assert any(
        "topology binding mismatch" in error
        for error in verify_attestation(
            attestation,
            topology,
            ".github/workflows/release.yml",
            "production",
            signing_key="test-signing-secret",
            signing_key_id="test-key",
            config_path=config,
        )
    )


def test_signature_key_identity_and_config_binding_are_enforced(tmp_path):
    config, topology = write_contract(tmp_path)
    with health_server(
        {"identity": "service", "version": "1", "status": "healthy"}
    ) as url:
        attestation = build_attestation(
            config,
            topology,
            "production",
            environ={
                "SERVICE_URL": url,
                "ATTESTATION_KEY": "test-signing-secret",
                "ATTESTATION_KEY_ID": "test-key",
            },
        )

    wrong_key_errors = verify_attestation(
        attestation,
        topology,
        ".github/workflows/release.yml",
        "production",
        signing_key="wrong-secret",
        signing_key_id="test-key",
        config_path=config,
    )
    assert "runtime attestation signature mismatch" in wrong_key_errors

    wrong_id_errors = verify_attestation(
        attestation,
        topology,
        ".github/workflows/release.yml",
        "production",
        signing_key="test-signing-secret",
        signing_key_id="rotated-key",
        config_path=config,
    )
    assert "runtime attestation signing key identity mismatch" in wrong_id_errors

    config.write_text(config.read_text() + "\n")
    drift_errors = verify_attestation(
        attestation,
        topology,
        ".github/workflows/release.yml",
        "production",
        signing_key="test-signing-secret",
        signing_key_id="test-key",
        config_path=config,
    )
    assert "runtime attestation adapter configuration binding mismatch" in drift_errors
