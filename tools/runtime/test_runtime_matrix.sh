#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

TMP_ROOT="$(mktemp -d)"
trap 'rm -rf "$TMP_ROOT"' EXIT

pass_count=0
fail_count=0

assert_exit() {
  local expected="$1"
  shift
  set +e
  "$@" >/dev/null 2>&1
  local rc=$?
  set -e
  if [[ "$rc" -eq "$expected" ]]; then
    echo "PASS rc=$rc :: $*"
    pass_count=$((pass_count + 1))
  else
    echo "FAIL expected=$expected got=$rc :: $*"
    fail_count=$((fail_count + 1))
  fi
}

# Scenario 1: Missing entrypoints => FAIL
mv tools/runtime/bootstrap_runtime.sh "$TMP_ROOT/bootstrap_runtime.sh.bak"
assert_exit 2 ./tools/runtime/preflight.sh --summary
mv "$TMP_ROOT/bootstrap_runtime.sh.bak" tools/runtime/bootstrap_runtime.sh

# Scenario 2: Low disk simulation by invalid mount => FAIL
assert_exit 2 env DISK_PATH="/path/does/not/exist" ./tools/runtime/preflight.sh --summary

# Scenario 3: Log pressure => WARN
mkdir -p "$TMP_ROOT/logs"
truncate -s 21M "$TMP_ROOT/logs/heavy.log"
assert_exit 2 env DISK_PATH="/" LOG_DIR="$TMP_ROOT/logs" DB_PATH="$TMP_ROOT/missing.db" ./tools/runtime/preflight.sh --summary

# Scenario 4: DB integrity fail => FAIL
mkdir -p "$TMP_ROOT/db"
printf 'not-a-sqlite-db' > "$TMP_ROOT/db/corrupt.sqlite"
assert_exit 2 env DISK_PATH="/" DB_PATH="$TMP_ROOT/db/corrupt.sqlite" LOG_DIR="$TMP_ROOT/logs" ./tools/runtime/preflight.sh --summary

# Scenario 5: DB lock simulation (single lock should warn) for daily runner
mkdir -p "$TMP_ROOT/state/dnr" "$TMP_ROOT/dblog" "$TMP_ROOT/db"
sqlite3 "$TMP_ROOT/db/memory.sqlite" "VACUUM;"
: > "$TMP_ROOT/state/dnr.lock"
assert_exit 1 env SKIP_PREFLIGHT=1 python3 tools/runtime/daily_dnr_run.py --db-path "$TMP_ROOT/db/memory.sqlite" --marker-dir "$TMP_ROOT/state/dnr" --lock-file "$TMP_ROOT/state/dnr.lock" --log-dir "$TMP_ROOT/dblog"

# Scenario 6: No launchctl environment + healthy local inputs => WARN (jobs not loaded)
rm -f "$TMP_ROOT/state/dnr.lock"
assert_exit 1 env DISK_PATH="/" DB_PATH="$TMP_ROOT/db/memory.sqlite" LOG_DIR="$TMP_ROOT/logs" JOB_PATTERN="unlikely-pattern" ./tools/runtime/preflight.sh --summary

echo "MATRIX_RESULT pass=$pass_count fail=$fail_count"
if [[ "$fail_count" -gt 0 ]]; then
  exit 2
fi
exit 0
