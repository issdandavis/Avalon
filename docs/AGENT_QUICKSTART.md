# Agent Task Quick Start Guide

Get your AI agents running in under 5 minutes!

## Prerequisites

✅ Python 3.11+ installed
✅ Git configured
✅ Repository cloned locally

## Step 1: Install Dependencies (Local Development)

```bash
pip install anthropic GitPython pyyaml
```

## Step 2: Test the System

```bash
python .github/scripts/test_agent_system.py
```

Expected output: **System Health: 93/100** ✅

## Step 3: Run Individual Agents

### Check System Health
```bash
python .github/scripts/agent_orchestrator.py
```

### Validate ChoiceScript Files
```bash
python .github/scripts/validate_choicescript.py choicescript_game/scenes/*.txt
```

### Find Dead Ends
```bash
python .github/scripts/find_dead_ends.py
```

### Analyze Stat Balance
```bash
python .github/scripts/stat_analyzer.py
```

### Check for Conflicts
```bash
python .github/scripts/conflict_resolver.py
```

## Step 4: Configure GitHub Actions (Optional)

### Add API Key for AI Workers

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `ANTHROPIC_API_KEY`
4. Value: Your Anthropic API key
5. Click **Add secret**

> **Note:** AI workers will be skipped automatically if the API key is not configured. This is intentional and safe.

### Enable Workflows

All workflows are configured and ready to run:

- ✅ **Agent Management** - Runs twice daily (6 AM & 6 PM UTC)
- ✅ **Scene Writer** - Every 3 hours (requires API key)
- ✅ **Content Polisher** - Every 4 hours (requires API key)
- ✅ **Stat Balancer** - Daily at noon UTC
- ✅ **Autonomous Worker** - Every 6 hours (requires API key)
- ✅ **Game Tester** - On pull requests

### Manual Workflow Triggers

1. Go to **Actions** tab
2. Select a workflow (e.g., "Agent Management Dashboard")
3. Click **Run workflow**
4. Choose branch (usually `main`)
5. Click **Run workflow**

## Step 5: Initialize Worker Branches (Optional)

Worker branches are created automatically when workflows run. To create them manually:

```bash
git checkout -b ai-scene-development
git push origin ai-scene-development

git checkout -b ai-content-polish
git push origin ai-content-polish

git checkout -b ai-stat-balance
git push origin ai-stat-balance

git checkout -b ai-autonomous-work
git push origin ai-autonomous-work

git checkout main
```

## Troubleshooting

### "anthropic package not installed"
```bash
pip install anthropic
```

### "ANTHROPIC_API_KEY not set"
For local testing:
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

For GitHub Actions, add it as a repository secret (see Step 4).

### System health below 70%
```bash
# Run full diagnostics
python .github/scripts/agent_orchestrator.py

# Check for specific issues
python .github/scripts/conflict_resolver.py
```

### Need more help?
See the comprehensive troubleshooting guide:
```bash
cat docs/AGENT_TROUBLESHOOTING.md
```

## What Each Agent Does

| Agent | Purpose | Frequency | Requires API |
|-------|---------|-----------|--------------|
| **Orchestrator** | Monitors system health | Twice daily | No |
| **Scene Writer** | Writes new ChoiceScript scenes | Every 3 hours | Yes |
| **Content Polisher** | Adds sensory details | Every 4 hours | Yes |
| **Stat Balancer** | Ensures fair stat distribution | Daily | No |
| **Autonomous Worker** | General task completion | Every 6 hours | Yes |
| **Game Tester** | Validates syntax & flow | On PRs | No |

## Success Indicators

✅ Test suite passes with 0 failures
✅ System health ≥ 85%
✅ All workflows run without errors
✅ Worker branches exist and are active
✅ No merge conflicts detected

## Next Steps

1. ✅ Run the test suite
2. ✅ Review the agent orchestrator output
3. ✅ Check GitHub Actions workflow runs
4. ✅ Review `docs/AI_TASK_QUEUE.md` for priorities
5. ✅ Monitor `logs/agent-management/` for reports

## Quick Commands Cheatsheet

```bash
# Test everything
python .github/scripts/test_agent_system.py

# System health
python .github/scripts/agent_orchestrator.py

# Validate all scenes
python .github/scripts/validate_choicescript.py choicescript_game/scenes/*.txt

# Stat analysis
python .github/scripts/stat_analyzer.py

# Find problems
python .github/scripts/find_dead_ends.py

# Check conflicts
python .github/scripts/conflict_resolver.py

# View logs
cat logs/agent-management/status-$(date +%Y-%m-%d).json
```

## Resources

- 📖 **Full Troubleshooting:** `docs/AGENT_TROUBLESHOOTING.md`
- 📋 **Task Queue:** `docs/AI_TASK_QUEUE.md`
- 📜 **Worker Rules:** `docs/AI_WORKER_RULES.md`
- ⚙️ **Configuration:** `config/automation-settings.json`
- 🎯 **Agent Overview:** `AGENT_MANAGEMENT_README.md`

---

**Last Updated:** 2025-12-08
**System Status:** ✅ All agents operational
**Health Score:** 93/100
