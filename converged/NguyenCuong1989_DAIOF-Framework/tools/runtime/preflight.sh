#!/usr/bin/env bash
set -euo pipefail

MIN_FREE_GB="${MIN_FREE_GB:-15}"
DISK_PATH="${DISK_PATH:-/Users/andy}"
DB_PATH="${DB_PATH:-$HOME/.hyperai/db/memory.sqlite}"
LOG_DIR="${LOG_DIR:-$HOME/.hyperai/logs}"
JOB_PATTERN="${JOB_PATTERN:-hyperai|daily-dnr-runner}"
SUMMARY_ONLY=0

REQUIRED_SCRIPTS=(
  "tools/runtime/preflight.sh"
  "tools/runtime/daily_dnr_run.py"
  "tools/runtime/launchd_safe_wrapper.sh"
  "tools/runtime/rotate_hyperai_logs.sh"
  "tools/runtime/bootstrap_runtime.sh"
)

if [[ "${1:-}" == "--summary" ]]; then
  SUMMARY_ONLY=1
fi
STATE_DIR="${STATE_DIR:-$HOME/.hyperai/state}"
DB_PATH="${DB_PATH:-$HOME/Desktop/workbench/hyperai_eternal_memories.db}"
JOB_FILTER="${JOB_FILTER:-hyperai}"
DNR_PATH="${DNR_PATH:-$HOME/workbench/daily_dnr_run.py}"
LOG_DIR="${LOG_DIR:-$HOME/.hyperai/logs}"

status_line() {
  local label="$1"
  local state="$2"
  local detail="$3"
  if (( SUMMARY_ONLY == 0 )); then
    printf '%s: %s (%s)\n' "$label" "$state" "$detail"
  fi
}

check_disk() {
  if [[ ! -d "$DISK_PATH" ]]; then
    status_line "DISK" "FAIL" "path not found: $DISK_PATH"
    return 2
  fi

  local free_kb
  free_kb="$(df -Pk "$DISK_PATH" | awk 'NR==2 {print $4}')"

  if [[ -z "$free_kb" ]]; then
    status_line "DISK" "FAIL" "unable to read free space"
    return 2
  fi

  if (( free_kb < MIN_FREE_GB * 1024 * 1024 )); then
    status_line "DISK" "FAIL" "free < ${MIN_FREE_GB}GB"
    return 2
  fi

  local free_gb
  free_gb=$((free_kb / 1024 / 1024))
  status_line "DISK" "OK" "${free_gb}GB free (threshold ${MIN_FREE_GB}GB)"
  return 0
}

check_entrypoints() {
  local missing=0
  for file in "${REQUIRED_SCRIPTS[@]}"; do
    if [[ ! -f "$file" ]]; then
      status_line "ENTRYPOINT" "FAIL" "missing $file"
      missing=1
    fi
  done

  if (( missing == 1 )); then
    return 2
  fi

  status_line "ENTRYPOINT" "OK" "all required scripts present"
  return 0
}

check_jobs() {
  if ! command -v launchctl >/dev/null 2>&1; then
    status_line "JOBS" "WARN" "launchctl not available"
    return 1
  fi

  if launchctl list 2>/dev/null | grep -E "$JOB_PATTERN" >/dev/null; then
    status_line "JOBS" "OK" "launchd jobs matched pattern: $JOB_PATTERN"
    return 0
  fi

  status_line "JOBS" "WARN" "launchd jobs not loaded"
  return 1
}

check_db_integrity() {
  if [[ ! -f "$DB_PATH" ]]; then
    status_line "DB" "WARN" "missing database: $DB_PATH"
    return 1
  fi

  if ! command -v sqlite3 >/dev/null 2>&1; then
    status_line "DB" "WARN" "sqlite3 command unavailable"
    return 1
  fi

  local result
  result="$(sqlite3 "$DB_PATH" 'PRAGMA integrity_check;' 2>/dev/null | tr -d '\r')"

  if [[ "$result" == "ok" ]]; then
    status_line "DB" "OK" "integrity_check=ok"
    return 0
  fi

  status_line "DB" "FAIL" "integrity_check=$result"
  return 2
  printf '%s: %s (%s)\n' "$label" "$state" "$detail"
}

check_disk() {
  local free_kb free_gb
  free_kb="$(df -Pk "$HOME" | awk 'NR==2 {print $4}')"
  free_gb=$((free_kb / 1024 / 1024))

  if (( free_gb >= MIN_FREE_GB )); then
    status_line "DISK" "OK" "${free_gb}GB free (threshold ${MIN_FREE_GB}GB)"
    return 0
  fi

  status_line "DISK" "WARN" "${free_gb}GB free (threshold ${MIN_FREE_GB}GB)"
  return 1
}

check_db() {
  if [[ ! -f "$DB_PATH" ]]; then
    status_line "DB $(basename "$DB_PATH")" "WARN" "missing at $DB_PATH"
    return 1
  fi

  local tables
  if ! tables="$(sqlite3 "$DB_PATH" '.tables' 2>/dev/null)"; then
    status_line "DB $(basename "$DB_PATH")" "WARN" "cannot query tables"
    return 1
  fi

  if [[ -z "$tables" ]]; then
    status_line "DB $(basename "$DB_PATH")" "WARN" "0 tables found"
    return 1
  fi

  local table_count
  table_count="$(wc -w <<<"$tables" | tr -d ' ')"
  status_line "DB $(basename "$DB_PATH")" "OK" "${table_count} tables"
  return 0
}

check_jobs() {
  local jobs
  jobs="$(launchctl list 2>/dev/null | awk -v needle="$JOB_FILTER" '$0 ~ needle {print $3}')"

  if [[ -z "$jobs" ]]; then
    status_line "Jobs ($JOB_FILTER)" "WARN" "no loaded jobs found"
    return 1
  fi

  local count
  count="$(wc -l <<<"$jobs" | tr -d ' ')"
  status_line "Jobs ($JOB_FILTER)" "OK" "${count} loaded"
  return 0
}

check_entrypoints() {
  if [[ -f "$DNR_PATH" ]]; then
    status_line "Entrypoint daily_dnr_run.py" "OK" "$DNR_PATH"
    return 0
  fi

  status_line "Entrypoint daily_dnr_run.py" "WARN" "missing at $DNR_PATH"
  return 1
}

check_logs() {
  if [[ ! -d "$LOG_DIR" ]]; then
    status_line "LOGS" "WARN" "directory missing: $LOG_DIR"
    return 1
  fi

  local large_count
  large_count="$(find "$LOG_DIR" -type f -size +20M 2>/dev/null | wc -l | tr -d ' ')"

  if (( large_count > 0 )); then
    status_line "LOGS" "WARN" "${large_count} files > 20MB"
    return 1
  fi

  status_line "LOGS" "OK" "no log pressure sampled"
  return 0
}

main() {
  local score=0
  local total=5
  local hard_fail=0
  local rc=0

  check_disk || rc=$?
  if (( rc == 0 )); then ((score+=1)); elif (( rc == 2 )); then hard_fail=1; fi

  rc=0
  check_entrypoints || rc=$?
  if (( rc == 0 )); then ((score+=1)); elif (( rc == 2 )); then hard_fail=1; fi

  rc=0
  check_jobs || rc=$?
  if (( rc == 0 )); then ((score+=1)); fi

  rc=0
  check_db_integrity || rc=$?
  if (( rc == 0 )); then ((score+=1)); elif (( rc == 2 )); then hard_fail=1; fi

  rc=0
  check_logs || rc=$?
  if (( rc == 0 )); then ((score+=1)); fi

  printf 'HEALTH_SCORE: %s/%s\n' "$score" "$total"

  if (( hard_fail == 1 || score <= 2 )); then
    status_line "SYSTEM_STATE" "FAIL" "hard gate failed"
    (( SUMMARY_ONLY == 1 )) && printf 'SUMMARY: FAIL score=%s/%s\n' "$score" "$total"
    exit 2
  fi

  if (( score <= 4 )); then
    status_line "SYSTEM_STATE" "WARN" "non-critical warnings present"
    (( SUMMARY_ONLY == 1 )) && printf 'SUMMARY: WARN score=%s/%s\n' "$score" "$total"
    exit 1
  fi

  status_line "SYSTEM_STATE" "OK" "preflight passed"
  (( SUMMARY_ONLY == 1 )) && printf 'SUMMARY: OK score=%s/%s\n' "$score" "$total"
  exit 0
    status_line "Logs" "WARN" "directory missing: $LOG_DIR"
    return 1
  fi

  local oversized
  oversized="$(find "$LOG_DIR" -type f -name '*.log' -size +20M 2>/dev/null | wc -l | tr -d ' ')"

  if (( oversized == 0 )); then
    status_line "Logs" "OK" "no *.log files >20MB"
    return 0
  fi

  status_line "Logs" "WARN" "${oversized} oversized log files >20MB"
  return 1
}

main() {
  mkdir -p "$STATE_DIR"

  local score=0
  local total=5

  check_disk && ((score+=1)) || true
  check_db && ((score+=1)) || true
  check_jobs && ((score+=1)) || true
  check_entrypoints && ((score+=1)) || true
  check_logs && ((score+=1)) || true

  printf 'HEALTH_SCORE: %s/%s\n' "$score" "$total"
  if (( score < 3 )); then
    status_line "SYSTEM_STATE" "WARN" "below deterministic baseline"
    exit 1
  fi

  status_line "SYSTEM_STATE" "OK" "ready for controlled launch"
}

main "$@"
