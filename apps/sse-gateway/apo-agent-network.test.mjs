import test from "node:test";
import assert from "node:assert/strict";
import { createNetwork, spawnAgent, transformState, reconstitute } from "../apo-agent-network/runtime.mjs";

test("APΩ runtime smoke: seed → guard → reconstitute", () => {
  const network = createNetwork({
    capabilities: [{ id: "github", name: "GitHub", domain: "C", capabilities: ["code"], authority: "C:write", boundary: ["C"] }],
    resources: { CPUQuota: 2, MemoryQuota: 2, IOQuota: 2, CloneTTL: 60 },
  });
  const agent = spawnAgent(network, { capabilityId: "github", domain: "C", authority: "C:write", boundary: ["C"], CPUQuota: 1, MemoryQuota: 1, IOQuota: 1, CloneTTL: 30 });
  assert.equal(agent.status, "PASS");
  assert.equal(transformState(network, { target: "S1", control: "admissible-write", evidence: ["commit:test"] }).status, "PASS");
  assert.equal(reconstitute(network).status, "PASS");
});

test("APΩ runtime smoke: Forbidden → STOP", () => {
  const network = createNetwork();
  const result = transformState(network, { target: "S_bad", control: "forbidden-write", forbidden: true });
  assert.equal(result.status, "STOP");
  assert.equal(network.state, "S_stop");
});
