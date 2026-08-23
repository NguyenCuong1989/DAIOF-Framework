# APΩ — Domain Object Ontology

> **FLOW NODE 5/12** — entered from [`01_canonical_checkpoint.md`](01_canonical_checkpoint.md); exits to [`03_evidence_gate_and_rules.md`](03_evidence_gate_and_rules.md).

## P0 — Supreme propositions

**P0.1** `REALITY > THEORY`.

**P0.2** `EVIDENCE != INTERPRETATION`.

**P0.3** `COMPUTATION != EVIDENCE`.

**P0.4** `g_dark` cannot appear as a preselected input before constraints act on it.

**P0.5** `g_dark` is not restricted a priori to astronomical systems. Any real physical system is a candidate domain if an admissible observable has a validated coupling to `g_dark`.

**P0.6** A computational environment is an analysis instrument, not a substitute for the physical system being measured. Simulation cannot manufacture evidence absent a real-world measurement anchor.

## O1 — Central unknown

**O1.1** `g ≡ g_dark` is the unknown to infer.

**O1.2** Normalize to `x ≡ g_dark/g_crit`, with `x ∈ R`.

**O1.3** Every admissible domain must yield `G_i ⊆ R`.

**O1.4** Global survivor: `G_* = intersection_i G_i`.

**O1.5** The search space is the set of real physical systems, not merely the set of astronomical systems.

## P2 — Domain decomposition

Each domain is decomposed as:

`D_i = (E_i, I_i, M_i, A_i)`

where `E` is empirical evidence, `I` inference, `M` model relation, and `A` assumption.

**P2.1** A domain is not a homogeneous evidentiary block.

**P2.2** An inadmissible component does not invalidate the whole domain.

**P2.3** A domain may be laboratory, atomic, molecular, particle, condensed-matter, precision-measurement, solar-system, stellar, galactic, cluster, or cosmological; classification does not determine admissibility.

## E3 — Observable

An observable is an empirically measured quantity with a reality-to-observable path. Examples: `V_c`, `K_z`, `v_R`, `v_phi`, `v_z`, density, dispersion, flux, frequency, cross section.

**E3.1** The physical system containing the observable may be astronomical or terrestrial/laboratory.

**E3.2** A simulated observable is not empirical evidence unless explicitly anchored to a real measurement dataset.

## E4 — Measurement

Measurement object: `M_i = (x_i, sigma_i, U_i)`.

Missing units → `QUARANTINE`.

Missing or undocumented uncertainty → `QUARANTINE` or reduced admissibility, depending on data type.

## E5 — Provenance

`P_i = (source, dataset, sample, method, version)`.

Minimum lineage:

`source → raw → processing → observable`.

Lost lineage → `NO SIGN`.

## I6 — Inferred quantity

`X_inferred = F(E)` is inferred, not measured. The label must remain `INFERRED`.

## I7 — Validated relation

A relation `R:E→X` enters computation only when definition, dimensional consistency, domain validity, component provenance, and non-circularity are explicit.

Distinguish empirical relations from model relations.

## M8 — Model

A model `M(g,theta;D)` maps data and parameters to predictions. `M(g) !→ E`. Any constraint dependent on a model must carry that dependency.

## A9 — Assumption

Anything not established from evidence is tagged `A`. Example: `q(x)=1-0.6x` is a model mapping unless independently empirically validated.

Running code repeatedly cannot promote an assumption to evidence.

## C10 — Constraint

Canonical form:

`C_i(g; D_i, theta_i)`

and:

`G_i = {g : C_i(g) satisfies criterion_i}`.

A valid constraint must be capable of excluding at least one part of the candidate domain. Otherwise it is `NON-INFORMATIVE`.

## D11–D14 — Direction

- Lower bound: `g > g_low`.
- Upper bound: `g < g_high`.
- Interior: `g_a < g < g_b`.
- Exterior exclusion: `g < g_a OR g > g_b`.

The 360-degree objective is maximizing independent boundary information, not maximizing the number of papers or domains.

## I15 — Independence

Independence must be assessed across sample, observable, systematic uncertainty, processing, and model dependency. If correlated, treat as `CORRELATED` and do not count it as an independent likelihood without a joint covariance treatment.

## X16 — Candidate-domain object

Canonical candidate schema:

`D_j = (O_j, M_j, P_j, R_j, C_j, G_j, Delta_j)`

Missing a critical link → `QUARANTINE`.

## R17 — Domain-search rules

Do not search for domains that support `x≈0.4`. Search for empirical observables capable of constraining `x`.

Do not search by target value. Do not reject a domain wholesale because one theory component is disputed. Do not retain a domain because consensus accepts it. Evaluate component-by-component.

**R17.1 — System-wide domain rule:** Search every real physical system in which `g_dark` could couple to an observable. Do not impose an astronomical-only prior.

**R17.2 — Cross-system rule:** A laboratory or terrestrial domain is admissible on exactly the same evidence gate as an astronomical domain; physical location is neither a privilege nor a rejection criterion.

**R17.3 — Environment rule:** Code may reproduce controlled mathematical/physical conditions needed to test a relation, but the resulting computation remains non-evidence until anchored to admissible real measurements.

**R17.4 — Information rule:** The existence of information/data inside a computational system does not itself establish a physical coupling. The coupling must be independently defined and testable.

## G18 — Candidate-domain families

1. Galactic dynamics
2. Stellar populations / independent tracers
3. Gravitational lensing
4. Galactic structure
5. Cluster dynamics
6. Cosmological observables, only through an explicit empirical coupling
7. Particle experiments
8. Atomic / molecular precision measurements
9. Quantum / condensed matter, only with an explicit physical coupling
10. Solar-system / laboratory gravity
11. Astrophysical transients
12. Time-domain / precision measurements
13. Laboratory information-bearing physical systems, only where a measurable physical observable and coupling exist

## G19 — Eight-entry admission gate

Every candidate must answer:

1. What is the observable?
2. Who measured it?
3. Where is the raw measurement?
4. What are uncertainty/systematics?
5. What relation couples the observable to `g`?
6. Is that relation empirical or model-based?
7. What interval of `g` is excluded?
8. What is the independence/correlation status?

Failures:

- no coupling → `DOMAIN REJECT`
- no raw lineage → `QUARANTINE`
- no exclusion power → `NON-INFORMATIVE`
- unknown independence → `DO NOT COMBINE`

## G20 — Canonical state before new search

Current full target constraint: `(0.3928,0.4107) g_crit`.

Current conservative envelope: `(0.3870,0.4167) g_crit`.

These are constraint targets, not target values. The next operation is **domain discovery first, computation second**.

## G21 — System-wide search objective

The next discovery pass must search for admissible constraints across the full physical-system space:

`astronomical ∪ laboratory ∪ atomic ∪ molecular ∪ particle ∪ condensed-matter ∪ precision-measurement ∪ solar-system ∪ other real physical systems`.

Priority is not given to a domain because it is theoretically fashionable or because it is expected to agree with the current survivor. Priority is given to domains with:

`observable → measurement → provenance → validated coupling → falsifiable constraint`.

The objective is to maximize independent boundary information on all sides of the current survivor while avoiding target-fitting and double-counting.

**NEXT NODE:** [`03_evidence_gate_and_rules.md`](03_evidence_gate_and_rules.md).