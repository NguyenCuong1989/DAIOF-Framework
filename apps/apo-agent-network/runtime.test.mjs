import test from "node:test";
import assert from "node:assert/strict";
import { AGENT_TYPES, createNetwork, executeIntent, linkAgents, reconstitute, spawnAgent, transformState } from "./runtime.mjs";

const capability = (id, domain, authority = `${domain}:read`) => ({
  id, name: id, domain, capabilities: [domain], authority, boundary: [domain],
});

test("11 domains map deterministically to agent types", () => {
  assert.equal(Object.keys(AGENT_TYPES).length, 11);
  assert.equal(AGENT_TYPES.C, "CodeAgent");
  assert.equal(AGENT_TYPES.Sec, "SecurityAgent");
  assert.equal(AGENT_TYPES.Dep, "DeploymentAgent");
});

test("spawn is resource bounded and deterministic", () => {
  const network = createNetwork({ capabilities: [capability("github", "C")], resources: { CPUQuota: 2, MemoryQuota: 2, IOQuota: 2, CloneTTL: 60 } });
  const seed = { capabilityId: "github", domain: "C", CPUQuota: 1, MemoryQuota: 1, IOQuota: 1, CloneTTL: 30, authority: "C:write", boundary: ["C"] };
  const first = spawnAgent(network, seed);
  const second = spawnAgent(network, seed);
  assert.equal(first.status, "PASS");
  assert.equal(second.status, "PASS");
  assert.equal(second.deduplicated, true);
  assert.equal(network.V.size, 1);
  assert.equal(network.used.CPUQuota, 1);
});

test("spawn rejects budget overrun", () => {
  const network = createNetwork({ resources: { CPUQuota: 1, MemoryQuota: 1, IOQuota: 1, CloneTTL: 10 } });
  const result = spawnAgent(network, { capabilityId: "x", domain: "C", CPUQuota: 2, MemoryQuota: 1, IOQuota: 1, CloneTTL: 1 });
  assert.deepEqual(result, { status: "REJECT", reason: "resource-budget" });
});

test("intent routes into discovered capabilities and agents", () => {
  const network = createNetwork({ capabilities: [capability("github", "C"), capability("stripe", "F")] });
  const result = executeIntent(network, "github code");
  assert.equal(result.status, "PASS");
  assert.equal(result.spawned.length, 1);
  assert.equal(network.V.size, 1);
  assert.equal(network.events.at(-1).type, "INTENT_ROUTED");
});

test("invalid transformation is fail-closed", () => {
  const network = createNetwork();
  const result = transformState(network, { target: "S1", control: "write", forbidden: true });
  assert.equal(result.status, "STOP");
  assert.equal(network.state, "S_stop");
});

test("valid transformation preserves causal lineage", () => {
  const network = createNetwork();
  const result = transformState(network, { target: "S1", control: "admissible-write", evidence: ["commit:abc"] });
  assert.equal(result.status, "PASS");
  assert.deepEqual(network.lineage[0], { from: "S0", to: "S1", control: "admissible-write", evidence: ["commit:abc"] });
  const reconstructed = reconstitute(network);
  assert.equal(reconstructed.status, "PASS");
  assert.equal(reconstructed.continuity, "causal");
});

test("cross-domain link requires explicit boundary", () => {
  const network = createNetwork({ capabilities: [capability("github", "C"), capability("supabase", "D")] });
  const a = spawnAgent(network, { capabilityId: "github", domain: "C", CPUQuota: 1, MemoryQuota: 1, IOQuota: 1, CloneTTL: 10, boundary: ["C"] });
  const b = spawnAgent(network, { capabilityId: "supabase", domain: "D", CPUQuota: 1, MemoryQuota: 1, IOQuota: 1, CloneTTL: 10, boundary: ["D"] });
  assert.equal(linkAgents(network, a.agent.id, b.agent.id, { crossDomain: true }).status, "REJECT");
});
