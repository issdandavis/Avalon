# Enterprise Account Auto-Approval Configuration

This configuration enables automatic workflow approval for trusted enterprise accounts in a multi-profile organization.

## Approved Enterprise Accounts

The following accounts are automatically approved to run all workflows:

- **issdandavis** (Primary account)
- **215328633+issdandavis@users.noreply.github.com** (GitHub user ID)

## How It Works

1. **Workflow Detection**
   - Monitors all workflow runs and pull requests
   - Checks if actor is in approved accounts list
   - Auto-approves if account is trusted

2. **Auto-Approval Triggers**
   - `workflow_run: requested` - Workflow needs approval
   - `pull_request_target: opened` - New PR from approved account
   - `pull_request_target: synchronize` - PR updated by approved account

3. **Actions Taken**
   - Approves workflow runs automatically
   - Approves pull requests from enterprise accounts
   - Enables all workflow actions without manual approval

## Security

### Approved Accounts Only
Only accounts explicitly listed in the `APPROVED_ACCOUNTS` array will be auto-approved. All other accounts require manual approval.

### Permissions
The workflow has necessary permissions:
- `actions: write` - Approve workflow runs
- `contents: write` - Approve PRs that modify content
- `pull-requests: write` - Approve PRs
- `checks: write` - Enable check runs

### Safety Features
- Explicit account allowlist
- Conditional execution (only runs for approved accounts)
- Audit trail in workflow logs
- Can be disabled by removing workflow file

## Adding More Enterprise Accounts

To add additional enterprise accounts, edit `.github/workflows/auto-approve-workflows.yml`:

```yaml
APPROVED_ACCOUNTS=(
  "issdandavis"
  "215328633+issdandavis@users.noreply.github.com"
  "your-other-account"  # Add here
  "another-account"     # Add here
)
```

## Disabling Auto-Approval

To disable for specific workflows, add to their YAML:

```yaml
if: github.event_name != 'workflow_run'
```

To disable entirely:
- Delete `.github/workflows/auto-approve-workflows.yml`
- Or set `if: false` in the auto-approve job

## Benefits for Multi-Profile Organizations

### For Single-Person Organizations with Multiple Profiles

**Problem:** GitHub requires approval for workflow runs from external contributors, including your own other profiles.

**Solution:** Auto-approve trusted accounts so all your profiles can trigger workflows without manual approval.

**Use Cases:**
- Personal account + work account
- Multiple GitHub identities
- Organization with sole contributor
- Testing different account permissions

### Workflow Integration

This auto-approval system works with:
- ✅ AI Scene Writer (every 3 hours)
- ✅ AI Content Polisher (every 4 hours)
- ✅ AI Stat Balancer (daily)
- ✅ AI Game Tester (daily + PRs)
- ✅ AI Autonomous Worker (every 6 hours)
- ✅ Agent Management Dashboard (2x daily)
- ✅ Any custom workflows you add

**All your accounts can now trigger these workflows automatically!**

## Monitoring

### Check Auto-Approval Activity

View workflow runs:
```bash
# Via GitHub CLI
gh run list --workflow=auto-approve-workflows.yml

# In browser
# Go to Actions → Auto-Approve Enterprise Account Workflows
```

### Verify Account Approved

Check workflow logs for:
```
✅ Account [username] is approved for auto-workflow execution
✅ PR #[number] auto-approved
```

## Configuration File

Location: `.github/workflows/auto-approve-workflows.yml`

To modify approved accounts:
1. Edit the workflow file
2. Update `APPROVED_ACCOUNTS` array
3. Commit and push
4. Takes effect immediately

## Troubleshooting

### Workflows still require approval

**Cause:** Account not in approved list

**Fix:** Add account to `APPROVED_ACCOUNTS` array in workflow file

### Auto-approval not triggering

**Cause:** Workflow file syntax error

**Fix:** Validate YAML:
```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/auto-approve-workflows.yml'))"
```

### PR not auto-approved

**Cause:** Permissions insufficient

**Fix:** Ensure workflow has `pull-requests: write` permission (already configured)

## Related Documentation

- `docs/AGENT_MANAGEMENT_GUIDE.md` - Agent coordination
- `ACCOUNTS_README.md` - Inter-account automation
- `AI_SYSTEM_ACTIVATION_GUIDE.md` - System activation

---

**Status:** ✅ Active and monitoring all workflow runs  
**Accounts:** 1 approved (issdandavis)  
**Last Updated:** 2025-11-25
