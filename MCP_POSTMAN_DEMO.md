# Postman MCP Server (local) — setup + demo

This repo includes an MCP configuration for the **Postman MCP Server** using **stdio** transport.

## 1) Configure Postman API key

The MCP server requires `POSTMAN_API_KEY`.

Your MCP host (VS Code / other MCP host) should prompt for the input defined in `.vscode/mcp.json`.

If your MCP host supports env vars directly, you can also set:

```bash
export POSTMAN_API_KEY="<YOUR_POSTMAN_API_KEY>"
```

## 2) Start the MCP server

The server is started by your MCP host using the configuration in:

- `.vscode/mcp.json`

It uses:

- `npx -y @postman/postman-mcp-server --minimal --region us`

## 3) Demonstrate a tool capability

Once the MCP host is connected and the server is running, call (tool name in Postman MCP v2.x):

- `getWorkspaces`

Expected: JSON listing workspaces you have access to.

## Notes

- This configuration uses **minimal** tool set to keep startup time low.
- To enable more tools, update the MCP server args from `--minimal` to `--full`.
