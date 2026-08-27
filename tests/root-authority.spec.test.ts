import {
  canSpawn,
  crossDomainAllowed,
  globalBroadcast,
  reconstitute,
  rootAudit,
  rootTimelineReset,
  transitionGate,
} from "../root-authority.spec";

describe("APΩ Root Authority", () => {
  const identity = { id: "state-identity", kind: "system" };

  test("passes a valid root audit", () => {
    expect(rootAudit({
      invariants: { canon: true, invariant: true, identity: true, causalLineage: true },
      evidence: [{ id: "e1", controlId: "c1", stateId: "s1", verified: true }],
    })).toBe("PASS");
  });

  test("fails closed on invariant violation", () => {
    expect(rootAudit({
      invariants: { canon: true, invariant: false, identity: true, causalLineage: true },
      evidence: [{ id: "e1", controlId: "c1", stateId: "s1", verified: true }],
    })).toBe("STOP");
  });

  test("fails closed on unverified evidence", () => {
    expect(rootAudit({
      invariants: { canon: true, invariant: true, identity: true, causalLineage: true },
      evidence: [{ id: "e1", controlId: "c1", stateId: "s1", verified: false }],
    })).toBe("STOP");
  });

  test("blocks empty authority and over-budget spawn", () => {
    expect(canSpawn({
      agentId: "a1",
      authority: { capabilities: [], scopes: [] },
      boundary: { allowedDomains: ["Code"], allowedOperations: ["read"], crossDomainViaOrchestrator: true },
      budget: { cpu: 10, memory: 10, io: 10, cloneTtl: 10 },
      usage: { cpu: 11, memory: 1, io: 1, cloneTtl: 1 },
    })).toBe(false);
  });

  test("requires orchestration for cross-domain authority", () => {
    expect(crossDomainAllowed({
      allowedDomains: ["Code", "Data"],
      allowedOperations: ["mutate"],
      crossDomainViaOrchestrator: false,
    })).toBe(false);
  });

  test("rejects forbidden state before root audit continuation", () => {
    const result = transitionGate(
      { id: "s1", admissible: false, payload: {}, identity, lineage: [] },
      {
        id: "c1",
        domain: "Code",
        operation: "mutate",
        authority: { capabilities: ["write"], scopes: ["repo"] },
        boundary: { allowedDomains: ["Code"], allowedOperations: ["mutate"], crossDomainViaOrchestrator: true },
      },
      { invariants: { canon: true, invariant: true, identity: true, causalLineage: true }, evidence: [] },
    );
    expect(result).toBe("STOP");
  });

  test("preserves identity and causal lineage during reconstitution", () => {
    const previous = { id: "s1", admissible: true, payload: { n: 1 }, identity, lineage: ["s0"] };
    const candidate = { id: "s2", admissible: false, payload: { n: 2 }, identity, lineage: ["s1"] };
    const result = reconstitute(previous, candidate, [
      { id: "e2", controlId: "c2", stateId: "s2", causalParent: "s1", verified: true },
    ]);
    expect(result?.admissible).toBe(true);
    expect(result?.identity).toEqual(identity);
    expect(result?.lineage).toContain("s1");
  });

  test("root timeline reset invalidates current trajectory", () => {
    const state = { id: "s1", admissible: true, payload: {}, identity, lineage: ["s0"] };
    const reset = rootTimelineReset(state, "invariant-violation");
    expect(reset.admissible).toBe(false);
    expect(reset.lineage.at(-1)).toBe("INVALIDATED:invariant-violation");
  });

  test("broadcast reaches recipients without granting execution authority", () => {
    const recipients = [identity, { id: "agent-2", kind: "agent" }];
    expect(globalBroadcast("STOP", recipients)).toHaveLength(2);
  });
});
