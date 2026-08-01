#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PROJECTS=(
  "."
  "vscode-merged"
  "vscode-merged/extensions"
  "vscode-merged/scripts"
  "vscode-merged/test"
  "vscode-merged/cli"
  "vscode-merged/remote"
)

SKIP_REMOTE_ON_MISSING_PREREQS="${SKIP_REMOTE_ON_MISSING_PREREQS:-1}"
FORCE_REMOTE="${FORCE_REMOTE:-0}"

log() {
  printf '%s\n' "$*"
}

have() {
  command -v "$1" >/dev/null 2>&1
}

activate_nvm_for_dir() {
  local dir="$1"
  local nvmrc=""
  local search="$dir"

  while [[ "$search" != "/" ]]; do
    if [[ -f "$search/.nvmrc" ]]; then
      nvmrc="$search/.nvmrc"
      break
    fi
    search="$(dirname "$search")"
  done

  [[ -n "$nvmrc" ]] || return 0

  if [[ -s "$HOME/.nvm/nvm.sh" ]]; then
    # shellcheck disable=SC1090
    source "$HOME/.nvm/nvm.sh"
    nvm use >/dev/null
  fi
}

configure_krb5_env() {
  local dir="$1"
  [[ "$dir" == */vscode-merged/remote ]] || return 0

  if [[ "$(uname -s)" == "Darwin" ]]; then
    if command -v xcrun >/dev/null 2>&1; then
      export CC="$(xcrun --find clang)"
      export CXX="$(xcrun --find clang++)"
      export SDKROOT="$(xcrun --sdk macosx --show-sdk-path)"
      export CXXFLAGS="-std=c++17 ${CXXFLAGS:-}"
    fi
  fi

  if [[ "$(uname -s)" == "Darwin" ]] && have brew; then
    local krb5_prefix=""
    krb5_prefix="$(brew --prefix krb5 2>/dev/null || true)"
    if [[ -n "$krb5_prefix" && -f "$krb5_prefix/include/gssapi/gssapi.h" ]]; then
      export CPPFLAGS="-I$krb5_prefix/include ${CPPFLAGS:-}"
      export LDFLAGS="-L$krb5_prefix/lib ${LDFLAGS:-}"
      export PKG_CONFIG_PATH="$krb5_prefix/lib/pkgconfig:${PKG_CONFIG_PATH:-}"
      return 0
    fi
  fi

  if have krb5-config; then
    return 0
  fi

  if [[ "$FORCE_REMOTE" == "1" || "$SKIP_REMOTE_ON_MISSING_PREREQS" != "1" ]]; then
    log "[WARN] kerberos/gssapi prerequisites not detected; continuing because FORCE_REMOTE=$FORCE_REMOTE"
    return 0
  fi

  log "[WARN] Skipping vscode-merged/remote: missing kerberos/gssapi prerequisites"
  log "       On macOS: brew install krb5 && rerun with PATH/flags or just rerun this script"
  return 10
}

run_node_install() {
  local dir="$1"
  if [[ -f "$dir/package-lock.json" ]]; then
    log "==> Node: npm ci ($dir)"
    if ! (cd "$dir" && activate_nvm_for_dir "$dir" && npm ci); then
      log "[WARN] npm ci failed in $dir; checking for lockfile drift fallback"
      if grep -Eq 'can only install packages when your package\.json and package-lock\.json|Missing: .* from lock file' "$HOME/.npm/_logs/"* 2>/dev/null; then
        log "[WARN] lockfile drift detected; falling back to npm install ($dir)"
        (cd "$dir" && activate_nvm_for_dir "$dir" && npm install)
      else
        return 1
      fi
    fi
  elif [[ -f "$dir/package.json" ]]; then
    log "==> Node: npm install --no-save --no-package-lock ($dir)"
    (cd "$dir" && activate_nvm_for_dir "$dir" && npm install --no-save --no-package-lock)
  fi
}

run_python_install() {
  local dir="$1"
  [[ -f "$dir/requirements.txt" ]] || return 0
  local venv_dir="$dir/.venv"
  log "==> Python: repo-local venv install ($dir)"
  (
    cd "$dir"
    python3 -m venv "$venv_dir"
    "$venv_dir/bin/python" -m pip install --upgrade pip
    "$venv_dir/bin/python" -m pip install -r requirements.txt
  )
}

run_rust_fetch() {
  local dir="$1"
  [[ -f "$dir/Cargo.toml" ]] || return 0
  log "==> Rust: cargo fetch ($dir)"
  (cd "$dir" && cargo fetch)
}

process_project() {
  local rel="$1"
  local dir="$ROOT_DIR/$rel"

  [[ -d "$dir" ]] || return 0
  case "$dir" in
    */node_modules/*|*/.git/*)
      return 0
      ;;
  esac

  if [[ "$dir" == */vscode-merged/remote ]]; then
    if ! configure_krb5_env "$dir"; then
      return 0
    fi
  fi

  log ""
  log "--- Checking $rel ---"
  run_node_install "$dir"
  run_python_install "$dir"
  run_rust_fetch "$dir"
}

main() {
  log "Running curated workspace bootstrap..."
  log "Repository: $ROOT_DIR"
  log "Mode: curated first-class projects only; node_modules/artifacts are excluded"

  for rel in "${PROJECTS[@]}"; do
    process_project "$rel"
  done

  log ""
  log "Done."
}

main "$@"
