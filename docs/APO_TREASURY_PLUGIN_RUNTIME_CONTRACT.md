# APΩ Treasury Plugin — Runtime Contract

This document turns the product contract into an executable-facing protocol. The plugin is a projection/orchestration layer; Canon remains authoritative.

## 1. Envelope

Every command is processed as:

`request → normalize → authority check → state snapshot → evidence evaluation → gate evaluation → finite action → receipt`

No step may infer authority from UI state, model confidence, credentials, or network availability.

## 2. Command envelope

```json
{
  "request_id": "deterministic-or-runtime-id",
  "command": "inspect_candidate",
  "subject_id": "candidate-001",
  "mode": "simulation",
  "canon_sha256": "7e0c0643642958ad3a2bb778be5f82f7dbf6641afc9eb17af8ee0577609cebcc",
  "observed_at": "ISO-8601",
  "actor": "operator"
}
```

`canon_sha256` must be verified against the loaded Canon manifest before any decision-capable operation.

## 3. Agent jurisdiction

| Agent | Reads | Writes | May authorize capital? |
|---|---|---|---|
| Sensing | observations, market state | observations, deltas | No |
| Evidence | observations, candidates | evidence records | No |
| Candidate | deltas, evidence | candidate lifecycle | No |
| Gate | state, evidence, risk | gate verdicts | No; only evaluates |
| Treasury | capital state, approved actions | ledger proposal | No; subject to gate |
| Execution Safety | mode, gates, exit path | execution admission | Only within configured authority |
| Evolution | receipts, attribution | N-Factor/evolution state | No |

## 4. Eligibility separation

For candidate `i` at time `t`:

- critical unknown → `capital_eligibility = 0`
- solvable, decision-relevant unknown → `research_eligibility = 1`
- research eligibility never implies capital eligibility
- `WAIT_FOR_PROOF` is represented as a research/evidence action, never as a terminal action

## 5. Gate result

```json
{
  "candidate_id": "candidate-001",
  "gates": {
    "causal": "PASS",
    "differential": "PASS",
    "risk": "PASS",
    "mobility": "PASS",
    "execution": "BLOCK"
  },
  "verdict": "RESEARCH_ONLY",
  "reasons": ["execution mode is paper-only"]
}
```

A blocked gate must expose a machine-readable reason code and human-readable explanation.

## 6. Finite action tuple

An admissible decision is always a tuple:

`(capital_action, evidence_action, universe_action)`

Examples:

- `(HOLD_CASH, VERIFY, KEEP_ACTIVE)`
- `(ZERO, RESEARCH_WITH_BUDGET, KEEP_ACTIVE)`
- `(ACT_SMALL, MONITOR, KEEP_ACTIVE)`
- `(EXIT, REFRESH, ARCHIVE)`

The plugin must reject malformed or empty action tuples.

## 7. Execution modes

`simulation` and `paper` are safe default modes. `read_only_live` may ingest external state but cannot mutate financial state. `live_capable` remains denied unless all runtime admission conditions are explicitly satisfied.

No UI control may directly invoke a live-capable operation without a validated execution admission receipt.

## 8. Receipt

Every decision-capable operation emits a receipt containing:

- request id
- Canon hash
- state snapshot id
- evidence ids
- gate results
- selected finite action
- execution mode
- result/attribution when executed
- timestamp
- failure/degradation code when applicable

Receipts are append-only from the plugin perspective.

## 9. Fail-closed rules

If Canon identity, state integrity, evidence provenance, gate result, execution mode, or exit path is undefined, the operation cannot escalate authority. It must return a deterministic blocked/degraded result.

## 10. Operator command surface

Supported initial commands:

`scan_state`, `sense_changes`, `show_anomalies`, `show_candidates`, `inspect_candidate`, `audit_gates`, `show_admissible_actions`, `run_simulation`, `run_paper`, `replay_decision`, `show_nfactor`, `audit_capital_block`.

All commands are read-only except explicit simulation/paper actions, and none may bypass the Canon kernel.
