# Contributing to Polly's Wingscroll

Welcome! This guide is for both human contributors and AI assistants working on this project.

---

## Quick Start

1. **Read the docs:** Start with `docs/AI_SESSION_HANDOFF.md` for full context
2. **Understand the goal:** Create a publishable choice-based game for Hosted Games
3. **Check current status:** See `docs/PROJECT_ROADMAP.md` for what's done and what's next

---

## For AI Assistants (Claude, etc.)

### Starting a New Session

1. Read `docs/AI_SESSION_HANDOFF.md` first
2. Check `docs/PROJECT_ROADMAP.md` for current phase
3. Review recent commits: `git log --oneline -10`
4. Look at `docs/NEXT_TASKS.md` for prioritized work

### Branch Naming Convention
```
claude/[descriptive-task]-[session-id]
```

### Before Finishing a Session

1. Commit all work with descriptive messages
2. Update `docs/AI_SESSION_HANDOFF.md` with:
   - Work completed
   - Session ID in history table
   - Any new information
3. Update `docs/NEXT_TASKS.md` if priorities changed
4. Push to branch and create PR

### Key Principle
The HTML version (`game/game.js`) is the complete reference. ChoiceScript version should port that content with proper formatting.

---

## For Human Contributors

### Areas to Help

**Writing:**
- Proofread game text
- Expand Polly's commentary
- Add flavor text variations
- Write additional endings

**Testing:**
- Play through all paths
- Report bugs
- Balance feedback
- Accessibility testing

**Technical:**
- ChoiceScript optimization
- Bug fixes
- Feature implementation

**Art & Design:**
- Game icon/logo
- Promotional materials
- UI improvements

### Getting Started

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Test locally (see below)
5. Submit a pull request

### Testing Locally

**HTML Version:**
```bash
# Just open in browser
open game/index.html
```

**ChoiceScript Version:**
1. Download ChoiceScript from choiceofgames.com
2. Copy `choicescript_game/` contents to `web/mygame/`
3. Open ChoiceScript `index.html`

---

## Project Structure

```
Avalon/
├── game/                  # HTML version (complete)
├── choicescript_game/     # ChoiceScript (in progress)
├── docs/                  # Documentation
│   ├── AI_SESSION_HANDOFF.md
│   ├── PROJECT_ROADMAP.md
│   ├── AUTOMATION_GUIDE.md
│   └── NEXT_TASKS.md
├── QUICK_START.md         # Player guide
└── CONTRIBUTING.md        # This file
```

---

## Code Style

### ChoiceScript
- Use consistent indentation (2 spaces)
- Comment complex logic with `*comment`
- Label names: `snake_case`
- Keep choices to 2-4 options typically

### General
- Maintain Polly's sarcastic voice
- Keep text readable on mobile (shorter paragraphs)
- Test all new paths thoroughly

---

## Commit Messages

Use clear, descriptive commit messages:

```
Add Singing Dunes truth-testing scene
Fix stat tracking in first lesson
Update documentation with new endpoints
```

---

## Questions?

- Check existing documentation
- Review similar code in the project
- Ask in a GitHub issue

---

*"Every contribution weaves another thread in the spiral."*
