# 🧪 Auto-Merge System - Integration Test Plan

## Pre-Deployment Checklist

### 1. File Validation ✅
- [x] Workflow YAML syntax validated
- [x] Python scripts execute without errors
- [x] All scripts have executable permissions
- [x] Documentation is complete

### 2. Component Testing ✅
- [x] auto_reviewer.py imports and functions work
- [x] auto_fixer.py imports and functions work
- [x] auto_merger.py imports and functions work
- [x] ChoiceScript validation tested on real files

### 3. Workflow Structure ✅
- [x] Triggers configured correctly
- [x] Job dependencies set properly
- [x] Permissions granted appropriately
- [x] Environment variables defined

## Post-Deployment Testing

### Test Case 1: Low-Risk PR (Documentation)
**Objective**: Verify auto-merge works for docs changes

1. Create test branch: `test/docs-update`
2. Modify a markdown file in `docs/`
3. Create PR
4. Expected: Auto-review → Auto-merge (no fixes needed)
5. Timeline: < 10 minutes

### Test Case 2: Medium-Risk PR (Game Content)
**Objective**: Verify approval requirement for game content

1. Create test branch: `test/scene-update`
2. Modify a file in `choicescript_game/scenes/`
3. Create PR
4. Expected: Auto-review → Requires 1 approval → Auto-merge after approval
5. Timeline: < 15 minutes

### Test Case 3: High-Risk PR (Workflow)
**Objective**: Verify manual review flag for workflows

1. Create test branch: `test/workflow-change`
2. Modify a file in `.github/workflows/`
3. Create PR
4. Expected: Auto-review → Flag for manual review (no auto-merge)
5. Timeline: < 5 minutes

### Test Case 4: PR with Syntax Errors
**Objective**: Verify auto-fix functionality

1. Create test branch: `test/syntax-error`
2. Add ChoiceScript file with intentional errors (unclosed quote, label with spaces)
3. Create PR
4. Expected: Auto-review → Auto-fix → Commit fixes → Re-review
5. Timeline: < 15 minutes

### Test Case 5: PR with Merge Conflict
**Objective**: Verify conflict resolution

1. Create test branch: `test/merge-conflict`
2. Create conflicting changes with main
3. Create PR
4. Expected: Auto-review → Detect conflict → Auto-fix attempts resolution
5. Timeline: < 15 minutes

### Test Case 6: Emergency Controls
**Objective**: Verify label-based blocking

1. Create test PR (any type)
2. Add label `no-auto-merge`
3. Expected: Auto-review completes → Auto-merge skipped
4. Timeline: < 10 minutes

## Monitoring Dashboard

### Key Metrics to Track

1. **Review Time**: Time from PR creation to review completion
   - Target: < 5 minutes
   
2. **Fix Success Rate**: % of issues successfully auto-fixed
   - Target: > 70%
   
3. **Auto-Merge Rate**: % of PRs auto-merged (by risk level)
   - Low Risk: Target > 90%
   - Medium Risk: Target > 60%
   - High Risk: Target 0%

4. **False Positive Rate**: PRs incorrectly blocked from auto-merge
   - Target: < 5%

### GitHub Actions Monitoring

```bash
# View recent runs
gh run list --workflow="🤖 Autonomous PR Review, Fix & Merge" --limit 20

# View specific run
gh run view <run-id> --log

# Download artifacts
gh run download <run-id>
```

### Artifact Review

For each PR, check artifacts:
- `review-report-pr-{number}` - Review analysis
- `fix-report-pr-{number}` - Fixes applied
- `merge-report-pr-{number}` - Merge decision

## Rollback Procedure

If system behaves unexpectedly:

### 1. Immediate Stop
```bash
gh workflow disable "🤖 Autonomous PR Review, Fix & Merge" \
  --repo issdandavis/Aethromoor
```

### 2. Investigate
- Review recent workflow runs
- Check artifact reports
- Examine PR comments from bot

### 3. Rollback Bad Merge (if needed)
```bash
# Find rollback tag
git tag -l "auto-merge-*" | tail -5

# Revert to pre-merge state
git reset --hard <tag>
git push origin main --force
```

### 4. Fix & Re-enable
- Address issues in workflow/scripts
- Test locally if possible
- Re-enable workflow

## Success Criteria

The system is considered successful if:

- ✅ All test cases pass
- ✅ No false positives in first 10 PRs
- ✅ No unintended merges
- ✅ Review times under 5 minutes
- ✅ Clear audit trail for all actions
- ✅ Emergency controls work as expected

## Production Readiness

### Before Going Live:
1. Review all documentation
2. Verify permissions
3. Test on sample PRs
4. Monitor first 5 auto-merges closely
5. Adjust risk thresholds if needed

### After Going Live:
1. Monitor workflow runs for first 48 hours
2. Review all auto-merge decisions
3. Collect metrics
4. Fine-tune based on results
5. Update documentation with lessons learned

## Known Limitations

1. **Complex Merge Conflicts**: May not resolve all conflict types
   - Fallback: Flag for manual resolution
   
2. **Context-Sensitive Fixes**: Cannot understand semantic correctness
   - Fallback: Manual review for breaking changes
   
3. **Rate Limits**: GitHub API has rate limits
   - Mitigation: Built-in retry logic, artifact caching

4. **Edge Cases**: Unusual PR structures may not be handled
   - Mitigation: Comprehensive logging, manual review flags

## Support & Troubleshooting

### Common Issues

**Issue**: PR not being reviewed
- **Check**: Workflow triggers in YAML
- **Fix**: Ensure PR matches trigger conditions

**Issue**: Auto-fix not working
- **Check**: Workflow logs for errors
- **Fix**: Review script output, fix manually if needed

**Issue**: Unexpected auto-merge
- **Check**: Risk level classification
- **Fix**: Adjust risk patterns in auto_reviewer.py

### Getting Help

1. Check `docs/AUTO_MERGE_SYSTEM.md`
2. Review workflow run logs
3. Check artifact reports
4. Open issue with workflow run link

---

**Test Plan Version**: 1.0
**Last Updated**: 2024-12-07
**Status**: Ready for deployment
