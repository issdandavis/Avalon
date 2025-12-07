# Auto-Merge System Quick Start

## 🚀 Getting Started

### Activation
The auto-merge system is **already active** on this repository! It will automatically:
1. Review every new or updated PR
2. Fix common issues automatically
3. Merge safe changes without manual intervention

### First-Time Setup
No setup needed! The system works automatically.

## 📝 How to Use

### As a PR Author

#### Normal Workflow
1. **Create your PR** as you normally would
2. **Wait ~2-5 minutes** for the auto-review bot to comment
3. **Read the review feedback** in the PR comments
4. If issues are found, they may be **auto-fixed** and committed
5. If all checks pass, your PR will **auto-merge**!

#### Prevent Auto-Merge
If you want manual review, add a label:
```bash
# Using GitHub CLI
gh pr edit YOUR_PR_NUMBER --add-label "no-auto-merge"

# Or add manually via GitHub web UI
```

#### Example PR Flow
```
You: Create PR #123
↓
Bot: [2 min] Posts auto-review results
Bot: "✅ Approved - Medium Risk - Can Auto-Merge"
↓
Bot: [30 sec] Waits for CI checks
↓
Bot: [Auto-merge] "✅ Merged using squash strategy"
↓
Bot: Deletes your branch
```

### As a Reviewer/Maintainer

#### Monitor Auto-Merges
1. Check the **Actions** tab to see workflow runs
2. Review **job summaries** for detailed reports
3. Check **PR comments** for review details

#### Override Auto-Merge
To prevent auto-merge on any PR:
```bash
# Add the no-auto-merge label
gh pr edit PR_NUMBER --add-label "no-auto-merge"

# The bot will skip that PR
```

#### Disable Globally
If you need to disable the entire system:
1. Go to **Settings → Actions → Workflows**
2. Find "Auto-Review, Fix & Merge PRs"
3. Click **"..." → Disable workflow**

## 🎯 What Gets Auto-Merged

### ✅ Auto-Merge Eligible (Low Risk)
- Documentation files (`.md`)
- Configuration files (non-critical)
- Asset files (images, JSON data)
- Text content files

### ⚠️ Auto-Merge After Review (Medium Risk)
- Game scene files (`choicescript_game/scenes/*.txt`)
- Game content (`game/scenes/*.txt`)
- Python helper scripts
- CSS/JavaScript files

### 🚫 Manual Review Required (High Risk)
- Workflow files (`.github/workflows/*.yml`)
- Core scripts (`.github/scripts/*.py`)
- Startup file (`choicescript_game/startup.txt`)
- Critical configuration files

## 🔧 Common Scenarios

### "My PR was auto-merged"
✅ **Great!** The system determined your changes were safe.
- Check the PR comments for review details
- Changes are on the main branch now

### "My PR wasn't auto-merged"
The bot will comment explaining why:
- **High Risk Changes** → Needs manual review
- **CI Failed** → Fix tests and push again
- **Merge Conflicts** → Bot tried to fix, may need manual help
- **Has 'no-auto-merge' label** → Remove label to enable auto-merge

### "Auto-fix changed my code"
The bot will:
- **Comment what it fixed**
- **Commit the changes** to your PR branch
- **Request your review** if significant changes

Common auto-fixes:
- Unclosed quotes in ChoiceScript
- Label name formatting
- Merge conflict resolution
- Syntax errors

### "I want to disable auto-merge for one PR"
```bash
gh pr edit YOUR_PR_NUMBER --add-label "no-auto-merge"
```

## 📊 Reading Auto-Review Results

### Review Comment Format
```markdown
## 🤖 Auto-Review Results

Risk Level: MEDIUM

### ❌ Errors
- filename.txt:42 - Unclosed quote

### ⚠️ Warnings  
- script.py - Uses eval() which can be unsafe

### 💡 Suggestions
- Add shebang line to Python script

✅ APPROVED (or ❌ CHANGES REQUESTED)
🤖 AUTO-MERGE ELIGIBLE (or 👤 MANUAL REVIEW REQUIRED)
```

### Understanding Risk Levels

**LOW** = Docs, config, assets → Auto-merge immediately  
**MEDIUM** = Game content, scenes → Auto-merge after validation  
**HIGH** = Workflows, core code → Manual review required

## 🐛 Troubleshooting

### "Auto-review didn't run"
**Check:**
1. Workflow is enabled (Settings → Actions)
2. PR has commits (not draft)
3. GitHub Actions is working (check status.github.com)

**Fix:**
- Re-run the workflow manually from Actions tab
- Close and reopen the PR
- Push a new commit

### "Auto-fix made it worse"
1. **Review the auto-fix commit** in your PR
2. **Revert if needed:**
   ```bash
   git revert COMMIT_HASH
   git push
   ```
3. **Add 'no-auto-merge' label** to prevent future auto-fixes
4. **Report the issue** so we can improve the fixer

### "CI is stuck"
The auto-merge waits max 5 minutes for CI.
- If CI is still running after 5 min, it will skip auto-merge
- Fix any failing CI checks
- Re-run the workflow

## 📚 More Information

- **Full Documentation:** [docs/AUTO_MERGE_SYSTEM.md](AUTO_MERGE_SYSTEM.md)
- **Workflow Code:** [.github/workflows/auto-review-fix-merge.yml](../.github/workflows/auto-review-fix-merge.yml)
- **Review Script:** [.github/scripts/auto_reviewer.py](../.github/scripts/auto_reviewer.py)

## 🆘 Getting Help

1. **Check the docs** above
2. **Review workflow logs** in Actions tab
3. **Check PR comments** for bot feedback
4. **Create an issue** with:
   - PR number
   - What you expected
   - What actually happened
   - Link to workflow run

## ✨ Tips for Best Results

### For Authors
- ✅ **Keep PRs small** - Single purpose per PR
- ✅ **Test locally first** - Run syntax checks before pushing  
- ✅ **Clear titles** - Describe what you changed
- ✅ **Watch CI** - Make sure tests pass

### For Reviewers  
- ✅ **Trust the bot** for low/medium risk PRs
- ✅ **Review high-risk PRs** manually
- ✅ **Check auto-merge results** periodically
- ✅ **Report issues** to improve the system

---

**Questions?** Check [docs/AUTO_MERGE_SYSTEM.md](AUTO_MERGE_SYSTEM.md) for detailed information.
