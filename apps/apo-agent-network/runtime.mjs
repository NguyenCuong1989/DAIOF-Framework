const TERMINAL = new Set(["REJECT", "STOP", "CLOSE"]);

export const DOMAINS = Object.freeze({
  K: "Knowledge", D: "Data", C: "Code", R: "Runtime", Dsg: "Design",
  M: "Media", Com: "Communication", F: "Finance", Res: "Research",
  Sec: "Security", Dep: "Deployment",
});

export const AGENT_TYPES = Object.freeze(Object.fromEntries(
  Object.entries(DOMAINS).map(([key, name]) => [key, `${name}Agent`]),
));

export function canonicalId(prefix, value) {
  const input = `${prefix}:${value}`;
  let hash = 2166136261;
  for (let i = 0; i < input.length; i += 1) {
    hash ^= input.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return `${prefix}-${(hash >>> 0).toString(16).padStart(8, "0")}`;
}

export function createNetwork({ capabilities = [], resources = {} } = {}) {
  const budget = {
    CPUQuota: Number(resources.CPUQuota ?? 100),
    MemoryQuota: Number(resources.MemoryQuota ?? 100),
    IOQuota: Number(resources.IOQuota ?? 100),
    CloneTTL: Number(resources.CloneTTL ?? 3600),
  };
  const network = {
    V: new Map(), E: [], C: new Map(capabilities.map((c) => [c.id, c])),
    P: new Set(["minimum-authority", "no-cross-domain-implicit", "fail-closed"]),
    A: new Map(), budget, used: { CPUQuota: 0, MemoryQuota: 0, IOQuota: 0 },
    state: "S0", lastValidState: "S0", events: [], lineage: [],
  };
  return network;
}

function event(network, type, data = {}) {
  network.events.push({ seq: network.events.length + 1, type, state: network.state, ...data });
}

export function discoverCapabilities(network, intent) {
  const text = String(intent || "").toLowerCase();
  const matches = [...network.C.values()].filter((c) => {
    const haystack = `${c.name} ${c.domain} ${(c.capabilities || []).join(" ")}`.toLowerCase();
    return text.split(/\s+/).some((token) => token.length > 2 && haystack.includes(token));
  });
  event(network, "CAPABILITY_DISCOVERY", { intent, count: matches.length });
  return matches;
}

export function canSpawn(network, spec) {
  const required = {
    CPUQuota: Number(spec.CPUQuota ?? 0),
    MemoryQuota: Number(spec.MemoryQuota ?? 0),
    IOQuota: Number(spec.IOQuota ?? 0),
  };
  const checks = Object.keys(required).map((key) => [key, network.used[key] + required[key] <= network.budget[key]]);
  const ttl = Number(spec.CloneTTL ?? 0) <= network.budget.CloneTTL;
  return checks.every(([, ok]) => ok) && ttl;
}

export function spawnAgent(network, seed) {
  if (!seed?.capabilityId || !seed?.domain) return { status: "REJECT", reason: "invalid-seed" };
  if (!canSpawn(network, seed)) {
    event(network, "SPAWN_REJECTED", { reason: "resource-budget" });
    return { status: "REJECT", reason: "resource-budget" };
  }
  const id = canonicalId("agent", `${seed.domain}:${seed.capabilityId}:${seed.instanceKey || "default"}`);
  if (network.V.has(id)) return { status: "PASS", agent: network.V.get(id), deduplicated: true };
  const agent = {
    id, type: AGENT_TYPES[seed.domain] || "Agent", capabilityId: seed.capabilityId,
    authority: seed.authority || "none", boundary: seed.boundary || [seed.domain],
    CloneTTL: Number(seed.CloneTTL ?? 3600), status: "ACTIVE",
  };
  network.V.set(id, agent);
  network.A.set(id, agent.authority);
  for (const key of ["CPUQuota", "MemoryQuota", "IOQuota"]) network.used[key] += Number(seed[key] ?? 0);
  event(network, "AGENT_SPAWN", { agentId: id, capabilityId: seed.capabilityId });
  return { status: "PASS", agent, deduplicated: false };
}

export function linkAgents(network, fromId, toId, { handoff = "evidence", crossDomain = false } = {}) {
  const from = network.V.get(fromId), to = network.V.get(toId);
  if (!from || !to) return { status: "REJECT", reason: "unknown-agent" };
  if (crossDomain && (!from.boundary.includes(to.type.replace(/Agent$/, "")))) {
    event(network, "LINK_REJECTED", { fromId, toId, reason: "boundary" });
    return { status: "REJECT", reason: "boundary" };
  }
  const edge = { from: fromId, to: toId, handoff, admissible: true };
  network.E.push(edge);
  event(network, "AGENT_LINK", edge);
  return { status: "PASS", edge };
}

export function transformState(network, transition) {
  const { target, control, evidence = [] } = transition || {};
  const forbidden = Boolean(transition?.forbidden || transition?.invariantViolation || transition?.unauthorized);
  if (forbidden || !target || !control) {
    network.state = "S_stop";
    event(network, "STOP", { target, reason: forbidden ? "forbidden-or-invariant" : "invalid-transition" });
    return { status: "STOP", state: network.state, rollbackTarget: network.lastValidState };
  }
  network.lastValidState = network.state;
  network.state = target;
  network.lineage.push({ from: network.lastValidState, to: target, control, evidence });
  event(network, "STATE_TRANSFORM", { from: network.lastValidState, to: target, evidence });
  return { status: "PASS", state: target };
}

export function reconstitute(network, { canon = true, invariant = true, identity = true, causalLineage = true } = {}) {
  const preserved = canon && invariant && identity && causalLineage && network.state !== "S_stop";
  if (!preserved) {
    network.state = "S_stop";
    event(network, "RECONSTITUTION_STOP", { canon, invariant, identity, causalLineage });
    return { status: "STOP", state: network.state };
  }
  event(network, "RECONSTITUTION_PASS", { lineageLength: network.lineage.length });
  return { status: "PASS", state: network.state, continuity: "causal" };
}

export function executeIntent(network, intent, seeds = []) {
  const discovered = discoverCapabilities(network, intent);
  const selected = discovered.length ? discovered : network.C.size ? [network.C.values().next().value] : [];
  const spawned = selected.map((capability) => spawnAgent(network, {
    capabilityId: capability.id, domain: capability.domain, authority: capability.authority,
    boundary: capability.boundary, CPUQuota: 1, MemoryQuota: 1, IOQuota: 1, CloneTTL: 60,
  }));
  const accepted = spawned.filter((x) => x.status === "PASS");
  event(network, "INTENT_ROUTED", { intent, discovered: selected.map((c) => c.id), spawned: accepted.length });
  return { status: accepted.length ? "PASS" : "REJECT", discovered: selected, spawned };
}

export { TERMINAL };
