# SSE Gateway (functional stream)

## Run

```bash
npm i express
node apps/sse-gateway/server.mjs
```

## Test

```bash
curl -N "http://localhost:5000/sse?q=email"
```

You should receive:
- `status` event
- `result` event
- periodic keep-alive comments (`: keep-alive`)
