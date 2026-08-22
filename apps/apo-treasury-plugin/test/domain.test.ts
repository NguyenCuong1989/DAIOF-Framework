import { describe, expect, it } from "vitest";
import {
  CANON_SHA256,
  assertFiniteAction,
  canExecuteLive,
  evaluateDecision,
  type GateSet,
} from "../src/domain.js";

const passGates: GateSet = {
  causal: "PASS",
  differential: "PASS",
  risk: "PASS",
  mobility: "PASS",
  execution: "PASS",
};

describe("APΩ Treasury decision kernel", () => {
  it("rejects an invalid Canon identity", () => {
    const decision = evaluateDecision(
      { id: "c1", criticalUnknown: false, decisionRelevantUnknown: false },
      passGates,
      { canonSha256: "bad", mode: "simulation", hasExitPath: true, explicitLiveAdmission: false },
    );
    expect(decision.verdict).toBe("BLOCKED");
  });

  it("blocks capital on critical unknown while preserving research", () => {
    const decision = evaluateDecision(
      { id: "c2", criticalUnknown: true, decisionRelevantUnknown: true },
      passGates,
      { canonSha256: CANON_SHA256, mode: "simulation", hasExitPath: true, explicitLiveAdmission: false },
    );
    expect(decision.verdict).toBe("RESEARCH_ONLY");
    expect(decision.action.capital).toBe("HOLD_CASH");
    expect(decision.action.evidence).toBe("VERIFY");
  });

  it("does not infer live authority", () => {
    expect(canExecuteLive({
      canonSha256: CANON_SHA256,
      mode: "live_capable",
      hasExitPath: true,
      explicitLiveAdmission: false,
    })).toBe(false);
  });

  it("requires explicit live admission and an exit path", () => {
    expect(canExecuteLive({
      canonSha256: CANON_SHA256,
      mode: "live_capable",
      hasExitPath: true,
      explicitLiveAdmission: true,
    })).toBe(true);
    expect(canExecuteLive({
      canonSha256: CANON_SHA256,
      mode: "live_capable",
      hasExitPath: false,
      explicitLiveAdmission: true,
    })).toBe(false);
  });

  it("keeps action tuples finite", () => {
    expect(() => assertFiniteAction({ capital: "HOLD_CASH", evidence: "VERIFY", universe: "KEEP_ACTIVE" })).not.toThrow();
  });
});
