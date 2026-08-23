# APΩ — UNIVERSAL ROOT-CAUSE INFERENCE LAW
## AXCONTROL v3 × EVIDENCE-FIRST

**Status:** CANONICAL LAW / LOCKED
**Scope:** All WC-DM research inference, audit, computation, constraint admission, falsification, and checkpoint transitions.

---

## LAW-01 — ONTOLOGICAL SEPARATION

Every research object MUST remain classified as one of:

`E | I | M | A | C | G | D`

where:

- `E` = empirical evidence
- `I` = inferred quantity
- `M` = model / mapping
- `A` = assumption
- `C` = constraint
- `G` = admissible state-space
- `D` = dependency / provenance graph

No class may be silently promoted into another class.

Forbidden:

`THEORY → EVIDENCE`
`MODEL → EVIDENCE`
`CODE → EVIDENCE`
`TARGET → INPUT`

---

## LAW-02 — REALITY-FIRST ORDER

The admissible inference direction is:

`REALITY → OBSERVABLE → MEASUREMENT → PROVENANCE → VALIDATED RELATION → INFERENCE → MODEL COUPLING → CONSTRAINT → G → INTERSECTION → CONCLUSION`

No shortcut is admissible.

---

## LAW-03 — READ-ONLY BEFORE ACTION

Before modifying a research object, the system MUST perform a read-only audit covering, where applicable:

- provenance;
- dependency graph;
- invariant status;
- processing lineage;
- model dependencies;
- data completeness;
- context consistency;
- correlation / overlap.

Mutation during the read-only phase is forbidden.

`SCAN ⟂ MUTATION`

---

## LAW-04 — ROOT CAUSE BEFORE ACTION

For every open anomaly or gap:

`GAP → REQUIRED_OBJECT → SOURCE → PROVENANCE → COUPLING → MODEL → CONSTRAINT`

Action is permitted only when:

`RootConfirmed = TRUE ∧ ImpactBoundaryKnown = TRUE ∧ DataGap = FALSE`

Otherwise:

`NO_ACTION`

---

## LAW-05 — GAP-FIRST EXECUTION

Research MUST proceed from the highest-priority OPEN GAP, not from attractive domains, suspected values, or convenient computations.

If no GAP is open:

`RESCAN_ONTOLOGY`

The system MUST NOT invent a new domain merely to continue execution.

---

## LAW-06 — SOURCE BEFORE EVIDENCE

A datum is not admissible evidence unless its measurement, units, uncertainty treatment, provenance, and lineage are sufficiently locked for the intended inference.

Missing critical provenance implies:

`QUARANTINE`

---

## LAW-07 — COUPLING BEFORE COMPUTATION

A domain MUST NOT constrain the unknown unless an explicit, dimensionally consistent, domain-valid, non-circular coupling to the unknown exists and its parameters have provenance.

Formally:

`¬CouplingValidated → ¬Computation → ¬Constraint`

Search may discover candidates. Search may NOT manufacture coupling.

---

## LAW-08 — NO GUESSING MISSING OBJECTS

When an essential object is missing, the system MUST build or locate that object through evidence and provenance.

It MUST NOT substitute:

- physical intuition;
- arbitrary parameterization;
- target-centered fitting;
- repeated computation;
- model convenience

for the missing object.

`DATA_GAP → BUILD/LOCATE → NEVER_GUESS`

---

## LAW-09 — ADMISSION GATE

A domain may enter computation only if the required evidence and coupling gates pass:

`Adm_E ∧ Adm_C ∧ RootConfirmed ∧ ¬DataGap`

Otherwise the domain remains `QUARANTINED`, `UNRESOLVED`, or `REJECTED` as appropriate.

---

## LAW-10 — INFORMATIONAL CONSTRAINT

A constraint is informative only if it excludes at least one admissible value of the unknown:

`∃a,b : a ∈ G_i ∧ b ∉ G_i`

If `G_i = X`, the constraint is `NON-INFORMATIVE`.

---

## LAW-11 — FALSIFICATION BEFORE SURVIVAL

Every admitted constraint MUST be tested against the current survivor:

`G_next = G_current ∩ G_i`

If:

`G_next = ∅ → FALSIFIED / CHẾT`

If:

`G_next ≠ ∅ → SURVIVE`

Survival is not proof.

No model, mapping, or evidence may be altered merely because the intersection is empty.

---

## LAW-12 — DEPENDENCY BEFORE INTERSECTION

Independence MUST be audited across:

- sample overlap;
- observable overlap;
- systematic errors;
- processing lineage;
- model dependency.

Correlated constraints MUST NOT receive independent evidential weight.

`CORRELATED ≠ INDEPENDENT`

Where necessary, combination MUST be covariance-aware.

---

## LAW-13 — ROBUSTNESS IS NOT NEW EVIDENCE

Removing bins, features, samples, or perturbing analysis choices to test robustness does not create an independent evidence domain unless genuinely independent observations and provenance exist.

`ROBUSTNESS ≠ NEW_EVIDENCE`

---

## LAW-14 — TARGET-FREE INFERENCE

Any suspected target `T` is forbidden as an input to model construction, parameter selection, fitting, or constraint generation.

`T ∉ INPUT`

A target-like value may appear only as an output of an independently admissible computation.

---

## LAW-15 — STATE TRANSITIONS ARE MONOTONIC

Objects MUST progress only through the authorized state machine:

`DISCOVERED → SOURCE_LOCKED → COUPLING_LOCKED → ADMISSIBLE → COMPUTED → VALIDATED | FALSIFIED`

Forbidden transitions include:

`DISCOVERED → COMPUTED`
`DISCOVERED → CONSTRAINT`
`SOURCE_LOCKED → CONSTRAINT`
`ASSUMPTION → EVIDENCE`
`MODEL → EVIDENCE`
`COMPUTATION → EVIDENCE`

---

## LAW-16 — FAIL-CLOSED

If any mandatory gate is unresolved, execution MUST halt at that gate.

`UNCERTAIN_OBJECT → NO_ACTION`

`NO_SOURCE → NO_EVIDENCE`

`NO_COUPLING → NO_COMPUTATION`

`NO_ADMISSION → NO_CONSTRAINT`

`NO_FALSIFICATION → NO_SURVIVAL`

`NO_INDEPENDENCE → NO_INDEPENDENT_WEIGHT`

---

## LAW-17 — 360° OBJECTIVE

The objective is NOT to maximize the number of domains or constraints.

The objective is:

`maximize IndependentBoundaryCoverage`

across lower, upper, interior, and exterior exclusion information.

A domain is valuable only to the extent that it contributes admissible, independently audited boundary information.

---

## LAW-18 — GLOBAL INFERENCE

Let `A = {i : AX(D_i) = PASS}`. Then:

`G_* = ⋂_{i∈A} G_i`

Only admitted and falsification-verified constraints may enter the global intersection.

---

## LAW-19 — CHECKPOINT INTEGRITY

Every completed execution MUST save:

1. current ontology state;
2. open/closed GAP_SET;
3. source/provenance status;
4. coupling status;
5. computation result, if any;
6. falsification result;
7. dependency/correlation status;
8. exact next resume object.

A checkpoint MUST NOT promote creator-supplied execution output to independently verified evidence.

---

## LAW-20 — UNIVERSAL EXECUTION ORDER

For every future inference task:

`LOCK ONTOLOGY`
→ `IDENTIFY GAP`
→ `READ-ONLY SCAN`
→ `TRACE ROOT CAUSE`
→ `LOCK SOURCE`
→ `LOCK PROVENANCE`
→ `LOCK COUPLING`
→ `ADMIT`
→ `COMPUTE`
→ `FALSIFY`
→ `AUDIT DEPENDENCY`
→ `INTERSECT`
→ `VERIFY`
→ `SAVE CHECKPOINT`

No stage may be skipped.

---

## MASTER LAW

> **NO ROOT → NO ACTION**  
> **NO SOURCE → NO EVIDENCE**  
> **NO COUPLING → NO COMPUTATION**  
> **NO ADMISSION → NO CONSTRAINT**  
> **NO FALSIFICATION → NO SURVIVAL**  
> **NO INDEPENDENCE → NO JOINT WEIGHT**  
> **EMPTY INTERSECTION → CHẾT**

This law governs the research process. It does not itself constitute physical evidence or a physical theory.
