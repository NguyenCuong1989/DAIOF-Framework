# APΩ — WC-DM 2.1 — DOMAIN CANDIDATE REGISTER

> **DISCOVERY SUBGRAPH** — entered from [`04_domain_search_matrix.md`](04_domain_search_matrix.md); candidate records never override [`00_TODO_RESUME.md`](00_TODO_RESUME.md) or [`01_canonical_checkpoint.md`](01_canonical_checkpoint.md).

Creator: alpha_prime_omega — Nguyễn Đức Cường
System: APΩ / WC-DM Evidence-First Boundary-Squeezing Protocol
Status: **DISCOVERY / NO TARGET FITTING**

## Mandatory schema

`D_j = (O_j, M_j, P_j, R_j, C_j, G_j, Δ_j)`

A candidate is not evidence merely because it is listed.

## Status vocabulary

`CANDIDATE / AUDIT / ADMISSIBLE / REJECT / QUARANTINE / NON-INFORMATIVE / CORRELATED / ROBUSTNESS`

## Direction vocabulary

- `LOWER`: `x>a`
- `UPPER`: `x<b`
- `INTERIOR`: `a<x<b`
- `EXTERIOR_EXCLUSION`: excludes an interior region
- `NONE`: no admissible boundary yet

## Gate — 8 questions

1. Observable?
2. Who measured it?
3. Where is raw measurement?
4. Uncertainty/systematic?
5. Relation to `x`?
6. Empirical or model relation?
7. What part of `x` is falsified?
8. Independence level?

Failure rules:

- No coupling → `REJECT`.
- No raw/provenance → `QUARANTINE`.
- No falsifiable restriction → `NON-INFORMATIVE`.
- Independence unresolved → `DO NOT COMBINE`.

## Candidate matrix — updated after Round 2

| ID | Domain | Observable | Dataset / sample | Provenance | Coupling to x | Relation E/I/M/A | Bound | Direction | Independence | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| D01 | Galactic dynamics | `K_z(R,z)` | SEGUE G dwarfs | recorded; source audit pending | WC-DM mapping | M/A | `(0.1548,0.5573)` execution record | INTERIOR | different sample; model correlation pending | AUDIT |
| D02 | Galactic rotation | `V_c(R)` | 903 Cepheids | recorded; source audit pending | `q(x)` mapping | M/A | `(0.3928,0.4107)` execution record | INTERIOR | related to density analysis | AUDIT |
| D03 | Galactic rotation robustness | `V_c(R)` | 5 bins outside `10<R<16 kpc` | recorded | same as D02 | M/A | `(0.3870,0.4167)` execution record | INTERIOR | NOT INDEPENDENT | ROBUSTNESS |
| D04 | Gaia 3D kinematics | `v_phi`, gradient, `R,z` dependence | Gaia DR3 populations | execution record; source audit pending | WC-DM kinematic mapping | M/A | none yet | NONE | overlap/correlation pending | AUDIT |
| D05 | Independent stellar tracers | maser/RGB/OBA kinematics | independent tracer samples | TBD | potential gravitational-potential coupling | I/M/A | none yet | NONE | potentially useful; audit required | CANDIDATE |
| D06 | Gravitational lensing | shear/convergence/mass profile | galaxy/cluster lensing | published empirical sources | WC-DM forward structure mapping absent | E/I/M | none | NONE | potentially independent; model dependency audit | CANDIDATE |
| D07 | Galactic halo / satellites | 6D phase space, `v_esc(r)` | Gaia DR3 / satellites | Roche et al. 2024 + source chain | `M(<r;x)` / `Phi(r;x)` not locked | E/I/M | none | NONE | Gaia/systematics overlap audit required | AUDIT / CANDIDATE |
| D08 | Cluster dynamics | dispersion + lensing/X-ray/SZ | cluster observations | published empirical sources | `sigma_self(x,v,m)` absent | E/I/M | none | NONE | distinct scale; model dependency unresolved | CANDIDATE |
| D09 | Particle experiments | recoil/electron events | SENSEI / direct detection | SENSEI arXiv:2312.13342 | `sigma_WC-DM(x,m)` absent | E/I/M | none | NONE | laboratory-independent of Galactic data | QUARANTINE |
| D10 | Atomic / molecular precision | transition/frequency ratios | clocks/cavities/spectroscopy | PRL/PRX sources | WC-DM SM portal/operator absent | E/I/M | none | NONE | laboratory-independent; model coupling unresolved | QUARANTINE |
| D11 | Quantum / condensed matter | precision resonances/sensors | laboratory observables | TBD / candidate sources | direct `x` coupling absent | E/I/M/A | none | NONE | potentially independent | CANDIDATE |
| D12 | Solar-system / laboratory gravity | precision gravity / fifth-force observables | laboratory/solar-system | candidate empirical sources | `x` coupling absent | E/I/M/A | none | NONE | potentially independent | CANDIDATE |
| D13 | Astrophysical transients / timing | timing/kinematics/transients | pulsars/compact objects/transients | candidate empirical sources | `x` coupling absent | E/I/M/A | none | NONE | potentially independent | CANDIDATE |
| D14 | Cosmological observables | individually auditable observables | CMB/LSS/BAO/etc. | candidate empirical sources | WC-DM-specific forward relation absent | E/I/M/A | none | NONE | correlation/model audit required | CANDIDATE |

## Round-2 source anchors

### D09 — Direct detection

SENSEI SNOLAB: 100.72 gram-day exposure; reported low-energy electron-event data and sub-GeV DM limits. Source: arXiv:2312.13342.

Status remains `QUARANTINE` because no source-locked `sigma_WC-DM(x,m)` exists in the current WC-DM codebase.

### D10 — Atomic/precision

Relevant empirical channels include:

- Kennedy et al., PRL 125, 201302 (2020), optical-clock/cavity frequency comparison.
- Filzinger et al., PRL 134, 031001 (2025), separated clocks/cavities.
- Zhang et al., PRL 130, 251002 (2023), atomic-transition spectroscopy.
- PRX 15, 021055 (2025), 229Th nuclear-line spectroscopy.

These constrain specific SM couplings of ultralight DM. They do not establish the WC-DM `x` coupling.

### D06 — Lensing

Adhikari et al., arXiv:2401.05788, weak-lensing constraints on SIDM; arXiv:2503.03413, strong-lensing study of scalar-field DM. These remain model-specific and cannot be renamed as `x` constraints.

### D07 — Escape velocity

Roche et al., arXiv:2402.00108, Gaia DR3 6D data and Milky Way escape-velocity profile from approximately 4–11 kpc. This is a high-value independent observable candidate, but `x → M(<r)` / `Phi(r;x)` remains unlocked.

## Intersection rule

No candidate enters the canonical survivor until:

`provenance → coupling → constraint → falsification → independence`

passes.

Then:

`G_next = G_current ∩ G_candidate`.

If empty → **CHẾT**. If non-empty → **SURVIVE — KÌM TIẾP**.

Current envelope:

`G_current=(0.3928,0.4107)`

`G_cons=(0.3870,0.4167)`

These are constraint intervals, **not target values**.

**NEXT:** return to [`04_domain_search_matrix.md`](04_domain_search_matrix.md) and obey [`00_TODO_RESUME.md`](00_TODO_RESUME.md) for the actual first-open gap.