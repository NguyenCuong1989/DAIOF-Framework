#!/usr/bin/env bash
set -euo pipefail

POLICY_ALLOW_WARN="${POLICY_ALLOW_WARN:-1}"
DB_PATH="${DB_PATH:-$HOME/.hyperai/db/memory.sqlite}"
STATE_DIR="${STATE_DIR:-$HOME/.hyperai/state}"
LOG_DIR="${LOG_DIR:-$HOME/.hyperai/logs}"
DB_DIR="$(dirname "$DB_PATH")"
PLIST_DIR="${PLIST_DIR:-$HOME/Library/LaunchAgents}"
JOB_ORDER=(
  "com.hyperai.preflight"
  "com.hyperai.logrotate"
  "com.hyperai.daily_dnr"
  "com.hyperai.os.master"
)

./tools/runtime/preflight.sh --summary || rc=$?
rc="${rc:-0}"

if [[ "$rc" -eq 2 ]]; then
  echo "[FATAL] Preflight FAIL"
  exit 2
fi

if [[ "$rc" -eq 1 && "$POLICY_ALLOW_WARN" -ne 1 ]]; then
  echo "[FATAL] Preflight WARN blocked by policy"
  exit 1
fi

mkdir -p "$LOG_DIR" "$STATE_DIR" "$DB_DIR"

echo "[INFO] Runtime directories ensured"

if [[ ! -f "$DB_PATH" ]]; then
  if command -v sqlite3 >/dev/null 2>&1; then
    sqlite3 "$DB_PATH" <<'SQL'
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
CREATE TABLE IF NOT EXISTS runtime_bootstrap (
  id INTEGER PRIMARY KEY,
  boot_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS dnr_runs (
  id INTEGER PRIMARY KEY,
  run_at TEXT NOT NULL
);
SQL
    sqlite3 "$DB_PATH" "INSERT INTO runtime_bootstrap(boot_at) VALUES(datetime('now'));"
    echo "[INFO] Initialized database at $DB_PATH"
  else
    echo "[WARN] sqlite3 unavailable, database initialization skipped"
  fi
else
  echo "[INFO] Database exists at $DB_PATH"
fi

if command -v python3 >/dev/null 2>&1; then
  python3 tools/runtime/daily_dnr_run.py \
    --db-path "$DB_PATH" \
    --marker-dir "$STATE_DIR/dnr" \
    --lock-file "$STATE_DIR/dnr.lock" \
    --log-dir "$LOG_DIR" || true
fi

./tools/runtime/rotate_hyperai_logs.sh || true

if command -v launchctl >/dev/null 2>&1; then
  for job in "${JOB_ORDER[@]}"; do
    plist="$PLIST_DIR/$job.plist"
    if [[ -f "$plist" ]]; then
      launchctl bootout "gui/$UID" "$plist" >/dev/null 2>&1 || true
      launchctl bootstrap "gui/$UID" "$plist" >/dev/null 2>&1 || true
      launchctl kickstart -k "gui/$UID/$job" >/dev/null 2>&1 || true
      echo "[INFO] launchctl loaded $job"
    else
      echo "[WARN] Missing plist: $plist"
    fi
  done
else
  echo "[WARN] launchctl unavailable; skipping job kickstart"
fi

./tools/runtime/preflight.sh --summary || rc=$?
rc="${rc:-0}"

if [[ "$rc" -eq 2 ]]; then
  echo "[FATAL] Post-bootstrap health FAIL"
  exit 2
fi

if [[ "$rc" -eq 1 ]]; then
  echo "[WARN] Bootstrap completed with warnings"
  exit 1
fi

echo "[OK] Bootstrap completed successfully"
exit 0
