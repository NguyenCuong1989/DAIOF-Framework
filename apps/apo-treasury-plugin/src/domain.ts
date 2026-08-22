export const CANON_SHA256 = "7e0c0643642958ad3a2bb778be5f82f7dbf6641afc9eb17af8ee0577609cebcc" as const;

export type Mode = "simulation" | "read_only_live" | "paper" | "live_capable";
export type GateStatus = "PASS" | "BLOCK" | "UNKNOWN";
export type Verdict = "CAPITAL_ALLOWED" | "RESEARCH_ONLY" | "BLOCKED";
export type CapitalAction = "HOLD_CASH" | "ALLOCATE" | "ACT_SMALL" | "SCALE" | "REDUCE" | "EXIT" | "ZERO";
export type EvidenceAction = "MONITOR" | "RESEARCH_WITH_BUDGET" | "VERIFY" | "FALSIFY" | "REFRESH";
export type UniverseAction = "KEEP_ACTIVE" | "PROMOTE" | "DEMOTE" | "ARCHIVE" | "REOPEN";

export interface Candidate {
  id: string;
  criticalUnknown: boolean;
  decisionRelevantUnknown: boolean;
}

export interface GateSet {
  causal: GateStatus;
  differential: GateStatus;
  risk: GateStatus;
  mobility: GateStatus;
  execution: GateStatus;
}

export interface ActionTuple {
  capital: CapitalAction;
  evidence: EvidenceAction;
  universe: UniverseAction;
}

export interface Decision {
  candidateId: string;
  verdict: Verdict;
  gates: GateSet;
  action: ActionTuple;
  reasons: string[];
}

export interface RuntimeEnvelope {
  canonSha256: string;
  mode: Mode;
  hasExitPath: boolean;
  explicitLiveAdmission: boolean;
}

const ALL_PASS = (gates: GateSet): boolean =>
  Object.values(gates).every((status) => status === "PASS");

export function validateCanon(canonSha256: string): boolean {
  return canonSha256 === CANON_SHA256;
}

export function evaluateDecision(candidate: Candidate, gates: GateSet, runtime: RuntimeEnvelope): Decision {
  const reasons: string[] = [];
  const canonValid = validateCanon(runtime.canonSha256);
  const liveAllowed = canExecuteLive(runtime);

  if (!canonValid) reasons.push("CANON_IDENTITY_INVALID");
  if (!runtime.hasExitPath) reasons.push("EXIT_PATH_MISSING");
  if (runtime.mode === "live_capable" && !runtime.explicitLiveAdmission) reasons.push("LIVE_ADMISSION_MISSING");
  if (candidate.criticalUnknown) reasons.push("CRITICAL_UNKNOWN_BLOCKS_CAPITAL");
  if (gates.execution === "BLOCK") reasons.push("EXECUTION_GATE_BLOCKED");
  if (gates.execution === "UNKNOWN") reasons.push("EXECUTION_GATE_UNKNOWN");

  const capitalAllowed = canonValid
    && runtime.hasExitPath
    && !candidate.criticalUnknown
    && ALL_PASS(gates)
    && (runtime.mode !== "live_capable" || liveAllowed);

  if (capitalAllowed) {
    return {
      candidateId: candidate.id,
      verdict: "CAPITAL_ALLOWED",
      gates,
      action: { capital: "ACT_SMALL", evidence: "MONITOR", universe: "KEEP_ACTIVE" },
      reasons,
    };
  }

  const researchAllowed = canonValid && (candidate.decisionRelevantUnknown || candidate.criticalUnknown || !ALL_PASS(gates));
  if (researchAllowed) {
    return {
      candidateId: candidate.id,
      verdict: "RESEARCH_ONLY",
      gates,
      action: { capital: "HOLD_CASH", evidence: "VERIFY", universe: "KEEP_ACTIVE" },
      reasons,
    };
  }

  return {
    candidateId: candidate.id,
    verdict: "BLOCKED",
    gates,
    action: { capital: "ZERO", evidence: "REFRESH", universe: "ARCHIVE" },
    reasons,
  };
}

export function assertFiniteAction(action: ActionTuple): void {
  if (!action.capital || !action.evidence || !action.universe) {
    throw new Error("FINITE_ACTION_REQUIRED");
  }
}

export function canExecuteLive(runtime: RuntimeEnvelope): boolean {
  return validateCanon(runtime.canonSha256)
    && runtime.mode === "live_capable"
    && runtime.explicitLiveAdmission
    && runtime.hasExitPath;
}
