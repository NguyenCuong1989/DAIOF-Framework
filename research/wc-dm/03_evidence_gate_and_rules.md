# APΩ — Evidence Gate and Iron Rules

## 0. Supreme rule

`EMPIRICAL EVIDENCE IS THE FOUNDATION.`

No special evidentiary authority is granted to consensus, authority, reputation, citation count, standards, popular theory, elegant models, or attractive fits.

## 1. Theory is testable

`THEORY != EVIDENCE`.

When a theory component conflicts with validated empirical evidence, retain the evidence and remove or revise the conflicting theory component. Never alter the data to save the theory.

## 2. Domain decomposition

`D = E_empirical + I_inferred + M_model + A_assumption`.

Remove invalid components; do not discard an entire domain automatically.

## 3. Datum gate

`observable → measurement → provenance → unit → uncertainty`.

Missing provenance or measurement path → `QUARANTINE`.

## 4. Inference boundary

`measured != inferred != model prediction`.

A prediction `P(g)` never becomes evidence merely because computation reproduces it.

## 5. Mathematics

Math operates only after evidence and relations are locked. Checks: units, domain, hidden assumptions, reproducibility, non-circularity.

## 6. Computation

Code may calculate, scan, solve, propagate uncertainty, test sensitivity/stability, and intersect constraints. Code cannot create evidence.

## 7. Constraint mechanics

For each domain:

`G_{i+1} = G_i ∩ G_i^constraint`.

A domain receives constraining authority only if there is an auditable path:

`observable → coupling to g_dark → constraint`.

## 8. No preselection

Forbidden workflow:

`g=0.4 → build model → fit → declare g=0.4`.

Required workflow:

`data → constraints → intersection → g_dark`.

## 9. Failure is valid

`G=empty` → candidate is dead. No rescue by changing data, uncertainty, subset selection, definitions, or hidden assumptions.

`G!=empty` → continue searching for more constraints.

## 10. Robustness

Required tests where applicable: suspect-data deletion, alternative binning, leave-one-out, uncertainty perturbation, numerical resolution, boundary-condition variation, and alternative admissible preprocessing.

Survives a specific test → robust to that test only. It is not automatically globally robust.

## 11. No double counting

Shared dataset or shared information must not be counted as independent evidence. Use covariance/joint likelihood or downgrade one analysis to robustness.

## 12. Provenance is computational input

Required lineage:

`source → raw → conversion → equation → calculated value → C(g)`.

Lost lineage → no sign-off.

## 13. Uncertainty taxonomy

Keep separate:

- measurement uncertainty
- systematic uncertainty
- model uncertainty
- numerical uncertainty

Do not call `(g_max-g_min)/2` a 1-sigma interval without a statistical derivation and stated coverage criterion.

## 14. Falsifiability

A valid constraint must be able to reject some candidate `g` values. An always-pass test is not an effective constraint.

## 15. Theory disputes

Ask: what was measured, what follows directly from measurement, and what is interpretation/model? Admit only the justified component.

## 16. Conceptual integrity — no category substitution

`REALITY != OBSERVABLE != MEASUREMENT != INFERENCE != MODEL != ASSUMPTION != THEORY != COMPUTATION`.

No implicit type conversion is permitted. A statement must retain its original epistemic type throughout the pipeline.

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
- `INTERVAL HALF-WIDTH → 1σ` without statistical derivation

If an inference step changes epistemic type, the conversion must be explicit, justified, and provenance-traceable. Otherwise the result is a `TYPE VIOLATION`.

On `TYPE VIOLATION`:

1. halt the affected inference chain;
2. trace back to the first type-changing step;
3. restore the original evidence/model/assumption labels;
4. quarantine downstream results dependent on the violation;
5. resume only after the ontology and provenance are repaired.

## 17. Locked inference order

`REALITY → OBSERVABLE → MEASUREMENT+PROVENANCE → VALIDATED RELATION → MATHEMATICS → COMPUTATION → BOUND → G_i → intersection → g_dark`.

## 18. Final rule

Empirical evidence does not serve theory. Theory serves empirical evidence.

`g_dark` must submit to all admissible empirical boundaries; no boundary may be altered to serve `g_dark`.
