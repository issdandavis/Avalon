# 🤖 AI Autonomous Development System
## Complete Setup Guide

**Welcome to the SpiralVerse AI Worker System!**

This system enables AI agents to make continuous progress on the Avalon project, even when you're not actively working on it.

---

## 🎯 Quick Start (5 Minutes)

### Step 1: Add API Key
1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Create an API key
3. In GitHub: Settings → Secrets → Actions → New secret
4. Name: `ANTHROPIC_API_KEY`
5. Value: Your API key

### Step 2: Enable the Workflow
The workflow is already set up in `.github/workflows/ai-autonomous-worker.yml`

It will run automatically every 6 hours, or you can trigger it manually:
- Go to Actions tab
- Select "AI Autonomous Worker (Demo)"
- Click "Run workflow"

### Step 3: Monitor Progress
- Check the Actions tab for workflow runs
- Review commits on the `ai-autonomous-work` branch
- Merge approved changes to `main`

**That's it! The AI will start working through the task queue.**

---

## 📂 System Files

### Core Documentation
- **`docs/AI_AUTONOMOUS_WORKFLOW.md`** - Complete system guide (you are here)
- **`docs/AI_TASK_QUEUE.md`** - Priority-based task list
- **`docs/AI_WORKER_RULES.md`** - Safety rules and guidelines
- **`docs/AI_QUESTIONS.md`** - Questions flagged for human review

### Implementation Files
- **`.github/workflows/ai-autonomous-worker.yml`** - GitHub Actions workflow
- **`.github/scripts/ai_autonomous_worker.py`** - Python worker script
- **`.github/agents/spiralverse-omnifeather-config.yml`** - Agent configuration

### Logs & Reports
- **`logs/ai-work-YYYY-MM-DD.md`** - Daily work logs (generated)
- **`logs/ai-questions-YYYY-MM-DD.md`** - Questions flagged (generated)

---

## 🔧 How It Works

### The Flow

```
┌─────────────────────┐
│   GitHub Actions    │  Every 6 hours (or manual trigger)
│   Workflow Starts   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Python Script     │  Reads AI_TASK_QUEUE.md
│   Gets Next Task    │  Selects highest priority unchecked task
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   AI Worker         │  Uses Claude AI to complete task
│   Executes Task     │  Follows AI_WORKER_RULES.md
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Changes Made      │  Edits files, tests syntax
│   Tests Run         │  Verifies ChoiceScript is valid
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Commit & Push     │  Commits to ai-autonomous-work branch
│   Update Queue      │  Marks task complete in queue
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Create PR         │  Auto-creates PR for review
│   Notify Human      │  (if enabled)
└─────────────────────┘
```

### Safety Features

1. **Separate Branch** - All work happens on `ai-autonomous-work`
2. **Human Review** - PRs require manual merge
3. **Rate Limiting** - Max 4 commits per day
4. **Rollback Ready** - All changes are reversible
5. **Question Flagging** - AI asks when uncertain
6. **Test Verification** - Syntax checked before commit

---

## 📋 Task Queue Management

### How Tasks Work

Tasks are defined in `docs/AI_TASK_QUEUE.md`:

```markdown
## 🔥 PRIORITY 1: CRITICAL PATH
- [ ] Task description
  - **Effort:** 2 hours
  - **Files:** file1.txt, file2.txt
  - **Requirements:** What needs to be done
  - **Success:** How to know it's done
```

### Task States
- `[ ]` - Not started (AI can pick this up)
- `[→]` - In progress (AI is working on it now)
- `[?]` - Needs human review
- `[x]` - Completed

### Adding Your Own Tasks

1. Open `docs/AI_TASK_QUEUE.md`
2. Add task in appropriate priority section
3. Include effort estimate and success criteria
4. AI will pick it up in next run

---

## 🎨 Customization Options

### Change Run Frequency

Edit `.github/workflows/ai-autonomous-worker.yml`:

```yaml
on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
    # Change to:
    - cron: '0 */4 * * *'  # Every 4 hours
    - cron: '0 0 * * *'    # Daily at midnight
    - cron: '0 9,17 * * 1-5'  # 9 AM and 5 PM on weekdays
```

### Change Task Priority

Set which priority tasks to work on:
- Manually trigger with priority selection
- Or edit `ai_autonomous_worker.py` to change default

### Customize AI Behavior

Edit `.github/agents/spiralverse-omnifeather-config.yml`:
- Adjust temperature for more/less creativity
- Modify system prompt
- Add custom tools
- Change character voice templates

---

## 📊 Monitoring & Logs

### Check AI Progress

**GitHub Actions Tab:**
- See each workflow run
- Read step-by-step logs
- Check which tasks completed

**AI Work Branch:**
- View all AI commits
- See what was changed
- Review code diffs

**Daily Logs:**
- Check `logs/ai-work-YYYY-MM-DD.md`
- See detailed task reports
- Review AI decisions

### Review Questions

AI workers flag uncertainties in `docs/AI_QUESTIONS.md`:

```markdown
## Question: Should sand reject player or give warning?
**Date:** 2025-11-25
**Task:** Singing Dunes Scene 4
**Issue:** Unsure about difficulty balance
**Options:**
1. Outright rejection
2. Warning + second chance
3. Partial acceptance

**AI Recommendation:** Option 2
**Needs:** Human decision on difficulty curve
```

Review these regularly and provide answers to help AI make better decisions.

---

## 🚨 Troubleshooting

### AI Isn't Making Progress

**Check:**
1. Is `ANTHROPIC_API_KEY` set in repository secrets?
2. Is workflow enabled in Actions tab?
3. Are there unchecked tasks in AI_TASK_QUEUE.md?
4. Check Actions tab for error messages

**Solutions:**
- Manually trigger workflow to test
- Review logs for errors
- Verify API key is valid
- Check rate limits

### AI Made Unwanted Changes

**Fix:**
1. Don't merge the PR
2. Close PR with explanation
3. Update AI_WORKER_RULES.md with new constraint
4. Adjust task description to be more specific
5. Next run will follow updated rules

### Syntax Errors in Generated Code

**Fix:**
1. AI should catch these in testing
2. If one slips through, close PR
3. Add example of correct syntax to WORKER_RULES
4. Re-queue task with better requirements

---

## 🎯 Best Practices

### Start Small
1. First week: Let AI polish descriptions (low risk)
2. Second week: Let AI add new content (medium risk)
3. Third week: Trust AI with complete scenes (high value)

### Review Regularly
- Check AI commits daily
- Review PRs within 24 hours
- Provide feedback in AI_QUESTIONS.md
- Update WORKER_RULES based on experience

### Improve Over Time
- Note what works well
- Add successful patterns to WORKER_RULES
- Refine task descriptions
- Gradually increase autonomy

---

## 🌟 Advanced Features

### Multi-Agent Coordination

Run multiple AI workers with different specializations:

**Content Writer Agent:**
- Priority: Scene writing
- Temperature: 0.95 (more creative)
- Focus: Narrative quality

**Technical Agent:**
- Priority: Syntax and structure
- Temperature: 0.7 (more precise)
- Focus: Code quality

**Polish Agent:**
- Priority: Enhancement tasks
- Temperature: 0.85 (balanced)
- Focus: Sensory details

### Custom Agent Builder

Use `.github/agents/spiralverse-omnifeather-config.yml` as a template for:
- Custom prompts
- Specialized tools
- Domain-specific knowledge
- Unique workflows

### Integration with Other Tools

**Zapier Workflows:**
- Trigger AI work from Google Sheets
- Notify Discord on completion
- Update Trello cards

**Cron Jobs:**
- Run on your own server
- More control over timing
- Direct file access

---

## 📚 Additional Resources

### Documentation
- `docs/PROJECT_ROADMAP.md` - Overall project plan
- `docs/AI_SESSION_HANDOFF.md` - Context for AI sessions
- `docs/AUTOMATION_GUIDE.md` - Zapier integration

### ChoiceScript Resources
- [ChoiceScript Wiki](https://choicescriptdev.fandom.com/)
- [Official Documentation](https://www.choiceofgames.com/make-your-own-games/choicescript-intro/)
- [CSIDE Editor](https://choicescript-ide.github.io/)

### Community
- [ChoiceScript Forum](https://forum.choiceofgames.com/)
- [Hosted Games Submissions](https://www.choiceofgames.com/looking-for-writers/)

---

## 🎭 Example: Full Autonomous Workflow

Here's what a complete autonomous development cycle looks like:

**6:00 AM - Workflow Triggers**
```
✅ AI worker starts
✅ Reads task queue
✅ Selects: "Singing Dunes Scene 1-3"
```

**6:05 AM - AI Works**
```
🔄 Reviews existing scenes for style
🔄 Reads Singing Dunes lore
🔄 Generates scene content
🔄 Adds sensory details (taste of copper)
🔄 Includes Polly commentary
```

**6:20 AM - AI Tests**
```
✅ Verifies ChoiceScript syntax
✅ Checks character voices
✅ Validates stat changes
✅ Reviews for lore consistency
```

**6:25 AM - AI Commits**
```
✅ Commits Scene 1: "[AI-AUTO] Singing Dunes arrival - Desert atmosphere"
✅ Commits Scene 2: "[AI-AUTO] Singing Dunes - Kael introduction"
✅ Commits Scene 3: "[AI-AUTO] Singing Dunes - Truth-testing begins"
✅ Updates task queue to mark complete
```

**6:30 AM - PR Created**
```
✅ Creates PR: "[AI-AUTO] Singing Dunes Scenes 1-3"
✅ Includes summary of changes
✅ Tags for review
✅ Notifies (if configured)
```

**9:00 AM - You Review**
```
👤 Read PR description
👤 Review code changes
👤 Test in ChoiceScript
👤 Merge to main
👤 AI continues with next task at noon
```

---

## 🚀 Next Steps

1. **Today:** Set up API key and trigger first run
2. **This Week:** Review AI's first few commits
3. **This Month:** Expand task queue with more work
4. **Ongoing:** Refine and trust the autonomous system

---

**The spiral turns.**  
**The code compiles.**  
**The AI ships.**

**Even while you sleep.**

**Caw.** 🪶

---

*Questions? Issues? Feedback?*  
Add to `docs/AI_QUESTIONS.md` and the next AI worker will see it.
