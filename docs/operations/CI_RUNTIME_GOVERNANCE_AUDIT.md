# DAIOF/OpenClaw CI-to-Runtime Governance Baseline

## Decision

The repository must treat deployment as an evidence chain rather than a direct
`code -> test -> deploy` transition:

```text
Intent -> D&R -> THE CHOICE -> Planner -> Runtime Topology
       -> Attestation -> Deploy -> Continuous Verification
```

This baseline does **not** claim that external OpenClaw, Planner, Phoenix,
Factory, or AXControl runtimes are healthy. Their state is explicitly recorded
as `external_evidence_required` in `governance/runtime_topology.json`.

## Enforced now

1. `workflow_manifest.json` is generated deterministically from every workflow.
2. Workflow drift fails the governance check.
3. Every deploy-capable workflow must be represented in the runtime topology.
4. THE CHOICE and D&R evidence must contain the mandatory governance fields.
5. Every D&R pillar must score at least 7.0.
6. Missing deployment evidence uses a fail-closed `block` policy.
7. Workflow-generated PR approval and direct merge API calls are prohibited.
8. Human approval remains mandatory for PRs, releases, overrides, and protocol
   changes.

## Measured baseline

Run:

```bash
python tools/governance/governance_gate.py report
```

The report measures workflow count, deploy-capable workflow count, explicit
permission coverage, and commit-SHA action pinning. These are inventory metrics,
not claims of runtime health.

## Artifact ownership

| Artifact | Authority | Purpose |
|---|---|---|
| `governance/workflow_manifest.json` | Generated from GitHub Actions | Workflow inventory and drift detection |
| `governance/runtime_topology.json` | Architecture/governance owners | Runtime and deployment dependency contract |
| `governance/choice_review.json` | Human release authority | Intent, risk, justification, override policy |
| `governance/dr_review.json` | D&R reviewer | Decomposition, focal point, risk graph, pillar gate |

## Next implementation stages

### P0 — runtime evidence adapters

- OpenClaw gateway health adapter
- Planner health adapter
- Phoenix/Factory/AXControl identity and availability probes
- freshness and environment binding for all health evidence

### P1 — artifact attestation

- SBOM generation
- RIL attestation schema implementation
- provenance binding to commit, workflow run, artifact digest, and environment
- signature verification before release/publish jobs

### P1 — deployment validator

A deployment validator must reject evidence that is missing, stale, for another
commit/environment, unsigned, or schema-incompatible. Until those adapters are
implemented, `external_evidence_required` must never be translated to `healthy`.

## Human escalation

Overrides require an actor, reason, scope, expiry, and incident reference. An
override may bypass availability policy only; it may not bypass artifact origin,
identity, or signature validation.
