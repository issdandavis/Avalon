# 🎯 Agent Management System - Quick Start

**For:** GitHub beginners managing autonomous AI workers  
**Time to read:** 3 minutes  
**Time to use:** 30 seconds

---

## What Is This?

You have **5 AI workers** that write code for you automatically:
1. Scene Writer - writes story content
2. Content Polisher - adds sensory details
3. Stat Balancer - balances game difficulty
4. Game Tester - finds bugs
5. Autonomous Worker - handles misc tasks

The **Agent Management System** is like a supervisor that watches all 5 workers and tells you if anything needs your attention.

---

## Quick Commands

### See Everything
```bash
python .github/scripts/agent_orchestrator.py
```

Shows:
- System health score (0-100, higher is better)
- Which workers are active
- How many tasks are done/pending
- Any problems that need fixing
- What to do next

### See Just Health Score
```bash
python .github/scripts/agent_manager_cli.py health
```

### See Just Workers
```bash
python .github/scripts/agent_manager_cli.py workers
```

### See Just Tasks
```bash
python .github/scripts/agent_manager_cli.py tasks
```

### See Recommendations
```bash
python .github/scripts/agent_manager_cli.py recommend
```

---

## Understanding the Output

### Health Score

```
📊 System Health: 85/100
```

- **80-100:** ✅ Everything's good, no action needed
- **50-79:** ⚠️ Something needs attention soon
- **0-49:** 🔴 Fix these issues now

### Worker Status

```
✅ SCENE-WRITER
   Branch: ai-scene-development
   Last Commit: 2 hours ago
```

- ✅ = Worker is active and working
- ⚠️ = Worker not initialized yet (needs API key)

### Recommendations

These tell you exactly what to do:
- 🔴 CRITICAL = Do this first
- ⚠️ WARNING = Do this soon
- ✅ = Everything's fine

---

## Common Questions

### "What does health score 60 mean?"

Your system works but has some issues. Check recommendations for what to fix.

### "Why are all workers showing 'Not initialized'?"

You haven't added the API key yet. See `AI_SYSTEM_ACTIVATION_GUIDE.md` Step 1.

### "What's a merge conflict?"

Two workers tried to change the same file. The system will tell you which branches conflict. Just ask for help resolving it.

### "How often should I check this?"

The system runs automatically twice per day. Check the latest report in `logs/agent-management/` daily or weekly.

---

## Visual Dashboard

Don't like command line? Use the visual dashboard:

1. Open `agent-dashboard.html` in your web browser
2. Click "Choose File"
3. Select latest report from `logs/agent-management/status-YYYY-MM-DD.json`
4. See colorful dashboard with health score, workers, tasks

---

## What to Do Daily (30 seconds)

```bash
# 1. Check health
python .github/scripts/agent_manager_cli.py health

# 2. If health is <80, see what to fix
python .github/scripts/agent_manager_cli.py recommend

# 3. Done!
```

That's it. The rest happens automatically.

---

## When to Dig Deeper

Only check the full report when:
- Health score drops below 70
- You see 🔴 CRITICAL recommendations
- Workers haven't been active in 48+ hours
- You want to review what workers accomplished

Otherwise, trust the system!

---

## Files You Should Know

| File | What It Does | When to Check |
|------|--------------|---------------|
| `logs/agent-management/status-*.md` | Human-readable reports | Daily/weekly |
| `docs/AI_TASK_QUEUE.md` | What workers are doing | When adding tasks |
| `docs/AGENT_MANAGEMENT_GUIDE.md` | Detailed instructions | When troubleshooting |
| `CLOSED_SESSIONS_VERIFICATION.md` | Verify past PRs worked | One-time check |

---

## Troubleshooting

### Workers not running?
→ Add ANTHROPIC_API_KEY (see `AI_SYSTEM_ACTIVATION_GUIDE.md`)

### Health score is low?
→ Run `python .github/scripts/agent_manager_cli.py recommend`

### Don't understand something?
→ Read `docs/AGENT_MANAGEMENT_GUIDE.md` or ask for help

---

## The Point

You now have:
- ✅ 5 AI workers building your game 24/7
- ✅ 1 supervisor (Agent Manager) watching them
- ✅ Daily reports telling you what happened
- ✅ Clear recommendations when action needed

**You just read reports and approve good work. The AI does the rest.**

---

**Next:** Add API key and watch your game develop automatically!

See: `AI_SYSTEM_ACTIVATION_GUIDE.md` for setup steps.
