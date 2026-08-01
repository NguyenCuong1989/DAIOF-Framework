# Copilot / VS Code Model Inventory Audit

Date: 2026-07-09  
Scope: local VS Code Stable, VS Code Insiders, Copilot Chat model cache, AI Toolkit / Foundry Local model exposure, MCP config, and local Ollama inventory.  
Mode: read-only audit; no cloud Foundry, training, deployment, or secret extraction was performed.

## Executive Summary

Stable VS Code is clean and small: 36 cached language models, all official Copilot-family models, with no BYOK models in the cache. Insiders is the main mixed-provider surface: 964 cached models, 465 BYOK models, and multiple local/cloud bridge providers.

Current primary Chat surfaces are normalized to `Claude Sonnet 4.5 (copilot)`:

- `chat.currentLanguageModel.panel`
- `chat.currentLanguageModel.editor`
- `chat.currentLanguageModel.terminal`
- `chat.planAgent.defaultModel`
- `inlineChat.defaultModel`
- `github.copilot.chat.askAgent.model`
- `github.copilot.chat.exploreAgent.model`
- `github.copilot.chat.implementAgent.model`

This keeps web-search and Copilot utility-model flows on an official non-BYOK model while preserving local/BYOK providers for explicit use.

## Inventory Totals

| Surface | Total Models | BYOK Models | Main Vendors |
| --- | ---: | ---: | --- |
| VS Code Stable | 36 | 0 | `copilot`, `copilotcli`, `claude-code` |
| VS Code Insiders | 964 | 465 | `agent-host-copilotcli`, `openrouter`, `aitk-foundry-local`, `ollama-*`, `copilot`, `copilotcli` |

## Normalized Provider Taxonomy

| Class | Count / Evidence | Canonical Use |
| --- | --- | --- |
| Official Copilot cloud | Stable: 36; Insiders: 34 | Default Chat, Agent, web search, utility-model workflows |
| Copilot utility models | Stable: `copilot-utility`, `copilot-utility-small` | Internal support only; not user-selectable |
| Agent-host BYOK | Insiders: 465 | Explicit BYOK experiments; do not set as default for web search |
| AI Toolkit Foundry Local | Insiders: 74 | Local inference/dev testing; classify separately from cloud Foundry deployments |
| AI Toolkit Foundry cloud | Insiders: 1 | Cloud-like Foundry model bridge; verify project/deployment before training |
| Ollama / Ollama Cloud / selfagency | Insiders: 103; local `ollama list`: 18 entries | Local/cloud bridge testing; explicit model use only |
| OpenRouter | Insiders: 252 | BYOK cloud aggregator; not a Copilot utility-model source |
| DeepSeek providers | Insiders: 6 | BYOK/cloud bridge testing |
| `llama-vscode` | Insiders: `finalai-titan`, disabled | Legacy local proxy path; keep disabled unless explicitly testing |
| Veyra | Insiders: 8 | BYOK orchestration workflows |
| Custom LLM catalog | Insiders: 9 Alibaba DashScope models | Catalog only; standardize names before training/eval use |

## Current Selected Models

Both Stable and Insiders global storage now select:

```text
panel    = copilot/claude-sonnet-4.5
editor   = copilot/claude-sonnet-4.5
terminal = copilot/claude-sonnet-4.5
copilotcli panel = copilotcli/claude-sonnet-4.5
```

## Local Runtime Inventory

Ollama is installed at `/opt/homebrew/bin/ollama`. Local inventory includes Vietnamese Qwen variants, embedding models, Qwen/Qwen coder, Llama 3.1, TinyLlama, and several Ollama cloud aliases such as `qwen3-coder-next:cloud`, `kimi-k2.7-code:cloud`, `gemini-3-flash-preview:cloud`, and `minimax-m2.7:cloud`.

AI Toolkit config exists at `/Users/andy/.aitk/mcp.json`. It exposes GitHub Copilot MCP, Playwright MCP, Hugging Face MCP, DeepWiki MCP, memory, MongoDB, Azure DevOps placeholders, and several generated MCP entries. Tokens and authorization headers were redacted during inspection.

## Drift / Risk Findings

1. Insiders has a very large mixed model cache. BYOK models should not be default for Copilot Chat, web search, or utility-model flows.
2. `github.copilot.selectedCompletionModel` in Insiders remains `"Ollama"`. Treat this as a completion-specific override, not Chat default. Review before changing completions.
3. Stable still has `vscode-openai.*` and GitLens AI pointing at local Ollama. These are separate extension surfaces and should stay explicitly local unless the desired standard is "all VS Code AI surfaces use Copilot cloud".
4. `llama-vscode` remains configured for `finalai-titan` but disabled. This is safe as long as it is not selected as a Chat model.
5. No active Foundry project/deployment/training job was verified in this pass. Foundry cloud standardization needs a separate authenticated audit.

## Standardization Rules

1. Default Chat/Agent/web-search surfaces: use official Copilot non-BYOK models.
2. Local/BYOK providers: keep available but label as explicit opt-in.
3. Foundry Local models: classify as local dev/runtime models, not cloud deployment evidence.
4. Fine-tuning candidates: require baseline eval, dataset lineage, and training type classification: SFT, DPO, or RFT.
5. Cloud-like providers through aggregators such as OpenRouter or Ollama Cloud must not be treated as Azure Foundry deployments without project/deployment evidence.

## Next Safe Step

Create a machine-readable registry from this audit, for example:

```text
docs/evidence/model_registry.normalized.json
```

Suggested schema:

```json
{
  "id": "copilot/claude-sonnet-4.5",
  "displayName": "Claude Sonnet 4.5",
  "providerClass": "official-copilot-cloud",
  "sourceSurface": "VS Code Chat",
  "byok": false,
  "defaultUse": ["chat", "agent", "web-search"],
  "trainingReadiness": "baseline-only",
  "foundryEvidence": "none"
}
```
