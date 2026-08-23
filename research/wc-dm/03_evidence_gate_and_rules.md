# APΩ — Canonical Evidence Laws

**Creator:** `alpha_prime_omega — Nguyễn Đức Cường`  
**System:** `APΩ / WC-DM Evidence-First Boundary-Squeezing Protocol`  
**Status:** `HARD / FAIL-CLOSED / CANONICAL`

> This document contains **LAWS**, not advisory rules. A Law violation invalidates the affected reasoning chain until repaired and re-gated.

## LAW 0 — EMPIRICAL EVIDENCE IS THE FOUNDATION

No special evidentiary authority is granted to consensus, authority, reputation, citation count, standards, popular theory, elegant models, or attractive fits.

`REALITY > THEORY`

## LAW 1 — THEORY IS TESTABLE

`THEORY != EVIDENCE`.

When a theory component conflicts with validated empirical evidence, retain the evidence and reject, revise, or quarantine the conflicting theory component. Never alter data to save theory.

## LAW 2 — DOMAIN DECOMPOSITION

`D = E_empirical + I_inferred + M_model + A_assumption`.

Remove invalid components; do not discard an entire domain automatically.

## LAW 3 — DATUM GATE

`observable → measurement → provenance → unit → uncertainty`.

Missing provenance or measurement path → `QUARANTINE`.

## LAW 4 — INFERENCE BOUNDARY

`measured != inferred != model prediction`.

`P(g) ↛ E`.

A prediction never becomes evidence merely because computation reproduces it.

## LAW 5 — MATHEMATICS FOLLOWS EVIDENCE

Mathematics operates only after evidence and relations are locked. Required checks: units, domain, hidden assumptions, reproducibility, and non-circularity.

## LAW 6 — COMPUTATION CANNOT CREATE EVIDENCE

Code may calculate, scan, solve, propagate uncertainty, test sensitivity/stability, and intersect constraints.

`COMPUTATION != EVIDENCE`.

## LAW 7 — CONSTRAINT MECHANICS

For each admissible domain:

`G_{i+1} = G_i ∩ G_i^constraint`.

Constraining authority requires an auditable path:

`observable → coupling to g_dark → constraint`.

## LAW 8 — NO PRESELECTION

Forbidden:

`g=0.4 → build model → fit → declare g=0.4`.

Required:

`data → constraints → intersection → g_dark`.

## LAW 9 — FAILURE IS VALID

`G = ∅ → DEAD`.

No rescue by changing data, uncertainty, subset selection, definitions, or hidden assumptions.

`G != ∅ → SURVIVE ONLY; CONTINUE SEARCHING`.

## LAW 10 — ROBUSTNESS

Where applicable: suspect-data deletion, alternative binning, leave-one-out, uncertainty perturbation, numerical resolution, boundary-condition variation, and alternative admissible preprocessing.

Survival through a specific test means robustness **to that test only**.

## LAW 11 — NO DOUBLE COUNTING

Shared dataset or shared information shall not be counted as independent evidence. Use covariance/joint likelihood or downgrade one analysis to robustness.

## LAW 12 — PROVENANCE IS PART OF THE CALCULATION

Required lineage:

`source → raw → conversion → equation → calculated value → C(g)`.

Lost lineage → `NO SIGN-OFF`.

## LAW 13 — UNCERTAINTY TAXONOMY

Keep separate:

- measurement uncertainty
- systematic uncertainty
- model uncertainty
- numerical uncertainty

`(g_max-g_min)/2` shall not be called `1σ` without statistical derivation and stated coverage.

## LAW 14 — FALSIFIABILITY

A valid constraint must be able to reject some candidate `g` values. An always-pass test is `NON-INFORMATIVE`.

## LAW 15 — THEORY DISPUTES

Separate:

1. what was measured;
2. what follows directly from measurement;
3. interpretation/model.

Admit only the justified component.

## LAW 16 — CONCEPTUAL INTEGRITY / NO CATEGORY SUBSTITUTION

`REALITY != OBSERVABLE != MEASUREMENT != INFERENCE != MODEL != ASSUMPTION != THEORY != COMPUTATION != LLM PRIOR`.

No implicit epistemic type conversion is permitted.

Forbidden substitutions include:

- `THEORY → EVIDENCE`
- `INFERENCE → MEASUREMENT`
- `MODEL PREDICTION → OBSERVATION`
- `CONSENSUS → TRUTH`
- `CITATION → PROVENANCE`
- `COMPUTATION → EVIDENCE`
- `GOOD FIT → REALITY`
- `ASSUMPTION → FACT`
- `MODEL-DEPENDENT CONSTRAINT → THEORY-INDEPENDENT CONSTRAINT`
- `CORRELATION → INDEPENDENCE`
- `INTERVAL HALF-WIDTH → 1σ` without derivation
- `LLM PRIOR → FACT/EVIDENCE`

Any type-changing step must be explicit, justified, and provenance-traceable. Otherwise: `TYPE VIOLATION`.

## LAW 17 — HARD READING GATE

`LOAD LAWS → VERIFY LAW STATE → EXPLICIT GATE PASS → READ/SEARCH DOWNSTREAM CONTENT`.

If Law state is unavailable, ambiguous, or failed:

`HALT + DO NOT READ FURTHER`.

The gate applies to canonical files, domain candidates, source material, execution records, computations, and continuation checkpoints.

## LAW 18 — LLM EPISTEMIC CONTAINMENT

The complete hard containment law is canonicalized in `LAW-LLM-EPISTEMIC-CONTAINMENT.md`.

Core invariants:

`LLM TRAINING PRIOR != CANONICAL EVIDENCE`

`CONTEXT != CANONICAL AUTHORITY`

`PROVENANCE > MEMORY`

`CANONICAL STATE > CONTEXT COMPLETION`

`LLM REASONING != EPISTEMIC AUTHORITY`

The LLM may explore candidates, domains, relations, computations, counterexamples, and falsification tests, but it may not expand evidentiary authority by itself.

An unverified LLM prior remains `UNVERIFIED PRIOR` and cannot self-upgrade into evidence, fact, measurement, or validated relation.

Any context drift, prior contamination, unauthorized theory injection, or provenance break triggers `HALT → TRACE → RESTORE TYPES → QUARANTINE DEPENDENTS → REPAIR → RE-GATE`.

## LAW 19 — LOCKED INFERENCE ORDER

`REALITY → OBSERVABLE → MEASUREMENT+PROVENANCE → VALIDATED RELATION → MATHEMATICS → COMPUTATION → BOUND → G_i → INTERSECTION → g_dark`.

## LAW 20 — FINAL SUBMISSION LAW

Empirical evidence does not serve theory. Theory serves empirical evidence.

`g_dark` must submit to all admissible empirical boundaries; no boundary may be altered to serve `g_dark`.
