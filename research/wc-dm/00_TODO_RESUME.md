# WC-DM — 00 TODO / RESUME

> **FLOW ENTRYPOINT / RESUME AUTHORITY.** A fresh agent/session starts here, follows the linked canonical flow once, executes only the first OPEN GAP, closes one cycle, writes the next TODO state here, commits, and returns to this file.

## 0. CLOSED-LOOP EXECUTION

```text
START
  ↓
00_TODO_RESUME
  ↓
LAW / MANIFEST / CHECKPOINT
  ↓
ONTOLOGY / EVIDENCE / AXCONTROL / ROOT-CAUSE
  ↓
ACTIVE GAP
  ↓
READ-ONLY AUDIT
  ↓
REQUIRED OBJECT
  ↓
SOURCE → PROVENANCE → COUPLING → ADMISSION
  ↓
COMPUTE → FALSIFY → DEPENDENCY → INTERSECT → VERIFY
  ↓
UPDATE CHECKPOINT
  ↓
GENERATE NEXT TODO
  ↓
COMMIT
  ↓
RETURN TO 00_TODO_RESUME
  ↺
```

**Round-closure law:** one cycle may modify only the objects authorized by the current GAP. At closure, the current TODO is replaced/extended with the next unresolved GAP and its exact required deliverable. A cycle is not closed until the new resume state is committed.

## 1. CANONICAL STARTUP FLOW

**START → `00_TODO_RESUME.md` → `LAW-DRIFT-PREVENTION.md` → `MANIFEST.md` → `01_canonical_checkpoint.md` → `02_domain_object_ontology.md` → `03_evidence_gate_and_rules.md` → `LAW-LLM-EPISTEMIC-CONTAINMENT.md` → `LAW-AXCONTROL-CODEGEN-CONTRACT.md` → `LAW_UNIVERSAL_ROOT_CAUSE_INFERENCE.md` → `04_domain_search_matrix.md` → ACTIVE GAP → `05_execution_record.md` → checkpoint → NEXT TODO → COMMIT → return here.**

No transcript is required to reconstruct the operational state.

## 2. RESUME AUTHORITY

This file is the operational pointer. It cannot override LAW or canonical physical state. If this file conflicts with `MANIFEST` or `01_canonical_checkpoint`, **HALT** and resolve authority before execution.

## 3. LOCKED STATE

`x = g_dark / g_crit`

`G_full=(0.3928,0.4107) g_crit`

`G_cons=(0.3870,0.4167) g_crit`

**SURVIVE — `g_dark` not concluded.**

These values are state, never targets or inputs.

## 4. CURRENT TODO — G3

### G3 — Full `K_z(R,z)` source / provenance / coupling audit

**Objective:** determine whether an admissible, source-locked, validated relation exists that connects the empirical `K_z(R,z)` object to `x=g_dark/g_crit`.

**Required object chain:**

`K_z(R,z) → observable/measurement → provenance → units/sign/normalization → validated relation → x-coupling → admission`

**Read-only deliverables:**

1. Identify the exact empirical `K_z(R,z)` source and dataset/profile scope.
2. Lock provenance, units, uncertainties, sample definition, and relevant covariance/systematics information.
3. Separate empirical `K_z` from baryonic/model/decomposition terms.
4. Identify the exact forward relation required for `x → K_z^model(R,z)`.
5. Audit whether that relation is source-locked, dimensionally valid, non-circular, and parameter-provenanced.
6. Classify the result as `PASS`, `DATA_GAP`, `COUPLING_GAP`, or `MODEL_GAP`.

**Hard prohibitions:**

`NO x-target fitting`  
`NO computation before coupling PASS`  
`NO new G3 constraint before admission`  
`NO independence claim from shared data`  
`NO substitution of another observable for full K_z(R,z)`

**Required artifact:** `G3 source/provenance/coupling audit` linked into the flow.

## 5. GAP PROTOCOL

`GAP → REQUIRED_OBJECT → SOURCE → PROVENANCE → COUPLING → ADMISSION → COMPUTATION → FALSIFICATION → DEPENDENCY → INTERSECTION → VERIFY → SAVE CHECKPOINT → GENERATE NEXT TODO → COMMIT → RESUME`

If an object is absent from admissible sources, record the exact gap type:

`DATA_GAP | COUPLING_GAP | MODEL_GAP`

Never guess, silently substitute, or reinterpret absence as falsification.

## 6. CYCLE CLOSURE CONTRACT

A cycle is `CLOSED` iff all are true:

- current GAP has a dedicated artifact;
- source/provenance status is recorded;
- coupling status is explicitly recorded;
- computation/constraint status is explicit, including `FORBIDDEN` where applicable;
- dependency/falsification status is explicit if computation occurred;
- canonical checkpoint is updated;
- this file contains the **next** actionable TODO;
- all changed files are committed;
- the commit is the new resume anchor.

`SPECIFIED ≠ IMPLEMENTED ≠ VERIFIED ≠ CLOSED`.

## 7. NEXT-TODO GENERATION LAW

At cycle closure:

```text
OPEN_GAPS = ontology.scan()

if current_gap is RESOLVED:
    select next highest-priority OPEN GAP
elif current_gap is UNRESOLVED because of DATA/COUPLING/MODEL GAP:
    select the smallest admissible object needed to resolve that gap

write:
    NEXT_GAP
    REQUIRED_OBJECT
    SOURCE_REQUIREMENT
    COUPLING_REQUIREMENT
    ADMISSION_GATE
    FORBIDDEN_ACTIONS
    DELIVERABLE

commit all state + TODO changes
```

If `OPEN_GAPS = ∅`, perform a full ontology rescan before inventing any domain. If the rescan produces no admissible unresolved object, declare the research state `CLOSED/NO_ADMISSIBLE_NEXT_ACTION` rather than inventing work.

## 8. HISTORICAL / SUPPORTING RECORDS

- [`06_domain_discovery_round1.md`](06_domain_discovery_round1.md) — historical discovery.
- [`07_domain_candidate_register.md`](07_domain_candidate_register.md) — candidate subgraph.
- [`08_domain_discovery_round2.md`](08_domain_discovery_round2.md) — historical discovery.
- [`10_G6_external_source_coupling_audit.md`](10_G6_external_source_coupling_audit.md) — closed G6 coupling audit.

Historical records cannot override current GAP or canonical state.

## 9. RETURN EDGE

**After completing G3, do not stop at the audit artifact. Update checkpoint → generate next TODO → commit → return to this file.**

**CURRENT RESUME:** `G3`  
**CURRENT STATE:** `SURVIVE / g_dark NOT CONCLUDED`  
**NEXT AUTHORIZED ACTION:** G3 read-only source/provenance/coupling audit.