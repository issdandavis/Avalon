# PROJECT AUTOMATION & INTEGRATION GUIDE
## For Polly's Wingscroll / Spiral of Pollyoneth

This document outlines how to automate and integrate various tools to streamline game development and publishing.

> **NEW:** For comprehensive inter-account automation setup, see [ACCOUNTS_README.md](../ACCOUNTS_README.md)  
> **Configuration:** Automation settings are in `config/automation-settings.json`  
> **Workflows:** GitHub Actions workflows are in `.github/workflows/ai-automation.yml`

---

## 🤖 AI-POWERED INTER-ACCOUNT AUTOMATION (NEW)

### Silent Automation System
The repository now includes automated workflows that handle inter-account communications without user notifications:

**Automated Tasks (Silent Mode):**
- ✅ Development progress tracking
- ✅ Content synchronization across platforms
- ✅ Quality checks and validation
- ✅ Metrics collection and reporting
- ✅ Daily maintenance and cleanup

**User Notifications Only For:**
- ❗ Build failures
- ❗ Security alerts
- ❗ Major releases
- ❗ Critical errors

### Quick Setup
1. Review `config/automation-settings.json` for preferences
2. Add required secrets in GitHub Settings → Secrets
3. Enable workflows in Actions tab
4. Automation runs automatically (silent by default)

For complete setup instructions, see [ACCOUNTS_README.md](../ACCOUNTS_README.md#-quick-setup-guide).

---

## 🔌 ZAPIER AUTOMATION IDEAS

### When Zapier Connects, Set Up These Workflows:

#### 1. **Writing & Content Management**
- **Google Docs → GitHub:** Auto-commit lore updates to repository
- **Notion → Game Files:** Update ChoiceScript scenes from writing database
- **Discord/Slack → GitHub Issues:** Community feedback becomes tracked tasks

#### 2. **Game Development Workflow**
- **GitHub Push → Discord:** Notify when new game content is committed
- **ChoiceScript Test → Trello/Asana:** Create tasks for bugs found
- **Google Sheets → Game Stats:** Update stat balancing from spreadsheet

#### 3. **Publishing & Distribution**
- **GitHub Release → Twitter/Social:** Auto-announce new versions
- **Hosted Games Submission → Email:** Track submission status
- **Beta Feedback Form → Google Sheets:** Collect playtester data

#### 4. **Community & Marketing**
- **New Game Update → MailChimp:** Notify email list
- **Reddit/Forum Post → Archive:** Save community discussions
- **Ko-fi/Patreon → Thank You Email:** Automated supporter thanks

---

## 📊 SUGGESTED TOOL STACK

### **Writing & Lore Management:**
- **Google Docs** - Collaborative lore writing
- **Notion** - Database of characters, locations, magic systems
- **GitHub** - Version control for all game files

### **Project Management:**
- **Trello/Asana** - Task tracking
- **GitHub Projects** - Development roadmap
- **Discord** - Community & beta testing

### **Game Development:**
- **ChoiceScript IDE** - Game engine
- **Visual Studio Code** - Advanced editing
- **CSIDE** - Online ChoiceScript editor

### **Testing & Analytics:**
- **Google Forms** - Beta tester feedback
- **Google Sheets** - Stat balancing, bug tracking
- **Discord** - Beta tester community

### **Publishing:**
- **Hosted Games** - App store publication
- **Itch.io** - Web version distribution
- **GitHub Pages** - Demo hosting

---

## 🤖 AUTOMATION WORKFLOWS TO CREATE

### **Workflow 1: Content Update Pipeline**
```
Lore Document Updated (Google Docs)
  ↓
Zapier Detects Changes
  ↓
Updates GitHub Repository
  ↓
Notifies Discord Channel
  ↓
Creates Task in Project Manager
```

### **Workflow 2: Bug Tracking**
```
Playtester Submits Bug (Google Form)
  ↓
Zapier Captures Submission
  ↓
Creates GitHub Issue
  ↓
Adds to Bug Tracking Sheet
  ↓
Notifies Development Team (Discord/Email)
```

### **Workflow 3: Release Process**
```
New Version Tagged in GitHub
  ↓
Zapier Triggers Release Workflow
  ↓
Posts to Social Media (Twitter, Reddit)
  ↓
Sends Email to Subscriber List
  ↓
Updates Website/Itch.io Page
```

### **Workflow 4: Community Engagement**
```
Player Feedback Received (Discord/Forum)
  ↓
Zapier Captures & Categorizes
  ↓
High-Priority → GitHub Issue
  ↓
General Feedback → Database
  ↓
Weekly Summary Email to Team
```

---

## 📋 PROJECT ORGANIZATION STRUCTURE

### **Recommended Folder Structure:**
```
Avalon/
├── lore/                    # All worldbuilding documents
│   ├── geography.md
│   ├── characters.md
│   ├── magic_systems.md
│   └── timeline.md
│
├── game/                    # HTML version (current)
│   ├── index.html
│   ├── style.css
│   └── game.js
│
├── choicescript_game/       # ChoiceScript version (for publishing)
│   ├── startup.txt
│   └── scenes/
│
├── docs/                    # Documentation
│   ├── automation_guide.md  # This file
│   ├── publishing_guide.md
│   └── beta_testing_guide.md
│
├── assets/                  # Images, music, etc.
│   ├── images/
│   └── audio/
│
└── releases/                # Published versions
    ├── v1.0/
    └── beta/
```

---

## 🎯 INTEGRATION POINTS FOR ZAPIER

### **When Setting Up Zapier, Connect:**

1. **GitHub Repository**
   - Trigger: New push to main branch
   - Trigger: New release created
   - Trigger: Issue created/commented

2. **Google Workspace**
   - Docs: Lore updates
   - Sheets: Stat balancing, bug tracking
   - Forms: Playtester feedback

3. **Communication**
   - Discord: Team notifications
   - Email: Subscriber updates
   - Slack: Internal team chat & real-time collaboration
     - Join: https://join.slack.com/shareDM/zt-3jpuiis8k-UsZfwP3zVm~MDxKmn1XbKA
     - See [COMMUNICATION_CHANNELS.md](../COMMUNICATION_CHANNELS.md) for all options

4. **Social Media**
   - Twitter: Release announcements
   - Reddit: Community updates
   - Facebook: Fan page updates

5. **Project Management**
   - Trello: Task boards
   - Asana: Project timeline
   - GitHub Projects: Development roadmap

---

## 🚀 QUICK START AUTOMATION (Priority Order)

### **Phase 1: Essential Automation**
1. ✅ GitHub → Discord (new commits notification)
2. ✅ Google Form → Google Sheet (bug tracking)
3. ✅ GitHub Release → Social Media (announcements)

### **Phase 2: Content Pipeline**
4. ⏳ Google Docs → GitHub (lore updates)
5. ⏳ Notion → ChoiceScript (content sync)
6. ⏳ Feedback Form → GitHub Issues

### **Phase 3: Advanced Automation**
7. ⏳ Analytics → Dashboard (player stats)
8. ⏳ Community Posts → Archive (discussion backup)
9. ⏳ Automated testing triggers

---

## 💡 ZAPIER RECIPE TEMPLATES

### **Recipe 1: New Commit Notification**
```
Trigger: GitHub - New Push to Branch
Filter: Branch = "main"
Action: Discord - Send Channel Message
Message: "🎮 New update pushed to Polly's Wingscroll!"
```

### **Recipe 2: Bug Report Processing**
```
Trigger: Google Forms - New Response
Action 1: Google Sheets - Create Spreadsheet Row
Action 2: GitHub - Create Issue
Action 3: Discord - Send Message
```

### **Recipe 3: Release Announcement**
```
Trigger: GitHub - New Release
Action 1: Twitter - Create Tweet
Action 2: Discord - Send Announcement
Action 3: Email - Send to Subscriber List
```

---

## 📱 MOBILE WORKFLOW

**For working on-the-go:**
- Mobile app: Working Copy (Git client for iOS)
- Mobile app: Editorial (Markdown editor)
- Mobile app: Discord (team communication)
- Zapier mobile app for monitoring automations

---

## 🔐 SECURITY BEST PRACTICES

**When connecting services:**
- Use API tokens, never passwords
- Set minimum required permissions
- Regularly audit connected apps
- Use 2FA on all accounts
- Keep backup access codes safe

---

## 📈 METRICS TO TRACK (with automation)

**Automatically track:**
- Downloads/plays per version
- Completion rates by path
- Most popular choices
- Average playtime
- Bug report frequency
- Community engagement stats

**Tools to use:**
- Google Analytics (web version)
- Hosted Games dashboard (app version)
- Discord bot analytics
- GitHub insights

---

## ⚙️ SETUP CHECKLIST

**Before enabling automations:**
- [ ] Connect GitHub repository
- [ ] Set up Google Workspace
- [ ] Create Discord server/channels
- [ ] Initialize project management tool
- [ ] Configure notification preferences
- [ ] Test each Zap individually
- [ ] Document custom workflows
- [ ] Train team on new systems

---

## 🆘 TROUBLESHOOTING

**Common issues:**
- **Zap not triggering:** Check permissions and filters
- **Duplicate notifications:** Review trigger settings
- **Missing data:** Verify field mappings
- **Rate limits:** Adjust polling frequency

---

## 📚 RESOURCES

**Zapier Templates:**
- https://zapier.com/apps/github/integrations
- https://zapier.com/apps/discord/integrations
- https://zapier.com/apps/google-docs/integrations

**Documentation:**
- ChoiceScript forums: https://forum.choiceofgames.com/
- GitHub Actions: https://docs.github.com/actions
- Discord webhooks: https://discord.com/developers/docs

---

## 🎊 RECOMMENDED FIRST ZAP

**Start simple with this automation:**

**"New Game Update Notifier"**
1. Trigger: GitHub push to main branch
2. Action: Post to Discord channel
3. Message: "New game content added! Check it out: [commit link]"

This gives immediate value and helps you learn the system!

---

*This guide will be updated as new integrations are added.*
*Last updated: [Auto-generated timestamp]*
