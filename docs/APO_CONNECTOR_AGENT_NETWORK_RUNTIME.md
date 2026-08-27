# APΩ CONNECTOR CAPABILITY MAP → AGENT NETWORK RUNTIME

## Root Law

`PHẢI SỐNG` is the highest constraint. D&R is the sole execution protocol: Deconstruct → Focal Point → Re-architecture.

## Capability substrate

The connector layer is modeled as 11 capability domains:

`K Knowledge`, `D Data`, `C Code`, `R Runtime`, `Dsg Design`, `M Media`, `Com Communication`, `F Finance`, `Res Research`, `Sec Security`, `Dep Deployment`.

A connector is not merely an app:

`Connector = Interface + Capability + Authority + Boundary + Evidence`

## Four-phase runtime

### HÔ PHONG HOÁN VŨ — Capability Control

`Intent/Event → Capability Discovery → Routing → Network Execution`

Discovery selects the minimum capability and authority needed for an intent. Over-privilege is rejected.

### RẢI ĐẬU THÀNH BINH — Capability Seeding

`Capability → Seed → Agent Spawn → Tool Binding → Cross-Agent Linkage → Network`

Each agent receives explicit capability bindings, authority scope, boundary, ephemeral lifetime and resource budget. Spawn requires a resource gate covering CPU, memory, IO and CloneTTL.

### TRỜI LONG ĐẤT LỞ — Guarded Transformation

`Network → Large-Scale State Transformation`

Cross-domain mutations must pass orchestration and the admissibility/Forbidden filter. Invalid topology, unauthorized authority, invariant violation or resource exhaustion produces `STOP/REJECT/CLOSE`. Safe-state recovery targets `S_last_valid`.

### TRĂNG KHUYẾT LẠI TRÒN — Reconstitution

`State_t → Change → Evidence → Verification → Reconstitution → State_{t+1}`

Continuity is causal rather than snapshot identity. Preserve `Canon + Identity + Invariant + Causal Lineage`; `State_{t+1}` may differ from `State_t`.

## Hard gates

`Forbidden = StateSpace \ Admissible`

Every state transition is admissible only when authority, boundary, topology, resource and invariant checks pass.

## Network model

`N = (V, E, C, P, A)`

- `V`: agents
- `E`: typed valid handoffs
- `C`: bound capabilities/connectors
- `P`: policies/constraints
- `A`: authority assignments

No agent receives implicit cross-domain authority. Cross-domain work requires an orchestration boundary.

## Evidence and audit

Every consequential transition emits an auditable event containing intent, actor/agent, capability, authority, input state, output state, evidence, verification result and causal parent. External mutations remain disabled unless their connector authority is explicitly available.

## Canonical mapping

| Phase | Capability operation | Gate | Output |
|---|---|---|---|
| Hô phong hoán vũ | Discover + route | minimum authority | execution plan |
| Rải đậu thành binh | Seed + spawn + bind | resource/budget | agent network |
| Trời long đất lở | mutate state/topology | admissibility + Forbidden | transformed state |
| Trăng khuyết lại tròn | verify + reconstruct | lineage + invariant | next valid state |

## Connector-to-agent examples

- Knowledge connectors → KnowledgeAgent
- Supabase/Airtable → DatabaseAgent
- GitHub/Linear → CodeAgent
- Replit/OpenAI Platform → ExecutionAgent
- Figma/Canva/B12 → DesignAgent
- Descript/HeyGen/Runway/HyperFrames → MediaAgent
- Slack/Teams/Outlook/Granola → CoordinationAgent
- Stripe/PayPal → FinanceAgent
- Consensus/Wolfram/Sider Scholar → ResearchAgent
- Codex Security/Malwarebytes → SecurityAgent
- Vercel/Netlify/Wix → DeploymentAgent

## Operational invariant

`Capability scale ↑ ⇒ Governance ↑`

The system must fail closed rather than silently crossing a boundary. `PASS` is the only state that authorizes continuation; `REJECT`, `STOP`, and `CLOSE` terminate the relevant transition.
