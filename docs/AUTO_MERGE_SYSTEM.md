# 🤖 Autonomous PR Management System

## Overview

The Avalon Codex repository features a fully autonomous PR management system that automatically:
- **Reviews** every pull request within minutes of creation
- **Fixes** common issues (merge conflicts, syntax errors, formatting)
- **Merges** PRs when safe to do so based on intelligent risk assessment

This system is designed to handle the 30+ open PRs efficiently while maintaining code quality and safety.

---

## 🎯 How It Works

### When a PR is Created or Updated

#### Step 1: Auto-Review (5 minutes)
The system automatically:
- ✅ Validates ChoiceScript syntax
- ✅ Checks for merge conflicts
- ✅ Scans for security issues
- ✅ Assesses code quality
- ✅ Posts detailed review comments
- ✅ Assigns a risk level (low/medium/high)

#### Step 2: Auto-Fix (if needed)
If issues are found, the system:
- 🔧 Resolves merge conflicts using intelligent strategies
- 🔧 Fixes ChoiceScript syntax errors
- 🔧 Updates formatting
- 🔧 Rebases branch with main
- 🔧 Pushes fixes back to PR
- 🔧 Comments on what was fixed

#### Step 3: Auto-Merge (when safe)
When all criteria are met:
- ✅ Merges using appropriate strategy (squash/merge)
- ✅ Deletes merged branch
- ✅ Creates rollback tag for safety
- ✅ Posts confirmation comment

---

## 🛡️ Safety Features

### Risk-Based Decision Making

The system classifies PRs into three risk levels:

#### 🟢 Low Risk - Auto-Merge Immediately
- Documentation changes (`*.md`, `docs/`)
- Lore updates (`lore/`)
- README updates
- Configuration files (non-workflow)

**Requirements:**
- No merge conflicts
- No syntax errors
- All status checks pass

#### 🟡 Medium Risk - Auto-Merge After AI Review
- Game content (`choicescript_game/scenes/`, `game/`)
- HTML/JavaScript changes
- Scene files

**Requirements:**
- No merge conflicts
- No syntax errors
- All status checks pass
- At least 1 approval (or auto-approved by AI)

#### 🔴 High Risk - Flag for Manual Review
- Workflow files (`.github/workflows/`)
- Scripts (`.github/scripts/`)
- Package dependencies (`package.json`, `requirements.txt`)
- Build configurations

**Requirements:**
- **ALWAYS requires manual review**
- System will add `manual-review-required` label
- Will not auto-merge

### Emergency Controls

#### Disable Auto-Merge for Specific PR
Add one of these labels to any PR:
- `no-auto-merge` - Completely disables auto-merge
- `manual-review-required` - Requires human approval
- `wip` or `work-in-progress` - Prevents merge while work is ongoing

#### Emergency Stop All Auto-Merges
Temporarily disable the workflow:
```bash
gh workflow disable "🤖 Autonomous PR Review, Fix & Merge" --repo issdandavis/Aethromoor
```

Re-enable when ready:
```bash
gh workflow enable "🤖 Autonomous PR Review, Fix & Merge" --repo issdandavis/Aethromoor
```

#### Rollback a Bad Merge
Each auto-merge creates a rollback tag:

```bash
# List recent auto-merge tags
git tag -l "auto-merge-*"

# Rollback to specific merge point
git reset --hard auto-merge-123-1701234567

# Force push (use with caution)
git push origin main --force
```

### What Gets Flagged for Manual Review
- Breaking changes detected
- Security vulnerabilities found
- Repeated CI failures after auto-fix
- Complex merge conflicts AI can't resolve
- More than 50 files changed
- Changes to critical infrastructure files

---

## 📋 Workflow Files

### Main Workflow
- **File:** `.github/workflows/auto-review-fix-merge.yml`
- **Triggers:** 
  - New PR opened
  - PR updated
  - Comment `/auto-review` on PR
  - Manual workflow dispatch
- **Jobs:**
  1. `auto-review` - Reviews PR and assigns risk level
  2. `auto-fix` - Fixes issues if found
  3. `auto-merge` - Merges if safe
  4. `flag-for-manual` - Flags high-risk PRs

### Scripts

#### Auto-Reviewer (`auto_reviewer.py`)
- Validates ChoiceScript syntax using existing validator
- Checks merge conflicts
- Scans for hardcoded secrets/credentials
- Assesses risk level based on changed files
- Generates detailed review report

#### Auto-Fixer (`auto_fixer.py`)
- Resolves merge conflicts intelligently
- Fixes ChoiceScript syntax errors:
  - Labels with spaces → underscores
  - Unclosed quotes → auto-close
  - Missing *set values → add default
- Removes trailing whitespace
- Updates branch with main

#### Auto-Merger (`auto_merger.py`)
- Evaluates merge safety based on:
  - Risk level
  - Status checks
  - Approvals
  - Labels
  - Changed files count
- Determines merge strategy (squash vs merge)
- Creates rollback points

---

## 🚀 Usage

### For Repository Maintainers

The system runs automatically - no action needed! However, you can:

#### Manually Trigger Review
Comment on any PR:
```
/auto-review
```

#### Manually Trigger Workflow
```bash
gh workflow run "🤖 Autonomous PR Review, Fix & Merge" \
  --repo issdandavis/Aethromoor \
  -f pr_number=123
```

#### Override Auto-Merge Decision
Add the `override-auto-merge` label to force merge a flagged PR (use cautiously).

### For Contributors

The auto-merge system helps you by:
1. **Instant Feedback** - Get review comments within 5 minutes
2. **Auto-Fix** - Common issues fixed automatically
3. **Faster Merges** - No waiting for manual review on low-risk changes

**Tips:**
- Keep PRs focused (under 50 files changed)
- Fix any issues the auto-reviewer flags
- Don't add `no-auto-merge` unless you want manual review

---

## 📊 Monitoring & Audit Trail

### View Review Reports
Each PR review generates artifacts:
- `review-report-pr-{number}` - Detailed review analysis
- `fix-report-pr-{number}` - List of fixes applied
- `merge-report-pr-{number}` - Merge decision rationale

Access in GitHub Actions → Workflow Run → Artifacts

### Check System Status
```bash
# View recent workflow runs
gh run list --workflow="🤖 Autonomous PR Review, Fix & Merge" --repo issdandavis/Aethromoor

# View specific run details
gh run view <run-id> --repo issdandavis/Aethromoor
```

### Full Audit Trail
Every automated action is logged:
- Review comments on PRs
- Commits made by auto-fixer
- Merge decisions with reasoning
- Rollback tags for safety

---

## 🔧 Troubleshooting

### PR Not Auto-Merging

**Check:**
1. Does it have `no-auto-merge` or `manual-review-required` label?
2. Are all status checks passing?
3. Are there merge conflicts?
4. Is it high-risk? (Check labels)
5. Does it need approvals? (Medium-risk needs 1 approval)

**Solution:**
- Review workflow run logs
- Check artifacts for detailed reports
- Address any blocking issues
- Remove blocking labels if appropriate

### Auto-Fix Didn't Fix My Issue

**Why:**
- Some issues require manual intervention
- Complex merge conflicts may be unfixable
- Breaking changes need human judgment

**Solution:**
- Fix issues locally
- Push to PR branch
- System will re-evaluate

### False Security Alert

**Why:**
- Simple pattern matching may flag false positives

**Solution:**
- Review the flagged code
- If false positive, add comment explaining why it's safe
- Consider refactoring to avoid pattern

---

## 🎯 First-Time Setup

The system is already configured! But if you need to modify:

### Required Secrets
None! The system uses `GITHUB_TOKEN` which is automatically provided.

### Required Permissions
The workflow has these permissions (already configured):
- `contents: write` - To push fixes
- `pull-requests: write` - To comment and merge
- `issues: write` - To add labels
- `checks: write` - To update status
- `statuses: write` - To set commit status

### Testing

Test on a sample PR:
```bash
# Create a test PR
git checkout -b test-auto-merge
echo "# Test" >> docs/TEST.md
git add docs/TEST.md
git commit -m "Test: auto-merge system"
git push origin test-auto-merge
gh pr create --title "Test: Auto-merge" --body "Testing autonomous PR system"

# Watch it work!
gh pr view --web
```

---

## 📈 Metrics & Performance

### Expected Performance
- **Review Time:** < 5 minutes per PR
- **Fix Time:** < 2 minutes for common issues
- **Merge Time:** < 1 minute after approval

### System Capacity
- Can handle 30+ PRs simultaneously
- Processes PRs in order of creation
- Prioritizes high-activity PRs

### Success Rates (Expected)
- **Auto-Review:** 100% of PRs
- **Auto-Fix:** ~70% of issues fixable
- **Auto-Merge:** ~60% of low-risk, ~30% of medium-risk

---

## 🤝 Contributing to the System

Want to improve the auto-merge system?

### Add New Fix Types
Edit `.github/scripts/auto_fixer.py`:
```python
def fix_my_new_issue():
    # Your fix logic
    pass
```

### Add New Review Checks
Edit `.github/scripts/auto_reviewer.py`:
```python
def check_my_new_requirement():
    # Your check logic
    pass
```

### Adjust Risk Levels
Edit risk assessment in `auto_reviewer.py`:
```python
high_risk_patterns = [
    r'your/pattern/here',
]
```

---

## 📞 Support

### Issues with Auto-Merge System
Open an issue with:
- PR number affected
- Workflow run link
- Expected vs actual behavior

### Questions
Check existing documentation:
- This file (AUTO_MERGE_SYSTEM.md)
- Workflow file comments
- Script docstrings

---

## 🔮 Future Enhancements

Planned improvements:
- [ ] AI-powered code review comments
- [ ] Automatic test generation
- [ ] Smart conflict resolution using GPT
- [ ] Performance regression detection
- [ ] Automated changelog generation
- [ ] Integration with project boards
- [ ] Slack/Discord notifications for important merges

---

## 📜 License & Credits

Part of The Avalon Codex project.

**Created by:** GitHub Copilot Autonomous Agent
**Maintained by:** issdandavis
**License:** Same as repository

---

**Last Updated:** 2024-12-07
**Version:** 1.0.0
**Status:** ✅ Active
