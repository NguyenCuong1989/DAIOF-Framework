import express from "express";

const PORT = Number(process.env.PORT) || 5000;

const app = express();

app.get("/", (_req, res) => {
  res.json({ ok: true, service: "sse-gateway" });
});

function detectIntent(q = "") {
  const s = String(q).toLowerCase();

  if (s.includes("email")) return ["email", ["Gmail"]];
  if (s.includes("docs")) return ["docs", ["Google Docs"]];
  if (s.includes("storage")) return ["storage", ["Google Drive"]];
  if (s.includes("dev")) return ["dev", ["Replit", "Vercel"]];
  if (s.includes("payment")) return ["payment", ["PayPal"]];
  if (s.includes("ai")) return ["ai", ["Hugging Face"]];

  return ["general", ["General"]];
}

app.get("/sse", (req, res) => {
  const q = String(req.query.q || "");
  const [intent, tools] = detectIntent(q);

  res.setHeader("Content-Type", "text/event-stream; charset=utf-8");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");

  if (typeof res.flushHeaders === "function") {
    res.flushHeaders();
  }

  res.write("event: status\n");
  res.write(`data: ${JSON.stringify({ status: "processing" })}\n\n`);

  const resultTimer = setTimeout(() => {
    res.write("event: result\n");
    res.write(
      `data: ${JSON.stringify({
        query: q,
        intent,
        tools,
      })}\n\n`,
    );
  }, 300);

  const heartbeat = setInterval(() => {
    res.write(": keep-alive\n\n");
  }, 15000);

  req.on("close", () => {
    clearTimeout(resultTimer);
    clearInterval(heartbeat);
    res.end();
  });
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`SSE gateway running on port ${PORT}`);
});
