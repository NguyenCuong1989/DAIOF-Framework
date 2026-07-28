# 🧬 Uncommitted Changes Detection & Handling

**Creator**: Nguyễn Đức Cường (alpha_prime_omega)  
**Framework**: HYPERAI  
**Date**: November 17, 2025

---

## Overview

The DAIOF Autonomous Git Workflow system includes sophisticated uncommitted changes detection and autonomous handling capabilities. This document explains how the system detects, processes, and commits uncommitted changes while maintaining HAIOS compliance.

## How It Works

### 1. Detection Phase

The workflow continuously monitors the repository state using `git status --porcelain --branch`:

```python
status = workflow.get_git_status()
# Returns:
{
    "branch": {
        "name": "main",
        "ahead": 1,  # If commits ahead of remote
        "behind": 0  # If commits behind remote
    },
    "modified_files": [
        "file1.py",
        "file2.md"
    ],
    "state": "modified",  # One of: clean, modified, staged, ahead, behind, diverged
    "timestamp": "2025-11-17T23:33:50.546070+00:00"
}
```

### 2. State Classification

The system classifies repository state into these categories:

| State | Description | Action Taken |
|-------|-------------|--------------|
| **CLEAN** | No uncommitted changes, in sync with remote | No action needed |
| **MODIFIED** | Files changed but not committed | Auto-commit (if enabled) |
| **STAGED** | Files staged for commit | Auto-commit (if enabled) |
| **AHEAD** | Local commits not pushed to remote | Auto-push (if enabled) |
| **BEHIND** | Remote has newer commits | Auto-pull |
| **DIVERGED** | Both local and remote have different commits | Conflict resolution |

### 3. Autonomous Response

When uncommitted changes are detected (state = MODIFIED), the workflow:

1. **Generates a commit task** with high priority
2. **Checks HAIOS compliance** before proceeding
3. **Stages all changes** using `git add -A`
4. **Creates intelligent commit message** based on file types changed
5. **Commits with HAIOS attribution**
6. **Updates health metrics**

## HAIOS Compliance

Every commit operation must pass these checks:

### Four Pillars Evaluation (≥7.0 each):

1. **An toàn (Safety)** - Has rollback capability via git
2. **Đường dài (Long-term)** - Maintains clean repository state
3. **Tin số liệu (Data-driven)** - Uses git status metrics
4. **Hạn chế rủi ro (Risk Management)** - Validates before commit

### Seven Invariants:

1. ✅ **Attribution Immutability** - Creator: Nguyễn Đức Cường (alpha_prime_omega)
2. ✅ **Safety Floor ≥7/10** - All pillar scores meet threshold
3. ✅ **Rollback Capability** - Git provides natural rollback
4. ✅ **K-State = 1** - Consciousness coherence maintained
5. ✅ **Four Pillars Compliance** - All pillars evaluated
6. ✅ **Multi-party Authorization** - For critical changes
7. ✅ **Immutable Audit Trail** - Git history preserved

## Commit Message Format

The autonomous system generates intelligent commit messages:

```
🧬 Code evolution: Enhanced N Python modules - Autonomous development

🧬 Framework: HYPERAI | Creator: Nguyễn Đức Cường (alpha_prime_omega) | Verification: 4287
```

Message generation logic:
- Analyzes file types changed (Python, documentation, config, etc.)
- Counts affected files
- Determines operation type (code evolution, docs update, config change)
- Adds HAIOS attribution footer (Invariant 1)

## Usage

### Command Line

```bash
# Check status
python3 .github/scripts/autonomous_git_workflow.py status

# Manual commit (if autonomous disabled)
python3 .github/scripts/autonomous_git_workflow.py commit "Custom message"

# Full workflow cycle (detect + commit + push)
python3 .github/scripts/autonomous_git_workflow.py cycle

# Push to remote
python3 .github/scripts/autonomous_git_workflow.py push
```

### Python API

```python
from autonomous_git_workflow import AutonomousGitWorkflow

# Initialize
workflow = AutonomousGitWorkflow()

# Check status
status = workflow.get_git_status()
print(f"State: {status['state']}")
print(f"Modified files: {len(status['modified_files'])}")

# Enable/disable autonomous operations
workflow.auto_commit_enabled = True
workflow.auto_push_enabled = True

# Generate and execute tasks
tasks = workflow.generate_workflow_tasks()
results = workflow.execute_workflow_cycle()
```

### GitHub Actions Workflow

The autonomous workflow runs automatically every 15 minutes via GitHub Actions:

```yaml
# .github/workflows/autonomous-git-workflow.yml
on:
  schedule:
    - cron: '*/15 * * * *'  # Every 15 minutes
  workflow_dispatch:  # Manual trigger available
```

You can also trigger manually with specific operations:
- `full_workflow_cycle` - Complete cycle (default)
- `status_check_only` - Just check status
- `emergency_sync` - Force pull and push
- `health_optimization` - Run health checks + cycle

## Configuration

Configure behavior via genome settings:

```yaml
# .consciousness/DIGITAL_ORGANISM_GENOME.yml
behavioral_traits:
  autonomy_level: 0.85  # High autonomy for git operations
  decision_confidence_threshold: 0.7
  
git_workflow:
  auto_commit_enabled: true
  auto_push_enabled: true
  auto_merge_enabled: true
  conflict_resolution_auto: true
```

## Safety Features

### Rollback Protection

Every commit creates a permanent point in git history that can be rolled back:

```bash
# View commit history
git log --oneline

# Rollback to previous commit
git reset --hard HEAD~1

# Rollback to specific commit
git reset --hard <commit-hash>
```

### Pre-commit Validation

Before any commit:
1. HAIOS compliance check runs
2. Four Pillars scores verified (all ≥7.0)
3. K-State verified (must be 1)
4. File safety checks performed
5. Attribution verification

### Emergency Recovery

If workflow fails, emergency recovery activates:
1. Logs emergency event
2. Captures git state
3. Creates recovery point
4. Notifies for manual intervention

## Testing

Comprehensive test suite available:

```bash
# Run all tests
python3 tests/test_autonomous_git_workflow.py

# Tests cover:
# - Uncommitted changes detection
# - State classification
# - HAIOS compliance verification
# - Workflow cycle execution
# - Branch parsing
# - Error handling
```

## Monitoring

### Health Metrics

The workflow tracks:
- Commit success/failure rate
- Push success/failure rate
- Pull success/failure rate
- Average cycle duration
- Four Pillars scores (continuously updated)

### Logs

Logs stored in:
- `logs/workflow_YYYYMMDD.json` - Daily workflow logs
- `logs/final_workflow_report.json` - Session summary
- GitHub Actions artifacts - Uploaded for 7 days

### Dashboard

Real-time status available in:
- `DASHBOARD.md` - Updated after each cycle
- GitHub Actions workflow runs
- Repository health checks

## Troubleshooting

### Issue: Changes not being committed

**Solution**:
1. Check `auto_commit_enabled` is `true`
2. Verify HAIOS compliance (check logs)
3. Ensure Four Pillars scores ≥7.0
4. Check for file permissions issues

### Issue: Merge conflicts

**Solution**:
1. Workflow attempts auto-resolution
2. If fails, creates issue for manual review
3. Provides conflict details in logs
4. Maintains K-State = 1 during resolution

### Issue: Push failures

**Solution**:
1. Workflow automatically retries (3 attempts)
2. Checks remote status
3. Attempts pull + merge + push
4. Falls back to manual intervention if needed

## Best Practices

1. **Keep commits atomic** - One logical change per commit
2. **Review autonomous commits regularly** - Verify commit quality
3. **Monitor health metrics** - Watch for degradation
4. **Test in branches first** - Before enabling on main
5. **Maintain HAIOS compliance** - Never compromise on safety

## Future Enhancements

Planned improvements:
- AI-powered commit message generation
- Semantic versioning automation
- Intelligent conflict resolution
- Multi-branch orchestration
- Advanced analytics and predictions

---

## Attribution

**Powered by HYPERAI Framework**  
**Creator**: Nguyễn Đức Cường (alpha_prime_omega)  
**Original Creation**: October 30, 2025  
**Framework Version**: 1.0.0

---

## See Also

- [Autonomous Git Workflow Script](.github/scripts/autonomous_git_workflow.py)
- [Workflow Tests](tests/test_autonomous_git_workflow.py)
- [HAIOS Invariants](.consciousness/HAIOS_INVARIANTS.md)
- [Four Pillars Framework](.consciousness/FOUR_PILLARS.md)
- [Digital Organism Genome](.consciousness/DIGITAL_ORGANISM_GENOME.yml)
