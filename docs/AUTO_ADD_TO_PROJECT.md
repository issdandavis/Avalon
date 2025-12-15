# Auto-Add to Project Configuration

This feature automatically adds pull requests and issues to your GitHub Projects board for better project management and tracking.

## Overview

The auto-add-to-project functionality is integrated into the following workflows:
- `auto-review-fix-merge.yml` - Adds PRs when they are opened
- `auto-approve-workflows.yml` - Adds PRs from enterprise accounts
- `inbox-management.yml` - Adds both PRs and issues

## How It Works

1. **Trigger Detection**
   - Monitors pull request events (opened, synchronized, reopened)
   - Monitors issue events (opened, labeled, assigned)
   - Runs automatically when these events occur

2. **Project Addition**
   - Uses `actions/add-to-project@v1.0.2` GitHub Action
   - Authenticates with `GITHUB_TOKEN`
   - Adds item to configured project board

3. **Conditional Execution**
   - Only runs for relevant event types
   - Runs as a separate job (doesn't block other workflow jobs)
   - Fails gracefully if project doesn't exist

## Configuration

### Project URL
Currently configured for: `https://github.com/users/issdandavis/projects/1`

To change the project:
1. Edit the workflow files:
   - `.github/workflows/auto-review-fix-merge.yml`
   - `.github/workflows/auto-approve-workflows.yml`
   - `.github/workflows/inbox-management.yml`

2. Update the `project-url` parameter:
   ```yaml
   - name: Add to project
     uses: actions/add-to-project@v1.0.2
     with:
       project-url: https://github.com/users/YOUR_USERNAME/projects/YOUR_PROJECT_NUMBER
       github-token: ${{ secrets.GITHUB_TOKEN }}
   ```

### Multiple Projects

To add items to multiple projects, duplicate the step:

```yaml
steps:
  - name: Add to Development Project
    uses: actions/add-to-project@v1.0.2
    with:
      project-url: https://github.com/users/issdandavis/projects/1
      github-token: ${{ secrets.GITHUB_TOKEN }}
  
  - name: Add to Content Project
    uses: actions/add-to-project@v1.0.2
    with:
      project-url: https://github.com/users/issdandavis/projects/2
      github-token: ${{ secrets.GITHUB_TOKEN }}
```

## Workflow Integration

### auto-review-fix-merge.yml
```yaml
jobs:
  add-to-project:
    name: Add to Project
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'
    
    steps:
      - name: Add PR to project
        uses: actions/add-to-project@v1.0.2
        with:
          project-url: https://github.com/users/issdandavis/projects/1
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

### auto-approve-workflows.yml
```yaml
jobs:
  add-to-project:
    name: Add to Project
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request_target'
    
    steps:
      - name: Add PR to project
        uses: actions/add-to-project@v1.0.2
        with:
          project-url: https://github.com/users/issdandavis/projects/1
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

### inbox-management.yml
```yaml
jobs:
  add-to-project:
    name: Add to Project
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request' || github.event_name == 'issues'
    
    steps:
      - name: Add item to project
        uses: actions/add-to-project@v1.0.2
        with:
          project-url: https://github.com/users/issdandavis/projects/1
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

## Benefits

### Automatic Project Management
- **No Manual Work:** PRs and issues automatically appear in project board
- **Centralized Tracking:** All work items in one place
- **Better Visibility:** See all active work at a glance
- **Status Tracking:** Follow items through project columns

### Integration with Existing Workflows
- Works alongside auto-review, auto-merge, and inbox management
- Doesn't interfere with other workflow jobs
- Runs independently for reliability

### Enterprise Account Support
- Works with multi-account setups
- Integrates with auto-approval system
- Supports both personal and organization projects

## Monitoring

### Check Activity

View workflow runs to see when items are added:
```bash
# Via GitHub CLI
gh run list --workflow=auto-review-fix-merge.yml
gh run list --workflow=auto-approve-workflows.yml
gh run list --workflow=inbox-management.yml

# In browser
# Go to Actions → Select workflow → View runs
```

### Verify Items Added

Check your project board:
1. Navigate to your GitHub Projects board
2. Look for recently added items
3. Items appear in the default "To Do" or first column

### Workflow Logs

Check logs for confirmation:
```
Add to Project / Add PR to project
✓ Item added to project successfully
```

## Troubleshooting

### Items Not Being Added

**Cause:** Project URL incorrect or project doesn't exist

**Fix:** 
1. Verify project URL is correct
2. Ensure project exists and is accessible
3. Check project number in URL matches configuration

### Permission Errors

**Cause:** GITHUB_TOKEN lacks permissions

**Fix:** Ensure workflow has necessary permissions:
```yaml
permissions:
  contents: write
  pull-requests: write
  issues: write
```

### Workflow Not Triggering

**Cause:** Event type mismatch

**Fix:** Check if condition matches event:
```yaml
if: github.event_name == 'pull_request'  # For PR events
if: github.event_name == 'issues'        # For issue events
```

### Action Version Issues

**Cause:** Outdated action version

**Fix:** Update to latest version:
```yaml
uses: actions/add-to-project@v1.0.2  # Current version
```

## Advanced Configuration

### Label-Based Project Routing

Add items to different projects based on labels:

```yaml
- name: Add to Bug Tracking Project
  if: contains(github.event.issue.labels.*.name, 'bug')
  uses: actions/add-to-project@v1.0.2
  with:
    project-url: https://github.com/users/issdandavis/projects/2
    github-token: ${{ secrets.GITHUB_TOKEN }}

- name: Add to Feature Project
  if: contains(github.event.pull_request.labels.*.name, 'feature')
  uses: actions/add-to-project@v1.0.2
  with:
    project-url: https://github.com/users/issdandavis/projects/3
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Organization Projects

For organization-level projects, update the URL:
```yaml
project-url: https://github.com/orgs/YOUR_ORG/projects/PROJECT_NUMBER
```

### Conditional Project Addition

Only add certain types of PRs:
```yaml
- name: Add to project
  if: |
    github.event_name == 'pull_request' &&
    github.event.pull_request.draft == false
  uses: actions/add-to-project@v1.0.2
  with:
    project-url: https://github.com/users/issdandavis/projects/1
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

## Disabling Auto-Add

### For Specific Workflow

Comment out or remove the `add-to-project` job:

```yaml
# jobs:
#   add-to-project:
#     name: Add to Project
#     ...
```

### For All Workflows

Edit all three workflow files and remove the `add-to-project` job sections.

### For Specific Items

Add a label to skip auto-add (requires custom configuration):
```yaml
- name: Add to project
  if: |
    github.event_name == 'pull_request' &&
    !contains(github.event.pull_request.labels.*.name, 'no-project')
  uses: actions/add-to-project@v1.0.2
  with:
    project-url: https://github.com/users/issdandavis/projects/1
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

## Related Documentation

- `AUTO_APPROVE_WORKFLOWS.md` - Enterprise account auto-approval
- `AUTO_MERGE_SYSTEM.md` - Automated PR merging
- `INBOX_MANAGEMENT.md` - Notification and issue management
- `AUTOMATION_GUIDE.md` - Complete automation overview

## GitHub Projects Resources

- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [actions/add-to-project Action](https://github.com/actions/add-to-project)
- [GitHub Actions Permissions](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)

---

**Status:** ✅ Active across 3 workflows  
**Project:** issdandavis/projects/1  
**Action Version:** v1.0.2  
**Last Updated:** 2025-12-14
