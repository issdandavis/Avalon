# 🔌 How to Use the Codex Connector

## What is the Codex Connector?

The **Codex Connector** is the multi-AI collaboration system that enables different AI assistants to work together seamlessly on **The Avalon Codex** project. Think of it as a "handoff protocol" that lets multiple AIs coordinate without stepping on each other's work.

**💡 Want to see it in action?** → [CODEX_CONNECTOR_EXAMPLE.md](CODEX_CONNECTOR_EXAMPLE.md) - Real workflow example

---

## 🚀 Quick Start (30 seconds)

### For Users
**Want AIs to collaborate on your project?**

1. **Share these files** with any AI you're working with:
   - `STATUS_CONTEXT.md` - Current work status
   - `SCENE_PARITY_CHECKLIST.md` - What's done vs. what's needed
   - `STATS_MATRIX.md` - How choices affect gameplay

2. **Tell the AI their role:**
   - "You're the Lore Curator" → validates story consistency
   - "You're the Conversion Engineer" → converts HTML to ChoiceScript
   - "You're the Structural Reviewer" → checks completeness
   - "You're the Quality Balancer" → tunes game difficulty

3. **Let them work!** Each AI will:
   - Check the status files
   - Do their specialized task
   - Update the shared files
   - Hand off to the next AI

**That's it!** The system handles the rest.

---

## 👥 For AI Assistants

### First Time Working on Avalon?

**Read these in order:**
1. ✅ This file (you're here!)
2. ✅ `STATUS_CONTEXT.md` - What's happening now
3. ✅ `SCENE_PARITY_CHECKLIST.md` - What needs work
4. ✅ `MULTI_AI_COLLABORATION_GUIDE.md` - Full details

### Continuing Previous Work?

**Quick checks:**
1. Update `STATUS_CONTEXT.md` with your session info
2. Find your role's checklist section
3. Work on your task
4. Update the shared files as you go

---

## 🎭 The Five Roles

### 1. 🎨 Lore Curator
**You validate story consistency**

**Files you care about:**
- `lore/` directory (all worldbuilding)
- `writing_drafts/IZACK_MASTER_CHRONICLE_UPDATED.txt`
- `SCENE_PARITY_CHECKLIST.md`

**Your job:**
- Check new content against established canon
- Flag timeline contradictions
- Ensure character voices are consistent
- Verify magic system rules

**When you're needed:**
- Before converting any scene
- When character dialogue seems off
- If magic usage seems inconsistent

---

### 2. 💻 Conversion Engineer
**You translate HTML to ChoiceScript**

**Files you care about:**
- `game/game.js` (source HTML game)
- `choicescript_game/scenes/*.txt` (target files)
- `SCENE_PARITY_CHECKLIST.md`

**Your job:**
- Convert HTML scenes to ChoiceScript format
- Preserve all choice logic and branching
- Implement proper stat tracking
- Maintain code quality

**When you're needed:**
- Creating new ChoiceScript scenes
- Updating existing scene files
- Technical ChoiceScript questions

---

### 3. 🔍 Structural Reviewer
**You verify completeness**

**Files you care about:**
- `game/game.js` (reference)
- `choicescript_game/scenes/*.txt` (verify these)
- `SCENE_PARITY_CHECKLIST.md`

**Your job:**
- Verify HTML and ChoiceScript versions match
- Check all choice paths go somewhere
- Ensure all 14 endings are reachable
- Validate stat progression

**When you're needed:**
- After Conversion Engineer finishes a scene
- Before marking scenes as "Verified"
- Quality assurance passes

---

### 4. ⚖️ Quality Balancer
**You tune game difficulty**

**Files you care about:**
- `STATS_MATRIX.md` (track all stat changes)
- `choicescript_game/scenes/*.txt`
- `choicescript_game/startup.txt`

**Your job:**
- Track stat modifications across scenes
- Identify imbalanced choices
- Ensure endings are reachable
- Balance difficulty

**When you're needed:**
- After scenes are verified
- When testing reveals stat problems
- Before beta testing

---

### 5. 📋 Automation Planner
**You document workflows**

**Files you care about:**
- `docs/AUTOMATION_GUIDE.md`
- `.github/workflows/*.yml`
- `MULTI_AI_COLLABORATION_GUIDE.md`

**Your job:**
- Update workflow documentation
- Document new content types
- Improve coordination processes

**When you're needed:**
- When new asset types are added
- For process improvements
- When workflows need updating

---

## 🔄 The Workflow

### Standard Scene Conversion
```
1. Lore Curator validates HTML scene
   ↓
2. Conversion Engineer drafts ChoiceScript version
   ↓
3. Structural Reviewer verifies completeness
   ↓
4. Quality Balancer tunes stat values
   ↓
5. Final review and commit
```

### Hand-off Markers
Use these in code comments (remove before final):
```choicescript
*comment TODO:[LORE]: Verify Kael's backstory
*comment TODO:[CONVERT]: Add stat modification
*comment TODO:[STRUCT]: Check path to ending
*comment TODO:[BALANCE]: High stat gain (+25)
```

### Commit Message Prefixes
```
Lore: Verified singing_dunes against desert lore
Convert: Drafted verdant_tithe.txt from HTML
Struct: Verified first_lesson.txt branching
Balance: Adjusted collaboration gains
Auto: Updated AUTOMATION_GUIDE.md
```

---

## 📋 The Shared Context Files

### STATUS_CONTEXT.md
**What is it?** Weekly snapshot of current work

**Update when:**
- Starting a new session
- Switching AI roles
- Completing a milestone

**Contains:**
- Current scene being worked on
- Pending lore updates
- Recent completions
- Next steps

---

### SCENE_PARITY_CHECKLIST.md
**What is it?** HTML vs. ChoiceScript alignment tracker

**Update when:**
- Starting scene conversion (mark 🚧 Draft)
- Completing conversion (mark ✅ Verified)
- Finding discrepancies

**Contains:**
- Scene-by-scene status
- Verification checklist per scene
- Notes on deviations

---

### STATS_MATRIX.md
**What is it?** Choice impact tracking

**Update when:**
- Extracting stats from a scene
- Balancing stat values
- Testing progression

**Contains:**
- Table of stat-modifying choices
- Balance analysis
- Recommended thresholds

---

## 🎯 Common Scenarios

### "I want to convert a scene to ChoiceScript"
1. ✅ Lore Curator validates source scene
2. ✅ You (Conversion Engineer) draft ChoiceScript
3. ✅ Structural Reviewer verifies it
4. ✅ Quality Balancer checks stats
5. ✅ Update all relevant checklists

### "I found a lore inconsistency"
1. ✅ Document it in `STATUS_CONTEXT.md`
2. ✅ Reference specific files/line numbers
3. ✅ Propose resolution based on canon
4. ✅ Update `SCENE_PARITY_CHECKLIST.md`
5. ✅ Wait for Lore Curator approval

### "Stats feel unbalanced"
1. ✅ Extract all values to `STATS_MATRIX.md`
2. ✅ Test multiple playthroughs
3. ✅ Calculate min/max possible stats
4. ✅ Propose adjusted values
5. ✅ Document reasoning

### "I don't know what to work on"
1. ✅ Read `STATUS_CONTEXT.md` for priorities
2. ✅ Check `SCENE_PARITY_CHECKLIST.md` for 🚧 or ❌ items
3. ✅ Review `STATS_MATRIX.md` for incomplete data
4. ✅ Pick a task matching your expertise
5. ✅ Update `STATUS_CONTEXT.md` with your choice

---

## ✅ Quality Checklist

### Before Marking Scene Complete
- [ ] Scene count matches HTML source
- [ ] All choices lead somewhere (no dead ends)
- [ ] Stat changes documented in `STATS_MATRIX.md`
- [ ] No new lore contradictions
- [ ] Polly's voice is consistent
- [ ] No TODO markers remain
- [ ] Checklists updated
- [ ] Status file reflects completion

---

## 🤖 Model Selection Tips

### Creative/Lore Tasks
**Use:** Claude, GPT-4 (creative), Gemini
- Lore Curator role
- Character consistency
- Magic system validation

### Code/Technical Tasks
**Use:** GitHub Copilot, Codeium, CodeLlama
- Conversion Engineer role
- ChoiceScript syntax
- Bug fixing

### Cross-File Analysis
**Use:** Cursor, Continue, Sourcegraph Cody
- Structural Reviewer role
- Finding stat references
- Scene comparison

### Balanced General Work
**Use:** GPT-4, Claude (balanced)
- Quality Balancer role
- Documentation
- Planning

---

## 🔗 Related Documentation

### Essential Reading
- **`MULTI_AI_COLLABORATION_GUIDE.md`** - Complete detailed guide
- **`STATUS_CONTEXT.md`** - Current project state
- **`SCENE_PARITY_CHECKLIST.md`** - What's done
- **`STATS_MATRIX.md`** - Stat tracking

### Reference Materials
- **`README.md`** - Project overview
- **`START_HERE.md`** - Quick orientation
- **`.github/copilot-instructions.md`** - AI coding guidelines
- **`docs/PROJECT_ROADMAP.md`** - Development phases

### For Users
- **`AGENT_START_HERE.md`** - Managing AI workers
- **`docs/AUTOMATION_GUIDE.md`** - Integration workflows

---

## 💡 Pro Tips

### DO:
✅ Update `STATUS_CONTEXT.md` at session start/end
✅ Use role-specific commit prefixes
✅ Cross-reference lore before changes
✅ Mark scenes in checklists as you work
✅ Test your changes when possible
✅ Ask other roles for review

### DON'T:
❌ Make lore changes without Lore Curator review
❌ Skip updating checklists
❌ Leave TODO markers in verified code
❌ Work in isolation - use the coordination files
❌ Commit without descriptive messages
❌ Break working scenes

---

## 🆘 Getting Help

### Stuck on Lore?
→ Check `lore/` directory
→ Reference `writing_drafts/IZACK_MASTER_CHRONICLE_UPDATED.txt`
→ Look at HTML game implementation

### Stuck on Technical?
→ Check ChoiceScript documentation
→ Review `choicescript_game/scenes/first_lesson.txt`
→ Compare to `game/game.js`

### Stuck on What to Do?
→ Read `STATUS_CONTEXT.md`
→ Look for ❌ or 🚧 in `SCENE_PARITY_CHECKLIST.md`
→ Check `STATS_MATRIX.md` for incomplete data

---

## 🎉 Success Indicators

### You're Using It Right When:
✅ Status file is always current
✅ Checklists update after every change
✅ Commits have descriptive prefixes
✅ Other AIs can pick up your work easily
✅ Lore stays consistent
✅ Stats balance across scenes
✅ No knowledge lost between sessions

---

## 📞 Support

**For Users:**
- See `AGENT_START_HERE.md` for managing AI workers
- Check `README.md` for project overview

**For AI Assistants:**
- Read `MULTI_AI_COLLABORATION_GUIDE.md` for full details
- Review `docs/AI_SESSION_HANDOFF.md` for session continuity

**Repository:** https://github.com/issdandavis/Aethromoor
**Maintainer:** @issdandavis

---

**The Codex Connector enables seamless multi-AI collaboration.**
*"Many voices, one story. The Avalon Codex continues through coordination."*

**Last Updated:** December 9, 2025
