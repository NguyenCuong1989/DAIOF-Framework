# WC-DM 2.1 — Execution Record

> **FLOW NODE 10/12 — execution evidence boundary.** Entered from the active GAP audit; exits to [`01_canonical_checkpoint.md`](01_canonical_checkpoint.md). This file records execution and can never by itself promote a result to evidence.

## Classification

This file preserves the computational results supplied in the research checkpoint. It is **not** a substitute for raw source files or independent source verification.

## Recorded executions

### RC full

12 bins, 903 Cepheids, `6<R<18 kpc`:

`G_RC,full = (0.3928,0.4107) g_crit`

Recorded minimum: `x=0.4018`.

### RC exclusion robustness

Exclude all `10<R<16 kpc`, retain 5 bins:

`G_RC,excl = (0.3870,0.4167) g_crit`.

Interpretation: the current survivor persists under this specific exclusion test.

### K_z local

16,269 SEGUE G dwarfs, Bovy & Rix 2013 execution mapping:

`K_z,DM,mean=20`, `K_z,DM,0=11.52`, `q(x)=1-0.6x`.

Recorded result:

`G_Kz=(0.1548,0.5573) g_crit`.

### Gaia 3D endpoint check

Recorded:

`x=0.3928 → gradient=-1.752`

`x=0.4107 → gradient=-1.683`

Recorded variation is below the stated observational error in the supplied run. Full `R,z` likelihood has not yet been established in this checkpoint.

## Numerical audit flags

1. Verify every endpoint convention: open/closed interval and rounding.
2. Recover raw tables and exact uncertainties before final statistical interpretation.
3. Verify covariance and shared systematics.
4. Verify the exact source equations used for every model mapping.
5. Keep model-constructed baryonic/DM decomposition separate from empirical observables.
6. Do not promote the interval center to `g_dark`.
7. Do not label interval half-width as `1 sigma` without a likelihood/coverage derivation.

## Execution boundary

`EXECUTION_RECORD ≠ EVIDENCE`.

Only a separately admitted chain may promote an execution result into a constraint:

`SOURCE → PROVENANCE → VALIDATED RELATION → COUPLING → ADMISSION → COMPUTATION → FALSIFICATION → DEPENDENCY`.

**NEXT NODE:** [`01_canonical_checkpoint.md`](01_canonical_checkpoint.md) → then [`00_TODO_RESUME.md`](00_TODO_RESUME.md).