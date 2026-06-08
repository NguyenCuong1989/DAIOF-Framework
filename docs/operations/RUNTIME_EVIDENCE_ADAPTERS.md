# Runtime Evidence Adapter Layer

## Purpose

`runtime_topology.json` describes what must exist. It does not prove that a
runtime exists, is reachable, has the expected identity, or is healthy.

The evidence adapter layer converts observations into a short-lived, signed
`runtime_reality` attestation:

```text
Runtime endpoint/file
  -> bounded probe
  -> identity + version + health observation
  -> topology-bound digest
  -> HMAC signature
  -> deployment-path verification
```

No generated production attestation is committed. Runtime output is written to
`.runtime/runtime_attestation.json`, which is ignored by Git.

## Required health response

OpenClaw, Planner, Phoenix, Factory, and AXControl use `http_json` adapters. Each
health endpoint must return a JSON object containing the configured fields:

```json
{
  "identity": "openclaw_gateway",
  "version": "1.4.2",
  "status": "healthy"
}
```

The endpoint must use HTTPS. Plain HTTP is accepted only for loopback tests.
Bearer tokens may be supplied through environment variables and are never
written to the attestation.

The deployment runtime uses a local `file_json` adapter with the same payload
shape. The attestation records the file digest, not its path or full contents.

## Environment contract

| Component | Endpoint/evidence variable | Optional token |
|---|---|---|
| OpenClaw Gateway | `OPENCLAW_HEALTH_URL` | `OPENCLAW_HEALTH_TOKEN` |
| Planner Service | `PLANNER_HEALTH_URL` | `PLANNER_HEALTH_TOKEN` |
| Phoenix Council | `PHOENIX_HEALTH_URL` | `PHOENIX_HEALTH_TOKEN` |
| Factory Executor | `FACTORY_HEALTH_URL` | `FACTORY_HEALTH_TOKEN` |
| AXControl | `AXCONTROL_HEALTH_URL` | `AXCONTROL_HEALTH_TOKEN` |
| Deployment Runtime | `DEPLOYMENT_RUNTIME_EVIDENCE_FILE` | N/A |

Signing also requires:

- `RUNTIME_ATTESTATION_HMAC_KEY`: secret shared by the trusted probe and verifier.
- `RUNTIME_ATTESTATION_KEY_ID`: non-secret identifier used for rotation/audit.

## Probe

Run from a host that can observe the real runtime topology:

```bash
python tools/governance/runtime_evidence.py probe \
  --environment production \
  --output .runtime/runtime_attestation.json
```

The command always records unavailable or unverified observations when signing
configuration is valid. It exits non-zero unless every required adapter produces
healthy identity, version, reachability, and health evidence.

## Verify before deployment

```bash
python tools/governance/runtime_evidence.py verify \
  --attestation .runtime/runtime_attestation.json \
  --workflow .github/workflows/release.yml \
  --environment production
```

Verification rejects:

- missing component evidence;
- unreachable or unhealthy components;
- identity mismatch;
- missing version evidence;
- expired or future-dated evidence;
- environment mismatch;
- topology drift;
- payload tampering;
- invalid HMAC signature.

The TTL is currently 300 seconds. A previously healthy runtime therefore cannot
authorize deployment indefinitely.

## Trusted execution surface

`.github/workflows/runtime-attestation.yml` runs only on a self-hosted runner
labeled `daiof-runtime`. This is intentional: a generic GitHub-hosted runner is
not assumed to have visibility into a local-first runtime topology.

The workflow creates and verifies the attestation, then uploads it with a
seven-day retention window for audit. Successful artifact creation proves only
the observations at the attestation timestamp and environment; it does not
create a permanent health claim.

## Closure rule

A deployment objective is not closed because a workflow completed. Closure
requires all of the following:

1. topology path mapped;
2. runtime evidence complete and fresh;
3. identity/version/health verified;
4. topology digest matched;
5. attestation signature verified;
6. human approval and artifact provenance checks satisfied.
