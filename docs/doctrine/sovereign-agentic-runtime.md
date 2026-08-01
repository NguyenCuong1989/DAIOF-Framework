---
layout: default
title: Sovereign Agentic Runtime Doctrine
doctrine_version: 0.1.0
source_of_truth: github_repo
last_synced_from: null
last_verified_at: 2026-05-14T23:47:26Z
runtime_consumer: DAIOF-Framework
connector_state: null
---

# Sovereign Agentic Runtime (SAR) — Canonical Doctrine

This repository (`NguyenCuong1989/DAIOF-Framework`) is the canonical source-of-truth for the **Sovereign Agentic Runtime (SAR)** doctrine, its connector lifecycle, runtime state machine, and execution evidence.

## 1) Definition (platform-grade capability)

**Sovereign Agentic Runtime (SAR)** is a platform-grade runtime that:
- Executes agentic plans across tools and connectors with **bounded authority**.
- Maintains an explicit, inspectable **state machine** for connector and runtime health.
- Produces **execution evidence** (audit events + snapshots) so actions are reviewable and recoverable.
- Enforces safety principles: **An toàn**, **Đường dài**, **Tin vào số liệu**, **Hạn chế rủi ro từ con người và AI khi thực thi thủ công**.

SAR is not “a chat”. SAR is an operational runtime with governance, lifecycle, and evidence.

## 2) Open-source boundary (what is / is not in this repo)

This repository is the open implementation boundary for:
- Doctrine and governance: definitions, invariants, and operating rules.
- Registries: machine-readable connector and evidence registries.
- Runtime inspection surfaces: state machine spec and probe requirements.

This repository does **not** contain:
- Secrets, tokens, or private connector credentials.
- Proprietary operational artifacts that cannot be redistributed.

Where external tooling (Asana/Figma/Linear/Airtable) is used, this repo must still contain **enough mirrored evidence** to remain canonical if those tools drift or become inaccessible.

## 3) Sovereign ownership

**Sovereign ownership and authorship** of SAR doctrine belongs to:
- Architect: **Nguyễn Đức Cường**
- Identity: **alpha_prime_omega**

Contributions are welcome, but doctrine changes must preserve sovereign constraints and safety invariants.

## 4) Canonical docs in this repo

- Connector lifecycle: `docs/runtime/connector-lifecycle.md`
- Runtime state machine + probes: `docs/runtime/state-machine.md`
- Source-of-truth metadata spec: `docs/doctrine/source-of-truth-metadata.md`
- Connector registry: `docs/registry/connectors.yml`
- Execution evidence registry + templates: `docs/evidence/README.md`

## 5) Canonical authority path map (single source-of-truth)

- Doctrine authority: `docs/doctrine/sovereign-agentic-runtime.md`
- Metadata authority: `docs/doctrine/source-of-truth-metadata.md`
- Runtime transition authority: `docs/runtime/state-machine.md`
- Connector lifecycle authority: `docs/runtime/connector-lifecycle.md`
- Connector state authority: `docs/registry/connectors.yml`
- Evidence policy authority: `docs/evidence/README.md`

Legacy or mirrored documents may exist in other folders for compatibility, but authority remains with the paths above.

## 6) Verification boundary (fail-closed)

Design truth is not runtime truth. A `CURRENT_VERIFIED` runtime claim is valid only when live probe evidence exists and includes a recent verification timestamp; otherwise classification must remain `STALE_REQUIRES_LIVE_VERIFY`.
