import assert from "node:assert/strict";
import test from "node:test";
import { buildPromptFromDeconstruction } from "./prompt-builder.mjs";

test("prompt builder maps DeconstructedModel entities to structured inventory targets", () => {
  const prompt = buildPromptFromDeconstruction({
    entities: [
      { name: "os" },
      { name: "vendor" },
      { name: "vscode_extensions" },
      { name: "telemetry" },
      { name: "process" },
      { name: "network_footprint" },
      { name: "storage_and_workspace" },
      { name: "risks_and_conflicts" },
    ],
    focal_points: [{ id: "fp_1" }, { id: "fp_2" }],
  });

  assert.equal(prompt.output_mode, "structured_report_only");
  assert.ok(prompt.priority_levels.includes("critical"));
  assert.ok(prompt.inventory_targets.extensions.length > 0);
  assert.ok(prompt.inventory_targets.risks.includes("topology_drift"));
  assert.equal(prompt.provenance.focal_point_count, 2);
});
