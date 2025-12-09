# QUICK COLLABORATION REFERENCE
## One-Page Guide for AI Assistants

**🆕 NEW TO THE CODEX CONNECTOR?** → Read [CODEX_CONNECTOR_USAGE.md](CODEX_CONNECTOR_USAGE.md) first!

---

## 🎯 Three Essential Files

1. **STATUS_CONTEXT.md** → What's happening NOW
2. **SCENE_PARITY_CHECKLIST.md** → What's done vs. what's needed
3. **STATS_MATRIX.md** → How choices affect gameplay

---

## 👥 Five AI Roles

| Role | Focus | Primary File | Model Type |
|------|-------|--------------|------------|
| **Lore Curator** | Story consistency | `lore/` | Creative |
| **Conversion Engineer** | HTML → ChoiceScript | `choicescript_game/scenes/` | Code |
| **Structural Reviewer** | Verify parity | SCENE_PARITY_CHECKLIST.md | Codebase-aware |
| **Quality Balancer** | Stat balancing | STATS_MATRIX.md | Analytical |
| **Automation Planner** | Process docs | `docs/AUTOMATION_GUIDE.md` | Any |

---

## 🔄 Standard Workflow

```
1. Lore Curator: ✅ Approve scene
2. Conversion Engineer: Draft ChoiceScript
3. Structural Reviewer: ✅ Verify accuracy
4. Quality Balancer: Balance stats
5. Final Review: ✅ Complete
```

---

## 📋 Scene Status Markers

- ✅ **Verified** - Complete and tested
- 🚧 **Draft** - Exists but needs verification
- 📝 **Partial** - Incomplete
- ❌ **Missing** - Not yet created

---

## 🏷️ Git Commit Prefixes

- `Lore:` - Lore validation/consistency
- `Convert:` - HTML to ChoiceScript conversion
- `Struct:` - Parity verification
- `Balance:` - Stat adjustments
- `Auto:` - Automation/docs

---

## ✅ Pre-Commit Checklist

- [ ] Updated STATUS_CONTEXT.md
- [ ] Updated relevant checklist
- [ ] No TODO markers in verified code
- [ ] Tested if possible
- [ ] Commit message has role prefix

---

## 🚀 Quick Start Actions

### Starting a Session?
1. Read `STATUS_CONTEXT.md`
2. Check your role's checklist section
3. Pick a task
4. Update STATUS_CONTEXT.md with your work

### Ending a Session?
1. Update STATUS_CONTEXT.md with progress
2. Update checklists/matrices
3. Remove TODO markers
4. Commit with prefix
5. Note blockers if any

---

## 📊 Current Priorities (Phase 2)

1. ⚠️ Verify `verdant_tithe.txt` (only 183 lines - seems incomplete)
2. ✅ Test all three expeditions
3. ✅ Verify all 14 endings exist
4. ⚠️ Balance stat requirements

---

## 🎯 The Golden Rules

1. **Always update STATUS_CONTEXT.md**
2. **Lore Curator approves story changes**
3. **Test before marking verified**
4. **Document your decisions**
5. **Use role prefixes in commits**

---

## 📁 Essential Locations

- **HTML Game:** `game/game.js` (reference)
- **ChoiceScript:** `choicescript_game/scenes/`
- **Lore:** `lore/` directory
- **Docs:** `docs/` directory

---

## 💡 Common Tasks

### Convert a Scene
→ Lore approves → You draft → Struct verifies → Balance checks stats

### Fix a Bug
→ Document in STATUS_CONTEXT.md → Fix → Test → Update checklists

### Balance Stats
→ Extract to STATS_MATRIX.md → Analyze → Propose changes → Test

---

**Full details in MULTI_AI_COLLABORATION_GUIDE.md**
