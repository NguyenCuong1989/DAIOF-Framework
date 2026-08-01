# Worktree Review Plan

## Current files

### Modified
- `package-lock.json`
- `vscode-merged/remote/package.json`

### Untracked
- `.nvmrc`
- `scripts/bootstrap_workspace.sh`
- `vscode-merged/remote/.nvmrc`

## Classification

### Keep: runtime / toolchain pinning
- `.nvmrc`
  - pins repo Node to `22.21.1`
- `vscode-merged/remote/.nvmrc`
  - pins remote Node to `22.21.1`
- `vscode-merged/remote/package.json`
  - adds:
    - `"engines": { "node": "22.21.1" }`

### Keep: bootstrap hardening
- `scripts/bootstrap_workspace.sh`
  - curated project-only bootstrap
  - `npm ci` with fallback to `npm install` on lockfile drift
  - repo-local Python `.venv`
  - Xcode compiler pinning for remote native builds via `xcrun`
  - `SDKROOT` + `CXXFLAGS=-std=c++17`
  - `krb5` / `gssapi` environment wiring

### Keep: dependency lock sync
- `package-lock.json`
  - syncs root lockfile with `package.json`
  - captures `express` dependency and transitive tree

## Suggested review / commit split

### Commit A — runtime pinning
Files:
- `.nvmrc`
- `vscode-merged/remote/.nvmrc`
- `vscode-merged/remote/package.json`

Why:
- establishes exact Node runtime contract first

### Commit B — workspace bootstrap hardening
Files:
- `scripts/bootstrap_workspace.sh`

Why:
- codifies successful bootstrap and native build environment fixes

### Commit C — root dependency lock sync
Files:
- `package-lock.json`

Why:
- keeps dependency graph update isolated from policy/tooling changes

## Files explicitly not part of keep set
- `node_modules/.package-lock.json`
  - generated artifact
  - already reverted from working tree

## Operational note
This worktree is now mostly intentional config + bootstrap policy + lock sync. It no longer contains the obvious generated noise that appeared during bootstrap.
