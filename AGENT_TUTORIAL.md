# 🎓 Agent Management Tutorial for GitHub Beginners

**Time:** 10 minutes  
**Prerequisites:** None - this is for total beginners!  
**Goal:** Understand and use your AI team

---

## Part 1: What You Have (2 minutes)

### The Team

Imagine you hired 5 employees to work on your game:

1. **Sarah (Scene Writer)** - Writes story content every 3 hours
2. **Emma (Content Polisher)** - Makes scenes more immersive every 4 hours  
3. **Bob (Stat Balancer)** - Balances game difficulty daily
4. **Tina (Game Tester)** - Finds bugs daily
5. **Alex (General Worker)** - Does misc tasks every 6 hours

Plus one supervisor:

6. **Morgan (Agent Manager)** - Watches everyone and reports to you twice daily

### The Catch

They're all AI! They work for free, never sleep, and follow your instructions perfectly.

But they need you to:
- Give them an API key (like a security badge to work)
- Tell them what to do (via task list)
- Review and approve their work (via pull requests)

---

## Part 2: Checking the System (3 minutes)

### Step 1: Open Your Terminal

**Windows:** Press Windows key, type "cmd", press Enter  
**Mac:** Press Cmd+Space, type "terminal", press Enter  
**Linux:** You know what to do 😉

### Step 2: Navigate to Repository

```bash
cd /path/to/Avalon
```

(Replace with your actual path)

### Step 3: Check System Health

```bash
python .github/scripts/agent_manager_cli.py health
```

You'll see something like:

```
==================================================
  SYSTEM HEALTH: 60/100
  STATUS: ⚠️ WARNING
==================================================
```

**What this means:**
- 60/100 = System works but needs setup
- ⚠️ WARNING = Not critical, but needs attention

### Step 4: See What Needs Fixing

```bash
python .github/scripts/agent_manager_cli.py recommend
```

You'll see:

```
💡 RECOMMENDATIONS

1. 🔴 CRITICAL: Add ANTHROPIC_API_KEY to repository secrets to activate workers
2. Initialize scene-writer by running its workflow manually
3. Initialize content-polisher by running its workflow manually
...
```

**What this means:**
The system is telling you exactly what to do! Just follow the recommendations in order.

---

## Part 3: Understanding the Status (2 minutes)

### What's a Health Score?

Think of it like a car dashboard:
- **80-100** = Green light ✅ (everything's fine)
- **50-79** = Yellow light ⚠️ (check soon)
- **0-49** = Red light 🔴 (fix now!)

### What Are Worker Branches?

Each AI worker has their own "workspace" (branch) where they work:
- `ai-scene-development` - Sarah's workspace
- `ai-content-polish` - Emma's workspace
- `ai-stat-balance` - Bob's workspace
- `ai-autonomous-work` - Alex's workspace

They work independently, then ask you to approve their work via Pull Requests.

### What's a Pull Request?

When a worker finishes something, they create a "Pull Request" (PR) = "Hey boss, I finished this work, can I add it to the main project?"

You review it and click "Merge" if it's good, or ask for changes if it's not.

---

## Part 4: Using the Visual Dashboard (3 minutes)

Don't like command line? Use the pretty dashboard!

### Step 1: Generate a Report

```bash
python .github/scripts/agent_orchestrator.py
```

This creates two files:
- `logs/agent-management/status-2025-11-25.json` (for computer)
- `logs/agent-management/status-2025-11-25.md` (for humans)

### Step 2: Open the Dashboard

Find and double-click: `agent-dashboard.html`

It opens in your web browser.

### Step 3: Load the Report

Click the "Choose File" button and select:
`logs/agent-management/status-2025-11-25.json`

### Step 4: See Pretty Colors!

You'll see:
- Big health score with color (green/yellow/red)
- Cards for each worker showing their status
- Progress bars for tasks and scenes
- List of what to do next

---

## Part 5: Daily Routine (30 seconds/day)

Once the system is activated (API key added), here's your daily routine:

### Morning (30 seconds)

```bash
# Navigate to repo
cd /path/to/Avalon

# Check health
python .github/scripts/agent_manager_cli.py health
```

**If health is 80+:** ✅ Done! AI is working fine.

**If health is <80:**
```bash
# See what needs fixing
python .github/scripts/agent_manager_cli.py recommend
```

Follow the recommendations (they tell you exactly what to do).

### Weekly (5 minutes)

1. Go to GitHub → Actions tab
2. Check if workflows are running
3. Go to Pull Requests tab
4. Review PRs created by workers
5. Merge the good ones

That's it!

---

## Part 6: Common Scenarios (Practice!)

### Scenario: First Day After Activation

**You see:**
```
SYSTEM HEALTH: 85/100
STATUS: ✅ HEALTHY
```

**What to do:** Nothing! The AI is working. Check again tomorrow.

---

### Scenario: Worker Created a PR

**You see:** Email notification "Pull request #111 opened by Copilot"

**What to do:**
1. Go to GitHub repository
2. Click "Pull requests" tab
3. Click the new PR
4. Read what changed
5. If good → click "Merge pull request"
6. If bad → click "Close pull request" and add comment explaining why

---

### Scenario: Health Score Dropped

**You see:**
```
SYSTEM HEALTH: 45/100
STATUS: 🔴 CRITICAL
```

**What to do:**
```bash
python .github/scripts/agent_manager_cli.py recommend
```

Follow each recommendation. Health will increase as you fix issues.

---

### Scenario: Don't Understand a Recommendation

**Recommendation says:** "Resolve merge conflicts in: ai-scene-development"

**You think:** "What's a merge conflict??"

**What to do:**
1. Copy the recommendation text
2. Create GitHub Issue
3. Paste the recommendation
4. Add: "I don't know how to do this, please help"
5. Tag with "help wanted"
6. Wait for assistance

Don't be afraid to ask for help!

---

## Part 7: Troubleshooting (Reference)

### "Python command not found"

**Fix:** Install Python from python.org

### "File not found"

**Fix:** Make sure you're in the Avalon directory:
```bash
pwd  # Shows current directory
ls   # Shows files (should see README.md, game/, etc.)
```

### "Permission denied"

**Fix:**
```bash
chmod +x .github/scripts/agent_manager_cli.py
```

### "Nothing is happening"

**Fix:** Workers need the API key to run. See `AI_SYSTEM_ACTIVATION_GUIDE.md` for how to add it.

---

## Part 8: Where to Get Help

### Built-in Help

```bash
# Show available commands
python .github/scripts/agent_manager_cli.py

# Full documentation
cat AGENT_MANAGEMENT_README.md
```

### Documentation Roadmap

**Start here:** `AGENT_MANAGEMENT_README.md` (3 min read)  
**Next:** `AI_SYSTEM_ACTIVATION_GUIDE.md` (10 min, includes setup)  
**Deep dive:** `docs/AGENT_MANAGEMENT_GUIDE.md` (full details)

### Visual Aids

**Dashboard:** `agent-dashboard.html` (colorful interface)  
**Reports:** `logs/agent-management/*.md` (daily summaries)

### Getting Stuck?

1. Read latest report: `logs/agent-management/status-*.md`
2. Check recommendations section
3. Google the error message
4. Create GitHub Issue with "help wanted" tag
5. Ask in GitHub Discussions

---

## Part 9: Understanding Git/GitHub Basics

### Terms You'll See

| Term | Simple Explanation | Example |
|------|-------------------|---------|
| **Branch** | Separate workspace | `ai-scene-development` |
| **Commit** | Saved change | "Added 347 lines to scene" |
| **Pull Request (PR)** | Request to merge work | "Please add my changes" |
| **Merge** | Combine work into main | Approving worker's PR |
| **Conflict** | Two changes clash | Two workers edited same line |
| **Repository** | Your project folder | This Avalon project |
| **Actions** | Automated workflows | Your AI workers |

### You Don't Need to Know Git!

The Agent Manager handles git for you. You just:
- Run commands it tells you
- Click "Merge" on good PRs
- Ask for help when confused

---

## Part 10: Next Steps

### Right Now
1. ✅ You understand the system
2. ✅ You know how to check status
3. ✅ You can read recommendations

### Next
1. 📖 Read `AI_SYSTEM_ACTIVATION_GUIDE.md`
2. 🔑 Add ANTHROPIC_API_KEY (takes 2 minutes)
3. ▶️ Trigger first worker runs
4. 👀 Watch the magic happen!

### After Activation
1. Check health daily (30 seconds)
2. Review PRs weekly (5 minutes)
3. Adjust task priorities as needed
4. Watch your game develop automatically!

---

## Cheat Sheet

```bash
# Daily check (30 sec)
python .github/scripts/agent_manager_cli.py health

# What to do next?
python .github/scripts/agent_manager_cli.py recommend

# Full status
python .github/scripts/agent_orchestrator.py

# Just tasks
python .github/scripts/agent_manager_cli.py tasks

# Just workers
python .github/scripts/agent_manager_cli.py workers
```

---

## Summary

You have:
- ✅ 5 AI workers ready to develop your game
- ✅ 1 supervisor monitoring everything
- ✅ Simple commands to check status
- ✅ Visual dashboard for pretty viewing
- ✅ Clear recommendations for what to do
- ✅ This tutorial to guide you

You need to:
- 🔑 Add API key (one time, 2 minutes)
- ✅ Check health daily (30 seconds)
- 📝 Review PRs weekly (5 minutes)

**Then your game develops automatically while you sleep!**

---

## Questions?

- **"What's a terminal?"** → The command-line interface (type commands)
- **"What's Python?"** → Programming language (already installed on most computers)
- **"What's an API key?"** → Security credential (get from Anthropic)
- **"What if I break something?"** → Git saves everything, can always undo
- **"Is this safe?"** → Yes! Workers never modify main branch directly

---

**Ready to activate your AI team?**

→ Next: [AI_SYSTEM_ACTIVATION_GUIDE.md](AI_SYSTEM_ACTIVATION_GUIDE.md)

---

*You got this! 🚀*
