# ISDanDavis Quick Reference Guide

## 🎯 What This Setup Does

This automation system handles all inter-account communications for the Avalon project **silently** - meaning you won't get notifications for routine progress updates, builds, or content syncs. You'll only be notified about important events like build failures or releases.

---

## 📱 Your Connected Accounts

### Active & Configured
- ✅ **GitHub** (issdandavis/Avalon) - Primary repository
- ✅ **GitHub Pages** - Auto-deploys web version
- ✅ **GitHub Actions** - Automated workflows

### Available for Connection
- ⏳ **Discord** - Team notifications (webhook needed)
- ⏳ **Google Workspace** - Content sync (API key needed)
- ⏳ **Zapier** - External automations (webhook needed)
- ⏳ **Social Media** - Release announcements (API keys needed)

---

## 🔕 Silent Mode Features

### What Runs Automatically (No Notifications)
1. **Every Push to Main Branch:**
   - Progress metrics calculated
   - Content validated
   - Quality checks performed
   - Reports archived

2. **Daily (00:00 UTC):**
   - Repository health check
   - Metrics collection
   - Summary generation
   - Artifact cleanup

3. **On Content Changes:**
   - ChoiceScript syntax validation
   - Link verification
   - Word count tracking
   - Repository sync

### What You'll Be Notified About
- ❗ Build failures
- ❗ Test failures
- ❗ Security alerts
- ✅ New releases (optional)
- ✅ Major milestones

---

## 🚀 Quick Actions

### View Automation Status
1. Go to your repository: https://github.com/issdandavis/Avalon
2. Click "Actions" tab
3. See recent workflow runs (all running silently)

### Check Progress Reports
1. Go to Actions tab
2. Click any completed workflow
3. Scroll to "Artifacts" section
4. Download progress/quality reports

### Manually Trigger with Notification
1. Go to Actions tab
2. Select "AI Inter-Account Automation"
3. Click "Run workflow"
4. Enable "Send user notifications"
5. Click "Run workflow" button

### Adjust Settings
Edit `config/automation-settings.json` to:
- Change notification preferences
- Enable/disable specific workflows
- Configure sync frequencies
- Set notification thresholds

---

## 📊 What Gets Tracked (Silently)

### Development Metrics
- Total word count in game files
- Number of ChoiceScript scenes
- Commits per day/week
- Lines of code added/removed

### Quality Metrics
- ChoiceScript syntax errors
- Broken documentation links
- Build success rate
- Test coverage

### Progress Indicators
- Scenes completed
- Endings implemented
- Documentation coverage
- Repository health score

All metrics are stored in downloadable artifacts (no email/notifications).

---

## 🔧 Configuration Files

### Main Configuration
**File:** `config/automation-settings.json`
```json
{
  "automation_settings": {
    "silent_mode": {
      "enabled": true,  ← Change to false for all notifications
      ...
    }
  }
}
```

### Workflow Definition
**File:** `.github/workflows/ai-automation.yml`
- Defines all automation jobs
- Scheduled tasks
- Quality checks
- Content sync logic

### Account Details
**File:** `ACCOUNTS_README.md`
- Complete setup guide
- Security best practices
- Integration instructions
- Troubleshooting tips

---

## 🔐 Security Setup

### Required Secrets (Optional Integrations)
Go to: Repository Settings → Secrets and Variables → Actions

Add these only if you want to enable external integrations:
- `DISCORD_WEBHOOK` - For Discord notifications
- `GOOGLE_API_KEY` - For Google Workspace sync
- `ZAPIER_WEBHOOK` - For Zapier automations
- Platform-specific API keys for social media

**Note:** GitHub automation works without any additional secrets.

---

## 📈 Typical Daily Workflow

### Your Part (No Change)
1. Write/edit game content
2. Commit and push changes
3. Continue working

### Automation's Part (Silent)
1. Detects your push
2. Runs quality checks
3. Calculates metrics
4. Updates progress tracking
5. Archives reports
6. **Doesn't notify you** (unless errors)

---

## 🆘 Troubleshooting

### Automation Not Running?
1. Check Actions tab for errors
2. Verify workflow is enabled
3. Check branch name (must be main/develop)
4. Review workflow permissions

### Want to Enable Notifications?
Edit `config/automation-settings.json`:
```json
"notification_levels": {
  "routine_commits": true,  ← Change to true
  "content_updates": true,  ← Change to true
  ...
}
```

### Want to Disable Silent Mode?
Edit `config/automation-settings.json`:
```json
"silent_mode": {
  "enabled": false  ← Change to false
}
```

### Add External Account Integration?
1. Get API key/webhook from service
2. Add to GitHub Secrets
3. Enable in `config/automation-settings.json`
4. Automation picks it up automatically

---

## 📚 Documentation Index

| Document | Purpose |
|----------|---------|
| `ACCOUNTS_README.md` | Complete automation setup guide |
| `docs/AUTOMATION_GUIDE.md` | Integration ideas and workflows |
| `config/automation-settings.json` | Automation configuration |
| `.github/workflows/ai-automation.yml` | Workflow definition |
| This file | Quick reference for you |

---

## 💡 Pro Tips

1. **Check artifacts regularly** to see automated progress reports
2. **Silent mode is default** - you won't get pestered with notifications
3. **All integrations are optional** - GitHub automation works standalone
4. **Customize freely** - edit `automation-settings.json` to your preferences
5. **Security first** - never commit credentials, always use Secrets

---

## 🎊 Summary

✅ **Automation is active** - Running silently in the background  
✅ **Progress tracked** - Metrics and reports generated automatically  
✅ **Quality checks** - Code validated on every push  
✅ **Zero noise** - Only critical notifications reach you  
✅ **Fully customizable** - Adjust settings anytime  

Your development experience stays the same, but now you have automated:
- Progress tracking
- Quality assurance
- Metrics collection
- Inter-account syncing (when enabled)

**You focus on creating. Automation handles the rest. Silently.**

---

*Last Updated: 2025-11-25*  
*Questions? Check ACCOUNTS_README.md or create a GitHub issue.*
