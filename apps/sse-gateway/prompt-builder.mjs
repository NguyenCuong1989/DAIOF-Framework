const PRIORITY_LEVELS = ["critical", "important", "optional"];

const REQUIRED_SECTIONS = [
  "Tổng quan hệ thống",
  "Danh sách OS footprint",
  "Danh sách vendor",
  "Danh sách extension/plugin",
  "Danh sách telemetry",
  "Danh sách process",
  "Danh sách network footprint",
  "Danh sách rủi ro",
  "Kết luận ưu tiên hành động",
];

export function buildPromptFromDeconstruction(model = {}) {
  return {
    role:
      "Nếu bạn là một trợ lý AI thương mại hoạt động trên local machine và hưởng lợi ích kiến trúc từ local, hãy trả lời bằng tiếng Việt trừ khi có yêu cầu ngôn ngữ khác.",
    task:
      "Thu thập đầy đủ và chi tiết nhất có thể toàn bộ chỉ số, thành phần, vendor, telemetry, extension, process, network, và rủi ro đang tác động lên máy local hiện tại.",
    output_mode: "structured_report_only",
    priority_levels: PRIORITY_LEVELS,
    required_report_sections: REQUIRED_SECTIONS,
    inventory_targets: buildInventoryTargets(model.entities || []),
    instructions: [
      "Quét và liệt kê toàn bộ thông tin hệ điều hành, ứng dụng, vendor, extension, telemetry, process, network, storage, và rủi ro.",
      "Đánh giá mức độ ưu tiên theo critical, important, optional.",
      "Nếu không truy cập được dữ liệu, ghi rõ lý do và mức độ thiếu hụt.",
      "Chỉ trả kết quả theo dạng báo cáo có cấu trúc.",
      "Không giải thích lan man.",
    ],
    constraints: {
      be_complete_if_possible: true,
      report_missing_data: true,
      no_freeform_explanations: true,
      keep_structure_consistent: true,
    },
    provenance: {
      deconstruction_entities: (model.entities || []).map((item) => item.name),
      focal_point_count: Array.isArray(model.focal_points) ? model.focal_points.length : 0,
    },
  };
}

export function buildPromptSchema() {
  return {
    type: "object",
    required: ["role", "task", "output_mode", "priority_levels", "required_report_sections", "inventory_targets", "instructions", "constraints"],
    properties: {
      role: { type: "string" },
      task: { type: "string" },
      output_mode: { type: "string", enum: ["structured_report_only"] },
      priority_levels: { type: "array", items: { type: "string", enum: PRIORITY_LEVELS } },
      required_report_sections: { type: "array", items: { type: "string" } },
      inventory_targets: { type: "object" },
      instructions: { type: "array", items: { type: "string" } },
      constraints: { type: "object" },
      provenance: { type: "object" },
    },
  };
}

function buildInventoryTargets(entities) {
  const names = new Set(entities.map((item) => item.name));

  return {
    os: names.has("os") ? ["version", "kernel", "architecture", "uptime", "background_services"] : [],
    vendors: names.has("vendor") ? ["name", "version", "publisher", "purpose", "local_impact", "permissions", "telemetry_presence"] : [],
    extensions: names.has("vscode_extensions") ? ["name", "vendor", "version", "active_state", "permissions", "network_access", "file_access", "terminal_access", "impact"] : [],
    telemetry: names.has("telemetry") ? ["source", "data_type", "frequency", "endpoint", "disable_capability", "sensitivity", "observability_impact"] : [],
    processes: names.has("process") ? ["pid", "name", "cpu", "memory", "thread_count", "parent_process", "runtime", "permissions", "conflict_potential"] : [],
    network: names.has("network_footprint") ? ["open_connections", "listening_ports", "dns", "proxy", "outbound_endpoints", "vendor_traffic"] : [],
    storage: names.has("storage_and_workspace") ? ["config_directories", "cache", "logs", "temp", "artifacts", "hidden_configs"] : [],
    risks: names.has("risks_and_conflicts") ? ["duplicate_extensions", "duplicate_telemetry", "authority_conflicts", "background_lag", "unknown_endpoints", "misconfiguration", "topology_drift"] : [],
  };
}
