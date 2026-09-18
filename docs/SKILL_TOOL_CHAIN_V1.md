# SKILL → TOOL CHAIN V1

**Schema:** `APO-SKILL-TOOL-CHAIN-1.0`  
**Originator:** Nguyễn Đức Cường / `alpha_prime_omega`  
**Repository:** `NguyenCuong1989/DAIOF-Framework`  
**Mode:** OBSERVED_PLUS_COMPOSED  
**Rule:** observed tool existence is evidence; chain order is an explicit composition and is not claimed as an already-running workflow.

## Observed MCP tool surface

Source: `NguyenCuong1989/hyperai1989/components/cognee/cognee-mcp/src/server.py`

1. `cognee_add_developer_rules`
2. `cognify`
3. `codify`
4. `search`
5. `get_developer_rules`
6. `list_data`
7. `delete`
8. `prune`
9. `cognify_status`
10. `codify_status`
11. `save_interaction`

## Skill chains

### Knowledge Ingestion
`cognify → cognify_status → search`

### Repository Codification
`codify → codify_status → search`

### Interaction Memory
`save_interaction → cognify_status → search`

### Developer Rules
`cognee_add_developer_rules → get_developer_rules`

### Data Inspection
`list_data → search`

### Data Lifecycle
`list_data → delete → cognify_status`

### Graph Reset
`prune → cognify_status`

## Execution doctrine

`SKILL = INTENT`  
`TOOL = EXECUTION NODE`  
`CHAIN = ORDERED TOOL COMPOSITION`

`OBSERVE → SELECT_SKILL → RESOLVE_TOOLS → EXECUTE_CHAIN → VERIFY → RECORD`

No chain is marked successful merely because its tools exist. Runtime execution evidence must come from an actual tool invocation and its result.

`UNKNOWN` remains unresolved until the next observation.

## Evidence boundary

The MCP server source proves the tool surface. The client source proves direct calls to `prune`, `codify`, and `search`. The multi-step skill chains above are architecture-level compositions built from those observed tools; they are not presented as historical execution logs.
