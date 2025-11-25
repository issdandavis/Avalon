# 🎯 Agent Management Quick Reference Card

**Print this or keep it open!**

---

## ⚡ Daily Commands (30 seconds)

```bash
# Navigate to repository
cd /path/to/Avalon

# Check health
python .github/scripts/agent_manager_cli.py health

# If <80, see what to do
python .github/scripts/agent_manager_cli.py recommend
```

---

## 📊 Understanding Health Scores

| Score | Symbol | Meaning | Action |
|-------|--------|---------|--------|
| 80-100 | ✅ | Healthy | None - check tomorrow |
| 50-79 | ⚠️ | Warning | Follow recommendations |
| 0-49 | 🔴 | Critical | Fix issues immediately |

---

## 🤖 The 6 AI Agents

| Agent | Emoji | Runs | Does |
|-------|-------|------|------|
| Scene Writer | 🎭 | Every 3hr | Writes 300-500 lines |
| Content Polisher | ✨ | Every 4hr | Adds sensory details |
| Stat Balancer | ⚖️ | Daily noon | Balances difficulty |
| Game Tester | 🧪 | Daily 6 AM | Finds bugs |
| Autonomous Worker | 🔧 | Every 6hr | Misc tasks |
| **Agent Manager** | 🎯 | **2x daily** | **Coordinates all** |

---

## 💻 All Commands

```bash
# Health check only
python .github/scripts/agent_manager_cli.py health

# See recommendations
python .github/scripts/agent_manager_cli.py recommend

# List all workers
python .github/scripts/agent_manager_cli.py workers

# Task queue status
python .github/scripts/agent_manager_cli.py tasks

# Full report
python .github/scripts/agent_orchestrator.py
```

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| `AGENT_START_HERE.md` | Quick orientation (2 min) |
| `AGENT_MANAGEMENT_README.md` | How to use (3 min) |
| `AGENT_TUTORIAL.md` | Learn by doing (10 min) |
| `AI_SYSTEM_ACTIVATION_GUIDE.md` | Add API key |
| `agent-dashboard.html` | Visual interface |
| `logs/agent-management/status-*.md` | Daily reports |

---

## 🆘 Common Issues

| Problem | Solution |
|---------|----------|
| Health is 60/100 | Normal before API key - add key |
| Workers not initialized | Add ANTHROPIC_API_KEY to GitHub Secrets |
| Don't understand recommendation | Create GitHub Issue asking for help |
| Command not working | Check you're in Avalon directory (`pwd`) |
| Python not found | Install Python from python.org |

---

## ✅ Quick Verification

Your closed PRs all worked:
- PR #110: ✅ Automation files created
- PR #109: ✅ AI workers created
- PR #72: ✅ Repository organized
- PR #50: ✅ Docs synced
- PR #48: ✅ Guides added

See: `CLOSED_SESSIONS_VERIFICATION.md` for details

---

## 🎯 Activation Checklist

- [ ] Read AGENT_START_HERE.md
- [ ] Run health check to see current status
- [ ] Get API key from https://console.anthropic.com
- [ ] Add to GitHub: Settings → Secrets → ANTHROPIC_API_KEY
- [ ] Trigger workflows in Actions tab
- [ ] Check health score (should jump to 80-100)
- [ ] Review PRs as workers create them
- [ ] Merge approved work

---

## 📱 Quick Help

**Question?** → Check `AGENT_MANAGEMENT_README.md`  
**Learning?** → Read `AGENT_TUTORIAL.md`  
**Activating?** → Follow `AI_SYSTEM_ACTIVATION_GUIDE.md`  
**Stuck?** → Create GitHub Issue with latest report

---

## 💡 The Simplest Explanation

**You have 5 AI workers that develop your game automatically.**

**Agent Manager watches them and tells you if anything needs attention.**

**You just check health daily (30 sec) and review their work weekly (5 min).**

**That's it!**

---

**Print this card or bookmark this file!** 📌

---

*Last Updated: November 25, 2025*
