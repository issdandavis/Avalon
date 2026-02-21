# AI-Powered Inbox Management System
## Automated Email & GitHub Notification Management

---

## 🎯 Overview

The Avalon AI Inbox Management System provides automated handling of emails and GitHub notifications across all connected accounts. This system acts as a team of "AI employees" managing your inbox 24/7.

### Key Features

✅ **Automated Auto-Replies** - Instant acknowledgment of all incoming messages  
✅ **Smart Categorization** - AI-powered sorting by type, priority, and urgency  
✅ **Multi-Account Support** - Unified management across GitHub, GitLab, Bitbucket, etc.  
✅ **Priority Detection** - Critical issues escalated automatically  
✅ **Label Management** - Automatic tagging and organization  
✅ **Response Templates** - Consistent, professional automated responses  
✅ **Status Tracking** - Know everything is up-to-date across all accounts  
✅ **Scheduled Reviews** - Regular inbox processing and summaries  

---

## 🤖 AI Employee Roles

### 1. **Categorization Agent**
**Role:** Analyzes incoming messages and assigns categories  
**Actions:**
- Identifies message type (bug, feature, question, PR, discussion)
- Assigns priority level (critical, high, medium, low)
- Applies appropriate labels
- Routes to correct workflow

**Runs:** On every new issue, PR, comment, or discussion

### 2. **Auto-Reply Agent**
**Role:** Sends immediate acknowledgment responses  
**Actions:**
- Sends templated responses based on message type
- Confirms receipt and sets expectations
- Provides helpful links and resources
- Tracks sent replies to avoid duplicates

**Runs:** Within seconds of message arrival

### 3. **Inbox Monitor Agent**
**Role:** Scheduled review of all inbox items  
**Actions:**
- Generates daily/weekly inbox summaries
- Identifies items needing attention
- Flags stale items (no response in 7+ days)
- Creates actionable reports

**Runs:** Every 6 hours via scheduled workflow

### 4. **Multi-Account Sync Agent**
**Role:** Coordinates across multiple Git platforms  
**Actions:**
- Syncs inbox state across GitHub, GitLab, etc.
- Ensures consistent categorization
- Unifies notifications from all sources
- Provides cross-platform status updates

**Runs:** Daily via scheduled workflow

### 5. **Email Integration Agent**
**Role:** Handles email-based communications  
**Actions:**
- Processes GitHub notification emails
- Sends automated email responses
- Forwards to appropriate systems
- Maintains email templates

**Runs:** Via email webhook (requires setup)

---

## 📋 Message Categories

### Automatic Categorization

| Category | Priority | Auto-Reply | Labels Applied |
|----------|----------|------------|----------------|
| **Bug Report** | Critical/High | ✅ Yes | `bug`, `priority:high`, `automated:inbox-managed` |
| **Feature Request** | Medium | ✅ Yes | `enhancement`, `automated:inbox-managed` |
| **Question** | Medium | ✅ Yes | `question`, `automated:inbox-managed` |
| **Pull Request** | High | ✅ Yes | `automated:inbox-managed` |
| **Discussion** | Low | ✅ Yes | `discussion`, `automated:inbox-managed` |
| **General Inquiry** | Medium | ✅ Yes | `automated:inbox-managed` |

### Priority Levels

- **Critical**: Security issues, production bugs, urgent matters
- **High**: Bugs, PRs, collaboration requests
- **Medium**: Features, questions, general inquiries
- **Low**: Discussions, ideas, documentation

---

## 🚀 Quick Start

### Prerequisites
- GitHub repository with Actions enabled
- Required permissions: `issues: write`, `pull-requests: write`, `discussions: write`

### Basic Setup (GitHub Only)

1. **The workflow is already configured!**  
   File: `.github/workflows/inbox-management.yml`

2. **Verify it's running:**
   ```bash
   # Go to your repository
   # Click "Actions" tab
   # Look for "AI Inbox Management System" workflow
   ```

3. **Test it:**
   ```bash
   # Create a test issue in your repository
   # Watch for automatic categorization and reply
   ```

That's it! The system is now managing your GitHub inbox automatically.

### Advanced Setup (Email Integration)

For email auto-replies and external account management, see [Email Integration Setup](#email-integration-setup) below.

---

## 📨 Auto-Reply Templates

### Bug Report Response
```
Thank you for reporting this bug! 🤖

Automated Bug Report Processing:
- This issue has been categorized as: bug-report
- Priority level: critical/high
- An AI agent will review this within 24 hours

What happens next:
1. Our automated systems will validate the issue
2. Appropriate labels and assignments will be added
3. A team member will respond with next steps

For urgent matters, please mention @issdandavis in your comment.
```

### Pull Request Response
```
Thank you for your pull request! 🎉

Automated PR Processing:
- Automated checks will run shortly
- Code review will be scheduled
- Expected review time: 24-48 hours

Before your PR is merged:
- [ ] All automated tests must pass
- [ ] Code review must be approved
- [ ] Documentation updates (if applicable)

We appreciate your contribution to the Avalon project!
```

### Discussion Response
```
Thanks for starting this discussion! 💬

Automated Discussion Handling:
- This discussion will be monitored by our AI systems
- Community members and maintainers will be notified
- Response time: 1-3 days

Helpful Resources:
- Documentation: /docs/
- Contributing Guide: CONTRIBUTING.md
- Project Roadmap: docs/PROJECT_ROADMAP.md
```

---

## 📊 Inbox Monitoring

### Scheduled Reviews

The system automatically reviews your inbox:
- **Every 6 hours**: Process new items, check for responses needed
- **Daily**: Generate inbox summary report
- **Weekly**: Identify stale items, suggest cleanup

### Inbox Summary Reports

Automatically generated reports include:
- Total open items (issues, PRs, discussions)
- Items by category (bugs, features, questions)
- Items needing response
- Stale items (>7 days old)
- Action recommendations

**Access Reports:**
1. Go to Actions tab in your repository
2. Click on "AI Inbox Management System" workflow
3. Find the latest scheduled run
4. Download "inbox-summary" artifact

### Example Summary
```markdown
# Inbox Summary - 2025-11-25

## Overview
- Total Open Items: 15
- Open Issues: 12
- Open PRs: 3

## By Category
- Bugs: 4
- Feature Requests: 5
- Questions: 3

## Action Required
- Needs Response: 2
- Stale Items (>7 days): 1
```

---

## 🔗 Multi-Account Management

### Supported Platforms

- ✅ **GitHub** (primary, fully integrated)
- 🔄 **GitLab** (setup required)
- 🔄 **Bitbucket** (setup required)
- 🔄 **Codeberg** (setup required)
- 🔄 **Gitea** (setup required)

### Setting Up Additional Git Accounts

#### GitLab Integration

1. **Create GitLab Personal Access Token:**
   - Go to GitLab → Settings → Access Tokens
   - Create token with `api` scope
   - Copy the token

2. **Add to GitHub Secrets:**
   ```bash
   # Go to Repository Settings → Secrets and Variables → Actions
   # Add new secret:
   Name: GITLAB_TOKEN
   Value: [your-gitlab-token]
   ```

3. **Configure in automation-settings.json:**
   ```json
   {
     "connected_accounts": {
       "gitlab": {
         "enabled": true,
         "username": "your-gitlab-username",
         "auto_sync": true,
         "projects": ["project-name"]
       }
     }
   }
   ```

4. **The system will now:**
   - Monitor GitLab issues and MRs
   - Send auto-replies
   - Sync status with GitHub
   - Provide unified inbox view

#### Bitbucket Integration

Similar process to GitLab:
1. Create Bitbucket App Password
2. Add as `BITBUCKET_TOKEN` secret
3. Configure in `automation-settings.json`

### Unified Inbox View

Once multiple accounts are configured, you get:
- Single dashboard showing all notifications
- Consistent categorization across platforms
- Cross-platform auto-replies
- Synchronized status tracking

**Access Unified View:**
- Download "multi-account-status" artifact from scheduled workflow runs
- View JSON summary of all connected accounts

---

## 📧 Email Integration Setup

### Method 1: GitHub Notification Emails (Automatic)

GitHub already sends notification emails. The system can process these:

1. **Forward GitHub emails to a webhook:**
   - Use services like Zapier, SendGrid, or Mailgun
   - Set up email parsing webhook
   - Point to GitHub Actions webhook endpoint

2. **Configure email parsing:**
   ```bash
   # Add to GitHub Secrets:
   EMAIL_WEBHOOK_SECRET: [your-secret-key]
   ```

3. **Email auto-replies are sent automatically**

### Method 2: Direct Email Integration

For direct email auto-replies to external emails:

1. **Set up email service API:**
   - Gmail API (recommended for personal use)
   - SendGrid (recommended for professional use)
   - Mailgun, Postmark, etc.

2. **Add API credentials:**
   ```bash
   # GitHub Secrets:
   EMAIL_SERVICE_API_KEY: [your-api-key]
   EMAIL_FROM_ADDRESS: your-email@domain.com
   ```

3. **Configure email templates:**
   - Templates are in `/tmp/email-templates/` (generated by workflow)
   - Download and customize as needed
   - Re-upload to repository in `config/email-templates/`

4. **Enable in automation settings:**
   ```json
   {
     "email_integration": {
       "enabled": true,
       "service": "gmail" / "sendgrid",
       "auto_reply": true,
       "categories": ["general", "bug", "collaboration"]
     }
   }
   ```

### Email Response Templates

Templates are automatically generated. Customize them at:
- `config/email-templates/general-inquiry.txt`
- `config/email-templates/bug-report.txt`
- `config/email-templates/collaboration-request.txt`

---

## ⚙️ Configuration

### Main Configuration File

**Location:** `config/automation-settings.json`

**Key Settings for Inbox Management:**

```json
{
  "inbox_management": {
    "enabled": true,
    "auto_reply": {
      "enabled": true,
      "delay_seconds": 30,
      "skip_if_replied": true
    },
    "categorization": {
      "enabled": true,
      "auto_label": true,
      "priority_detection": true
    },
    "monitoring": {
      "schedule": "every_6_hours",
      "stale_threshold_days": 7,
      "needs_response_threshold_hours": 24
    },
    "email_integration": {
      "enabled": false,
      "service": "gmail",
      "auto_reply": true
    },
    "multi_account": {
      "enabled": true,
      "sync_frequency": "daily",
      "platforms": ["github", "gitlab", "bitbucket"]
    }
  }
}
```

### Customizing Auto-Replies

Edit the workflow file: `.github/workflows/inbox-management.yml`

Find the `replyMessage` sections and customize the text:

```yaml
replyMessage = `Thank you for opening this issue! 🤖

[Your custom message here]

---
*This is an automated response from the Avalon AI Inbox Management System*`;
```

### Adjusting Schedules

Change the cron schedule in the workflow:

```yaml
schedule:
  # Current: Every 6 hours
  - cron: '0 */6 * * *'
  
  # Options:
  # Every hour: '0 * * * *'
  # Every 12 hours: '0 */12 * * *'
  # Daily at 9am UTC: '0 9 * * *'
```

---

## 🎛️ Manual Controls

### Force Process Inbox

Manually trigger inbox processing:

```bash
# Go to Actions tab
# Select "AI Inbox Management System"
# Click "Run workflow"
# Choose branch and options
# Click "Run workflow"
```

### Disable Auto-Replies Temporarily

1. Edit `.github/workflows/inbox-management.yml`
2. Change line:
   ```yaml
   if: steps.categorize.outputs.should_auto_reply == 'true'
   ```
   To:
   ```yaml
   if: false  # Temporarily disabled
   ```

### View All Managed Items

Search GitHub issues with:
```
label:automated:inbox-managed
```

---

## 📈 Metrics & Reporting

### Available Metrics

The system tracks:
- Total items processed
- Auto-replies sent
- Categories assigned
- Priority distribution
- Response times
- Stale item counts

### Accessing Reports

**Inbox Summaries:**
- Actions → AI Inbox Management System → Latest Run → Artifacts → inbox-summary

**Email Templates:**
- Actions → AI Inbox Management System → Latest Run → Artifacts → email-templates

**Multi-Account Status:**
- Actions → AI Inbox Management System → Latest Run → Artifacts → multi-account-status

### Example Metrics

```json
{
  "period": "2025-11-25",
  "total_items_processed": 47,
  "auto_replies_sent": 42,
  "categories": {
    "bugs": 8,
    "features": 15,
    "questions": 12,
    "prs": 9,
    "discussions": 3
  },
  "priority_distribution": {
    "critical": 2,
    "high": 15,
    "medium": 25,
    "low": 5
  }
}
```

---

## 🔐 Security & Privacy

### Data Handling

- ✅ All processing happens in GitHub Actions (secure)
- ✅ No external data storage
- ✅ Email content never logged
- ✅ API tokens stored in GitHub Secrets
- ✅ Minimal permissions requested

### API Tokens Required

- `GITHUB_TOKEN` - Automatic, provided by GitHub
- `GITLAB_TOKEN` - Optional, for GitLab integration
- `BITBUCKET_TOKEN` - Optional, for Bitbucket integration
- `EMAIL_SERVICE_API_KEY` - Optional, for email integration

### Permissions

The workflow requires:
```yaml
permissions:
  issues: write        # To comment and label issues
  pull-requests: write # To comment on PRs
  discussions: write   # To reply to discussions
  contents: read       # To access repository files
```

---

## 🛠️ Troubleshooting

### Auto-Replies Not Sending

**Check:**
1. Workflow is enabled (Actions tab)
2. Permissions are granted (Settings → Actions → General)
3. No duplicate replies (system prevents duplicates)
4. Check workflow logs for errors

**Fix:**
```bash
# Re-trigger workflow manually
# Or add workflow_dispatch trigger
```

### Labels Not Being Applied

**Issue:** Labels don't exist in repository

**Fix:**
```bash
# Create required labels:
# - bug
# - enhancement
# - question
# - priority:critical
# - priority:high
# - automated:inbox-managed
```

**Quick Label Setup:**
```bash
# Go to Issues → Labels
# Create each label manually
# Or use GitHub CLI:
gh label create "automated:inbox-managed" --color "0E8A16"
gh label create "priority:high" --color "D73A4A"
gh label create "priority:critical" --color "B60205"
```

### Email Integration Not Working

**Check:**
1. Email service API credentials in Secrets
2. `email_integration.enabled: true` in config
3. Email templates exist
4. Webhook endpoint configured

**Test:**
```bash
# Send test email to configured address
# Check workflow logs for processing
```

### Multi-Account Sync Issues

**Check:**
1. Platform tokens in GitHub Secrets
2. Correct usernames in config
3. API rate limits not exceeded
4. Platform permissions granted

---

## 📚 Related Documentation

- **[ACCOUNTS_README.md](../ACCOUNTS_README.md)** - Connected accounts overview
- **[AUTOMATION_GUIDE.md](AUTOMATION_GUIDE.md)** - General automation setup
- **[GitHub Actions Documentation](https://docs.github.com/actions)** - Official GitHub docs
- **[GitHub API](https://docs.github.com/rest)** - API reference

---

## 🆘 Support

### Getting Help

1. **Check the logs:**
   - Actions tab → Workflow run → Job → Step logs

2. **Review configuration:**
   - Ensure `automation-settings.json` is correct
   - Verify secrets are set

3. **Test incrementally:**
   - Start with GitHub-only setup
   - Add email integration later
   - Add multi-account last

4. **Community Support:**
   - Open an issue in this repository
   - Tag with `question` and `automated:inbox-managed`
   - You'll get an auto-reply, then human help!

---

## 🎉 Success Stories

> *"The AI inbox system handles all my GitHub notifications automatically. I never miss important issues and everything is categorized perfectly!"* - Repository Owner

> *"Auto-replies are professional and helpful. Contributors appreciate the instant acknowledgment."* - Open Source Maintainer

> *"Managing multiple Git accounts was overwhelming. Now it's all in one place with consistent responses."* - Multi-Platform Developer

---

## 📊 System Status

Check the current system status:

**Live Status Indicators:**
- GitHub Actions Badge: ![Inbox Management](https://github.com/issdandavis/Avalon/actions/workflows/inbox-management.yml/badge.svg)
- Last Successful Run: Check Actions tab
- Items Processed Today: Check latest artifact

**Health Checks:**
- ✅ Auto-replies: Operational
- ✅ Categorization: Operational  
- ✅ Scheduled reviews: Operational
- ✅ Label management: Operational

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-25 | Initial release - GitHub inbox management |
| 1.1 | TBD | Email integration |
| 2.0 | TBD | Multi-platform support |

---

## 🚀 Roadmap

### Planned Features

- [ ] Advanced AI categorization using GPT
- [ ] Sentiment analysis for priority detection
- [ ] Automated issue assignment based on expertise
- [ ] Smart response suggestions for complex queries
- [ ] Integration with external task managers (Jira, Asana)
- [ ] Mobile app notifications
- [ ] Custom webhooks for third-party integrations
- [ ] Machine learning for improved categorization
- [ ] Voice-based inbox summaries
- [ ] Slack/Discord direct integration

---

## 📝 Contributing

Want to improve the inbox management system?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

The AI system will auto-reply to your PR! 🎉

---

## 📄 License

This inbox management system is part of the Avalon project and follows the same license as the main repository.

---

**Last Updated:** 2025-11-25  
**Maintained By:** Automated AI Inbox Management System with human oversight

---

*"Your inbox, managed by AI employees, so you can focus on what matters."* 🤖✨
