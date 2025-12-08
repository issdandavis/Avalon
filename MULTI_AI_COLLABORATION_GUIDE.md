# MULTI-AI COLLABORATION GUIDE
## Avalon Project Coordination System

**Purpose:** Enable multiple AI assistants to work together effectively on the Avalon Codex project  
**Last Updated:** 2025-11-25  
**Status:** ✅ System Initialized

---

## 🎯 Quick Start for AI Collaborators

### New to This Project?
1. **Read this file first** (you're here!)
2. Read `STATUS_CONTEXT.md` - Current project state
3. Read `SCENE_PARITY_CHECKLIST.md` - What's done vs what's needed
4. Review `STATS_MATRIX.md` - How choices affect gameplay
5. Check `docs/PROJECT_ROADMAP.md` - Long-term plan
6. Read `docs/AI_SESSION_HANDOFF.md` - Detailed context

### Continuing Work?
1. Update `STATUS_CONTEXT.md` with your session info
2. Check relevant checklist for your role
3. Update matrices/checklists as you work
4. Document any lore discoveries

---

## 👥 Defined AI Roles

### 1. Lore Curator (Creative Model Recommended)
**Expertise:** Narrative consistency, character canon, worldbuilding  
**Primary Files:**
- `lore/` directory (all worldbuilding)
- `writing_drafts/IZACK_MASTER_CHRONICLE_UPDATED.txt` (if exists)
- `SCENE_PARITY_CHECKLIST.md` (verify story accuracy)

**Responsibilities:**
- Validate new narrative against established canon
- Flag timeline contradictions
- Ensure magic system rules are consistent
- Verify character voice and personality
- Check dimensional theory accuracy

**When to Call:**
- Before converting any scene (validate source material)
- When character dialogue seems off
- If magic system usage seems inconsistent
- Before implementing new story elements

**Deliverables:**
- ✅ Approved / 🚫 Needs revision for lore accuracy
- List of canon references to check
- Suggestions for maintaining consistency

---

### 2. Conversion Engineer (Code-Focused Model Recommended)
**Expertise:** HTML to ChoiceScript translation, technical implementation  
**Primary Files:**
- `game/game.js` (source HTML game)
- `choicescript_game/scenes/*.txt` (target files)
- `SCENE_PARITY_CHECKLIST.md` (track conversions)

**Responsibilities:**
- Translate HTML scenes to ChoiceScript format
- Preserve choice logic and branching
- Implement stat tracking correctly
- Convert game mechanics accurately
- Maintain code quality and formatting

**When to Call:**
- When creating new ChoiceScript scenes
- When updating existing scene files
- For technical ChoiceScript questions

**Deliverables:**
- New/updated ChoiceScript scene files
- Updated `SCENE_PARITY_CHECKLIST.md` (mark as Draft)
- List of stat modifications made
- Notes on any deviations from HTML

---

### 3. Structural Reviewer (Codebase-Indexing Model Recommended)
**Expertise:** Scene parity verification, branching logic, completeness  
**Primary Files:**
- `game/game.js` (reference implementation)
- `choicescript_game/scenes/*.txt` (verify against reference)
- `SCENE_PARITY_CHECKLIST.md` (maintain status)

**Responsibilities:**
- Verify scene count matches (HTML vs ChoiceScript)
- Check all choice paths lead somewhere
- Ensure ending count is correct (14 total)
- Validate stat progression consistency
- Flag missing or incomplete scenes

**When to Call:**
- After Conversion Engineer completes a scene
- Before marking scenes as "Verified"
- When testing complete playthroughs
- For quality assurance passes

**Deliverables:**
- Updated `SCENE_PARITY_CHECKLIST.md` (✅ Verified or issues found)
- List of discrepancies between versions
- Recommendations for fixes

---

### 4. Quality Balancer (Analytical Model Recommended)
**Expertise:** Stat balancing, difficulty tuning, gameplay feel  
**Primary Files:**
- `STATS_MATRIX.md` (track all stat changes)
- `choicescript_game/scenes/*.txt` (source of stat modifications)
- `choicescript_game/startup.txt` (stat definitions)

**Responsibilities:**
- Track all stat modifications across scenes
- Identify imbalanced choices
- Ensure endings are reachable
- Balance Collaboration stat difficulty
- Verify stat thresholds are fair

**When to Call:**
- After scene conversions are verified
- When testing reveals stat problems
- Before beta testing
- For final balance pass

**Deliverables:**
- Updated `STATS_MATRIX.md` with actual values
- Proposed stat adjustments
- Difficulty analysis per path
- Recommended threshold changes

---

### 5. Automation Planner (Any Model)
**Expertise:** Workflow documentation, tool integration, process improvement  
**Primary Files:**
- `docs/AUTOMATION_GUIDE.md`
- `.github/workflows/*.yml`
- This file (MULTI_AI_COLLABORATION_GUIDE.md)

**Responsibilities:**
- Update Zapier workflow documentation
- Document new content type workflows
- Improve coordination processes
- Maintain collaboration guides

**When to Call:**
- When new asset types are added
- For process improvement suggestions
- When workflows need updating

**Deliverables:**
- Updated automation documentation
- Process improvement proposals

---

## 📋 Shared Context Artifacts

### Must-Maintain Files (All AIs)

#### 1. STATUS_CONTEXT.md
**Purpose:** Weekly snapshot of current work  
**Update When:**
- Starting a new work session
- Switching AI roles
- Completing a major milestone
- Weekly (minimum)

**Contents:**
- Current scene being worked on
- Pending lore updates
- Recent completions
- Blockers/issues
- Next steps

#### 2. SCENE_PARITY_CHECKLIST.md
**Purpose:** Track HTML ↔ ChoiceScript alignment  
**Update When:**
- Starting scene conversion (mark 🚧 Draft)
- Completing scene conversion (mark ✅ Verified)
- Finding discrepancies

**Contents:**
- Scene-by-scene status
- Verification checklist per scene
- Notes on deviations
- Summary statistics

#### 3. STATS_MATRIX.md
**Purpose:** Track all choice impacts on stats  
**Update When:**
- Extracting stats from a scene
- Balancing stat values
- Testing stat progression
- Finding balance issues

**Contents:**
- Table of all stat-modifying choices
- Balance analysis
- Recommended thresholds
- Testing results

---

## 🔄 Collaboration Workflow

### Standard Scene Conversion Process

#### Step 1: Lore Approval (Lore Curator)
```
Input: HTML scene from game/game.js
Process:
  - Read scene content
  - Cross-reference with lore/ documents
  - Check character consistency
  - Verify magic system usage
  - Flag any contradictions
Output: ✅ Approved or 🚫 Needs revision
Update: Add findings to STATUS_CONTEXT.md
```

#### Step 2: Conversion (Conversion Engineer)
```
Input: Approved HTML scene
Process:
  - Convert to ChoiceScript syntax
  - Implement choice logic
  - Add stat modifications
  - Format correctly
  - Add comments for clarity
Output: Draft ChoiceScript scene file
Update: Mark scene as 🚧 Draft in SCENE_PARITY_CHECKLIST.md
```

#### Step 3: Verification (Structural Reviewer)
```
Input: Draft ChoiceScript scene
Process:
  - Compare to HTML source
  - Verify choice count matches
  - Check all paths have destinations
  - Validate branching logic
  - Test for dead ends
Output: ✅ Verified or list of issues
Update: Mark scene status in SCENE_PARITY_CHECKLIST.md
```

#### Step 4: Balancing (Quality Balancer)
```
Input: Verified scene
Process:
  - Extract all stat modifications
  - Add to STATS_MATRIX.md
  - Analyze stat progression
  - Compare to other scenes
  - Propose adjustments if needed
Output: Updated STATS_MATRIX.md, balance recommendations
Update: Flag any imbalanced choices
```

#### Step 5: Final Review (Any AI)
```
Input: Balanced scene
Process:
  - Read through for quality
  - Check Polly's voice
  - Verify formatting
  - Final proofread
Output: ✅ Complete scene ready for commit
Update: Mark ✅ Verified in checklist
```

---

## 🤝 Hand-off Conventions

### Inline Code Markers (Use Sparingly)
**Only in draft ChoiceScript files** - Remove before marking verified

```choicescript
*comment TODO:[LORE]: Verify Kael's backstory matches desert lore
*comment TODO:[CONVERT]: Add stat modification for this choice
*comment TODO:[STRUCT]: Check if this path connects to ending properly  
*comment TODO:[BALANCE]: This seems like a high stat gain (+25)
```

**Role Tags:**
- `[LORE]` - Lore Curator needed
- `[CONVERT]` - Conversion Engineer task
- `[STRUCT]` - Structural Reviewer needed
- `[BALANCE]` - Quality Balancer task
- `[AUTO]` - Automation Planner task

### Git Commit Prefixes
```
Lore: Verified singing_dunes scene against desert lore
Convert: Drafted verdant_tithe.txt from HTML source
Struct: Verified first_lesson.txt matches HTML branching
Balance: Adjusted collaboration gains in rune_glacier.txt
Auto: Updated AUTOMATION_GUIDE.md with new scene workflow
```

### Session Boundaries
**At End of Session:**
1. Update STATUS_CONTEXT.md with progress
2. Update relevant checklists/matrices
3. Remove TODO markers from verified code
4. Commit with appropriate prefix
5. Note any blockers for next session

**At Start of Session:**
1. Read STATUS_CONTEXT.md
2. Check relevant checklist for your role
3. Review any TODO markers tagged for you
4. Plan your work for the session

---

## 🎯 Model Selection Tips

### Creative/Lore Tasks → Higher Reasoning Models
- **Claude** (Sonnet/Opus)
- **GPT-4** (creative variant)
- **Gemini** (for deep lore queries)

**Best For:**
- Lore Curator role
- Writing Polly's dialogue
- Character consistency checks
- Magic system validation

### Structural/Code Tasks → Code-Focused Models
- **GitHub Copilot**
- **Codeium**
- **CodeLlama**

**Best For:**
- Conversion Engineer role
- ChoiceScript syntax
- Technical implementation
- Bug fixing

### Cross-File Analysis → Codebase-Indexing Models
- **Cursor**
- **Continue**
- **Sourcegraph Cody**

**Best For:**
- Structural Reviewer role
- Finding all stat references
- Scene comparison
- Completeness verification

### Balanced General Work → GPT-4/Claude
- **GPT-4** (balanced)
- **Claude** (Sonnet)

**Best For:**
- Quality Balancer role
- General review
- Documentation
- Planning

---

## ✅ Pre-Merge Verification (ALL AIs)

### Before Marking Scene as Complete
- [ ] Scene count matches HTML source
- [ ] All choices lead somewhere (no dead ends)
- [ ] Stat changes documented in STATS_MATRIX.md
- [ ] No new lore contradictions
- [ ] Polly's voice is consistent
- [ ] No TODO markers remain in code
- [ ] SCENE_PARITY_CHECKLIST.md updated
- [ ] STATUS_CONTEXT.md reflects completion

### Before Committing Code
- [ ] No debug/temporary comments
- [ ] Proper ChoiceScript formatting
- [ ] Tested at least one playthrough
- [ ] Git commit has role prefix
- [ ] Checklists updated

---

## 🚨 Conflict Resolution

### Lore Disagreements
1. Lore Curator has final say on canon
2. Reference `lore/` directory as source of truth
3. Check `writing_drafts/IZACK_MASTER_CHRONICLE_UPDATED.txt` (if exists)
4. When in doubt, maintain HTML game's interpretation
5. Document decision in STATUS_CONTEXT.md

### Technical Disagreements
1. Conversion Engineer proposes implementation
2. Structural Reviewer validates correctness
3. Quality Balancer suggests improvements
4. Maintain HTML game's behavior as baseline
5. Document deviation if necessary

### Stat Balance Disagreements
1. Quality Balancer proposes thresholds
2. Test multiple playthroughs
3. Aim for 14 endings all being reachable
4. Collaborative path should feel rewarding, not easy
5. Control path should be challenging but viable

---

## 📊 Project Health Metrics

### Green (Healthy)
- ✅ All active scenes verified
- ✅ Stat matrix up to date
- ✅ No lore contradictions
- ✅ All TODO markers resolved
- ✅ Weekly status updates

### Yellow (Needs Attention)
- ⚠️ Some scenes in draft state
- ⚠️ Stat matrix partially complete
- ⚠️ Minor lore questions
- ⚠️ Some TODO markers present
- ⚠️ Status slightly outdated

### Red (Requires Action)
- 🚫 Multiple unverified scenes
- 🚫 Stat matrix missing data
- 🚫 Lore contradictions found
- 🚫 Many TODO markers
- 🚫 Status not updated in 2+ weeks

---

## 🎓 Best Practices

### DO:
- ✅ Update STATUS_CONTEXT.md at session start/end
- ✅ Use role-specific commit prefixes
- ✅ Cross-reference lore before changes
- ✅ Mark scenes in checklists as you work
- ✅ Document deviations from HTML
- ✅ Test your changes when possible
- ✅ Ask other roles for review

### DON'T:
- ❌ Make lore changes without Lore Curator review
- ❌ Skip updating checklists
- ❌ Leave TODO markers in verified code
- ❌ Assume HTML game is always right (verify!)
- ❌ Work in isolation - use the coordination files
- ❌ Commit without descriptive messages
- ❌ Break working scenes

---

## 🚀 Quick Reference Scenarios

### "I want to convert a scene to ChoiceScript"
1. **First:** Lore Curator validates source scene
2. **Then:** You (Conversion Engineer) draft ChoiceScript
3. **Next:** Structural Reviewer verifies it
4. **Finally:** Quality Balancer checks stats
5. **Update:** All relevant checklists

### "I found a lore inconsistency"
1. **Document** it in STATUS_CONTEXT.md
2. **Reference** specific files/line numbers
3. **Propose** resolution based on canon
4. **Update** SCENE_PARITY_CHECKLIST.md with note
5. **Wait** for Lore Curator approval

### "Stats feel unbalanced"
1. **Extract** all stat values to STATS_MATRIX.md
2. **Test** multiple playthroughs
3. **Calculate** min/max possible stats
4. **Propose** adjusted values
5. **Document** reasoning for changes

### "I don't know what to work on"
1. **Read** STATUS_CONTEXT.md for current priorities
2. **Check** SCENE_PARITY_CHECKLIST.md for 🚧 or ❌ items
3. **Review** STATS_MATRIX.md for incomplete data
4. **Pick** a task matching your expertise
5. **Update** STATUS_CONTEXT.md with your choice

---

## 📚 Essential File Reference

### Must-Read Every Session
- `STATUS_CONTEXT.md` - Current state
- Role-specific checklist section

### Reference As Needed
- `SCENE_PARITY_CHECKLIST.md` - Scene status
- `STATS_MATRIX.md` - Stat tracking
- `docs/PROJECT_ROADMAP.md` - Overall plan
- `docs/AI_SESSION_HANDOFF.md` - Detailed context

### Lore Reference
- `lore/` directory - All worldbuilding
- `writing_drafts/` - Novel manuscripts
- `game/game.js` - Reference implementation

### Technical Reference
- `choicescript_game/startup.txt` - Stat definitions
- `choicescript_game/scenes/` - All scene files
- `docs/AUTOMATION_GUIDE.md` - Workflows

---

## 🎉 Success Indicators

### You're Doing It Right When:
- ✅ STATUS_CONTEXT.md is always current
- ✅ Checklists update after every change
- ✅ Commits have descriptive prefixes
- ✅ Other AIs can pick up your work easily
- ✅ Lore stays consistent
- ✅ Stats balance across scenes
- ✅ No knowledge is lost between sessions

### You Need to Improve When:
- ❌ Making changes without updating docs
- ❌ Working in isolation from other AIs
- ❌ Leaving work half-documented
- ❌ Creating lore contradictions
- ❌ Not testing changes
- ❌ Forgetting to update checklists

---

## 🔗 Related Documentation

- `README.md` - Project overview
- `CONTRIBUTING.md` - Contribution guidelines
- `docs/PROJECT_ROADMAP.md` - Development phases
- `docs/AI_SESSION_HANDOFF.md` - Session continuity
- `docs/AUTOMATION_GUIDE.md` - Tool integration
- `.github/copilot-instructions.md` - AI coding guidelines

---

## 🆘 Getting Help

### Stuck on Lore Question?
→ Check `lore/` directory  
→ Reference `docs/AETHERMOOR_CHRONICLES.md`  
→ Look at HTML game implementation

### Stuck on Technical Issue?
→ Check ChoiceScript documentation  
→ Review `choicescript_game/scenes/first_lesson.txt` (good example)  
→ Compare to HTML `game/game.js`

### Stuck on What to Do?
→ Read `STATUS_CONTEXT.md`  
→ Look for ❌ or 🚧 in `SCENE_PARITY_CHECKLIST.md`  
→ Check `STATS_MATRIX.md` for incomplete data

---

## 📝 Changelog

### 2025-11-25 - Initial System
- ✅ Created STATUS_CONTEXT.md
- ✅ Created SCENE_PARITY_CHECKLIST.md
- ✅ Created STATS_MATRIX.md
- ✅ Created MULTI_AI_COLLABORATION_GUIDE.md (this file)
- ✅ Defined 5 AI roles with clear responsibilities
- ✅ Established workflow and hand-off conventions
- ✅ Set up pre-merge verification checklist

---

**Welcome to the Avalon multi-AI collaboration system!**  
*"Many voices, one story. The spiral continues."*
