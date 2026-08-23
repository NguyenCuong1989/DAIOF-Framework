# APΩ — Canonical Checkpoint: WC-DM 2.1

Creator: alpha_prime_omega — Nguyễn Đức Cường  
System: APΩ / WC-DM Evidence-First Boundary-Squeezing Protocol  
Date: 2026-08-24

## Step 1 — Iron-law protocol

`REALITY → OBSERVABLE → MEASUREMENT + PROVENANCE → VALIDATED RELATION → MATH → COMPUTATION → BOUND → G_i → intersection → g_dark`

Invariants:

- Theory is not evidence.
- Computation is not evidence.
- A model prediction is not an observation.
- `G = ∅` means the candidate is dead.
- `G != ∅` means continue squeezing; survival is not proof.
- Evidence cannot be altered to rescue a model.

## Step 2 — Initial physical gate

Execution record:

`G_physical = (0.387, 0.795) g_crit`

Dependencies requiring final provenance audit: `S_max(g)` mapping and `sigma_self(g)` mapping.

## Step 3 — TF/local-density gate

Recorded benchmark:

- `R = 15.7 kpc`
- `rho_S = 3.43e7 M_sun kpc^-3`
- `k = pi/R = 0.20010 kpc^-1`
- `rho_S ≈ 1.30 GeV cm^-3`
- `m = 0.1 GeV`
- `n_S ≈ 13.0 cm^-3`
- `rho_h = 0.30 GeV cm^-3`
- `n_h = 3.0 cm^-3`
- density contrast `n_S/n_h ≈ 4.34`

Recorded density budget with `sigma_v,h = 86 km/s`:

`(sigma_v,0^2 + |omega_0|) < 3.21e4 (km/s)^2`

This is a gate, not a direct measurement of `g_dark`.

## Step 4 — 903 Cepheids rotation curve

Dataset recorded as:

- Gaia DR3
- 903 Cepheids
- `6 < R < 18 kpc`
- 12 radial bins

Canonical analysis mapping used in the execution record:

`q(x) = 1 - 0.6 x`

`V_model(R;x) = sqrt(V_bar^2 + V_DM,mean^2 * q_mean/q(x))`

The baseline decomposition `f_DM(R)=0.25→0.75` is an analysis construction and must not be promoted to independent baryonic evidence.

Full 12-bin execution result:

`G_RC,full = (0.3928, 0.4107) g_crit`

Recorded best point: `x_best = 0.4018`.

## Step 5 — robustness exclusion

Entire region `10 < R < 16 kpc` removed to test dependence on reported dip/bump features.

Execution result:

`G_RC,excl = (0.3870, 0.4167) g_crit`

This is a robustness result, not an independent evidence domain.

## Step 6 — K_z local execution

Recorded dataset:

- 16,269 G dwarfs
- SEGUE
- Bovy & Rix 2013

Recorded model mapping:

`K_z,DM,mean = 20`

`K_z,DM,0 = 11.52` at `q=1`

`K_z,model(x) = Sigma_bar + K_z,DM,0 / q(x)^2`

Execution result:

`G_Kz = (0.1548, 0.5573) g_crit`

Intersection with full RC leaves the RC survivor unchanged. The mapping is a WC-DM model component; `K_z^obs` remains the empirical datum.

## Step 7 — Gaia 3D execution

Recorded endpoint checks:

- `x=0.3928 → gradient=-1.752`
- `x=0.4107 → gradient=-1.683`
- recorded variation is below the reported observational error in the supplied execution record.

Execution conclusion: the tested Gaia-3D constraint contains the current full RC interval and therefore does not narrow it.

## Step 8 — double-count audit

Current datasets include 903 Cepheids, 16,269 SEGUE G dwarfs, and a large Gaia-3D stellar sample. Independence is **not automatically granted**. Sample overlap, observable correlation, shared systematics, and processing dependencies must be checked before joint likelihood combination.

## Step 9 — current survivor

Full:

`G_final,full = (0.3928, 0.4107) g_crit`

Conservative:

`G_cons = (0.3870, 0.4167) g_crit`

Widths:

- full: `0.0179 g_crit`
- conservative: `0.0297 g_crit`

The values `0.4018` and `0.4019` are centers/best points of the recorded constraints, not an admissible preselected target.

The half-widths must not be called `1 sigma` unless derived from an explicit statistical likelihood/coverage definition.

## Step 10 — canonical verdict

`G_final != empty` → **SURVIVE**.

`g_dark` is **not yet authorized as a final reported value**.

## Step 11 — next gates

1. Full `K_z(R,z)` profile.
2. Gaia-3D `R,z` dependence rather than a single gradient check.
3. Locked canonical `q(x)` for the current model variant; any changed mapping becomes a separate model variant.
4. Search additional empirical domains before attempting further target-centered fitting.
