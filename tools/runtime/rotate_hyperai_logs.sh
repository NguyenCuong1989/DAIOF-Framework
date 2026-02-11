#!/usr/bin/env bash
set -euo pipefail

LOG_DIR="${LOG_DIR:-$HOME/.hyperai/logs}"
RETENTION_DAYS_STANDARD="${RETENTION_DAYS_STANDARD:-14}"
RETENTION_DAYS_ERROR="${RETENTION_DAYS_ERROR:-7}"
MAX_STANDARD_MB="${MAX_STANDARD_MB:-20}"
MAX_ERROR_MB="${MAX_ERROR_MB:-10}"
MIN_AGE_SECONDS="${MIN_AGE_SECONDS:-60}"

stat_size() {
  local file="$1"
  stat -f%z "$file" 2>/dev/null || stat -c%s "$file"
}

stat_mtime() {
  local file="$1"
  stat -f%m "$file" 2>/dev/null || stat -c%Y "$file"
}

rotate_one() {
  local file="$1"
  local threshold_mb="$2"

  [[ -f "$file" ]] || return 0

  local now mtime age_seconds
  now="$(date +%s)"
  mtime="$(stat_mtime "$file")"
  age_seconds=$((now - mtime))
  if (( age_seconds <= MIN_AGE_SECONDS )); then
    printf 'SKIP_RECENT: %s (%ss old)\n' "$file" "$age_seconds"
    return 0
  fi

  local file_size threshold_bytes
  file_size="$(stat_size "$file")"
  threshold_bytes=$((threshold_mb * 1024 * 1024))

  if (( file_size <= threshold_bytes )); then
    return 0
  fi

  local ts rotated
  ts="$(date '+%Y%m%d_%H%M%S')"
  rotated="${file}.${ts}"

  mv "$file" "$rotated"
  : > "$file"
  gzip "$rotated"

  printf 'ROTATED: %s -> %s.gz\n' "$file" "$rotated"
}

cleanup_old_archives() {
  local pattern="$1"
  local days="$2"
  find "$LOG_DIR" -type f -name "$pattern" -mtime "+$days" -print -delete
}

main() {
  if [[ ! -d "$LOG_DIR" ]]; then
    echo "Log directory not found: $LOG_DIR"
    exit 0
  fi

  while IFS= read -r -d '' file; do
    [[ -f "$file" ]] || continue
    if [[ "$file" == *error* ]]; then
      rotate_one "$file" "$MAX_ERROR_MB"
    else
      rotate_one "$file" "$MAX_STANDARD_MB"
    fi
  done < <(find "$LOG_DIR" -type f -name '*.log' -print0)

  cleanup_old_archives '*.error.log.*.gz' "$RETENTION_DAYS_ERROR"
  cleanup_old_archives '*.log.*.gz' "$RETENTION_DAYS_STANDARD"

  echo "Rotation complete for $LOG_DIR"
}

main "$@"
