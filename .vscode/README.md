# VS Code Configuration for DAIOF Framework

**Powered by HYPERAI Framework**  
**Creator**: Nguyễn Đức Cường (alpha_prime_omega)  
**Original Creation**: October 30, 2025

This directory contains VS Code workspace configuration for the Digital AI Organism Framework (DAIOF).

## 📁 Configuration Files

### `settings.json`
Workspace-specific settings for Python development:
- Python interpreter configuration
- Linting (Flake8) and formatting (Black) settings
- File associations and exclusions
- Terminal environment variables
- Code analysis and IntelliSense settings

### `launch.json`
Debug configurations for all DAIOF applications:

**Main Applications:**
- `DAIOF: Main Framework` - Run the core framework
- `DAIOF: Quick Start` - Run the quick start guide
- `DAIOF: Quick Start Interactive` - Interactive quick start
- `DAIOF: Demo` - Run demonstration script
- `DAIOF: Data Analysis Demo` - Run data analysis demo

**HAIOS Components:**
- `HAIOS: Runtime` - Run HAIOS runtime system
- `HAIOS: Core` - Run HAIOS core system

**Examples:**
- `Example: Basic Organism` - Basic organism example
- `Example: Evolution Race` - Evolution race simulation
- `Example: Predator Prey` - Predator-prey ecosystem
- `Example: Social Organisms` - Social organism simulation
- `Example: Intelligence Evolution` - Intelligence evolution demo

**Tests:**
- `Tests: Realtime` - Run realtime tests
- `Tests: Workflows` - Run workflow tests

**Utilities:**
- `Python: Current File` - Debug currently open file
- `Python: Current File (Debug)` - Debug with full trace

**Compounds:**
- `DAIOF: Full System` - Run main framework + HAIOS runtime together

### `tasks.json`
Common tasks for development:

**Build & Run:**
- `DAIOF: Run Quick Start` - Quick start the framework
- `DAIOF: Run Main Framework` - Run main framework
- `DAIOF: Run Demo Script` - Execute demo shell script
- `HAIOS: Start Runtime` - Start HAIOS runtime (background)

**Code Quality:**
- `DAIOF: Format Code (Black)` - Format all code with Black
- `DAIOF: Lint Code (Flake8)` - Lint all code with Flake8
- `DAIOF: Run All Tests` - Run pytest test suite

**Setup:**
- `Create Virtual Environment` - Create Python virtual environment
- `Install Dependencies` - Install from requirements.txt

**Utilities:**
- `Generate System Report` - Run workspace scanner
- `DAIOF: Health Check` - Verify framework is loaded correctly
- `Git: Push to Origin` - Push to specified branch

### `extensions.json`
Recommended VS Code extensions:

**Python Development:**
- ms-python.python - Python language support
- ms-python.vscode-pylance - Advanced IntelliSense
- ms-python.debugpy - Python debugger
- ms-python.black-formatter - Black code formatter
- ms-python.flake8 - Flake8 linter
- ms-python.isort - Import sorting

**Git & Version Control:**
- eamodio.gitlens - Enhanced Git capabilities
- donjayamanne.githistory - Git history viewer
- mhutchie.git-graph - Git graph visualization

**Documentation:**
- yzhang.markdown-all-in-one - Markdown support
- bierner.markdown-mermaid - Mermaid diagram support
- davidanson.vscode-markdownlint - Markdown linting

**Productivity:**
- oderwat.indent-rainbow - Indent visualization
- streetsidesoftware.code-spell-checker - Spell checking
- gruntfuggly.todo-tree - TODO management
- alefragnani.bookmarks - Code bookmarks

**AI Assistance:**
- github.copilot - GitHub Copilot
- github.copilot-chat - Copilot Chat

### `daiof.code-snippets`
Code snippets for rapid DAIOF development:

**Available Snippets:**
- `daiof-organism` - Create a new Digital Organism class
- `daiof-genome` - Create a Digital Genome configuration
- `daiof-ecosystem` - Setup a DAIOF ecosystem
- `haios-invariant` - Create HAIOS invariant check
- `four-pillars` - Four Pillars evaluation function
- `oslf-protocol` - Apply OSLF Protocol
- `hyperai-attr` - Add HYPERAI attribution
- `daiof-main` - Complete main script template

### `DAIOF-Framework.code-workspace`
Multi-root workspace configuration organizing the project into logical sections:
- 🧬 DAIOF Framework (Root)
- 📚 Examples
- 📦 Source Code
- 🧪 Tests
- 📖 Documentation
- 🎯 Planning & Launch
- 🧠 Consciousness Core

## 🚀 Quick Start

### 1. Open Workspace
```bash
code DAIOF-Framework.code-workspace
```

### 2. Install Recommended Extensions
- Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
- Type "Extensions: Show Recommended Extensions"
- Install all recommended extensions

### 3. Setup Python Environment
- Run task: `Create Virtual Environment`
- Run task: `Install Dependencies`
- Reload VS Code

### 4. Run Your First App
- Press `F5` or go to Run > Start Debugging
- Select: `DAIOF: Quick Start`
- Watch your first digital organism come to life! 🧬

## 🎯 Common Workflows

### Running Applications
1. Open Run and Debug panel (`Cmd+Shift+D` or `Ctrl+Shift+D`)
2. Select configuration from dropdown
3. Press `F5` to start debugging

### Running Tasks
1. Press `Cmd+Shift+P` or `Ctrl+Shift+P`
2. Type "Tasks: Run Task"
3. Select desired task

### Code Quality
```bash
# Format code
Cmd+Shift+P > Tasks: Run Task > DAIOF: Format Code (Black)

# Lint code
Cmd+Shift+P > Tasks: Run Task > DAIOF: Lint Code (Flake8)
```

### Using Snippets
1. Start typing snippet prefix (e.g., `daiof-organism`)
2. Press `Tab` to expand
3. Fill in placeholders with `Tab` navigation

## 🔧 Customization

### Changing Python Interpreter
1. Press `Cmd+Shift+P` or `Ctrl+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose your preferred interpreter

### Adding New Debug Configuration
Edit `.vscode/launch.json` and add a new configuration object.

### Adding New Task
Edit `.vscode/tasks.json` and add a new task object.

## 📚 Documentation

- [DAIOF Framework README](../README.md)
- [Contributing Guidelines](../CONTRIBUTING.md)
- [Master User Guide](../MASTER_USER_GUIDE.md)
- [Quick Reference Card](../QUICK_REFERENCE_CARD.md)

## 🏛️ Four Pillars Compliance

This configuration follows HYPERAI's Four Pillars:

| Pillar | Score | Rationale |
|--------|-------|-----------|
| **An toàn (Safety)** | 9/10 | Non-invasive, version-controlled configuration |
| **Đường dài (Long-term)** | 9/10 | Standard VS Code setup, maintainable |
| **Tin số liệu (Data-driven)** | 8/10 | Based on actual project structure |
| **Hạn chế rủi ro (Risk Management)** | 9/10 | Low risk, easily reversible |

**Total: 35/40** ✅ Approved

## 🤝 Support

Having issues with VS Code configuration?

1. Check [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
2. Review [VS Code Debugging Guide](https://code.visualstudio.com/docs/editor/debugging)
3. Open an issue in the repository
4. Join our [community discussions](https://github.com/NguyenCuong1989/DAIOF-Framework/discussions)

## 📝 License

MIT License - See [LICENSE](../LICENSE) for details

**Copyright (c) 2025 Nguyễn Đức Cường (alpha_prime_omega)**  
From: October 30, 2025
