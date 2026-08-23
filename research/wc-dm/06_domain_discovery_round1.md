# APΩ — WC-DM 2.1 — DOMAIN DISCOVERY ROUND 1

> **HISTORICAL FLOW NODE.** Entered from [`04_domain_search_matrix.md`](04_domain_search_matrix.md); exits to [`08_domain_discovery_round2.md`](08_domain_discovery_round2.md). Immutable discovery lineage; cannot override current resume authority [`00_TODO_RESUME.md`](00_TODO_RESUME.md).

Creator: alpha_prime_omega — Nguyễn Đức Cường  
System: APΩ / WC-DM Evidence-First Boundary-Squeezing Protocol  
Date: 2026-08-24

## 0. Discovery rule

This round is **candidate discovery only**. No new value of `x = g_dark/g_crit` is selected or fitted.

Current canonical state remains:

- `G_full = (0.3928, 0.4107)`
- `G_cons = (0.3870, 0.4167)`
- `SURVIVE — g_dark not concluded`

The purpose is to locate observables that can, after coupling audit, generate LOWER / UPPER / INTERIOR constraints on `x`.

## 1. Candidate D-01 — Milky Way satellite dynamics

### Observable

6D phase-space measurements of Milky Way satellite galaxies: positions/distances, proper motions, radial velocities, hence orbital velocity information.

### Empirical status

The measurements are observational. Gaia proper motions provide the kinematic component. The downstream halo-mass inference is **not itself a raw observable**.

### Provenance found

Callingham et al., MNRAS: 10 classical Milky Way satellites with six-dimensional phase-space measurements were used to infer a Milky Way halo mass of `1.17^{+0.21}_{-0.15} × 10^12 M_sun` at 68% confidence. The analysis uses a distribution-function calibration against EAGLE/AURIGA simulations, so the inferred halo mass is model-dependent rather than direct evidence of a WC-DM coupling. [Source: Oxford Academic MNRAS, https://academic.oup.com/mnras/article/484/4/5453/5307100]

An independent Gaia-era analysis using satellite proper motions reports `0.58^{+0.15}_{-0.14} × 10^12 M_sun` within 64 kpc and `1.43^{+0.35}_{-0.32} × 10^12 M_sun` within 273 kpc, demonstrating that satellite dynamics constitute a distinct observable channel but also that halo-mass inference is analysis-dependent. [Source: Oxford Academic MNRAS, https://academic.oup.com/mnras/article/494/4/5178/5824653]

### Coupling to x

Required path:

`observed satellite phase space → gravitational potential / enclosed mass → WC-DM prediction M(<r;x) → constraint C(x)`.

This path is **not yet validated for WC-DM 2.1** in the current round.

### Gate assessment

- Observable: **PASS**
- Measurement/provenance: **PASS**
- Units/uncertainties: **PASS at source level; exact raw table still required**
- Coupling to `x`: **NOT YET ESTABLISHED**
- Constraint direction: **potentially interior / two-sided**
- Independence: **potentially strong relative to 903-Cepheid RC**, but shared Galactic potential/systematic dependencies must be audited
- Numerical `G_i`: **NOT COMPUTED**

### Status

`AUDIT / CANDIDATE`

**No intersection performed.**

## 2. Candidate D-02 — Direct dark-matter detection / sub-GeV scattering

### Observable

Low-energy recoil/event spectra in cryogenic and semiconductor detectors; the observable is an event count/energy spectrum, not a theory prediction.

### Provenance found

A 2026 CRESST perspective documents experimentally measured low-energy backgrounds and prior exclusion sensitivity for sub-GeV dark matter, including sensitivity down to tens of MeV masses. It also explicitly notes a low-energy excess that overlaps part of the DM search region, so background treatment is a material systematic. [Source: Communications Physics, 2026, https://doi.org/10.1038/s42005-025-02476-5]

### Coupling to x

Required path:

`event spectrum → scattering-rate limit → σ(parameter) → WC-DM relation σ(x,m)`.

The exact WC-DM 2.1 relation between `g_dark` and the experimentally constrained cross section has **not yet been source-locked**.

### Gate assessment

- Observable: **PASS**
- Measurement/provenance: **PASS**
- Background/systematic: **KNOWN / MUST BE AUDITED**
- Coupling to `x`: **NOT YET ESTABLISHED**
- Constraint direction: potentially upper/lower depending on WC-DM cross-section law
- Independence: laboratory/particle observable is potentially highly independent of Galactic kinematics
- Numerical `G_i`: **NOT COMPUTED**

### Status

`QUARANTINE — COUPLING UNLOCKED`

The experiment is not admitted as a constraint until the exact WC-DM scattering relation is established.

## 3. Candidate D-03 — Milky Way halo mass from independent satellite dynamics

This is retained separately from D-01 only as an **independence audit branch**, not as a second independent domain yet. Different satellite datasets/estimators can still share the same latent Galactic potential and simulation calibration.

Status: `CORRELATION AUDIT REQUIRED`.

## 4. Candidate D-04 — Gravitational lensing

Search result confirms that strong-lensing observables have been used to constrain dark-matter free-streaming/halo-scale properties, but those published constraints are generally on specific particle models or derived halo parameters. A direct WC-DM `x` coupling is not established in this round.

Example: joint strong-lensing/Ly-alpha/Milky-Way-satellite analysis constrains a warm-DM half-mode scale and corresponding particle mass under a specified model. This is not admissible for `x` without an explicit WC-DM mapping. [Source: Oxford Academic MNRAS, https://academic.oup.com/mnras/article/506/4/5848/6318874]

Status: `CANDIDATE — COUPLING AUDIT REQUIRED`.

## 5. Candidate D-05 — Atomic / molecular precision measurements

Search target: spectroscopy, clocks, molecular transitions and fifth-force/dark-sector observables with a direct parameterized coupling to `g_dark`.

No admissible source-locked WC-DM coupling was established in this round.

Status: `SEARCH CONTINUES`.

## 6. Candidate matrix after Round 1

| ID | Domain | Observable | Provenance | Coupling to x | Bound | Direction | Independence | Status |
|---|---|---|---|---|---|---|---|---|
| D-01 | Satellite dynamics | 6D satellite phase space | MNRAS/Gaia-era studies | not yet WC-DM locked | — | potentially 2-sided/interior | potentially high vs Cepheids | AUDIT/CANDIDATE |
| D-02 | Direct detection | recoil/event spectrum | CRESST 2026 + experiment record | not yet WC-DM locked | — | model-dependent | potentially high | QUARANTINE |
| D-03 | Independent satellite estimators | satellite kinematics | multiple Gaia-era analyses | same latent potential | — | potentially 2-sided | correlated with D-01 | CORRELATION AUDIT |
| D-04 | Gravitational lensing | lensing observables | MNRAS lensing analysis | no WC-DM mapping yet | — | potentially 2-sided | potentially high | CANDIDATE |
| D-05 | Atomic/molecular | transition frequencies | not yet source-locked | no WC-DM mapping yet | — | potentially either | potentially high | SEARCH CONTINUES |

## 7. Important negative result

Round 1 found **no new admissible numerical constraint on `x`** that can be honestly intersected with the canonical survivor.

This is a valid discovery result: the domain has observable data, but the crucial `observable → WC-DM g_dark` coupling is not yet locked.

Therefore:

`G_current` is unchanged.

No target-fitting has been performed.

No new evidence has been counted.

## 8. Next execution gates

1. Recover exact raw satellite phase-space tables and uncertainty structure.
2. Determine whether WC-DM 2.1 predicts a unique mass/potential observable as a function of `x` without importing an unvalidated theory layer.
3. Recover exact direct-detection cross-section relation for WC-DM 2.1, if one exists.
4. Search lensing observables for a direct, auditable WC-DM coupling.
5. Search atomic/molecular precision data only where a concrete coupling exists.
6. Do not compute `G_i` until the coupling passes the ontology gate.

## 9. Canonical effect of this checkpoint

`G_full = (0.3928,0.4107)` — unchanged.  
`G_cons = (0.3870,0.4167)` — unchanged.  
`SURVIVE — g_dark not concluded.`

This file records the discovery work completed so far and is intentionally conservative: **candidate discovery is not constraint admission**.

**NEXT:** [`08_domain_discovery_round2.md`](08_domain_discovery_round2.md).