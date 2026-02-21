# 🎯 Agent Management System Guide

## Overview

The **Agent Management System** is a coordination layer that monitors, optimizes, and coordinates the five specialized AI workers in the Avalon autonomous development system. Think of it as the "manager" overseeing a team of AI employees.

---

## What It Does

### Core Functions

1. **Health Monitoring**
   - Tracks all 5 AI worker statuses
   - Monitors workflow success/failure rates
   - Checks API usage and rate limits
   - Calculates overall system health score (0-100)

2. **Coordination**
   - Prevents workers from conflicting work
   - Detects merge conflicts between worker branches
   - Ensures optimal task sequencing
   - Manages dependencies in task queue

3. **Quality Assurance**
   - Reviews AI-generated content
   - Validates consistency across workers
   - Ensures lore and character voice accuracy
   - Checks stat balance across all content

4. **Progress Tracking**
   - Generates daily status reports
   - Tracks completion metrics
   - Identifies bottlenecks
   - Updates session handoff documentation

5. **Problem Resolution**
   - Detects and flags issues early
   - Provides actionable recommendations
   - Escalates to human when needed
   - Resolves minor conflicts automatically

---

## Architecture

### Components

```
Agent Management System
├── Custom Agent
│   └── .github/agents/agent-manager.agent.md
│       (AI-powered coordination logic)
│
├── Orchestrator Script
│   └── .github/scripts/agent_orchestrator.py
│       (Status monitoring and analysis)
│
├── Workflow
│   └── .github/workflows/agent-management.yml
│       (Scheduled execution and reporting)
│
└── Reports
    └── logs/agent-management/
        ├── status-YYYY-MM-DD.json
        └── status-YYYY-MM-DD.md
```

### Workflow Schedule

- **Runs:** Twice daily (6 AM and 6 PM UTC)
- **Manual Trigger:** Available via workflow_dispatch
- **Branch:** Reports committed to `agent-management-logs`
- **Artifacts:** 30-day retention for detailed reports

---

## The Five Managed Workers

### 1. Scene Writer
- **Frequency:** Every 3 hours
- **Branch:** `ai-scene-development`
- **Output:** 300-500 lines per run
- **Focus:** Writing narrative scenes
- **Script:** `scene_writer_agent.py`

### 2. Content Polisher
- **Frequency:** Every 4 hours
- **Branch:** `ai-content-polish`
- **Output:** Sensory enhancements
- **Focus:** Adding taste/smell details
- **Script:** `content_polisher.py`

### 3. Stat Balancer
- **Frequency:** Daily at noon
- **Branch:** `ai-stat-balance`
- **Output:** Balance reports
- **Focus:** Fair stat distribution
- **Script:** `stat_analyzer.py`

### 4. Game Tester
- **Frequency:** Daily at 6 AM + all PRs
- **Branch:** Various (runs everywhere)
- **Output:** QA reports
- **Focus:** Validation and bugs
- **Scripts:** `validate_choicescript.py`, `find_dead_ends.py`

### 5. Autonomous Worker
- **Frequency:** Every 6 hours
- **Branch:** `ai-autonomous-work`
- **Output:** Flexible tasks
- **Focus:** General queue processing
- **Script:** `ai_autonomous_worker.py`

---

## How to Use

### Quick Status Check

Run manually for immediate status:

```bash
python .github/scripts/agent_orchestrator.py
```

This displays:
- System health score (0-100)
- Worker branch status
- Task queue progress
- Scene completion percentages
- Merge conflict warnings
- Actionable recommendations

### Viewing Reports

**Console Output:**
```
🎯 AGENT MANAGEMENT SYSTEM - STATUS REPORT
================================================================================

⏰ Timestamp: 2025-11-25T18:30:00
📊 System Health: 85/100

🔧 CONFIGURATION
  • Silent Mode: ✅ Enabled
  • API Key: ⚠️ Missing (workers won't run)

🤖 AI WORKERS
  ✅ SCENE-WRITER
     Branch: ai-scene-development
     Last Commit: 2 hours ago
     Message: [AI-SCENE] Added content to singing_dunes.txt (+347 lines)
  ...
```

**JSON Reports:** `logs/agent-management/status-YYYY-MM-DD.json`
**Markdown Summaries:** `logs/agent-management/status-YYYY-MM-DD.md`

### GitHub Actions Dashboard

1. Go to **Actions** tab
2. Select **Agent Management Dashboard** workflow
3. View most recent run
4. Check **Summary** for health score and recommendations
5. Download **agent-management-reports** artifact for details

---

## Health Score Calculation

The system calculates a health score (0-100) based on:

| Factor | Impact | Points Deducted |
|--------|--------|-----------------|
| Worker branch missing | Critical | -10 per worker |
| Merge conflicts | High | -15 per conflict |
| Too many tasks in progress (>5) | Medium | -10 |
| No completed tasks | Low | -5 |

**Interpretation:**
- **80-100:** ✅ Healthy - system operating normally
- **50-79:** ⚠️ Warning - needs attention
- **0-49:** 🔴 Critical - immediate intervention required

---

## Common Scenarios

### Scenario 1: All Workers Idle

**Symptom:** No worker branches initialized, health score 50-60

**Cause:** ANTHROPIC_API_KEY not configured

**Solution:**
1. Add API key to repository secrets (see `AI_SYSTEM_ACTIVATION_GUIDE.md`)
2. Manually trigger each worker workflow once
3. Agent Manager will show workers active within 24 hours

### Scenario 2: Merge Conflicts

**Symptom:** Health score drops, conflict warnings in report

**Cause:** Multiple workers modified same files

**Solution:**
1. Review `logs/agent-management/status-*.md` for conflict details
2. Manually merge conflicting branches in priority order:
   - Scene Writer (highest priority)
   - Content Polisher
   - Stat Balancer
   - Autonomous Worker
3. Agent Manager will detect resolution automatically

### Scenario 3: Worker Stuck

**Symptom:** Worker hasn't committed in >24 hours, same task marked in-progress

**Cause:** Task too complex, syntax errors, or API issues

**Solution:**
1. Check workflow run logs in Actions tab
2. Review error messages
3. Manually complete or skip problematic task
4. Update `docs/AI_TASK_QUEUE.md` to unblock worker

### Scenario 4: Too Many Tasks In Progress

**Symptom:** 5+ tasks marked `[→]`, few completions

**Cause:** Workers picking up tasks but not finishing them

**Solution:**
1. Review task scope in `docs/AI_TASK_QUEUE.md`
2. Break large tasks into smaller chunks
3. Mark overly ambitious tasks as `[?]` (needs review)
4. Consolidate related tasks

---

## Integration with Existing System

### Task Queue Updates

Agent Manager monitors `docs/AI_TASK_QUEUE.md` for:
- Task status changes (`[ ]` → `[→]` → `[x]`)
- Blocking dependencies
- Tasks needing review `[?]`

Workers update the queue; Agent Manager analyzes patterns.

### Worker Rules Enforcement

Agent Manager ensures workers follow `docs/AI_WORKER_RULES.md`:
- Max 4 commits per day per worker
- Syntax validation before commit
- Character voice preservation
- Lore consistency checks

### Session Handoff

Updates `docs/AI_SESSION_HANDOFF.md` with:
- Current system state
- Active workers
- Recent progress
- Known issues

---

## Advanced Features

### Custom Agent Integration

The Agent Manager is itself a custom agent (`.github/agents/agent-manager.agent.md`). You can interact with it directly:

```bash
# Via custom agent (if configured in your environment)
@agent-manager analyze current system health
@agent-manager recommend next priorities
@agent-manager resolve coordination issue between scene-writer and content-polisher
```

### Programmatic API

The orchestrator script can be imported and used programmatically:

```python
from agent_orchestrator import AgentOrchestrator

orchestrator = AgentOrchestrator()
report = orchestrator.generate_status_report()
health = report['health_score']

if health < 70:
    recommendations = orchestrator.generate_recommendations(report)
    # Take action based on recommendations
```

### Workflow Triggers

Automatically triggered by:
- **Schedule:** Twice daily (6 AM, 6 PM UTC)
- **Workflow Dispatch:** Manual runs
- **Future:** Could trigger on PR creation, workflow failures, etc.

---

## Troubleshooting

### "No worker branches found"

**Cause:** Workers haven't run yet

**Fix:**
1. Ensure `ANTHROPIC_API_KEY` is configured
2. Manually trigger each worker workflow once
3. Wait for scheduled runs to create branches

### "Health score is 0"

**Cause:** Multiple critical issues

**Fix:**
1. Review detailed JSON report
2. Address each issue in priority order:
   - Add API key (if missing)
   - Resolve merge conflicts
   - Initialize missing workers
   - Clear task bottlenecks

### "Coordination issues detected"

**Cause:** Workers modifying same files simultaneously

**Fix:**
1. Check recent commits on affected branches
2. Manually merge in priority order
3. Consider adjusting worker schedules to avoid overlap
4. Update task queue to separate concerns

### "Workers not making progress"

**Cause:** Could be task complexity, API issues, or syntax errors

**Fix:**
1. Check Actions tab for workflow run logs
2. Review error messages in failed runs
3. Simplify tasks in queue if too complex
4. Verify API key is valid and has credits

---

## Maintenance

### Daily Review (Recommended)

1. Check latest status report in `logs/agent-management/`
2. Review health score trend
3. Merge approved worker PRs
4. Update task priorities if needed

### Weekly Review

1. Analyze worker productivity metrics
2. Adjust workflow schedules if needed
3. Review and consolidate task queue
4. Update worker rules based on learnings

### Monthly Review

1. Evaluate overall system effectiveness
2. Consider new specialized workers
3. Archive old reports
4. Update documentation

---

## Best Practices

### For Beginners (You!)

1. **Start Simple**
   - Let Agent Manager run for 1 week before making changes
   - Review reports but don't override workers unless critical
   - Trust the health score as a guide

2. **Learn the Patterns**
   - Watch how workers interact
   - Note which tasks complete fastest
   - Identify common issues

3. **Gradual Optimization**
   - Adjust one thing at a time
   - Monitor impact for 24-48 hours
   - Document what works

### For Collaboration

1. **Check Status First**
   - Always review latest agent report before manual work
   - Avoid working on files workers are modifying
   - Coordinate through task queue

2. **Update Task Queue**
   - Add new tasks with clear descriptions
   - Mark tasks appropriately ([ ], [→], [?], [x])
   - Provide context for workers

3. **Review Worker Output**
   - Check PRs created by workers
   - Provide feedback in PR comments
   - Merge approved work promptly

---

## Key Metrics

Agent Manager tracks:

- **Worker Activity:** Commits per worker per day
- **Task Velocity:** Tasks completed per week
- **Content Generation:** Lines added per day
- **Quality:** Syntax errors per 1000 lines
- **Efficiency:** Time from task start to completion
- **Coordination:** Conflicts between workers

These metrics are available in daily JSON reports.

---

## Configuration

### Adjusting Worker Schedules

Edit workflow cron schedules in `.github/workflows/`:
- `ai-scene-writer.yml`: Default every 3 hours
- `ai-content-polish.yml`: Default every 4 hours
- `ai-stat-balancer.yml`: Default daily at noon
- `ai-game-tester.yml`: Default daily at 6 AM
- `ai-autonomous-worker.yml`: Default every 6 hours

**Recommendation:** Stagger schedules to avoid simultaneous execution.

### Tuning Task Priorities

Edit `docs/AI_TASK_QUEUE.md`:
- Move urgent tasks to Priority 1
- Break large tasks into smaller chunks
- Add effort estimates for planning
- Mark dependencies clearly

### Customizing Worker Behavior

Edit `.github/agents/spiralverse-omnifeather-config.yml`:
- Adjust character voice templates
- Update quality standards
- Add new validation rules
- Configure coding patterns

---

## Emergency Procedures

### Stop All Workers

If workers are causing issues:

1. **Pause Workflows:**
   - Go to Actions > [workflow name] > ... > Disable workflow
   - Repeat for each AI worker workflow

2. **Create Issue:**
   - Document what went wrong
   - Tag with `ai-system` label
   - Agent Manager will detect pause

3. **Fix Issues:**
   - Review error logs
   - Correct configuration
   - Update task queue or rules

4. **Resume:**
   - Re-enable workflows one at a time
   - Monitor Agent Manager reports
   - Verify health score recovers

### Rollback Worker Changes

If a worker made bad changes:

```bash
# Checkout the worker branch
git checkout ai-scene-development

# Find the bad commit
git log --oneline

# Revert specific commits
git revert <commit-sha>

# Or reset to a known good state
git reset --hard <good-commit-sha>

# Force push
git push origin ai-scene-development --force
```

Agent Manager will detect the rollback and update status.

---

## Future Enhancements

Planned features:
- **Auto-conflict resolution:** Automatically merge compatible changes
- **Predictive analytics:** Estimate task completion times
- **Worker load balancing:** Distribute work based on capacity
- **Smart scheduling:** Adjust frequencies based on queue depth
- **Quality scoring:** Rate worker output quality
- **Learning system:** Improve based on past performance

---

## Getting Help

### For Issues

1. Check latest `logs/agent-management/status-*.md`
2. Review recommendations section
3. Consult this guide for scenario
4. Check `docs/AI_AUTONOMOUS_WORKFLOW.md` for worker details
5. Review `AI_SYSTEM_ACTIVATION_GUIDE.md` for setup

### For Questions

Add questions to `docs/AI_QUESTIONS.md`:
- Agent Manager monitors this file
- Flags items for human review
- Provides context in reports

### For Bugs

Create GitHub issue with:
- Latest agent management report
- Specific worker involved
- Expected vs actual behavior
- Tag with `ai-system` label

---

## Quick Reference

### Status Check Commands

```bash
# Run orchestrator manually
python .github/scripts/agent_orchestrator.py

# View latest report
cat logs/agent-management/status-$(date +%Y-%m-%d).md

# Check worker branches
git branch -r | grep -E "(ai-scene|ai-content|ai-stat|ai-autonomous)"

# See recent worker activity
git log --all --oneline --author="SpiralVerse" --since="1 week ago"
```

### Important Files

- **Configuration:** `config/automation-settings.json`
- **Task Queue:** `docs/AI_TASK_QUEUE.md`
- **Worker Rules:** `docs/AI_WORKER_RULES.md`
- **Status Reports:** `logs/agent-management/status-*.md`
- **Workflow:** `.github/workflows/agent-management.yml`

### Key Concepts

- **Health Score:** 0-100 rating of system health
- **Worker Branch:** Isolated branch where each worker commits
- **Task Queue:** Priority-ordered work list in `AI_TASK_QUEUE.md`
- **Coordination Issue:** When workers conflict or duplicate work
- **Silent Mode:** No user notifications for routine operations

---

## Integration with GitHub

### Artifacts

Agent Management uploads reports as artifacts:
- Navigate to Actions > Agent Management Dashboard
- Click latest run
- Download "agent-management-reports" artifact
- Extract and review JSON/Markdown files

### Branch Structure

```
main (protected)
├── ai-scene-development (Scene Writer)
├── ai-content-polish (Content Polisher)
├── ai-stat-balance (Stat Balancer)
├── ai-autonomous-work (Autonomous Worker)
└── agent-management-logs (Management Reports)
```

Each branch merges into `main` via PR after human review.

### Notifications

With silent mode enabled (default):
- ✅ No notifications for routine operations
- ⚠️ Notifications for warnings (health <70)
- 🔴 Notifications for critical issues
- 📊 Reports available in artifacts (no email)

---

## Success Indicators

Your system is working well when:

1. ✅ Health score consistently >80
2. ✅ 3-5 tasks completing per week
3. ✅ Worker branches active and conflict-free
4. ✅ PRs created regularly with quality content
5. ✅ No workers stuck on same task >48 hours
6. ✅ Stat balance improving over time
7. ✅ Syntax validation passing
8. ✅ Lore consistency maintained

---

## Comparison to Manual Development

| Aspect | Manual | With Agent Manager |
|--------|--------|-------------------|
| Scene writing | 2-4 hours per scene | 300-500 lines every 3 hours |
| Stat balancing | Manual spreadsheet work | Automated daily analysis |
| Quality checks | Manual testing | Automated every PR |
| Coordination | Mental overhead | Automated monitoring |
| Progress tracking | Manual notes | Automated reports |
| Merge conflicts | Surprise problems | Early detection |

---

## Tips for GitHub Beginners

### Understanding the Dashboard

1. **Actions Tab** = Where workers run
2. **Branches** = Separate workspaces for each worker
3. **Pull Requests** = Workers asking to merge their work
4. **Artifacts** = Downloaded reports and data

### Reading Reports

- **Green ✅** = Everything good
- **Yellow ⚠️** = Needs attention soon
- **Red 🔴** = Fix immediately

### When to Intervene

**✅ Let Workers Handle:**
- Writing scene content
- Adding sensory details
- Basic stat adjustments
- Syntax validation

**⚠️ You Should Review:**
- Major lore changes
- Character relationship changes
- New magical mechanics
- Ending implementations

**🔴 You Must Handle:**
- Merge conflicts
- Security issues
- API key configuration
- Final approval before release

---

## Related Documentation

- `AI_SYSTEM_ACTIVATION_GUIDE.md` - Initial setup
- `docs/AI_AUTONOMOUS_WORKFLOW.md` - System architecture
- `docs/AI_WORKER_RULES.md` - Worker behavior standards
- `docs/AI_TASK_QUEUE.md` - Current work priorities
- `ACCOUNTS_README.md` - Inter-account automation
- `.github/README_AI_SYSTEM.md` - Quick start guide

---

## Summary

The Agent Management System gives you **visibility and control** over your AI workforce without requiring constant oversight. It:

- Monitors 5 specialized workers automatically
- Detects and prevents problems early
- Provides clear status and recommendations
- Coordinates complex multi-worker tasks
- Scales with your project needs

**You focus on creative decisions and review; the Agent Manager handles coordination.**

---

**Last Updated:** 2025-11-25  
**Version:** 1.0  
**Maintenance:** Automated via agent-management.yml workflow
