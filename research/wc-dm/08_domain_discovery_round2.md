# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
# ORIGINATOR / CREATOR: alpha_prime_omega — Nguyễn Đức Cường
# STATUS: DISCOVERY RECORD — NON-AUTONOMOUS — NON-OWNERLESS
# TRACEABILITY: Canon -> COG -> Projection(Π) -> Artifact
# =============================================================================

# APΩ — WC-DM 2.1 — DOMAIN DISCOVERY ROUND 2

Checkpoint date: 2026-08-24
Canonical state entering round:

`G_full = (0.3928,0.4107)`

`G_cons = (0.3870,0.4167)`

`SURVIVE — g_dark NOT CONCLUDED`

## 0. ROUND LAW

Round 2 is **discovery and coupling audit first**.

No target fitting.
No selection of evidence because it overlaps `x≈0.4`.
No intersection unless the complete chain passes:

`observable → measurement → provenance → validated coupling to x → falsifiable constraint → independence audit → intersection`.

A published constraint on a generic dark-matter parameter is **not** a constraint on `x = g_dark/g_crit` unless WC-DM 2.1 supplies the forward mapping.

---

## D-09 — PARTICLE / DIRECT DETECTION

### Observable
Low-energy recoil / electron-event spectra from direct-detection experiments.

### Empirical source found
SENSEI at SNOLAB reported a 100.72 gram-day exposure, 55 two-electron events, 4 three-electron events, and no 4–10 electron events; the collaboration derived constraints on sub-GeV DM interacting with electrons and nuclei.

Source: SENSEI Collaboration, arXiv:2312.13342.

### Evidence classification
- Observable: `E`
- Measurement: `E`
- Published DM interpretation: `I/M`
- WC-DM mapping `σ_WC-DM(x,m)`: **not source-locked in current codebase**

### Gate result
The experimental datum is real and independently useful as a particle-physics candidate. However:

`event spectrum → σ_limit → σ_WC-DM(x,m)`

is not currently established.

### Status
`QUARANTINE — COUPLING UNLOCKED`

### Direction
`NONE`

### Intersection
**FORBIDDEN.**

### Falsification readiness
Potentially strong once the exact WC-DM scattering relation is source-locked.

---

## D-10 — ATOMIC / MOLECULAR / PRECISION METROLOGY

### Observable
Atomic transition frequencies, clock-frequency ratios, cavity-frequency ratios and related precision time-series.

### Empirical sources found
1. Kennedy et al., PRL 125, 201302 (2020): frequency comparisons using Sr optical lattice clock, cryogenic Si cavity and H maser; bounds on ultralight-DM couplings over approximately `10^-16–10^-21 eV`.
2. Filzinger et al., PRL 134, 031001 (2025): space-time separated atomic clocks/cavities; constraints on scalar-DM coupling to electrons over `10^-19–2×10^-15 eV/c^2`.
3. Zhang et al., PRL 130, 251002 (2023): atomic-transition spectroscopy constraining scalar/pseudoscalar UBDM couplings to SM fields.
4. 229Th nuclear-line spectroscopy analysis, PRX 15, 021055 (2025), probing ultralight-DM couplings to quarks/gluons.

### Evidence classification
- Frequency measurements: `E`
- Reported coupling limits: `I/M`
- Couplings to photons/electrons/quarks/gluons: model-specific parameterization
- WC-DM coupling from `x` to those SM operators: **not established**

### Gate result
The domain contains high-quality empirical measurements and genuine independent observables. It does **not** yet supply an admissible constraint on `x` because the current WC-DM 2.1 ontology does not define a source-locked portal/operator relation:

`x → SM coupling → frequency shift`.

### Status
`QUARANTINE — COUPLING UNLOCKED`

### Direction
`NONE`

### Intersection
**FORBIDDEN.**

### Important negative result
The existence of atomic constraints does not authorize importing a scalar/dilaton/axion coupling as `g_dark`. That would be concept substitution.

---

## D-06 — GRAVITATIONAL LENSING

### Observable
Strong/weak-lensing shear, convergence and reconstructed mass profiles.

### Empirical source found
Adhikari et al. (arXiv:2401.05788) use weak-lensing measurements around clusters and report constraints on isotropic elastic SIDM, including `σ/m < 1 cm^2/g` at 95% CL under their SIDM model construction.

A 2025 strong-lensing study (arXiv:2503.03413) explicitly maps lensing observables to solitonic-core properties in a scalar-field-DM framework.

### Evidence classification
- Lensing observables: `E`
- Reconstructed mass: `I`
- SIDM/SFDM mapping: `M`
- WC-DM 2.1 mapping `x → lensing observable`: **not source-locked**

### Gate result
The measurements are admissible as empirical gravitational observables. Existing model-specific particle constraints cannot be renamed `g_dark`.

### Status
`CANDIDATE — COUPLING AUDIT REQUIRED`

### Direction
`NONE`

### Intersection
**FORBIDDEN.**

---

## D-01 / D-07 — GALACTIC ESCAPE VELOCITY / SATELLITE-HALO DYNAMICS

### New empirical source
Roche et al., Gaia DR3 escape-velocity profile (arXiv:2402.00108): 6D stellar kinematics, escape-velocity profile from approximately 4–11 kpc, and an inferred Milky Way mass model.

### Evidence classification
- Gaia 6D phase-space measurements: `E`
- Escape-velocity profile: `I`
- NFW halo inference: `M`
- WC-DM `x → M(<r)` relation: **not source-locked**

### Gate result
This is a genuinely different observable from the current `V_c(R)` channel and is therefore a high-value candidate for the 360° search. However, the current framework has not yet established an empirical/validated relation from the measured escape-velocity profile to `x`.

### Status
`AUDIT / CANDIDATE`

### Direction
`NONE` until WC-DM mass-profile coupling is locked.

### Independence
Not automatically independent of Galactic kinematic evidence. Shared Gaia systematics, tracer populations, spatial coverage and inferred gravitational potential must be audited.

### Intersection
**FORBIDDEN pending coupling + covariance audit.**

---

## ROUND-2 VERDICT

No new numerical `G_i` is admitted in Round 2.

This is a **valid negative result**, not a failed search.

The round establishes that:

1. Direct detection has real particle measurements but lacks a WC-DM-specific `σ(x,m)` relation.
2. Atomic/precision metrology has real measurements and strong independent observables but lacks a WC-DM-specific SM-portal relation.
3. Lensing has real mass observables but published bounds are model-specific and cannot be imported as `x` bounds.
4. Gaia escape velocity / satellite-halo dynamics provides a promising independent observable channel, but requires an explicit WC-DM mass-profile coupling before admission.

Therefore:

`G_current` remains unchanged.

`G_full = (0.3928,0.4107)`

`G_cons = (0.3870,0.4167)`

`SURVIVE — g_dark NOT CONCLUDED`

## NEXT GATES

Priority order:

1. Lock a WC-DM forward relation for `M(<r;x)` / `Φ(r;x)` and test Gaia escape velocity + satellite dynamics.
2. Audit whether any existing WC-DM relation provides `σ_self(x,v,m)`; if yes, revisit cluster/SIDM observations as a real coupling chain rather than importing SIDM limits.
3. Search for a source-locked portal/operator relation that connects the existing `g_dark` object to atomic/particle observables.
4. Continue lensing only where the WC-DM forward model is explicit.

No target value may be introduced during these searches.
