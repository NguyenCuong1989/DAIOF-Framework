#!/usr/bin/env bash
set -euo pipefail

SCRIPT_PATH="${1:-${ORIG:-$HOME/workbench/daily_dnr_run.py}}"
if [[ $# -gt 0 ]]; then
  shift
fi

ERR_LOG="${ERR_LOG:-$HOME/.hyperai/logs/os_master_error.log}"
RUN_LOG="${RUN_LOG:-$HOME/.hyperai/logs/os_master.log}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

mkdir -p "$(dirname "$ERR_LOG")"

ts() {
  date '+%Y-%m-%dT%H:%M:%S%z'
}

./tools/runtime/preflight.sh --summary >> "$RUN_LOG" 2>> "$ERR_LOG" || rc=$?
rc="${rc:-0}"
if [[ "$rc" -eq 2 ]]; then
  echo "$(ts) [FATAL] Preflight FAIL" >> "$ERR_LOG"
  exit 2
fi

if [[ ! -f "$SCRIPT_PATH" ]]; then
  echo "$(ts) Missing entrypoint: $SCRIPT_PATH" >> "$ERR_LOG"
  sleep 2
  exit 0
fi

if ! "$PYTHON_BIN" "$SCRIPT_PATH" "$@" >> "$RUN_LOG" 2>> "$ERR_LOG"; then
  echo "$(ts) Execution fail for $SCRIPT_PATH" >> "$ERR_LOG"
  sleep 2
  exit 0
fi

exit 0
