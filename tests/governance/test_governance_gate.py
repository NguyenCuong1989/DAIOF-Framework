import json
import shutil
from pathlib import Path

import pytest

from tools.governance.governance_gate import (
    build_manifest,
    is_pinned_action,
    validate,
)


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_repository_governance_contract_is_valid():
    assert validate(REPO_ROOT) == []


def test_manifest_maps_every_workflow():
    manifest = build_manifest(REPO_ROOT)
    workflow_files = {
        path.relative_to(REPO_ROOT).as_posix()
        for pattern in ("*.yml", "*.yaml")
        for path in (REPO_ROOT / ".github" / "workflows").glob(pattern)
    }
    assert manifest["workflow_count"] == len(workflow_files)
    assert {item["path"] for item in manifest["workflows"]} == workflow_files


def test_action_pinning_requires_full_commit_sha():
    assert is_pinned_action("actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683")
    assert not is_pinned_action("actions/checkout@v4")
    assert is_pinned_action("./.github/actions/local")


def test_manifest_drift_fails_closed(tmp_path):
    repo = tmp_path / "repo"
    shutil.copytree(REPO_ROOT / ".github", repo / ".github")
    shutil.copytree(REPO_ROOT / "governance", repo / "governance")
    (repo / "tools" / "governance").mkdir(parents=True)

    workflow = repo / ".github" / "workflows" / "new-workflow.yml"
    workflow.write_text(
        "name: Drift\non: [push]\npermissions:\n  contents: read\njobs:\n  check:\n    runs-on: ubuntu-latest\n    steps: []\n"
    )

    errors = validate(repo)
    assert any("drift detected" in error for error in errors)


def test_missing_choice_evidence_fails_closed(tmp_path):
    repo = tmp_path / "repo"
    shutil.copytree(REPO_ROOT / ".github", repo / ".github")
    shutil.copytree(REPO_ROOT / "governance", repo / "governance")
    review_path = repo / "governance" / "choice_review.json"
    review = json.loads(review_path.read_text())
    review.pop("override_tracking")
    review_path.write_text(json.dumps(review))

    errors = validate(repo)
    assert any("choice_review missing fields" in error for error in errors)


def test_direct_merge_api_is_rejected(tmp_path):
    repo = tmp_path / "repo"
    shutil.copytree(REPO_ROOT / ".github", repo / ".github")
    shutil.copytree(REPO_ROOT / "governance", repo / "governance")
    unsafe = repo / ".github" / "workflows" / "unsafe.yml"
    unsafe.write_text(
        "name: Unsafe\non: [pull_request]\npermissions:\n  contents: write\njobs:\n  merge:\n    runs-on: ubuntu-latest\n    steps:\n      - run: echo github.rest.pulls.merge\n"
    )

    # Refreshing the manifest cannot make a prohibited merge path acceptable.
    errors = validate(repo, write_manifest=True)
    assert any("direct merge API bypass" in error for error in errors)
