# 🚀 Auto-Merge Quick Reference

## Commands

### Trigger Auto-Review
Comment on PR: `/auto-review`

### Disable Auto-Merge
Add label: `no-auto-merge`

### Force Manual Review
Add label: `manual-review-required`

### Manual Workflow Trigger
```bash
gh workflow run "🤖 Autonomous PR Review, Fix & Merge" -f pr_number=123
```

---

## Labels

| Label | Effect |
|-------|--------|
| `no-auto-merge` | Completely disables auto-merge |
| `manual-review-required` | Requires human approval before merge |
| `wip` or `work-in-progress` | Prevents merge while work is ongoing |
| `override-auto-merge` | Forces merge of flagged PR (use cautiously) |

---

## Risk Levels

### 🟢 Low Risk
- Docs, READMEs, lore
- **Auto-merges:** Immediately after passing checks

### 🟡 Medium Risk  
- Game scenes, content files
- **Auto-merges:** After 1 approval + passing checks

### 🔴 High Risk
- Workflows, scripts, dependencies
- **Requires:** Manual review (never auto-merges)

---

## Emergency Controls

### Stop All Auto-Merges
```bash
gh workflow disable "🤖 Autonomous PR Review, Fix & Merge"
```

### Rollback Bad Merge
```bash
git tag -l "auto-merge-*"  # Find tag
git reset --hard auto-merge-XXX-TIMESTAMP
git push origin main --force  # Use with caution!
```

---

## Common Issues

### PR Not Merging?
1. Check for blocking labels
2. Verify status checks pass
3. Check if high-risk (needs manual review)
4. Ensure no merge conflicts

### Auto-Fix Not Working?
1. Issue may need manual fix
2. Check workflow logs
3. Fix locally and push

### Need Help?
See full docs: `docs/AUTO_MERGE_SYSTEM.md`

---

## Workflow Status

Check: `gh run list --workflow="🤖 Autonomous PR Review, Fix & Merge"`

View run: `gh run view <run-id>`

---

**Quick Tip:** Most PRs (especially docs/lore) will auto-merge within 5-10 minutes if all checks pass!
