# APΩ — WC-DM 2.1 — CODEBASE MATURITY & GAP-CLOSURE PROGRAM

Status: CANONICAL WORK PLAN  
Date: 2026-08-24  
Purpose: close methodological weaknesses without weakening the Evidence-First / AXCONTROL / Gap-First laws.

## 1. GOVERNING PRINCIPLE

This document does **not** authorize new physical claims. It defines work required to remove weaknesses in the research infrastructure.

`WEAKNESS → REQUIRED OBJECT → SOURCE/TEST → VALIDATION → LAW-COMPLIANT INTEGRATION`

No weakness may be closed by changing evidence, target-fitting, or weakening a gate.

## 2. MATURITY GAPS TO CLOSE

| ID | Weakness | Required closure object | Status |
|---|---|---|---|
| W1 | Falsification gate needs executable criteria | machine-readable falsification contract | OPEN |
| W2 | Dependency control is defined but not fully operational | dependency/covariance audit schema | OPEN |
| W3 | Provenance is strong conceptually but needs uniform artifact contract | provenance manifest/schema | OPEN |
| W4 | State transitions are documented but need enforcement | admissibility state machine + transition checks | OPEN |
| W5 | Numerical reproducibility needs explicit contract | deterministic computation manifest | OPEN |
| W6 | Units/dimensional analysis need a universal gate | unit + dimensional validation contract | OPEN |
| W7 | Evidence/model/assumption separation needs machine-readable tagging | E/I/M/A/C object schema | OPEN |
| W8 | Robustness results need explicit non-evidence classification | robustness artifact contract | OPEN |
| W9 | Negative results need structured recording | failed-search / unresolved-gap schema | OPEN |
| W10 | Checkpoint resume needs integrity verification | checkpoint manifest + lineage verification | OPEN |
| W11 | Source-lock needs exact equation/parameter capture | source-lock artifact contract | OPEN |
| W12 | Physical coupling gaps need explicit terminal states | DATA_GAP / COUPLING_GAP / MODEL_GAP taxonomy | OPEN |
| W13 | 360° objective needs measurable boundary-coverage metric | independent-boundary coverage schema | OPEN |
| W14 | Audit execution records must remain distinct from evidence | execution/evidence separation contract | OPEN |
| W15 | Canonical laws need one authoritative index | LAW registry / precedence map | OPEN |

## 3. REQUIRED ARCHITECTURE

Every research object MUST be representable as:

`Object = (ID, Type, State, Evidence, Provenance, Relation, Model, Assumption, Constraint, Dependency, Result, Lineage)`

Mandatory type separation:

`E ≠ I ≠ M ≠ A ≠ C ≠ G`

No transformation may silently change type.

## 4. UNIVERSAL ADMISSION CONTRACT

An object may become computationally admissible only if:

`OntologyLocked ∧ SourceLocked ∧ UnitsValid ∧ UncertaintyValid ∧ ProvenanceComplete ∧ CouplingValidated ∧ NonCircular ∧ DependencyKnown`

Otherwise:

`QUARANTINE / HALT`

The system MUST record the blocking reason rather than silently dropping the object.

## 5. FALSIFICATION CONTRACT

Every admitted constraint MUST declare:

- null/current hypothesis;
- observable;
- criterion;
- excluded region;
- uncertainty treatment;
- systematic treatment;
- model dependence;
- reproducibility procedure;
- empty-intersection consequence.

A result that cannot exclude any region is `NON-INFORMATIVE`.

An empty intersection is `FALSIFIED / CHẾT` unless an independently documented ontology inconsistency is found; changing the model merely to restore survival is prohibited.

## 6. DEPENDENCY CONTRACT

For every pair of candidate constraints record:

`Δij = (sample, observable, systematic, processing, model, calibration, source)`.

Each component is classified as:

`UNKNOWN | NONE | PARTIAL | MATERIAL`.

`UNKNOWN` MUST NOT be treated as independence.

If material dependency exists, use covariance/joint-likelihood or conservative combination rather than multiplying independent likelihoods.

## 7. PROVENANCE CONTRACT

Minimum lineage:

`source → raw datum → processing → observable → relation → result`.

Every numerical value entering computation MUST carry:

- source identifier;
- dataset/version;
- sample definition;
- measurement method;
- units;
- uncertainty;
- processing transformation;
- equation/version;
- parameter provenance;
- timestamp where relevant.

Missing lineage means `NO SIGN` for the affected claim.

## 8. DETERMINISM CONTRACT

Every numerical computation MUST declare:

`code_version, dependency_versions, input_hash, parameter_hash, random_seed(if any), numerical_precision, solver/tolerance, environment`.

If randomness is unnecessary, deterministic execution is preferred and MUST be used where technically possible.

Two replays with identical manifests MUST reproduce the canonical result within a predeclared numerical tolerance.

## 9. UNIT / DIMENSION CONTRACT

Before computation:

`UnitsValid = TRUE ∧ DimensionsConsistent = TRUE`.

No unitless number may enter a physical equation merely because the code accepts it.

Any conversion must be explicit and provenance-preserving.

## 10. NEGATIVE-RESULT CONTRACT

Search failure is not evidence of physical impossibility.

Every unresolved object MUST be classified as one of:

`DATA_GAP | COUPLING_GAP | MODEL_IDENTIFICATION_GAP | PROVENANCE_GAP | DEPENDENCY_GAP`.

A negative audit closes only the audited claim, not the entire domain.

## 11. ROBUSTNESS CONTRACT

Robustness checks MAY establish stability of an existing result, but MUST NOT automatically create a new independent evidence object.

Required relation:

`ROBUSTNESS_RESULT → supports stability claim`

not:

`ROBUSTNESS_RESULT → independent constraint`.

## 12. CHECKPOINT INTEGRITY

A checkpoint MUST contain:

`canonical_state, open_gaps, law_version, lineage, latest_commit, forbidden_transitions, resume_point`.

Resume procedure:

`LOAD → VERIFY HASH/COMMIT → VERIFY LAW STATE → VERIFY CANON → OPEN FIRST GAP → EXECUTE → SAVE → COMMIT`.

A stale checkpoint cannot override newer canonical state.

## 13. LAW REGISTRY

The codebase SHALL maintain one authoritative LAW index containing:

1. Evidence-First Laws.
2. AXCONTROL Laws.
3. Universal Root-Cause Inference Laws.
4. Gap-First Execution Laws.
5. LLM Epistemic Containment Laws.
6. Provenance / Reproducibility Laws.

Precedence:

`ONTOLOGY → EVIDENCE → PROVENANCE → COUPLING → COMPUTATION → FALSIFICATION → DEPENDENCY → INTERSECTION → CONCLUSION`.

Governance may block a physical claim but MUST NOT manufacture one.

## 14. CURRENT PHYSICAL WORK IS UNCHANGED

This closure program does not alter the physical resume point.

Current state:

`G_full=(0.3928,0.4107)`

`G_cons=(0.3870,0.4167)`

`SURVIVE — g_dark NOT CONCLUDED`

G6 remains resolved as an unresolved coupling/model-identification gap.

Next physical action remains:

`G3 — FULL K_z(R,z) SOURCE / RELATION / PROVENANCE AUDIT`

No computation is authorized until its coupling gate passes.

## 15. COMPLETION CRITERION

The codebase is considered methodologically hardened only when W1–W15 are either:

`CLOSED` with auditable artifacts, or `FORMALLY DEFERRED` with a documented reason and no hidden dependency.

Completion of this program does not imply physical validation of WC-DM or identification of `g_dark`.

## MASTER LAW

`CLOSE WEAKNESS BY ADDING VERIFIABLE STRUCTURE — NEVER BY WEAKENING EVIDENCE REQUIREMENTS.`
