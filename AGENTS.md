# Repository Guidelines

## Project Structure & Module Organization

Core Python code lives under `src/hyperai/`, grouped by responsibility: `core/` for runtime primitives, `components/` for organism parts, `protocols/` for governance and D&R protocol logic, `ecosystem/` for simulations, and `utils/` for helpers. Tests live in `tests/`, with focused subfolders such as `tests/governance/` and `tests/runtime/`. Documentation, doctrine, evidence, and registry material are under `docs/`; examples are in `examples/`; runtime launch notes are in `launch/`. The Node SSE gateway is isolated in `apps/sse-gateway/`. Treat `vscode-merged/` as a large imported VS Code subtree and avoid broad edits there unless the task explicitly targets it.

## Build, Test, and Development Commands

Install Python dependencies with:

```bash
pip install -r requirements.txt
pip install -e .[dev]
```

Run the Python test suite with `pytest`, or target a subset such as `pytest tests/governance`. Run the Node gateway tests with `npm test`; start the SSE gateway locally with `npm run sse:gateway`. Use `python quick_start.py` for the README demo. Validate Docker wiring with `docker compose config` before running services.

## Coding Style & Naming Conventions

Use Python 3.8+ and keep modules importable from `src/`. Follow Black-compatible formatting, four-space indentation, snake_case for functions/modules, PascalCase for classes, and clear protocol names such as `dr_protocol.py`. Keep public APIs small and documented. JavaScript in `apps/sse-gateway/` uses ESM `.mjs` files and Node's built-in test runner.

## Testing Guidelines

Add tests beside the behavior being changed, using `test_*.py` for Python and `*.test.mjs` for the gateway. Cover governance gates, runtime evidence, imports, and smoke behavior when touching shared runtime paths. Prefer narrow regression tests for bug fixes, then run the nearest suite plus `pytest` before submitting broad changes.

## Commit & Pull Request Guidelines

Recent history uses concise Conventional Commit style, for example `fix: consolidate DAIOF runtime activation` and `chore(mcp): add Postman MCP server stdio config and demo`. PRs should explain the runtime or doctrine impact, list validation commands, link issues when relevant, and include screenshots or logs for UI/runtime changes.

## Security & Configuration Tips

Do not commit secrets, tokens, generated credentials, or local `.env` values. Preserve provenance and canonical runtime records in `docs/evidence/`, `docs/operations/`, and governance artifacts. Avoid destructive cleanup, Docker pruning, public sync, or cloud actions without an explicit maintainer gate.
