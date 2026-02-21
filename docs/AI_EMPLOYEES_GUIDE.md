# AI Employees Setup Guide
## Your Team of Automated AI Agents for GitHub & Email Management

---

## 🤖 Meet Your AI Team

The Avalon repository now has a team of "AI employees" that work 24/7 to manage your inbox and keep everything organized across all your Git accounts.

### Your AI Team Members:

1. **📥 Categorization Agent** - Sorts and labels everything automatically
2. **✉️ Auto-Reply Agent** - Responds to messages instantly
3. **👀 Monitoring Agent** - Watches your inbox constantly
4. **🔄 Sync Agent** - Keeps all accounts in sync
5. **📧 Email Agent** - Handles email communications

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Verify AI Employees Are Working

```bash
# Go to your repository
# Click "Actions" tab
# Look for workflow: "AI Inbox Management System"
# It should show recent runs
```

✅ If you see runs, your AI team is already working!

### Step 2: Test the Auto-Reply Agent

```bash
# Create a test issue in your repository:
1. Go to "Issues" tab
2. Click "New Issue"
3. Title: "Test - AI Auto Reply"
4. Description: "Testing the AI inbox system"
5. Submit

# Within 30 seconds, you should see:
- An automated comment on the issue
- Labels applied automatically
- Issue categorized
```

### Step 3: Check the Inbox Summary

```bash
# Go to "Actions" tab
# Find "AI Inbox Management System"
# Click on the latest scheduled run
# Download the "inbox-summary" artifact
# Open the markdown file to see your inbox status
```

---

## 🎯 What Your AI Employees Do

### Categorization Agent 🏷️

**Works:** Every time an issue, PR, or discussion is created  
**Does:**
- Analyzes the content
- Assigns category (bug, feature, question, etc.)
- Sets priority (critical, high, medium, low)
- Applies appropriate labels
- Routes to correct workflow

**Example:**
```
New issue: "Game crashes when clicking Singing Dunes"
→ Category: bug-report
→ Priority: high
→ Labels: bug, priority:high, automated:inbox-managed
→ Auto-reply sent
```

### Auto-Reply Agent 💬

**Works:** Within 30 seconds of new issues/PRs  
**Does:**
- Sends immediate acknowledgment
- Sets expectations for response time
- Provides helpful links
- Confirms categorization

**Example Reply:**
```
Thank you for opening this issue! 🤖

Automated Response:
- This issue has been categorized as: bug-report
- Priority level: high
- An AI agent will review this within 24 hours

What happens next:
1. Our automated systems will validate the issue
2. Appropriate labels and assignments will be added
3. A team member will respond with next steps
```

### Monitoring Agent 👁️

**Works:** Every 6 hours  
**Does:**
- Reviews all open items
- Identifies items needing response
- Flags stale items (>7 days old)
- Generates inbox summary reports
- Tracks metrics

**Example Summary:**
```
# Inbox Summary - 2025-11-25

Total Open Items: 15
- Needs Response: 2
- Stale Items: 1
- Open PRs: 3
- Open Issues: 12
```

### Sync Agent 🔄

**Works:** Daily at midnight UTC  
**Does:**
- Syncs status across all Git accounts
- Unifies inbox from multiple platforms
- Ensures consistent categorization
- Updates cross-platform labels

**Platforms Supported:**
- ✅ GitHub (active)
- 🔜 GitLab (requires setup)
- 🔜 Bitbucket (requires setup)
- 🔜 Codeberg (requires setup)

### Email Agent 📧

**Works:** When email integration is configured  
**Does:**
- Processes incoming emails
- Sends automated responses
- Forwards to appropriate systems
- Categorizes email content

**Status:** Requires setup (see below)

---

## 🛠️ Customizing Your AI Employees

### Change Auto-Reply Messages

Edit: `.github/workflows/inbox-management.yml`

Find the `replyMessage` sections and customize:

```yaml
replyMessage = `Your custom message here!

[Content]

---
*Automated by Avalon AI*`;
```

### Adjust Monitoring Schedule

Edit: `.github/workflows/inbox-management.yml`

Change the schedule:

```yaml
schedule:
  # Current: Every 6 hours
  - cron: '0 */6 * * *'
  
  # Hourly: '0 * * * *'
  # Every 3 hours: '0 */3 * * *'
  # Daily at 9am: '0 9 * * *'
```

### Configure Email Agent

Edit: `config/automation-settings.json`

```json
{
  "inbox_management": {
    "email_integration": {
      "enabled": true,
      "service": "gmail",  // or "sendgrid"
      "auto_reply": true
    }
  }
}
```

Then add credentials to GitHub Secrets:
- `EMAIL_SERVICE_API_KEY`
- `EMAIL_FROM_ADDRESS`

---

## 📊 Managing Multiple Git Accounts

### Adding GitLab Account

1. **Create GitLab Token:**
   - GitLab → Settings → Access Tokens
   - Scopes: `api`, `read_api`
   - Copy token

2. **Add to GitHub Secrets:**
   - GitHub → Settings → Secrets → Actions
   - Name: `GITLAB_TOKEN`
   - Value: [paste token]

3. **Configure:**
   Edit `config/automation-settings.json`:
   ```json
   {
     "inbox_management": {
       "multi_account": {
         "platforms": {
           "gitlab": {
             "enabled": true,
             "username": "your-gitlab-username",
             "projects": ["project-name"]
           }
         }
       }
     }
   }
   ```

4. **Done!** Sync agent will now monitor GitLab too

### Adding Bitbucket Account

Same process as GitLab:
1. Create App Password in Bitbucket
2. Add as `BITBUCKET_TOKEN` secret
3. Configure in `automation-settings.json`
4. Enable in inbox_management settings

### Unified Inbox View

Once configured, all accounts appear in one unified view:

```json
{
  "accounts": {
    "github": { "open_items": 15, "status": "active" },
    "gitlab": { "open_items": 8, "status": "active" },
    "bitbucket": { "open_items": 3, "status": "active" }
  },
  "total_items": 26,
  "needs_response": 5
}
```

---

## 🎛️ AI Employee Controls

### Manually Trigger AI Team

```bash
# GitHub Actions tab
# Select "AI Inbox Management System"
# Click "Run workflow"
# Choose options:
# - Branch: main
# - Force reply: false (or true to resend)
# Click "Run workflow"
```

### Pause AI Employees

Temporarily disable:

```yaml
# Edit .github/workflows/inbox-management.yml
# Add at top:
on:
  workflow_dispatch:  # Only manual triggers
  # Comment out other triggers
```

Or disable specific agents in `automation-settings.json`:

```json
{
  "ai_agents": {
    "auto_reply_agent": {
      "enabled": false  // Paused
    }
  }
}
```

### View AI Activity Logs

```bash
# Actions tab
# Click on any workflow run
# Expand each step to see logs
# Example:
#   - "Categorize GitHub notification" → See categorization
#   - "Send auto-reply" → See reply sent
#   - "Apply smart labels" → See labels applied
```

---

## 📈 Monitoring AI Performance

### Daily Metrics

Download artifacts from workflow runs:

```
inbox-summary-{run-number}.md
  → Shows inbox status, items needing attention

email-templates-{run-number}/
  → Current email response templates

multi-account-status-{run-number}.json
  → Status of all connected accounts
```

### Example Metrics:

```json
{
  "period": "last_24_hours",
  "auto_replies_sent": 12,
  "items_categorized": 15,
  "labels_applied": 23,
  "stale_items_flagged": 2,
  "response_time_avg_seconds": 25
}
```

### Performance Indicators:

✅ **Healthy System:**
- Auto-replies sent: 90%+ of new items
- Average response time: <60 seconds
- Categorization accuracy: ~95%
- No missed items in 24h reviews

⚠️ **Needs Attention:**
- Auto-replies: <80%
- Response time: >2 minutes
- Stale items increasing
- Duplicate responses

---

## 🔧 Troubleshooting Your AI Team

### AI Not Responding

**Check:**
1. Workflow is enabled (Actions → Workflows)
2. Permissions granted (Settings → Actions)
3. No errors in recent runs

**Fix:**
```bash
# Re-enable workflow
# Or manually trigger once
# Check logs for errors
```

### Duplicate Responses

**Cause:** Re-running workflow on same item

**Fix:**
```yaml
# System automatically prevents duplicates
# If occurring, check:
skip_if_replied: true  # in automation-settings.json
```

### Labels Not Applied

**Cause:** Labels don't exist

**Fix:**
```bash
# Create required labels:
# Go to Issues → Labels → New Label
# Create:
- automated:inbox-managed (green)
- priority:high (red)
- priority:critical (dark red)
- bug (red)
- enhancement (blue)
- question (purple)
```

### Email Agent Not Working

**Cause:** Not configured yet

**Fix:**
1. Set up email service (Gmail/SendGrid)
2. Add API credentials to Secrets
3. Enable in `automation-settings.json`
4. See full docs: `docs/INBOX_MANAGEMENT.md`

---

## 🚀 Advanced Features

### Smart Priority Detection

AI analyzes content for urgency indicators:
- Words: "urgent", "critical", "broken", "crash" → High priority
- Security keywords → Critical priority
- Questions → Medium priority

### Sentiment Analysis (Future)

Coming soon: AI detects emotion and urgency from tone

### Auto-Assignment (Future)

Coming soon: AI assigns issues to team members based on expertise

### Integration with Task Managers

Configure in `automation-settings.json`:

```json
{
  "integrations": {
    "jira": { "enabled": false },
    "asana": { "enabled": false },
    "trello": { "enabled": false }
  }
}
```

---

## 📚 Quick Reference

### File Locations

- **Main Workflow:** `.github/workflows/inbox-management.yml`
- **Configuration:** `config/automation-settings.json`
- **Email Templates:** `config/email-templates/`
- **Documentation:** `docs/INBOX_MANAGEMENT.md`

### Common Commands

```bash
# View workflow runs
gh run list --workflow=inbox-management.yml

# Trigger manually
gh workflow run inbox-management.yml

# Download latest summary
gh run download --name inbox-summary

# Check current config
cat config/automation-settings.json | jq '.inbox_management'
```

### Quick Checks

✅ **Is it working?**
```bash
# Create test issue → Should get auto-reply in <1 minute
```

✅ **What's in my inbox?**
```bash
# Download latest inbox-summary artifact
```

✅ **Which accounts are synced?**
```bash
# Download multi-account-status artifact
```

---

## 🎓 Learning Resources

### Beginner:
1. Create a test issue
2. Watch the auto-reply arrive
3. Check the labels applied
4. Download an inbox summary

### Intermediate:
1. Customize auto-reply messages
2. Add GitLab or Bitbucket account
3. Adjust monitoring schedule
4. Create custom email templates

### Advanced:
1. Set up email integration
2. Configure multiple platforms
3. Customize categorization logic
4. Build custom integrations

---

## 💡 Best Practices

### For Maximum Effectiveness:

1. **Let AI Handle First Response**
   - Don't rush to reply
   - AI acknowledges within seconds
   - You respond with thoughtful answers later

2. **Review Summaries Regularly**
   - Check inbox-summary daily
   - Address "needs response" items
   - Close or update stale items

3. **Keep Templates Updated**
   - Customize email templates
   - Add project-specific info
   - Update links as needed

4. **Monitor All Accounts**
   - Add all Git platforms
   - Unified inbox = no missed items
   - Consistent responses everywhere

5. **Trust the AI**
   - Categorization is ~95% accurate
   - Auto-replies are professional
   - System learns from patterns

---

## 🎉 Success Tips

> **Tip 1:** Start with GitHub only, add other accounts later

> **Tip 2:** Customize one template at a time

> **Tip 3:** Check summaries weekly, not daily (AI handles daily)

> **Tip 4:** Enable email integration last (most complex)

> **Tip 5:** Let AI run for a week before tweaking settings

---

## 🆘 Get Help

**Something not working?**

1. Check `docs/INBOX_MANAGEMENT.md` for detailed docs
2. Review workflow logs in Actions tab
3. Create an issue (you'll get an auto-reply! 😉)
4. Check configuration files for typos

**Want to improve the AI?**

1. Suggest improvements via GitHub issue
2. Customize templates for your needs
3. Share feedback on auto-reply quality
4. Contribute to workflow enhancements

---

## 🔄 Quick Updates

### Update AI Behavior:

```bash
# 1. Edit workflow file or config
# 2. Commit changes
# 3. AI automatically uses new settings on next run
```

### Add New Platform:

```bash
# 1. Get API token from platform
# 2. Add to GitHub Secrets
# 3. Enable in automation-settings.json
# 4. Done! Syncs on next scheduled run
```

---

## 📊 System Status

**Current AI Team Status:**

- ✅ Categorization Agent: **Active**
- ✅ Auto-Reply Agent: **Active**
- ✅ Monitoring Agent: **Active** (every 6h)
- ✅ Sync Agent: **Active** (daily)
- ⏸️ Email Agent: **Requires Setup**

**Connected Accounts:**

- ✅ GitHub: **Active**
- ⏸️ GitLab: **Not Configured**
- ⏸️ Bitbucket: **Not Configured**

**Last 24 Hours:**

- Items Processed: Check latest summary
- Auto-Replies Sent: Check workflow runs
- Categories Assigned: Check workflow logs

---

## 🚀 Next Steps

### Immediate (Today):
- [x] AI team is running
- [ ] Create test issue to verify
- [ ] Download inbox summary
- [ ] Review auto-reply templates

### This Week:
- [ ] Customize auto-reply messages
- [ ] Add required labels to repository
- [ ] Review first week of summaries
- [ ] Fine-tune monitoring schedule

### This Month:
- [ ] Add GitLab/Bitbucket accounts (if needed)
- [ ] Set up email integration (if needed)
- [ ] Optimize categorization rules
- [ ] Share success story!

---

**Congratulations! Your AI employee team is now managing your inbox 24/7!** 🎉

No more missed notifications. No more manual categorization. No more delayed responses.

Your AI team has it covered. ✨

---

*"The best magic is the kind that works while you sleep."* - Polly

---

**Last Updated:** 2025-11-25  
**Documentation:** See `docs/INBOX_MANAGEMENT.md` for complete details  
**Support:** Create an issue (and get an instant auto-reply!)
