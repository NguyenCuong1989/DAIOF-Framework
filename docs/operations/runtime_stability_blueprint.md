# Runtime Stability Blueprint (Deterministic Execution)

This blueprint encodes a strict stabilization order for local runtime reliability.
Each step is a **gate**. If a hard gate fails, stop rollout.

## Exit semantics

- `0` => OK
- `1` => WARN (non-critical)
- `2` => FAIL (hard gate)

## Deployment Order (Gate-by-Gate)

1. Disk stabilization (>= 15GB free)
2. Run preflight gate (`tools/runtime/preflight.sh`)
3. Run log rotation (`tools/runtime/rotate_hyperai_logs.sh`)
4. Run daily cycle (`tools/runtime/daily_dnr_run.py`) with lock/marker
5. Run deterministic bootstrap (`tools/runtime/bootstrap_runtime.sh`)
6. Kickstart launchd jobs sequentially (KeepAlive jobs last)

## Runtime State Table

| Job | Schedule | Entry Script | Writes DB | Writes Logs | Risk |
| --- | --- | --- | --- | --- | --- |
| `com.hyperai.os.master` | `StartInterval=300`, `KeepAlive=true` | `launchd_safe_wrapper.sh` -> `daily_dnr_run.py` | Yes | Yes | Respawn amplification if non-zero exits are unbounded. |
| `com.hyperai.daily_dnr` | Daily | `daily_dnr_run.py` | Yes | Yes | Multi-run inflation without cycle marker guard. |
| `com.hyperai.preflight` | Manual / pre-enable gate | `preflight.sh` | Read-only check | Yes (stdout/stderr) | False confidence if checks are skipped. |
| `com.hyperai.logrotate` | Hourly / daily | `rotate_hyperai_logs.sh` | No | Yes | Disk pressure if rotation is absent or retention is too long. |
| `com.hyperai.healthd` | Every N minutes | `runtime_health_daemon.py` | Read-only check + state markers | Yes | Missed degradation trend if disabled. |

## Required Behaviors

- **Disk floor**: Keep at least **15GB free** before enabling autonomous jobs.
- **Deterministic disk check**: `df -Pk /Users/andy | awk 'NR==2 {print $4}'`
- **Entrypoint safety**: Runtime entrypoints call preflight and stop only on hard FAIL (`rc==2`).
- **DB lock mitigation**: `sqlite3.connect(timeout=30)` + WAL (`PRAGMA journal_mode=WAL`) + `PRAGMA synchronous=NORMAL`.
- **DB integrity gate**: `sqlite3 "$DB_PATH" "PRAGMA integrity_check;"` must return `ok`.
- **Daily cycle guard**: One run/day marker and lockfile to prevent overlap.
- **Log rotation safety**: Skip files modified within last 60s.

## Daily cycle invocation

```bash
python3 tools/runtime/daily_dnr_run.py \
  --db-path "$HOME/.hyperai/db/memory.sqlite" \
  --marker-dir "$HOME/.hyperai/state/dnr" \
  --lock-file "$HOME/.hyperai/state/dnr.lock" \
  --log-dir "$HOME/.hyperai/logs"
```

## Bootstrap invocation

```bash
POLICY_ALLOW_WARN=1 ./tools/runtime/bootstrap_runtime.sh
```

## Runtime matrix tests

```bash
./tools/runtime/test_runtime_matrix.sh
```

## Low-risk cleanup commands

```bash
rm -rf ~/Library/Caches/ms-playwright*
rm -rf ~/Library/Caches/pip
brew cleanup -s
```

Do **not** remove canonical model storage (`~/.aitk/models`) without explicit migration planning.
