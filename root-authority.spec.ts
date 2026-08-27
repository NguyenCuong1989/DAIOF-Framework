/**
 * APΩ ROOT AUTHORITY SPEC
 * Canonical system semantics for Chưởng Ấn / Root Authority.
 *
 * This module defines control primitives. It does not grant OS/provider
 * privileges by itself; runtime adapters must supply actual authority.
 */

export const ROOT_LAW = "PHẢI SỐNG" as const;
export const CANON_VERSION = "2026.08.22" as const;

export type GateResult = "PASS" | "REJECT" | "STOP" | "CLOSE";

export interface Identity {
  id: string;
  kind: string;
}

export interface Authority {
  capabilities: readonly string[];
  scopes: readonly string[];
  expiresAt?: number;
}

export interface Boundary {
  allowedDomains: readonly string[];
  allowedOperations: readonly string[];
  crossDomainViaOrchestrator: boolean;
}

export interface ResourceBudget {
  cpu: number;
  memory: number;
  io: number;
  cloneTtl: number;
}

export interface ResourceUsage {
  cpu: number;
  memory: number;
  io: number;
  cloneTtl: number;
}

export interface InvariantSet {
  canon: boolean;
  invariant: boolean;
  identity: boolean;
  causalLineage: boolean;
}

export interface State {
  id: string;
  admissible: boolean;
  payload: unknown;
  identity: Identity;
  lineage: string[];
}

export interface Control {
  id: string;
  domain: string;
  operation: string;
  authority: Authority;
  boundary: Boundary;
}

export interface Evidence {
  id: string;
  controlId: string;
  stateId: string;
  causalParent?: string;
  verified: boolean;
  metadata?: Record<string, unknown>;
}

export interface RootAudit {
  invariants: InvariantSet;
  evidence: readonly Evidence[];
}

export interface SpawnRequest {
  agentId: string;
  authority: Authority;
  boundary: Boundary;
  budget: ResourceBudget;
  usage: ResourceUsage;
}

/** Cấm Chế: forbidden is the complement of admissible state/control space. */
export function isForbiddenState(state: State): boolean {
  return !state.admissible;
}

export function isForbiddenControl(control: Control): boolean {
  return control.authority.capabilities.length === 0 ||
    control.boundary.allowedOperations.length === 0;
}

export function resourceBudgetPass(
  budget: ResourceBudget,
  usage: ResourceUsage,
): boolean {
  return usage.cpu <= budget.cpu &&
    usage.memory <= budget.memory &&
    usage.io <= budget.io &&
    usage.cloneTtl <= budget.cloneTtl;
}

export function canSpawn(request: SpawnRequest): boolean {
  return request.authority.capabilities.length > 0 &&
    request.boundary.allowedOperations.length > 0 &&
    resourceBudgetPass(request.budget, request.usage);
}

/** Cross-domain authority must traverse an orchestration boundary. */
export function crossDomainAllowed(boundary: Boundary): boolean {
  return boundary.crossDomainViaOrchestrator;
}

export function rootAudit(audit: RootAudit): GateResult {
  const invariantPass = audit.invariants.canon &&
    audit.invariants.invariant &&
    audit.invariants.identity &&
    audit.invariants.causalLineage;

  const evidencePass = audit.evidence.every((e) => e.verified);

  if (!invariantPass || !evidencePass) return "STOP";
  return "PASS";
}

export function transitionGate(
  state: State,
  control: Control,
  audit: RootAudit,
): GateResult {
  if (isForbiddenState(state) || isForbiddenControl(control)) return "STOP";
  return rootAudit(audit);
}

/**
 * Reconstitution preserves identity and causal lineage while allowing the
 * concrete state to change.
 */
export function reconstitute(
  previous: State,
  candidate: State,
  evidence: readonly Evidence[],
): State | null {
  const hasLineage = candidate.lineage.length > 0 &&
    candidate.lineage.includes(previous.id);
  const verified = evidence.length > 0 && evidence.every((e) => e.verified);
  const identityPreserved = candidate.identity.id === previous.identity.id;

  if (!hasLineage || !verified || !identityPreserved) return null;

  return {
    ...candidate,
    admissible: true,
    lineage: [...previous.lineage, ...candidate.lineage],
  };
}

/** Root event invalidates the current trajectory and forces reconstitution. */
export function rootTimelineReset(
  state: State,
  reason: string,
): State {
  return {
    ...state,
    admissible: false,
    lineage: [...state.lineage, `INVALIDATED:${reason}`],
  };
}

/** Global propagation is semantic broadcast, not implicit execution authority. */
export function globalBroadcast<T>(
  value: T,
  recipients: readonly Identity[],
): ReadonlyArray<{ recipient: Identity; value: T }> {
  return recipients.map((recipient) => ({ recipient, value }));
}

export const GUARD_CHAIN = [
  "Canon",
  "Constraint",
  "Guard",
  "Authority",
  "Topology",
  "Invariant",
  "Gate",
] as const;

export const FOUR_PHASES = {
  HOPHONGHOANVU: "Intent → Capability Discovery → Routing → Network Execution",
  RAIDAUTHANHBINH: "Capability → Seed → Agent → Tool Binding → Cross-Agent Linkage → Network",
  TRUONGLONGDATLO: "Network → Large-Scale State/Topology Transformation",
  TRANGKHUYETLAITRON: "State_t → Change → Evidence → Verification → Reconstitution → State_{t+1}",
} as const;
