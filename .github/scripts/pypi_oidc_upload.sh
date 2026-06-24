#!/usr/bin/env bash
# Self-contained PyPI/TestPyPI trusted publishing (OIDC) without any external
# GitHub Action. Re-implements what pypa/gh-action-pypi-publish does:
#   1. Ask GitHub for an OIDC id-token (audience = pypi).
#   2. Exchange it at the index's mint-token endpoint for a short-lived API token.
#   3. Upload dist/* with twine using that token.
#
# Requires job permission `id-token: write` and env:
#   PYPI_MINT_URL        e.g. https://pypi.org/_/oidc/mint-token
#   TWINE_REPOSITORY_URL e.g. https://upload.pypi.org/legacy/
set -euo pipefail

if [ -z "${ACTIONS_ID_TOKEN_REQUEST_TOKEN:-}" ] || [ -z "${ACTIONS_ID_TOKEN_REQUEST_URL:-}" ]; then
  echo "::error::OIDC not available (need permissions: id-token: write)"
  exit 1
fi

echo "→ Requesting GitHub OIDC token (audience=pypi)…"
oidc_resp=$(curl -sS -H "Authorization: bearer ${ACTIONS_ID_TOKEN_REQUEST_TOKEN}" \
  "${ACTIONS_ID_TOKEN_REQUEST_URL}&audience=pypi")
oidc_token=$(printf '%s' "$oidc_resp" | python3 -c 'import sys,json;print(json.load(sys.stdin)["value"])')

echo "→ Minting PyPI API token at ${PYPI_MINT_URL}…"
mint_resp=$(curl -sS -X POST "${PYPI_MINT_URL}" \
  -d "{\"token\":\"${oidc_token}\"}")
api_token=$(printf '%s' "$mint_resp" | python3 -c 'import sys,json;print(json.load(sys.stdin)["token"])')

echo "→ Uploading dist/* to ${TWINE_REPOSITORY_URL}…"
TWINE_USERNAME="__token__" TWINE_PASSWORD="${api_token}" \
  twine upload --non-interactive --repository-url "${TWINE_REPOSITORY_URL}" dist/*
echo "✅ Published."
