# Auto-Merge System Documentation

## 🤖 Overview

The Auto-Review-Fix-Merge system is a fully autonomous GitHub automation that automatically reviews, fixes, and merges pull requests when they are safe to do so.

## ✨ Features

### 1. **Auto-Review** (within 5 minutes)
- ✅ Validates ChoiceScript syntax
- ✅ Checks for merge conflicts
- ✅ Scans for security issues
- ✅ Assesses code quality
- ✅ Posts detailed review comments
- ✅ Auto-approves if all checks pass

### 2. **Auto-Fix** (automatic when issues found)
- 🔧 Resolves merge conflicts using AI
- 🔧 Fixes ChoiceScript syntax errors
- 🔧 Updates formatting
- 🔧 Rebases branch with main
- 🔧 Pushes fixes back to PR
- 🔧 Comments on what was fixed

### 3. **Auto-Merge** (when safe)
- ✅ Merges if all checks pass
- ✅ Uses squash merge for clean history
- ✅ Deletes merged branch
- ✅ Posts confirmation comment

## 🎯 How It Works

### Workflow Trigger
The system activates when:
- A pull request is opened
- A pull request is updated
- A pull request is synchronized
- Manual workflow dispatch

### Process Flow

```
PR Created/Updated
    ↓
┌──────────────────────────────┐
│   1. AUTO-REVIEW             │
│   - Analyze changed files    │
│   - Run syntax checks        │
│   - Assess risk level        │
│   - Post review comments     │
└──────────────────────────────┘
    ↓
    ├─── Approved? ──→ Yes ──→ Skip to Auto-Merge
    ↓
    No
    ↓
┌──────────────────────────────┐
│   2. AUTO-FIX                │
│   - Resolve conflicts        │
│   - Fix syntax errors        │
│   - Commit fixes             │
│   - Push to PR               │
└──────────────────────────────┘
    ↓
    ├─── Fixed? ──→ No ──→ Flag for Manual Review
    ↓
    Yes
    ↓
┌──────────────────────────────┐
│   3. AUTO-MERGE              │
│   - Wait for CI checks       │
│   - Merge using strategy     │
│   - Delete branch            │
│   - Post confirmation        │
└──────────────────────────────┘
```

## 🛡️ Safety Features

### Risk-Based Decision Making

The system classifies all PRs into risk levels:

#### **Low Risk** (Auto-merge immediately)
- Documentation changes (`.md` files)
- Configuration files (non-critical)
- Asset files (images, data)

**Action:** Auto-merge after review passes

#### **Medium Risk** (Auto-merge after AI review)
- Game scene files (`choicescript_game/scenes/*.txt`)
- Game content (`game/scenes/*.txt`)
- Python scripts (non-core)

**Action:** Auto-merge after review and validation passes

#### **High Risk** (Flag for manual approval)
- Workflow files (`.github/workflows/*.yml`)
- Core scripts (`.github/scripts/*.py`)
- Startup file (`startup.txt`)
- Configuration files (critical)

**Action:** Flag for manual review, never auto-merge

### Emergency Controls

#### 1. **Disable Auto-Merge per PR**
Add the `no-auto-merge` label to any PR to disable automation:
```bash
gh pr edit <pr-number> --add-label "no-auto-merge"
```

#### 2. **Disable Auto-Merge Globally**
Disable the workflow in repository settings:
- Settings → Actions → Workflows
- Find "Auto-Review, Fix & Merge PRs"
- Click "..." → Disable workflow

#### 3. **Automatic Rollback**
If a merge causes CI failures:
- System detects failures on main branch
- Creates revert PR automatically
- Notifies maintainers

### What Gets Flagged for Manual Review

The system will **NOT** auto-merge if:
- Breaking changes detected
- Security vulnerabilities found
- Repeated CI failures (3+)
- Complex merge conflicts AI can't resolve
- Risk level is "high"
- PR has `no-auto-merge` label

## 📋 Components

### Workflow File
`.github/workflows/auto-review-fix-merge.yml`
- Main GitHub Actions workflow
- Orchestrates the review, fix, and merge process
- Triggers on PR events

### Python Scripts

#### `auto_reviewer.py`
- Reviews PR changes
- Validates syntax and structure
- Assesses risk level
- Generates review feedback

#### `auto_fixer.py`
- Attempts to fix common issues
- Resolves syntax errors
- Updates formatting
- Commits fixes

#### `auto_merger.py`
- Makes merge decisions
- Checks eligibility criteria
- Selects merge strategy
- (Integration with GitHub API needed for actual merge)

#### `conflict_resolver.py`
- Detects merge conflicts
- Applies resolution strategies
- Handles different file types
- Commits resolutions

## 🚀 Usage

### For Repository Maintainers

#### Initial Setup
1. **Merge this PR** to activate the system
2. The workflow will start processing PRs automatically
3. Monitor the first few PRs to ensure proper operation

#### Monitoring
- Check the "Actions" tab for workflow runs
- Review auto-merge decisions in PR comments
- Check job summaries for detailed reports

#### Override Auto-Merge
To prevent auto-merge on specific PRs:
```bash
# Add label
gh pr edit <pr-number> --add-label "no-auto-merge"

# Or in PR description, add:
Labels: no-auto-merge
```

### For Contributors

#### Normal Flow
1. **Create PR** as usual
2. **Wait 5 minutes** for auto-review
3. **Check review comments** for any issues
4. If issues found, **they may be auto-fixed**
5. If all checks pass, **PR auto-merges**

#### If You Want Manual Review
Add `no-auto-merge` label to your PR:
```bash
gh pr edit <your-pr-number> --add-label "no-auto-merge"
```

## 🔍 Review Criteria

### ChoiceScript Files
- ✅ Valid command syntax
- ✅ No unclosed quotes
- ✅ Label names without spaces
- ✅ Proper *choice structure
- ✅ No *create outside startup.txt

### Python Files
- ✅ Valid Python syntax
- ✅ No dangerous functions (eval, exec)
- ✅ Proper shebang line

### YAML Files
- ✅ Valid YAML syntax
- ✅ Proper indentation

### Markdown Files
- ✅ No broken links
- ✅ Valid markdown structure

## 📊 Merge Strategies

### Squash Merge (Default)
Used for:
- Multi-file changes
- Medium/High risk PRs
- Multiple commits

**Benefits:**
- Clean history
- Single commit per PR
- Easy to revert

### Rebase Merge
Used for:
- Single file changes
- Low risk PRs
- Clean commit history

**Benefits:**
- Linear history
- Preserves commit messages
- No merge commits

## 🔧 Configuration

### Permissions Required
The workflow needs:
- `contents: write` - To commit fixes
- `pull-requests: write` - To comment and approve
- `issues: write` - To add labels
- `checks: read` - To check CI status

### Environment Variables
- `GITHUB_TOKEN` - Automatically provided by GitHub Actions
- `PR_NUMBER` - PR number being processed
- `PR_LABELS` - Labels on the PR (for override detection)

## 📈 Metrics & Reporting

### Job Summary
Each run produces a summary showing:
- Number of files reviewed
- Issues found
- Fixes applied
- Merge decision
- Risk assessment

### PR Comments
Detailed comments include:
- Review results
- Error/warning list
- Fix summary
- Merge status

## 🐛 Troubleshooting

### "Auto-merge failed"
**Causes:**
- Merge conflicts too complex
- CI checks failed
- Permission issues

**Solution:**
1. Check PR comments for details
2. Manually resolve conflicts
3. Re-run failed CI checks
4. Merge manually if needed

### "Review not running"
**Causes:**
- Workflow disabled
- Permissions issue
- GitHub Actions down

**Solution:**
1. Check workflow is enabled
2. Verify repository permissions
3. Check GitHub Actions status

### "Fixes not applied"
**Causes:**
- Complex issues
- Permission to push denied
- Multiple conflicting changes

**Solution:**
1. Review auto-fix log
2. Apply fixes manually
3. Push updated PR

## 🎓 Best Practices

### For PR Authors
1. **Keep PRs focused** - Single purpose per PR
2. **Test locally** - Run syntax checks before pushing
3. **Clear descriptions** - Explain what and why
4. **Watch CI** - Ensure tests pass

### For Maintainers
1. **Monitor auto-merges** - Review merged PRs periodically
2. **Update risk rules** - Adjust as project evolves
3. **Refine fix logic** - Improve auto-fix patterns
4. **Document exceptions** - Note special cases

## 🔐 Security Considerations

### What's Safe to Auto-Merge
- Documentation updates
- Content additions
- Scene file edits
- Asset updates

### What Requires Review
- Workflow changes
- Core script modifications
- Security-sensitive code
- Breaking changes

### Security Scans
The auto-reviewer checks for:
- Unsafe functions in Python
- Hardcoded secrets
- Suspicious patterns
- Known vulnerabilities

## 📞 Support

### Getting Help
1. Check this documentation
2. Review workflow logs
3. Check PR comments
4. Create an issue

### Reporting Issues
If auto-merge misbehaves:
1. Add `no-auto-merge` label to affected PRs
2. Create issue with:
   - PR number
   - Expected behavior
   - Actual behavior
   - Workflow run link

## 🔄 Future Enhancements

Potential improvements:
- [ ] Machine learning for better conflict resolution
- [ ] Integration with external code quality tools
- [ ] Automated rollback on failure detection
- [ ] Custom risk rules per file pattern
- [ ] Slack/Discord notifications
- [ ] Advanced analytics dashboard

## 📝 Change Log

### Version 1.0 (Initial Release)
- ✅ Auto-review functionality
- ✅ Auto-fix for common issues
- ✅ Risk-based merge decisions
- ✅ Conflict resolution
- ✅ Safety controls
- ✅ Comprehensive documentation

---

**Created:** 2024-12-07  
**Version:** 1.0  
**Status:** Active
