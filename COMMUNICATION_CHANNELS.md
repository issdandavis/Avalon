# Communication Channels
**Project:** The Avalon Codex / Polly's Wingscroll: The First Thread  
**Last Updated:** December 8, 2025

This document serves as the central reference for all project communication methods and integration points.

---

## 🎯 COMMUNICATION PHILOSOPHY

**Primary Principle:** All critical decisions and work artifacts live in GitHub for transparency, version control, and AI agent accessibility.

**Secondary Channels:** Support human collaboration and real-time discussion, but sync important outcomes back to GitHub.

---

## 📱 ACTIVE COMMUNICATION CHANNELS

### 1. GitHub (Primary - AI Accessible)

**Repository:** [issdandavis/Aethromoor](https://github.com/issdandavis/Aethromoor)

#### Issues
- **Purpose:** Task tracking, bug reports, feature requests
- **Best For:** Concrete, actionable work items
- **AI Access:** ✅ Full read/write via GitHub Copilot
- **Response Time:** Within 48 hours for new issues

**How to Use:**
```
Good Issue: "Add Verdant Tithe expedition - forest scenes"
- Clear objective
- Links to roadmap
- Lists acceptance criteria

Poor Issue: "Make game better"
- Too vague
- No context
- No success criteria
```

#### Pull Requests
- **Purpose:** Code review, proposed changes
- **Best For:** All code, documentation, and content changes
- **AI Access:** ✅ Auto-review system active
- **Features:** Auto-fix, auto-merge (risk-based)

**Workflow:**
```
1. Create PR with descriptive title
2. Auto-review runs (syntax, security, style)
3. Auto-fix applies corrections if needed
4. Risk assessment determines merge path:
   - LOW: Auto-merge (docs, lore)
   - MEDIUM: Auto-merge after validation (game content)
   - HIGH: Manual review required (workflows, core scripts)
```

#### Discussions
- **Purpose:** Long-form planning, brainstorming, Q&A
- **Best For:** Open-ended topics, community engagement
- **AI Access:** ✅ Can read and respond
- **Categories:** Ideas, Q&A, Show & Tell, Roadmap Planning

#### GitHub Actions
- **Purpose:** Automated workflows, CI/CD
- **Status:** See [WORKFLOW_STATUS.md](WORKFLOW_STATUS.md)
- **Active Workflows:**
  - Auto-review-fix-merge
  - Inbox management (scheduled)
  - AI autonomous tasks

---

### 2. Slack (Human Collaboration)

**Status:** Available for direct messaging  
**AI Access:** ❌ Not directly accessible by AI agents

#### Direct Message Link
Use this link to start a direct message with @issdandavis:
```
https://join.slack.com/shareDM/zt-3jpuiis8k-UsZfwP3zVm~MDxKmn1XbKA
```

#### Best Use Cases
- Quick questions and clarifications
- Real-time brainstorming
- Urgent coordination
- Human-to-human planning

#### ⚠️ Important Note for AI Collaboration
AI coding agents (GitHub Copilot, etc.) **cannot directly access Slack**. For AI-assisted work:

1. **Discuss in Slack** (humans only)
2. **Document decisions in GitHub** (create issue/PR)
3. **AI agents see GitHub activity** and can assist

**Example Workflow:**
```
You (Slack): "Should we add voice acting to the game?"
Team (Slack): "Yes! Let's plan it."
↓
You (GitHub): Create issue "Plan voice acting integration"
                - Reference Slack discussion
                - List requirements
                - Tag for AI assistance
↓
AI Agent (GitHub): Comments with implementation plan
                    - Technical requirements
                    - File structure
                    - Integration points
```

---

### 3. Zapier Integrations (Automation Layer)

**Status:** Configured but not fully activated  
**Documentation:** See [docs/AUTOMATION_GUIDE.md](docs/AUTOMATION_GUIDE.md)

#### Potential Automations

**GitHub → Slack:**
- New PR opened → Slack notification
- Build failure → Alert in Slack
- New release → Announcement

**Slack → GitHub:**
- Message with @github → Create issue
- Discussion with #bug → File bug report
- Decision with #document → Add to discussions

**Setup Required:**
1. Connect Zapier to GitHub (webhook)
2. Connect Zapier to Slack (app installation)
3. Configure triggers and actions
4. Test with low-priority workflows first

**Current Status:** ⏳ Documented but not yet implemented

---

### 4. Email (Asynchronous Updates)

**Purpose:** Low-frequency project updates, subscriber notifications  
**Frequency:** As needed (releases, major milestones)

**Types:**
- Development progress summaries
- Beta testing invitations
- Launch announcements
- Community updates

**Integration Points:**
- GitHub releases → Email announcement
- Milestone completion → Progress update
- Critical issues → Alert notifications

---

## 🔄 INTEGRATION WORKFLOWS

### Workflow A: Feature Request

```
User (Any Channel):
    "I want feature X"
    ↓
Create GitHub Issue:
    Title: "Feature: [X]"
    Body: Requirements, use case
    Labels: enhancement, needs-triage
    ↓
AI Agent Review:
    - Adds technical analysis
    - Links to related code
    - Suggests implementation
    ↓
Discussion:
    - GitHub comments (primary)
    - Slack for quick questions
    - Decisions documented in issue
    ↓
Implementation:
    - PR created
    - Auto-review runs
    - Merged (auto or manual)
    ↓
Notification:
    - GitHub: PR merged
    - Slack: Update posted (if configured)
    - Email: In next digest
```

### Workflow B: Bug Report

```
Discovery (Any Channel):
    "Found a bug!"
    ↓
Create GitHub Issue:
    Template: Bug report
    Labels: bug, needs-triage
    Include: Steps to reproduce
    ↓
Triage:
    - Severity assessment
    - Priority assignment
    - Assign to milestone
    ↓
Fix:
    - PR with bug fix
    - Auto-review validation
    - Test verification
    ↓
Close:
    - Link to fix PR
    - Update changelog
    - Notify reporter
```

### Workflow C: Content Generation

```
Planning (Slack/GitHub):
    "We need to create expedition scenes"
    ↓
Create GitHub Issue:
    Reference: docs/PROJECT_ROADMAP.md
    Lists: Specific scenes needed
    Links: Related lore documents
    ↓
AI-Assisted Creation:
    - Agent generates ChoiceScript
    - Follows game conventions
    - Maintains stat tracking
    ↓
Review:
    - Auto-review syntax
    - Human review narrative
    - Test gameplay paths
    ↓
Merge:
    - Update progress tracker
    - Close issue
    - Update roadmap
```

---

## 📋 COMMUNICATION BEST PRACTICES

### For GitHub Issues

**Do:**
- ✅ Use descriptive titles
- ✅ Include context and requirements
- ✅ Link to relevant documents
- ✅ Add appropriate labels
- ✅ Set clear acceptance criteria

**Don't:**
- ❌ Create duplicate issues (search first)
- ❌ Use vague descriptions
- ❌ Mix multiple requests in one issue
- ❌ Forget to link related PRs

### For Slack Conversations

**Do:**
- ✅ Use threads for organized discussion
- ✅ Document important decisions in GitHub
- ✅ Use @mentions for urgent items
- ✅ Share links to relevant GitHub items

**Don't:**
- ❌ Make critical decisions only in Slack
- ❌ Expect AI agents to see Slack content
- ❌ Use for code review (use GitHub PRs)
- ❌ Store important context only in chat

### For Pull Requests

**Do:**
- ✅ Write clear PR descriptions
- ✅ Reference related issues
- ✅ Respond to review comments
- ✅ Test before requesting review
- ✅ Use conventional commit messages

**Don't:**
- ❌ Submit WIP without draft status
- ❌ Merge without review (unless low-risk)
- ❌ Ignore auto-review feedback
- ❌ Mix unrelated changes

---

## 🤖 AI AGENT INTEGRATION

### What AI Agents Can Do

**GitHub Copilot (Coding Agent):**
- ✅ Read issues, PRs, discussions
- ✅ Create/update code files
- ✅ Run automated reviews
- ✅ Suggest improvements
- ✅ Generate documentation
- ✅ Apply fixes automatically

**Limitations:**
- ❌ Cannot access Slack directly
- ❌ Cannot read email
- ❌ Cannot access external tools (unless API integrated)
- ❌ Cannot make business decisions (needs human input)

### How to Work Effectively with AI Agents

**1. Provide Context in GitHub**
```markdown
Good: "Add Verdant Tithe expedition based on 
       docs/PROJECT_ROADMAP.md Phase 2 requirements.
       Reference game/scenes/verdant_tithe.txt for HTML version.
       Must maintain stat parity with existing expeditions."

Poor: "Add forest stuff"
```

**2. Reference Documentation**
- Link to roadmap, guides, or examples
- Cite specific files or sections
- Provide success criteria

**3. Use Labels Effectively**
- `ai-assisted`: Can be done by AI agent
- `needs-human-review`: Requires human judgment
- `blocked`: Waiting on external input
- `good-first-issue`: Well-defined, clear scope

**4. Iterate with Feedback**
- Review AI-generated code/content
- Provide specific feedback
- Request adjustments as needed

---

## 📊 CHANNEL SELECTION GUIDE

**Use GitHub Issues When:**
- Defining a concrete task
- Tracking a bug
- Requesting a feature
- Need AI assistance
- Want version history

**Use GitHub Discussions When:**
- Brainstorming ideas
- Asking open questions
- Sharing knowledge
- Building community
- Long-form planning

**Use Slack When:**
- Quick questions
- Real-time coordination
- Urgent matters
- Human-only discussion
- Team building

**Use Email When:**
- Broad announcements
- Marketing updates
- Newsletter content
- External communication

**Use Pull Requests When:**
- Proposing any code change
- Updating documentation
- Adding game content
- Modifying workflows
- Need code review

---

## 🔧 SETUP CHECKLIST

### GitHub Configuration
- [x] Repository created
- [x] Auto-review workflow active
- [x] Auto-fix enabled
- [x] Auto-merge configured
- [x] Issue templates created
- [ ] Discussion categories defined
- [ ] Project board set up
- [ ] Milestone planning

### Slack Integration
- [x] Slack workspace identified
- [x] DM link documented
- [ ] Webhook configured (optional)
- [ ] Zapier connection (optional)
- [ ] Notification preferences set

### Automation
- [ ] Zapier account connected
- [ ] GitHub → Slack zaps created
- [ ] Slack → GitHub zaps created
- [ ] Test workflows validated
- [ ] Error handling configured

### Documentation
- [x] This document created
- [x] AUTOMATION_GUIDE.md updated
- [x] PROJECT_ROADMAP.md current
- [ ] CONTRIBUTING.md updated
- [ ] README.md includes comm info

---

## 🆘 TROUBLESHOOTING

### Issue: AI Agent Not Responding
- Check that issue is in GitHub (not Slack)
- Verify issue has clear requirements
- Ensure not labeled `no-auto-review`
- Check Actions tab for workflow runs

### Issue: Slack Integration Not Working
- Verify webhook URL is correct
- Check Zapier connection status
- Test with simple trigger first
- Review Zapier task history for errors

### Issue: Auto-Review Not Running
- Check `.github/workflows/` for workflow files
- Verify repository Actions are enabled
- Check PR doesn't have `manual-review-required` label
- Review workflow logs in Actions tab

### Issue: Communication Confusion
- Clarify which channel for this type of discussion
- Reference this document's selection guide
- Document decision in appropriate channel
- Update this guide if new pattern emerges

---

## 📈 METRICS & MONITORING

**Track These Communication Metrics:**
- Issue response time (target: <48 hours)
- PR review time (target: <24 hours)
- Slack → GitHub conversion rate
- Auto-review success rate
- Community engagement level

**Tools:**
- GitHub Insights (built-in)
- Zapier dashboard (if configured)
- Manual monthly review

---

## 🔄 CONTINUOUS IMPROVEMENT

This document should be updated:
- When new communication channels are added
- When workflows change significantly
- When integration tools are configured
- When best practices evolve
- Quarterly review for accuracy

**Feedback:**
Create a GitHub issue with the label `communication` to suggest improvements to this document.

---

## 📞 QUICK REFERENCE

| Need | Channel | AI Access | Response Time |
|------|---------|-----------|---------------|
| Report Bug | GitHub Issue | ✅ | < 48 hours |
| Request Feature | GitHub Issue | ✅ | < 48 hours |
| Ask Question | GitHub Discussion | ✅ | Variable |
| Quick Chat | Slack DM | ❌ | Immediate |
| Code Review | GitHub PR | ✅ | < 24 hours |
| Urgent Problem | Slack + GitHub | Partial | Immediate |
| Announcement | Email + GitHub | Partial | As scheduled |
| Planning | Slack → GitHub | ❌ then ✅ | Session-based |

---

## ✅ SUMMARY

**Primary Hub:** GitHub (issues, PRs, discussions)  
**Human Collaboration:** Slack (with GitHub sync)  
**AI Assistance:** GitHub only (create issues/PRs)  
**Automation:** Zapier (optional, documented)  
**Updates:** Email (scheduled, infrequent)

**Golden Rule:** If it's important, it lives in GitHub.

---

*For questions about this document, create a GitHub issue with the `documentation` label.*

**Related Documentation:**
- [docs/AUTOMATION_GUIDE.md](docs/AUTOMATION_GUIDE.md) - Automation setup
- [docs/PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md) - Development plan
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [START_HERE.md](START_HERE.md) - Quick orientation
