# GitHub Scripts Directory

This directory contains automation scripts used by GitHub Actions workflows.

## 🤖 Autonomous PR Management Scripts

### Auto-Review System
- **`auto_reviewer.py`** - Automated PR reviewer that validates ChoiceScript syntax, checks merge conflicts, scans for security issues, and assesses risk levels
- **`post_review_comments.py`** - Posts automated review comments to PRs

### Auto-Fix System  
- **`auto_fixer.py`** - Automatically fixes common issues in PRs including merge conflicts, ChoiceScript syntax errors, and formatting

### Auto-Merge System
- **`auto_merger.py`** - Intelligently decides whether to merge a PR based on risk assessment and safety checks

## 🎮 Game Development Scripts

### ChoiceScript Tools
- **`validate_choicescript.py`** - Validates ChoiceScript syntax for common errors
- **`find_dead_ends.py`** - Finds dead ends and unreachable content in game scenes
- **`stat_analyzer.py`** - Analyzes stat progression and balance

### Content Creation
- **`scene_writer_agent.py`** - AI-powered scene writing assistant
- **`content_polisher.py`** - Polishes and improves game content
- **`ai_autonomous_worker.py`** - Autonomous AI worker for various tasks

## 🔧 Management & Orchestration

- **`agent_manager_cli.py`** - Command-line interface for managing AI agents
- **`agent_orchestrator.py`** - Orchestrates multiple AI agents for complex tasks

## Usage

Most scripts are designed to be called by GitHub Actions workflows. To use manually:

```bash
# Review a PR
python .github/scripts/auto_reviewer.py --pr-number 123 --repo owner/repo

# Validate ChoiceScript files
python .github/scripts/validate_choicescript.py choicescript_game/scenes/*.txt

# Analyze stats
python .github/scripts/stat_analyzer.py
```

## Documentation

See individual script files for detailed documentation and usage examples.

For the autonomous PR management system, see: `docs/AUTO_MERGE_SYSTEM.md`
