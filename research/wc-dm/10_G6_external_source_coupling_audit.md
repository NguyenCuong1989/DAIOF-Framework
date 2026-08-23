# APΩ — G6 EXTERNAL SOURCE / COUPLING AUDIT

> **ACTIVE-AUDIT HISTORY NODE** — entered from the G6 gap path; exits to [`01_canonical_checkpoint.md`](01_canonical_checkpoint.md) and [`00_TODO_RESUME.md`](00_TODO_RESUME.md). G6 is closed as unresolved coupling/model-identification gap; it does not control the current resume point.

Creator: **alpha_prime_omega**  
System: **APΩ / WC-DM Evidence-First Boundary-Squeezing Protocol**  
Execution date: **2026-08-24**  
Status: **G6 COUPLING GAP — EXTERNAL SOURCE AUDIT COMPLETED**

## 1. Authorized scope

This execution is restricted to the first open gap G6.

Required objects:

- `S_max(x)`
- `σ_self(x)` or `σ_self(x,v,m)`
- source-locked forward relation from `x = g_dark/g_crit` to those quantities

Forbidden:

- target fitting;
- computation of a new `G_i` without coupling;
- promoting generic SIDM limits into a `g_dark` constraint;
- changing the current survivor to rescue a physical gate.

## 2. Read-only source audit

The existing codebase record had already established that no source-locked canonical relation was present in the accessible WC-DM records. This execution extended the search to external scientific literature for two distinct questions:

1. Do empirical/validated limits on dark-matter self-interaction exist?
2. Do those limits define the required WC-DM-specific map `x → σ_self(x,v,m)` or `x → S_max(x)`?

## 3. What external literature does establish

Published SIDM work does provide empirical/observational constraints on self-interaction cross sections per unit mass.

Examples include:

- Bullet Cluster analyses deriving limits around `σ/m < 1 cm²/g` from the observed separation of gas, galaxies and lensing mass.
- Numerical Bullet Cluster analyses deriving limits such as `σ/m < 1.25 cm²/g` (68% CL), with stronger limits under additional assumptions.
- Group/cluster analyses reporting velocity-scale-dependent constraints, including a cluster upper limit `σ/m < 0.35 cm²/g` at 95% confidence.
- Recent merging-cluster work reporting `σ/m < 0.22 cm²/g` for a specified sample and analysis framework.

These are real external constraints on SIDM/self-interaction parameters. They are **not automatically constraints on `x = g_dark/g_crit`**.

## 4. Why the required G6 coupling is still absent

The literature expresses the physical interaction in model-specific quantities such as:

`σ/m`, `σ_T/m`, mediator mass, particle mass, coupling strength, velocity scale, or a specified particle model.

A representative particle model can give an explicit relation such as a cross section depending on a coupling, DM mass, mediator mass and velocity.

However, none of the audited sources supplies the required WC-DM-specific identity:

`x = g_dark/g_crit → σ_self(x,v,m)`

or:

`x = g_dark/g_crit → S_max(x)`.

Introducing such a map from one of those particle/SIDM models would add a new model assumption and would therefore violate the current coupling gate unless WC-DM explicitly adopts and independently validates that mapping.

## 5. S_max audit

No source-locked definition tying the WC-DM variable `x` to a quantity canonically named `S_max(x)` was established in the audited codebase or external literature search.

The term `S_max` therefore remains an unresolved WC-DM object, not an observable and not an independently validated relation.

No numerical lower boundary may be generated from it.

## 6. Formal gate result

The evidence branch exists:

`observation/validated analysis → σ_self/m constraint`

but the required WC-DM coupling branch does not:

`σ_self/m constraint → σ_self(x,v,m)` **MISSING**

and:

`S_max observable/criterion → S_max(x)` **MISSING**

Therefore:

`Adm_E(external SIDM evidence) = potentially PASS for its own stated quantity`

but:

`Adm_C(WC-DM G6) = 0`

and hence:

`¬Adm_C → ¬Computation → ¬Constraint`.

## 7. Boundary consequence

The existing numerical statements:

`x > 0.387`

and

`x < 0.795`

remain creator-supplied execution records pending a valid WC-DM coupling audit.

This external search does **not** upgrade them into canonical empirical constraints.

No new `G_G6` is admitted.

Thus:

`G_current` remains unchanged.

## 8. Root-cause classification

G6 is now classified as:

`COUPLING GAP / MODEL-IDENTIFICATION GAP`

not:

`MEASUREMENT ABSENCE`.

There are genuine self-interaction measurements/limits in the literature. The missing object is the validated WC-DM mapping from those measured quantities to `g_dark`.

## 9. No-drift decision

Do not construct a mapping merely by selecting a familiar SIDM particle model.

Do not rename `σ/m < ...` as a `g_dark` bound.

Do not introduce `S_max(x)` by definition after the fact.

Do not compute an intersection from G6.

The correct transition is:

`G6 → explicit unresolved coupling gap → next authorized gap G3`.

This transition is not a failure of G6; it is the completed root-cause determination required by AXCONTROL.

## 10. Canonical state after audit

`G_full = (0.3928,0.4107) g_crit`

`G_cons = (0.3870,0.4167) g_crit`

`SURVIVE — g_dark NOT CONCLUDED`

Forbidden target inputs remain:

`x = 0.4`, `0.4018`, `0.4019`.

## 11. Next authorized action

`G3 — FULL K_z(R,z) SOURCE / RELATION / PROVENANCE AUDIT`

Only source/provenance/coupling audit first. No new numerical constraint until the G3 coupling gate passes.

**NEXT:** [`00_TODO_RESUME.md`](00_TODO_RESUME.md) → current first-open gap G3.