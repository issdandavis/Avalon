# ISDanDavis Connected Accounts & Automation System

## Overview
This document describes the connected accounts ecosystem for the Avalon/Spiral of Pollyoneth project and the automated communication workflows between them.

> **🤖 NEW: AI Inbox Management System**  
> Automated email and GitHub notification management with AI-powered auto-replies and categorization.  
> **Quick Start:** See [AI Employees Guide](docs/AI_EMPLOYEES_GUIDE.md)  
> **Full Documentation:** See [Inbox Management Guide](docs/INBOX_MANAGEMENT.md)

---

## 🔗 Connected Accounts

### Primary Account
- **GitHub:** [@issdandavis/Avalon](https://github.com/issdandavis/Avalon)
  - **Purpose:** Main repository for game development, lore, and automation
  - **Automation Role:** Central hub for all automated workflows
  - **Access Level:** Full control

### Development & Publishing
- **Hosted Games Account**
  - **Purpose:** App store publication platform
  - **Automation Role:** Receives automated submission updates
  - **Access Level:** Publishing

- **GitHub Pages**
  - **Purpose:** Web demo hosting
  - **Automation Role:** Auto-deploy on main branch updates
  - **Access Level:** Automated deployment

### Content Management
- **Google Workspace** (if configured)
  - **Google Docs:** Collaborative lore writing
  - **Google Sheets:** Stat balancing, bug tracking
  - **Google Forms:** Playtester feedback collection
  - **Automation Role:** Content sync to repository
  - **Access Level:** Read/Write via API

- **Notion** (optional)
  - **Purpose:** Character/location database
  - **Automation Role:** Structured content export
  - **Access Level:** Read via API

### Communication & Community
- **Discord Server** (if configured)
  - **Purpose:** Development updates, community engagement
  - **Automation Role:** Receives commit notifications, release announcements
  - **Access Level:** Webhook integration

- **Social Media Accounts** (if configured)
  - **Twitter/X:** Release announcements
  - **Reddit:** Community updates
  - **Automation Role:** Automated post generation
  - **Access Level:** API posting

### Project Management
- **GitHub Projects**
  - **Purpose:** Development roadmap tracking
  - **Automation Role:** Auto-update from commits and issues
  - **Access Level:** Full integration

- **Trello/Asana** (optional)
  - **Purpose:** Task management
  - **Automation Role:** Issue sync from GitHub
  - **Access Level:** Read/Write via API

---

## 🤖 AI Automation Architecture

### Automation Layers

#### Layer 1: GitHub Actions (Infrastructure)
- **Location:** `.github/workflows/`
- **Triggers:** Push, PR, Release, Schedule
- **Purpose:** Core automation infrastructure
- **Silent Mode:** ✅ Runs without user notifications

#### Layer 2: AI Communication Hub
- **Location:** `.github/workflows/ai-automation.yml`
- **Purpose:** Inter-account data synchronization
- **Features:**
  - Automated content updates
  - Cross-platform posting
  - Progress tracking
  - Error recovery
- **Silent Mode:** ✅ Configured for background operation

#### Layer 3: AI Inbox Management (NEW)
- **Location:** `.github/workflows/inbox-management.yml`
- **Purpose:** Automated inbox and email management
- **Features:**
  - Auto-reply to all GitHub notifications
  - Smart categorization and labeling
  - Multi-account synchronization
  - Email integration support
  - Scheduled inbox monitoring
- **AI Employees:** 5 specialized agents working 24/7
- **Documentation:** [AI Employees Guide](docs/AI_EMPLOYEES_GUIDE.md)

#### Layer 4: Integration Services
- **Zapier/Make/n8n:** External automation platform
- **Purpose:** Complex multi-service workflows
- **Silent Mode:** ✅ Configured to suppress non-critical notifications

---

## 📊 Automated Communication Workflows

### Workflow 1: AI Inbox Management (NEW)
```
GitHub Notification → AI Categorization → Auto-Reply
├── Analyze content and priority
├── Send automated acknowledgment
├── Apply smart labels
├── Update project board
└── Track in unified inbox

Schedule: Every 6 hours + on-demand
AI Agents: 5 specialized agents
Documentation: docs/INBOX_MANAGEMENT.md
```
**User Notifications:** Auto-replies to users; silent admin operation

### Workflow 2: Development Progress Sync
```
GitHub Commit → Actions Workflow → Multi-Account Update
├── Update GitHub Projects board
├── Log to Google Sheets (if configured)
├── Post to Discord (silent channel, if configured)
└── Update internal progress tracker
```
**User Notifications:** None (silent operation)

### Workflow 2: Content Pipeline
```
Lore Update (Docs) → Detection → Repository Sync
├── Check for changes in lore documents
├── Auto-commit to designated branch
├── Create PR for review (optional)
└── Update changelog
```
**User Notifications:** None for routine updates

### Workflow 3: Release Automation
```
Version Tag → Release Workflow → Multi-Platform Deploy
├── Build release artifacts
├── Update GitHub Release notes
├── Deploy to GitHub Pages
├── Post to social media (if configured)
└── Email subscriber list (if configured)
```
**User Notifications:** Only for major releases

### Workflow 4: Community Engagement
```
Issue/PR Created → Analysis → Automated Response
├── Label classification
├── Template response (if applicable)
├── Assign to project board
└── Log metrics
```
**User Notifications:** Standard GitHub notifications only

### Workflow 5: Content Quality Checks
```
Scene Update → Validation → Report
├── ChoiceScript syntax check
├── Word count tracking
├── Link validation
├── Stat consistency check
└── Generate quality report
```
**User Notifications:** None (reports stored in artifacts)

---

## 🔧 Configuration Files

### Primary Configuration
- **File:** `.github/workflows/ai-automation.yml`
- **Purpose:** Main automation orchestration
- **Secrets Required:**
  - `GITHUB_TOKEN` (automatic)
  - `DISCORD_WEBHOOK` (optional)
  - `GOOGLE_API_KEY` (optional)
  - `ZAPIER_WEBHOOK` (optional)

### Environment Variables
- **File:** `config/.env.example`
- **Setup:** Copy to `config/.env` and populate
- **Never Commit:** `.env` is gitignored for security

### Automation Settings
- **File:** `config/automation-settings.json`
- **Purpose:** Fine-tune automation behavior
- **Key Settings:**
  - Notification thresholds
  - Sync frequencies
  - Silent mode toggles
  - Error handling preferences

---

## 📋 Account Access Matrix

| Account/Service | Access Method | Required Secrets | Auto-Sync | Silent Mode |
|----------------|---------------|------------------|-----------|-------------|
| GitHub | Native | `GITHUB_TOKEN` | ✅ | ✅ |
| GitHub Pages | Deploy Action | `GITHUB_TOKEN` | ✅ | ✅ |
| Discord | Webhook | `DISCORD_WEBHOOK` | ✅ | ✅ |
| Google Workspace | API | `GOOGLE_API_KEY` | ✅ | ✅ |
| Hosted Games | Manual | N/A | ❌ | N/A |
| Social Media | API | Platform-specific | ⏳ | ✅ |
| Zapier | Webhook | `ZAPIER_WEBHOOK` | ✅ | ✅ |

---

## 🚀 Quick Setup Guide

### Step 1: Configure Secrets
1. Navigate to Repository Settings → Secrets and Variables → Actions
2. Add required secrets:
   ```
   DISCORD_WEBHOOK=https://discord.com/api/webhooks/...
   GOOGLE_API_KEY=your_key_here
   ZAPIER_WEBHOOK=https://hooks.zapier.com/...
   ```

### Step 2: Enable Workflows
1. Review `.github/workflows/ai-automation.yml`
2. Customize notification preferences
3. Enable workflow in Actions tab

### Step 3: Configure Silent Mode
1. Edit `config/automation-settings.json`
2. Set notification levels:
   ```json
   {
     "notifications": {
       "routine_commits": false,
       "content_updates": false,
       "build_success": false,
       "build_failure": true,
       "releases": true
     }
   }
   ```

### Step 4: Test Automation
1. Make a test commit to a feature branch
2. Verify workflows execute silently
3. Check automated updates in connected accounts
4. Review logs in Actions tab

---

## 🔐 Security Best Practices

### Credential Management
- ✅ **DO:** Store all credentials in GitHub Secrets
- ✅ **DO:** Use repository-specific API tokens with minimum permissions
- ✅ **DO:** Rotate credentials quarterly
- ❌ **DON'T:** Commit credentials to repository
- ❌ **DON'T:** Share credentials across multiple projects
- ❌ **DON'T:** Use personal access tokens for automation

### Access Control
- Limit workflow permissions to minimum required
- Use separate service accounts for automations
- Enable 2FA on all connected accounts
- Regular audit of connected applications

### Monitoring
- Review Actions logs weekly
- Set up alerts for authentication failures
- Monitor API rate limits
- Track unusual activity patterns

---

## 📈 Automation Metrics

### Tracked Metrics (Silent)
- Commits per day
- Content word count changes
- Scene completion progress
- Build success rate
- Workflow execution time
- API usage and rate limits

### Reporting
- **Daily:** Internal progress logs (no notifications)
- **Weekly:** Aggregated metrics (silent report)
- **Monthly:** Comprehensive analytics (optional notification)
- **On-Demand:** Query via GitHub Actions artifacts

---

## 🛠️ Maintenance

### Regular Tasks
- **Weekly:** Review automation logs for errors
- **Monthly:** Update dependencies in workflows
- **Quarterly:** Audit connected accounts and permissions
- **Annually:** Rotate all API keys and credentials

### Troubleshooting
- Check Actions logs: Repository → Actions tab
- Review workflow YAML syntax
- Verify secret availability
- Test webhooks with curl/Postman
- Check rate limits on external services

---

## 📞 Support & Resources

### Documentation
- [GitHub Actions Docs](https://docs.github.com/actions)
- [Zapier Integration Guide](../docs/AUTOMATION_GUIDE.md)
- [ChoiceScript Testing](../choicescript_game/README.md)

### Templates
- Workflow templates in `.github/workflows/`
- Zapier recipes in `docs/AUTOMATION_GUIDE.md`
- Configuration examples in `config/`

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-25 | Initial setup with silent automation infrastructure |

---

*Last Updated: 2025-11-25*
*Maintained by: Automated system with manual oversight*
