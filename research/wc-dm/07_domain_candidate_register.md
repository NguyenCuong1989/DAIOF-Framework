# APΩ — WC-DM 2.1 — DOMAIN CANDIDATE REGISTER

Creator: alpha_prime_omega — Nguyễn Đức Cường  
System: APΩ / WC-DM Evidence-First Boundary-Squeezing Protocol  
Status: **DISCOVERY / NO TARGET FITTING**

## Purpose

Single normalized register for every candidate domain considered for the 360° search.

A candidate is not evidence merely because it is listed here.

## Mandatory schema

`D_j = (O_j, M_j, P_j, R_j, C_j, G_j, Δ_j)`

| Field | Meaning |
|---|---|
| `O_j` | Observable |
| `M_j` | Measurement / uncertainty / systematic |
| `P_j` | Provenance / raw-data lineage |
| `R_j` | Observable → `x` relation |
| `C_j` | Falsifiable constraint |
| `G_j` | Admissible set |
| `Δ_j` | Dependency / correlation |

## Status vocabulary

`CANDIDATE` / `AUDIT` / `ADMISSIBLE` / `REJECT` / `QUARANTINE` / `NON-INFORMATIVE` / `CORRELATED`

## Direction vocabulary

- `LOWER`: `x > a`
- `UPPER`: `x < b`
- `INTERIOR`: `a < x < b`
- `EXTERIOR_EXCLUSION`: excludes an interior region
- `NONE`: no useful boundary yet

## Gate — 8 questions

1. Observable là gì?
2. Ai đo?
3. Raw measurement ở đâu?
4. Uncertainty/systematic là gì?
5. Relation từ observable tới `x` là gì?
6. Relation là empirical hay model?
7. Constraint loại được khoảng nào của `x`?
8. Độc lập với evidence hiện tại ở mức nào?

Failure rules:

- No coupling → `REJECT`.
- No raw/provenance → `QUARANTINE`.
- No falsifiable restriction → `NON-INFORMATIVE`.
- Independence unresolved → `DO NOT COMBINE` / `CORRELATED` until audited.

## Candidate matrix

| ID | Domain | Observable | Dataset / sample | Provenance | Coupling to x | Relation E/I/M/A | Bound | Direction | Independence | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| D01 | Galactic dynamics | `K_z(R,z)` | SEGUE G dwarfs | recorded; source audit pending | WC-DM mapping | M/A | `(0.1548,0.5573)` execution record | INTERIOR | different sample; model correlation audit pending | AUDIT |
| D02 | Galactic rotation | `V_c(R)` | 903 Cepheids | recorded; source audit pending | `q(x)` mapping | M/A | `(0.3928,0.4107)` execution record | INTERIOR | related to density analysis | AUDIT |
| D03 | Galactic rotation robustness | `V_c(R)` | 5 bins outside `10<R<16 kpc` | recorded | same as D02 | M/A | `(0.3870,0.4167)` execution record | INTERIOR | NOT INDEPENDENT | ROBUSTNESS |
| D04 | Gaia 3D kinematics | `v_phi`, gradient / `R,z` dependence | Gaia DR3 populations | execution record; source audit pending | WC-DM kinematic mapping | M/A | not yet established from full profile | NONE | overlap/correlation audit pending | AUDIT |
| D05 | Independent stellar tracers | TBD | masers / RGB / OBA / independent samples | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |
| D06 | Gravitational lensing | TBD | galaxy / cluster lensing | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |
| D07 | Galactic halo / satellites | TBD | satellite dynamics / halo structure | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |
| D08 | Cluster dynamics | TBD | dispersion + lensing / X-ray / SZ | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |
| D09 | Particle experiments | TBD | direct detection / collider / decay | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |
| D10 | Atomic / molecular precision | TBD | spectroscopy / transition measurements | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |
| D11 | Quantum / condensed matter | TBD | laboratory observables | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |
| D12 | Solar-system / laboratory gravity | TBD | precision measurements | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |
| D13 | Astrophysical transients / timing | TBD | timing / kinematics / transients | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |
| D14 | Cosmological observables | TBD | only individually auditable observables | TBD | TBD | TBD | TBD | TBD | TBD | CANDIDATE |

## Intersection rule

No candidate is intersected into the canonical survivor until:

`provenance → coupling → constraint → falsification → independence`

has passed.

Then, and only then:

`G_next = G_current ∩ G_candidate`

If `G_next = ∅`: **CHẾT**.  
If `G_next ≠ ∅`: **SURVIVE — continue squeezing**.

## Current target envelope

Full:

`G_current = (0.3928,0.4107)`

Conservative:

`G_cons = (0.3870,0.4167)`

These are constraint intervals, **not target values**.
