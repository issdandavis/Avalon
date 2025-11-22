# NEXT TASKS - Priority Queue

**Last Updated:** November 22, 2025
**Current Phase:** Phase 2 - Complete ChoiceScript Game

---

## IMMEDIATE PRIORITIES

### Task 1: Complete Singing Dunes Expedition
**Priority:** HIGH
**Effort:** Medium (2-4 hours)
**Status:** Not Started

**Description:**
Convert the Singing Dunes content from `game/game.js` to ChoiceScript format in `choicescript_game/scenes/singing_dunes.txt`

**Steps:**
1. Read the Singing Dunes section in `game/game.js` (search for "singingDunes")
2. Create ChoiceScript scenes for:
   - Desert arrival and atmosphere
   - Kael (desert guide) introduction
   - Truth-testing sand interactions
   - Oath-magic learning sequence
   - Choice: embrace truth vs resist
3. Connect to Truthbound Mage ending path
4. Test all paths

**Key Elements:**
- Truth-sworn sand that judges honesty
- Kael as guide character
- Collaboration stat affects sand's response
- Can become Truthbound Mage or be rejected

---

### Task 2: Complete Verdant Tithe Expedition
**Priority:** HIGH
**Effort:** Medium (2-4 hours)
**Status:** Not Started

**Description:**
Convert the Verdant Tithe content to ChoiceScript format in `choicescript_game/scenes/verdant_tithe.txt`

**Steps:**
1. Read the Verdant Tithe section in `game/game.js` (search for "verdantTithe")
2. Create ChoiceScript scenes for:
   - Sentient forest entrance
   - Thoughtvine interactions
   - Dreamwillow vision sequence
   - Heartwood Tree encounter
3. Three paths: Dreamwillow, Thoughtvine, Heartwood
4. Connect to forest-related endings

**Key Elements:**
- Forest is alive and sentient
- Thoughtvines read and share thoughts
- Dreamwillow shows possible futures
- Heartwood Guardian is most powerful forest ending

---

### Task 3: Complete Rune Glacier Expedition
**Priority:** HIGH
**Effort:** Medium (2-4 hours)
**Status:** Not Started

**Description:**
Convert the Rune Glacier content to ChoiceScript format in `choicescript_game/scenes/rune_glacier.txt`

**Steps:**
1. Read the Rune Glacier section in `game/game.js` (search for "runeGlacier")
2. Create ChoiceScript scenes for:
   - Living ice introduction
   - Control vs Harmony approaches
   - Aria's teaching sequences
   - Frozen spell library discovery
3. Connect to glacier-related endings

**Key Elements:**
- Ice is inscribed with adaptive runes
- Control approach vs Partnership approach
- Runeweaver ending (control)
- Glacier Partner ending (harmony)

---

### Task 4: Implement All 14 Endings
**Priority:** MEDIUM
**Effort:** Medium (2-3 hours)
**Status:** Not Started

**Description:**
Port all endings from HTML to ChoiceScript in `choicescript_game/scenes/endings.txt`

**Endings to Implement:**
- [ ] Collaborative Master (high collab)
- [ ] Truthbound Mage (Dunes)
- [ ] Forestbound Guardian (Forest)
- [ ] Heartwood Guardian (Forest - special)
- [ ] Runeweaver (Glacier - control)
- [ ] Glacier Partner (Glacier - harmony)
- [ ] Balanced Mage (mixed stats)
- [ ] Boundary Specialist
- [ ] Collaborative Scholar
- [ ] Humble Seeker
- [ ] Second Chance
- [ ] Humbled Student
- [ ] Expelled (failure)
- [ ] Standard Path (neutral)

---

## MEDIUM PRIORITIES

### Task 5: Add Achievement System
**Priority:** MEDIUM
**Effort:** Small (1-2 hours)

Add achievements throughout the game:
- First choice made
- Met all three mentors
- Completed first lesson
- Reached each ending
- Special discoveries

### Task 6: Balance Stat Requirements
**Priority:** MEDIUM
**Effort:** Small (1 hour)

Review and balance:
- Collaboration thresholds for each path
- Relationship requirements for special scenes
- Difficulty of achieving each ending

### Task 7: Polish Polly's Commentary
**Priority:** MEDIUM
**Effort:** Medium (2-3 hours)

Add more of Polly's sarcastic commentary:
- Reactions to player choices
- Random observations
- References to past students
- Fourth-wall breaks

---

## LOW PRIORITIES

### Task 8: Beta Testing Setup
**Priority:** LOW (until content complete)
**Effort:** Small (1 hour)

- Create beta tester feedback form
- Write beta testing guide
- Set up issue tracking for bugs

### Task 9: Repository Cleanup
**Priority:** LOW
**Effort:** Small (1 hour)

- Organize lore files into `lore/` folder
- Archive old/duplicate files
- Update .gitignore if needed

### Task 10: Marketing Preparation
**Priority:** LOW (until near publication)
**Effort:** Medium

- Game description for Hosted Games
- Screenshots/mockups
- Author bio
- Social media presence

---

## COMPLETED TASKS

- [x] Create HTML version (full game)
- [x] Set up ChoiceScript foundation
- [x] Implement character creation
- [x] Create three arrival paths
- [x] Complete first lesson
- [x] Create QUICK_START.md
- [x] Create AUTOMATION_GUIDE.md
- [x] Create PROJECT_ROADMAP.md
- [x] Create AI_SESSION_HANDOFF.md
- [x] Create CONTRIBUTING.md
- [x] Create NEXT_TASKS.md

---

## HOW TO PICK UP A TASK

1. **Check this file** for current priorities
2. **Read the task description** and steps
3. **Check the reference** - usually `game/game.js`
4. **Create your branch** following naming convention
5. **Implement the task**
6. **Test thoroughly**
7. **Update this file** - mark task complete, add any new tasks
8. **Commit, push, PR**

---

## ADDING NEW TASKS

When adding tasks, include:
- **Priority:** HIGH/MEDIUM/LOW
- **Effort:** Small/Medium/Large
- **Status:** Not Started/In Progress/Complete
- **Description:** What needs to be done
- **Steps:** Breakdown of subtasks
- **Key Elements:** Important things to remember

---

*Updated by session: teleport-session-recovery (Nov 22, 2025)*
