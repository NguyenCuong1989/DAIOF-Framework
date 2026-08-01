---
layout: default
title: Live Runtime Probe Receipt (Template)
doctrine_version: 0.1.0
source_of_truth: github_repo
last_synced_from: null
last_verified_at: 2026-08-01T00:00:00Z
runtime_consumer: DAIOF-Framework
connector_state: null
---

# Live Runtime Probe Receipt

Use this receipt for any runtime-level claim.  
Fail-closed policy: without a fresh receipt and recent timestamp, do not classify as `CURRENT_VERIFIED`.

## Probe identity

- cycle_id:
- component:
- environment:
- observer:
- observed_at (UTC):

## Required probes

- source_present:
- config_present:
- process_running:
- process_evidence (PID / command / host):
- port_listening:
- port_evidence (host:port / listener output):
- endpoint_responding:
- endpoint_evidence (request + status + latency):
- route_registered:
- upstream_reachable:
- functional_test_passed:
- authority_bound:

## Execution receipt

- receipt_id:
- receipt_path_or_uri:
- integrity_hash (sha256):
- evidence_provenance:

## Decision mapping

- classification:
- confidence (0..1):
- missing_evidence:
- contradiction_state:
- selected_decision:

## Notes

- risks:
- reconciliation_actions:
- next_questions (max 3):

