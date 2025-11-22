# AI SESSION HANDOFF DOCUMENT
## For Claude Code and Other AI Assistants

**Last Updated:** November 22, 2025
**Last Session:** `session_01GguS4Bausc4TYaFt9z1kxW` (Design Choice Game)
**Current Branch:** `claude/design-choice-game-01GguS4Bausc4TYaFt9z1kxW` (merged to main)

---

## PROJECT OVERVIEW

**Project:** Polly's Wingscroll: The First Thread
**Universe:** The Spiral of Pollyoneth / Avalon Codex
**Type:** Choice-based narrative game (interactive fiction)
**Goal:** Create a publishable game for Hosted Games (app stores)

### Quick Context

This is an interactive fiction game where players are students at Avalon Academy, guided by Polly - a sarcastic, immortal raven. The game uses the "Spiral of Pollyoneth" lore which includes dimensional magic, collaborative spellcasting, and three unique magical realms.

---

## REPOSITORY STRUCTURE

```
Avalon/
├── game/                      # HTML VERSION (COMPLETE)
│   ├── index.html             # Main game file
│   ├── style.css              # Styling
│   └── game.js                # Full game logic (30+ scenes, 14 endings)
│
├── choicescript_game/         # CHOICESCRIPT VERSION (IN PROGRESS)
│   ├── startup.txt            # Main config & character creation
│   └── scenes/
│       ├── arrival.txt        # Three arrival paths (COMPLETE)
│       ├── first_lesson.txt   # Dimensional magic lesson (COMPLETE)
│       ├── singing_dunes.txt  # Desert expedition (PLACEHOLDER)
│       ├── verdant_tithe.txt  # Forest expedition (PLACEHOLDER)
│       ├── rune_glacier.txt   # Ice expedition (PLACEHOLDER)
│       ├── endings.txt        # All endings (PLACEHOLDER)
│       └── choicescript_stats.txt  # Stats screen
│
├── docs/                      # DOCUMENTATION
│   ├── AUTOMATION_GUIDE.md    # Zapier integration guide
│   ├── PROJECT_ROADMAP.md     # Full development roadmap
│   └── AI_SESSION_HANDOFF.md  # THIS FILE
│
├── QUICK_START.md             # Player quick start guide
├── AvalonBook STUFF/          # Lore source documents
└── [various .txt files]       # Original lore/story files
```

---

## CURRENT STATUS

### Phase 1: Foundation - COMPLETE
- [x] Game concept design
- [x] Lore integration
- [x] Character system (Izack, Aria, Zara, Polly)
- [x] HTML version (full game)
- [x] ChoiceScript foundation
- [x] Documentation

### Phase 2: Complete ChoiceScript Game - IN PROGRESS
- [x] Character creation
- [x] Opening sequence
- [x] Three arrival paths
- [x] First lesson
- [x] **Singing Dunes expedition**
- [x] Verdant Tithe expedition
- [x] Rune Glacier expedition
- [ ] All 14 endings <-- NEXT PRIORITY

### Phase 3-5: Polish, Beta, Publish - PLANNED
- See PROJECT_ROADMAP.md for full details

---

## KEY GAME MECHANICS

### Stats System
- **Collaboration Score (0-100):** Higher = collaborative magic approach
- **Relationships:** Track bonds with Izack, Aria, Zara, Polly

### Three Realms (Expeditions)
1. **Singing Dunes** - Truth-testing desert, oath magic
2. **Verdant Tithe** - Sentient forest, Thoughtvines, Heartwood Tree
3. **Rune Glacier** - Living ice with adaptive magical runes

### 14 Planned Endings
1. Collaborative Master
2. Truthbound Mage (Dunes path)
3. Forestbound Guardian (Forest path)
4. Heartwood Guardian (Forest - most powerful)
5. Runeweaver (Glacier path)
6. Glacier Partner (Glacier - partnership)
7. Balanced Mage
8. Boundary Specialist
9. Collaborative Scholar
10. Humble Seeker
11. Second Chance
12. Humbled Student
13. Expelled (failure)
14. Standard Path (neutral)

---

## KEY CHARACTERS

### Polly (Narrator)
- Sarcastic, immortal raven
- 3000+ years old
- Provides commentary throughout
- Has seen countless students

### Izack (Mentor)
- Legendary mage, player's mentor
- Teaches collaborative magic
- Has dimensional abilities

### Aria Ravencrest
- Boundary specialist
- Expert in protective magic
- Political background

### Zara
- Chaos mage
- Experimental magic approach
- Fun, unpredictable

---

## IMPORTANT FILES FOR AI SESSIONS

### To Understand the Game
1. `game/game.js` - Complete HTML game logic (reference for ChoiceScript conversion)
2. `choicescript_game/scenes/first_lesson.txt` - Example of completed ChoiceScript scene
3. `docs/PROJECT_ROADMAP.md` - Full development plan

### To Understand the Lore
1. `spiral-of-pollyoneth-novel.md` - Main novel/lore document
2. `AvalonBook STUFF/` folder - Source lore materials
3. Various `.txt` files in root - Character/world details

### To Test the Game
1. HTML: Open `game/index.html` in browser
2. ChoiceScript: Need ChoiceScript IDE (see QUICK_START.md)

---

## NEXT TASKS FOR AI SESSIONS

### Priority 1: Complete Singing Dunes (ChoiceScript)
Convert the Singing Dunes content from `game/game.js` to ChoiceScript format:
- Truth-testing desert scenes
- Kael (desert guide) interactions
- Oath-magic learning sequence
- Connect to Truthbound Mage ending

### Priority 2: Complete Verdant Tithe
- Sentient forest atmosphere
- Thoughtvine interactions
- Dreamwillow vision sequence
- Heartwood Tree encounter
- Three forest paths

### Priority 3: Complete Rune Glacier
- Living ice mechanics
- Control vs Harmony paths
- Aria's teaching sequences
- Glacier partnership ending

### Priority 4: Implement All Endings
- Port all 14 endings from HTML to ChoiceScript
- Ensure proper stat checks
- Achievement triggers

---

## CODE PATTERNS (ChoiceScript)

### Basic Choice Structure
```choicescript
*choice
    #Option text
        Result text
        *goto next_label
    #Another option
        Different result
        *goto different_label
```

### Stat Modification
```choicescript
*set collaboration +10
*set izack_relationship +5
```

### Conditional Logic
```choicescript
*if collaboration >= 60
    High collaboration text
*elseif collaboration >= 30
    Medium collaboration text
*else
    Low collaboration text
```

### Scene Transitions
```choicescript
*goto_scene singing_dunes
```

---

## SESSION HISTORY

| Session ID | Date | Work Completed |
|------------|------|----------------|
| `01GguS4Bausc4TYaFt9z1kxW` | Nov 2025 | Created full HTML game, ChoiceScript foundation, documentation |
| (current session) | Nov 22, 2025 | Session recovery, documentation enhancement |

---

## COMMUNICATION FOR FUTURE AI

### How This Handoff Works
When a new AI session starts on this project:
1. Read this document first for context
2. Check `PROJECT_ROADMAP.md` for current phase
3. Review `game/game.js` for complete game logic to port
4. Work on the "Next Tasks" section above

### Notes for Future Sessions
- The HTML version in `game/` is the complete reference implementation
- ChoiceScript version should match HTML game content
- Polly's sarcastic voice should be maintained throughout
- Collaboration vs Individual Power is the core stat tension
- All paths should feel rewarding, not just "correct" path

### Git Workflow
- Create branch: `claude/[task-name]-[session-id]`
- Commit frequently with descriptive messages
- Push to branch and create PR to main

---

## CONTACT & RESOURCES

**ChoiceScript Documentation:**
- https://www.choiceofgames.com/make-your-own-games/choicescript-intro/

**Hosted Games Forum:**
- https://forum.choiceofgames.com/

**Project Owner:** @issdandavis (GitHub)

---

## UPDATE LOG

- **Nov 22, 2025:** Created AI handoff document
- **Nov 22, 2025:** Expanded all three expedition scenes (singing_dunes, verdant_tithe, rune_glacier) from placeholders to full content (600+ lines each)
- **Nov 20, 2025:** Merged choice game foundation (PRs #6, #7)

---

*"The spiral continues. Every session writes the next chapter."*
