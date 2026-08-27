# APΩ Treasury Plugin — Product Specification

## Status

Design/implementation contract for the APΩ PERSONAL_FINANCIAL_MACHINE / SURVIVAL_TREASURY operator surface.

The plugin is an interface and orchestration layer. It is not the canonical authority and must not redefine financial-machine semantics.

## Root invariant

`PHẢI SỐNG` remains the root law. Capital is fuel, not the machine.

The product surface must expose the machine's state, evidence, gates, actions, execution result, and learning loop without hiding rejection conditions.

## System boundary

```text
APΩ Canon
  ↓
Canonical Domain Kernel
  ↓
Ω Orchestrator
  ├── Sensing Agent
  ├── Evidence Agent
  ├── Candidate Agent
  ├── Gate Agent
  ├── Treasury Agent
  ├── Execution-Safety Agent
  └── Evolution Agent
  ↓
Plugin/API surface
  ├── ChatGPT operator surface
  └── Web cockpit
```

## Agent jurisdiction

Each agent is bounded by an explicit contract:

- input contract
- state read/write boundary
- authority boundary
- admissible actions
- evidence requirements
- output contract
- failure policy

Agents cooperate through the orchestrator. No individual agent may grant itself authority or bypass a canonical gate.

## Core product surfaces

### Ω Core

Displays the current machine state:

- Survival
- Mobility
- Maneuver
- Strike
- Strategic Reserve
- Risk
- Evidence
- Capability

### Reality / Sensing

Shows observations, state deltas, anomalies, sensing freshness, and unresolved questions.

### Candidate Universe

Candidates are outputs of sensing/reasoning, not assumptions. A candidate may remain research-eligible even when capital-ineligible.

### Gate Inspector

For every decision, expose gate-level status and reason:

- causal
- differential
- risk
- mobility
- execution

Never reduce a rejected action to an opaque `REJECTED` label.

### Action Field

Represent the three action domains independently:

- capital: HOLD_CASH, ALLOCATE, ACT_SMALL, SCALE, REDUCE, EXIT, ZERO
- evidence: MONITOR, RESEARCH_WITH_BUDGET, VERIFY, FALSIFY, REFRESH
- universe: KEEP_ACTIVE, PROMOTE, DEMOTE, ARCHIVE, REOPEN

`WAIT_FOR_PROOF` is never a terminal state.

### Execution Safety

Default modes:

1. Simulation
2. Read-only live data
3. Paper execution
4. Live-capable

Live execution remains disabled by default and requires explicit admission. The plugin must never infer live authority from environment, credentials, or UI state.

### Evolution

After every finite action, expose:

`Result → Attribution → N-Factor → Exploit/Explore → Resource Migration → State Improvement`

The product must show what the machine learned, not only financial outcome.

## UX principles

- command-center rather than conventional fintech dashboard
- high information density without decorative card overload
- state transitions are visually explicit
- rejection and uncertainty remain visible
- no gamification of risk
- no accidental live-action affordance
- responsive and keyboard accessible
- deterministic seeded simulation for demonstrations and tests

## Safety invariants

1. Critical unknowns block capital deployment.
2. Decision-relevant solvable unknowns may enable research.
3. No admissible action set may collapse into an implicit terminal wait state.
4. Plugin output cannot mutate canonical rules.
5. Live execution is fail-closed.
6. Every execution-capable action must have an observable exit path.
7. UI state is never authority state.
8. Every displayed decision should be traceable to evidence and gate results.

## Initial operator commands

- `scan state`
- `sense changes`
- `show anomalies`
- `show candidates`
- `inspect candidate <id>`
- `audit gates <id>`
- `show admissible actions <id>`
- `run simulation <id>`
- `replay decision <id>`
- `show N-Factor evolution`
- `audit why capital is blocked`

## Acceptance criteria

The product is not considered complete until:

- domain semantics are represented without contradiction;
- capital/research eligibility are visibly separated;
- gate explanations are inspectable;
- fail-closed behavior is testable;
- simulation/paper flows work without external financial execution;
- state persists locally for the operator prototype;
- accessibility and responsive behavior are verified;
- typecheck/tests/build pass for the implementation;
- the product can be extended to a ChatGPT App without changing canonical semantics.
