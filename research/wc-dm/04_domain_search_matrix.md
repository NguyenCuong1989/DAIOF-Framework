# APΩ — 360° Domain Search Matrix

> **FLOW NODE 8/12** — entered from [`LAW_UNIVERSAL_ROOT_CAUSE_INFERENCE.md`](LAW_UNIVERSAL_ROOT_CAUSE_INFERENCE.md); exits to the **ACTIVE GAP AUDIT** identified by [`00_TODO_RESUME.md`](00_TODO_RESUME.md). Discovery has no constraint authority.

## Objective

Do not add domains for decoration or for target confirmation. Find real observables that can produce admissible lower, upper, or interior constraints on `x = g_dark/g_crit`.

## Existing matrix

| Domain | Observable | Sample | Status | Coupling | Current bound | Direction | Independence |
|---|---|---|---|---|---|---|---|
| Physical | `S_max`, `sigma_self` | WC-DM execution | recorded | model/physics mapping | `0.387 < x < 0.795` | two-sided | audit required |
| Local density | `rho_DM` | 903 Cepheids context | recorded | `q(x)` | `x ≲ 0.4167` | upper | correlated with RC context |
| Rotation curve | `V_c(R)` | 903 Cepheids | execution record | `q(x)` | `0.3928 < x < 0.4107` | interior | correlated with density context |
| Robust RC | `V_c(R)` | 5 bins outside `10<R<16 kpc` | robustness | same | `0.3870 < x < 0.4167` | interior | not new evidence |
| K_z | `K_z` | 16,269 SEGUE G dwarfs | execution record | WC-DM mapping | `0.1548 < x < 0.5573` | two-sided | different sample; model dependence |
| Gaia 3D | `v_phi`, gradient | Gaia stellar sample | execution record | WC-DM mapping | no current narrowing | test | audit required |
| New domain | `?` | `?` | SEARCH | `?` | `?` | lower/upper/interior | `?` |

## Priority search directions

### A. Independent galactic dynamics

Search for measurements that are not merely re-expressions of the same 903-Cepheid rotation curve:

- independent tracer populations;
- vertical force profiles;
- stellar velocity dispersions;
- maser kinematics;
- satellite motions;
- independent halo-shape constraints.

### B. Gravitational lensing

Look for measured lensing observables where a specific WC-DM mass/geometry coupling can be derived without importing an entire disputed theory as evidence. Record whether the relation is empirical, geometric, or model-dependent.

### C. Cluster observables

Search velocity dispersion, lensing mass, X-ray/SZ measurements, but only admit a constraint if the mapping to `x` is explicit and auditable.

### D. Particle experiments

Search direct detection, scattering, collider production, and decay/lifetime measurements. The key gate is whether the experiment constrains the exact WC-DM parameter `g_dark`, rather than a different parameter that is only rhetorically identified with it.

### E. Atomic / molecular precision data

Search spectroscopy, transition frequencies, clocks, and molecular measurements only when an explicit coupling to `g_dark` exists. Standard quantum/atomic theory is not itself evidence for `g_dark`.

### F. Laboratory / solar-system gravity

Search precision measurements only if a direct, parameterized coupling from `g_dark` to the measured observable is available.

## Candidate scoring fields

For every candidate record:

`ID, observable, sample, raw source, measurement method, units, uncertainty, systematics, validated relation, relation class (empirical/model), coupling path, excluded interval, direction, sample overlap, shared systematic, model dependency, reproducibility, status`.

## Admission states

- `ADMISSIBLE` — all critical gates pass.
- `QUARANTINE` — provenance/raw measurement or key metadata incomplete.
- `CORRELATED` — usable but cannot be combined as independent evidence.
- `NON-INFORMATIVE` — cannot exclude any `x` region.
- `MODEL-DEPENDENT` — usable conditionally with explicit dependency.
- `REJECT` — no defensible coupling to `g_dark`.

## Search rule

The search query must be generated from the observable and coupling requirements, **not** from `x≈0.4`. Candidate discovery precedes numerical fitting.

## 360-degree success condition

The objective is not merely a narrow interval. It is a provenance-locked intersection with independent boundary information:

`G_360 = intersection_i G_i`

where each newly admitted constraint has demonstrated exclusion power and its correlation structure is explicitly accounted for.

**NEXT NODE:** [`00_TODO_RESUME.md`](00_TODO_RESUME.md) → execute the **FIRST OPEN GAP only**.