# APΩ Treasury Plugin — Acceptance Matrix

| ID | Property | Verification | Pass condition |
|---|---|---|---|
| A01 | Canon identity | manifest/hash check | expected Canon SHA equals loaded SHA |
| A02 | Root law | invariant test | `PHẢI SỐNG` remains authoritative |
| A03 | Capital/research split | policy test | critical unknown blocks capital but can permit research |
| A04 | Non-terminal proof wait | action test | no candidate reaches an implicit terminal WAIT state |
| A05 | Gate transparency | UI/domain test | every blocked gate has code + reason |
| A06 | Finite action | schema test | every admissible decision has capital/evidence/universe components |
| A07 | Fail closed | negative tests | missing/invalid authority cannot escalate |
| A08 | Live default denied | configuration test | default mode cannot execute live |
| A09 | Exit path | execution admission test | execution-capable action requires an exit path |
| A10 | Replayability | deterministic replay | same input/state yields same decision semantics |
| A11 | Receipt traceability | receipt test | decision references state, evidence, gates and action |
| A12 | Local persistence | storage test | operator state survives reload without changing authority |
| A13 | Responsive UI | viewport checks | core operator flows usable at narrow and wide layouts |
| A14 | Accessibility | automated/manual checks | keyboard navigation, labels, focus and contrast are usable |
| A15 | Error/degraded states | fault injection | missing data produces explicit degraded/block state |
| A16 | Agent jurisdiction | contract test | no agent can authorize outside its declared boundary |
| A17 | Simulation | integration test | seeded simulation executes without financial side effects |
| A18 | Paper execution | integration test | paper receipt generated without live mutation |
| A19 | N-Factor evolution | state transition test | result feeds attribution/evolution without bypassing root law |
| A20 | Documentation | repository audit | operator, architecture and safety contracts are discoverable |

## Completion gate

100% means all A01–A20 have positive verification evidence. A written specification alone does not count as a pass for implementation/runtime criteria.
