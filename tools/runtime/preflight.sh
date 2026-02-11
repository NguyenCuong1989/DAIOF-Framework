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
}

main "$@"
