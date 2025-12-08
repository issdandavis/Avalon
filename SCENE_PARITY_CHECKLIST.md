# SCENE PARITY CHECKLIST
## HTML ↔ ChoiceScript Content Alignment

**Last Updated:** 2025-11-25  
**Purpose:** Track which HTML scenes have been converted to ChoiceScript and verify consistency

---

## 📖 Legend

- ✅ **Verified** - Scene converted, tested, and confirmed identical story
- 🚧 **Draft** - Scene file exists but needs verification
- ❌ **Missing** - Scene not yet converted to ChoiceScript
- 📝 **Partial** - Scene partially implemented

---

## 🎬 Opening & Setup

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Game Introduction | `startup.txt` | ✅ | Character creation complete |
| Polly's Narration | `startup.txt` | ✅ | Sarcastic tone matches |
| Character Creation | `startup.txt` | ✅ | Name, pronouns, familiar selection |
| Familiar Selection | `scenes/familiar_selection.txt` | 🚧 | File exists, needs test |

---

## 🚪 Arrival Paths

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Arrival Choice Hub | `scenes/arrival.txt` | ✅ | Three paths implemented |
| Confident Entrance | `scenes/arrival.txt` | ✅ | Stat changes verified |
| Nervous Entrance | `scenes/arrival.txt` | ✅ | Stat changes verified |
| Curious Entrance | `scenes/arrival.txt` | ✅ | Stat changes verified |

---

## 📚 First Lesson

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Dimensional Theory Intro | `scenes/first_lesson.txt` | ✅ | Complete implementation |
| Collaborative vs Control | `scenes/first_lesson.txt` | ✅ | Core mechanic explained |
| Practical Exercise | `scenes/first_lesson.txt` | ✅ | Choices affect Collaboration stat |
| Lesson Conclusion | `scenes/first_lesson.txt` | ✅ | Leads to expedition selection |

---

## 🏜️ Singing Dunes Expedition

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Desert Introduction | `scenes/singing_dunes.txt` | 🚧 | File exists (931 lines) |
| Meeting Kael (Guide) | `scenes/singing_dunes.txt` | 🚧 | Character interactions |
| Truth-Testing Challenges | `scenes/singing_dunes.txt` | 🚧 | Oath magic mechanics |
| Sand Artifact Discovery | `scenes/singing_dunes.txt` | 🚧 | Truth-sworn sand system |
| Desert Acceptance/Rejection | `scenes/singing_dunes.txt` | 🚧 | Multiple outcome paths |
| Truthbound Mage Path | `scenes/endings.txt` | 🚧 | Ending connection needed |

**Verification Needed:**
- [ ] Compare scene count: HTML vs ChoiceScript
- [ ] Verify all Kael dialogue matches
- [ ] Check Collaboration stat changes align
- [ ] Test path to Truthbound Mage ending

---

## 🌲 Verdant Tithe Expedition

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Forest Introduction | `scenes/verdant_tithe.txt` | 🚧 | File exists (183 lines) - seems short! |
| Thoughtvine Encounters | `scenes/verdant_tithe.txt` | 📝 | May need expansion |
| Dreamwillow Vision | `scenes/verdant_tithe.txt` | 📝 | Key lore moment |
| Heartwood Tree | `scenes/verdant_tithe.txt` | 📝 | Most powerful forest entity |
| Forest Path Choices | `scenes/verdant_tithe.txt` | 📝 | Three distinct paths |
| Forestbound Endings | `scenes/endings.txt` | 🚧 | 2-3 forest endings |

**Verification Needed:**
- [ ] ⚠️ File only 183 lines - check if complete
- [ ] Compare to HTML forest content length
- [ ] Verify Thoughtvine interaction mechanics
- [ ] Check all three forest paths exist
- [ ] Test Heartwood Guardian ending

---

## ❄️ Rune Glacier Expedition

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Glacier Introduction | `scenes/rune_glacier.txt` | 🚧 | File exists (1266 lines) |
| Living Ice Mechanics | `scenes/rune_glacier.txt` | 🚧 | Control vs Harmony theme |
| Aria's Teaching | `scenes/rune_glacier.txt` | 🚧 | Mentor interactions |
| Rune Adaptation System | `scenes/rune_glacier.txt` | 🚧 | Magical rune mechanics |
| Glacier Partnership Path | `scenes/rune_glacier.txt` | 🚧 | Mystery/partnership option |
| Glacier Endings | `scenes/endings.txt` | 🚧 | Runeweaver + Partner endings |

**Verification Needed:**
- [ ] Compare control vs harmony paths
- [ ] Verify Aria dialogue matches lore
- [ ] Check partnership path mechanics
- [ ] Test connection to glacier endings

---

## 🏫 Academy Life Scenes

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Dorm Room Events | `scenes/dorm_room.txt` | 🚧 | File exists (124 lines) |
| Academy Life Moments | `scenes/academy_life.txt` | 🚧 | File exists (167 lines) |
| Golem Workshop | `scenes/golem_workshop.txt` | 🚧 | File exists (174 lines) |
| Secret Paths Discovery | `scenes/secret_paths.txt` | 🚧 | File exists (295 lines) |

**Verification Needed:**
- [ ] Check if these scenes exist in HTML version
- [ ] Verify they don't conflict with main story
- [ ] Test integration with main narrative flow

---

## 💕 Relationship Content

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Character Bonding | `scenes/character_bonds.txt` | 🚧 | File exists (196 lines) |
| Romance Options | `scenes/romance_scenes.txt` | 🚧 | File exists (213 lines) |

**Verification Needed:**
- [ ] Check if romance was in original HTML game
- [ ] Verify character relationship stats used
- [ ] Ensure optional/tasteful implementation

---

## 🏁 Endings

| Ending Name | HTML Present | ChoiceScript File | Status | Trigger Conditions |
|-------------|--------------|-------------------|--------|-------------------|
| Collaborative Master | ✅ | `scenes/endings.txt` | 🚧 | collaboration >= 80 |
| Truthbound Mage | ✅ | `scenes/endings.txt` | 🚧 | Desert + high truth stat |
| Forestbound Guardian | ✅ | `scenes/endings.txt` | 🚧 | Forest + moderate connection |
| Heartwood Guardian | ✅ | `scenes/endings.txt` | 🚧 | Forest + highest connection |
| Runeweaver | ✅ | `scenes/endings.txt` | 🚧 | Glacier + control path |
| Glacier Partner | ✅ | `scenes/endings.txt` | 🚧 | Glacier + partnership path |
| Balanced Mage | ✅ | `scenes/endings.txt` | 🚧 | 40-60 collaboration |
| Boundary Specialist | ✅ | `scenes/endings.txt` | 🚧 | High Aria relationship |
| Collaborative Scholar | ✅ | `scenes/endings.txt` | 🚧 | 60-80 collaboration |
| Humble Seeker | ✅ | `scenes/endings.txt` | 🚧 | Low stats but good character |
| Second Chance | ✅ | `scenes/endings.txt` | 🚧 | Failed once, recovered |
| Humbled Student | ✅ | `scenes/endings.txt` | 🚧 | Low collaboration |
| Expelled | ✅ | `scenes/endings.txt` | 🚧 | Critical failures |
| Standard Path | ✅ | `scenes/endings.txt` | 🚧 | Default/neutral |

**Verification Needed:**
- [ ] Count endings in endings.txt file (should be 14)
- [ ] Verify each ending has proper stat checks
- [ ] Test at least one path to each ending
- [ ] Compare ending text to HTML version

---

## 🎮 Final Trial

| HTML Scene | ChoiceScript File | Status | Notes |
|------------|-------------------|--------|-------|
| Final Trial Sequence | `scenes/final_trial.txt` | 🚧 | File exists (622 lines) |
| Expedition Preparation | `scenes/expedition_prep.txt` | 🚧 | File exists (108 lines) |

**Verification Needed:**
- [ ] Check if final trial exists in HTML
- [ ] Verify it connects to ending selection
- [ ] Test stat requirements

---

## 📊 Summary Statistics

### Content Parity Status
- **Files Created:** 16 scene files
- **Verified Complete:** 4 scenes (startup, arrival, first_lesson)
- **Need Verification:** 12 scenes
- **Potentially Incomplete:** verdant_tithe.txt (too short?)

### Estimated Completion
- **Opening Sequence:** ~90% (needs minor testing)
- **Core Expeditions:** ~70% (files exist, need verification)
- **Endings:** ~80% (file exists with 1118 lines)
- **Optional Content:** ~50% (academy life, romance - may not be in HTML)

---

## 🔍 Quality Checklist

### For Each Scene Verification:
- [ ] Scene count matches (HTML has X scenes, ChoiceScript has X)
- [ ] Character dialogue identical or improved
- [ ] Stat changes match or improve upon HTML version
- [ ] No new lore contradictions introduced
- [ ] Polly's voice remains consistent
- [ ] Choices lead to expected outcomes
- [ ] No dead-end paths (all choices lead somewhere)

---

## 🚀 Next Actions

### Immediate Priorities (This Week)
1. **Verify verdant_tithe.txt** - File seems short, may need expansion
2. **Test one complete playthrough** - Start to any ending
3. **Count endings in endings.txt** - Ensure all 14 present
4. **Document stat changes** - Feed into STATS_MATRIX.md

### Medium-Term (Next 2 Weeks)
1. Systematically verify each expedition (Dunes, Forest, Glacier)
2. Test all 14 endings can be reached
3. Balance stat requirements across paths
4. Proofread all text for consistency

---

## 📝 Notes

### Scene Files Not in Original HTML (Need Decision)
- `academy_life.txt` - Added content?
- `character_bonds.txt` - Added content?
- `romance_scenes.txt` - Added content?
- `golem_workshop.txt` - Added content?
- `secret_paths.txt` - Added content?
- `final_trial.txt` - Added content?
- `expedition_prep.txt` - Added content?

**Action Required:** Review HTML `game/game.js` to see if these scenes existed or are new additions.

---

**Maintained By:** Structural Reviewer AI + All collaborators  
**Update After:** Each scene verification, each conversion, each test
