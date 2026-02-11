# Agent-Oriented Runtime Prompt Guide

Use this prompt block for Codex/agents working on runtime stabilization in this repository.

## Core contract
- Exit semantics are strict across runtime scripts:
  - `0` => OK
  - `1` => WARN
  - `2` => FAIL
- Always run `tools/runtime/preflight.sh --summary` before running runtime entrypoints.
- If preflight returns `2`, stop execution immediately.

## Runtime entrypoint policy
Inject this guard in shell entrypoints:

```bash
./tools/runtime/preflight.sh --summary
rc=$?
if [ "$rc" -eq 2 ]; then
  echo "[FATAL] Preflight FAIL"
  exit "$rc"
fi
```

## Required scripts
- `tools/runtime/preflight.sh`
- `tools/runtime/bootstrap_runtime.sh`
- `tools/runtime/daily_dnr_run.py`
- `tools/runtime/launchd_safe_wrapper.sh`
- `tools/runtime/rotate_hyperai_logs.sh`
- `tools/runtime/runtime_health_daemon.py`
- `tools/runtime/test_runtime_matrix.sh`

## Validation checklist
```bash
bash -n tools/runtime/preflight.sh
bash -n tools/runtime/bootstrap_runtime.sh
bash -n tools/runtime/rotate_hyperai_logs.sh
bash -n tools/runtime/launchd_safe_wrapper.sh
bash -n tools/runtime/test_runtime_matrix.sh
python3 -m py_compile tools/runtime/daily_dnr_run.py
python3 -m py_compile tools/runtime/runtime_health_daemon.py
python3 -m unittest tests.runtime.test_runtime_tools
```

## Coding rules
- Keep scripts deterministic and idempotent.
- Prefer explicit paths and environment overrides.
- Avoid silent failures; print diagnostics.
- Use portable shell behavior (`df -Pk`, GNU/BSD stat fallback).
