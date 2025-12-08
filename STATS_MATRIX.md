# STATS MATRIX
## Choice Impact Tracking Across All Scenes

**Last Updated:** 2025-11-25  
**Purpose:** Track every choice that affects stats to ensure balance and consistency

---

## 📊 Core Stats

### Primary Stats
- **Collaboration** (0-100) - Core moral choice: collaborative vs hierarchical magic
- **Izack_relationship** (0-100) - Bond with mentor Izack
- **Aria_relationship** (0-100) - Bond with Aria Ravencrest
- **Zara_relationship** (0-100) - Bond with Zara (chaos mage)
- **Polly_relationship** (0-100) - Bond with Polly (narrator)

### Secondary/Derived Stats
- **Familiar Bond** - Relationship with chosen familiar
- **Realm Affinity** - Connection to visited realm (Desert/Forest/Glacier)
- **Truth Stat** (Singing Dunes) - Oath-magic alignment
- **Forest Connection** (Verdant Tithe) - Sentient forest bond
- **Rune Mastery** (Rune Glacier) - Ice magic understanding

---

## 🎬 Startup & Character Creation

| Scene | Choice/Action | Collaboration | Relationships | Other Stats | Source File |
|-------|---------------|---------------|---------------|-------------|-------------|
| Name Selection | Enter name | - | - | Sets ${name} | startup.txt |
| Pronoun Selection | Choose pronouns | - | - | Sets ${he_she}, ${him_her}, etc. | startup.txt |
| Familiar Choice | Raven | - | polly +5 | Sets familiar_type | startup.txt |
| Familiar Choice | Cat | - | - | Sets familiar_type | startup.txt |
| Familiar Choice | Owl | - | - | Sets familiar_type | startup.txt |
| Familiar Choice | Fox | - | - | Sets familiar_type | startup.txt |

**Balance Check:**
- ✅ Familiar choices don't drastically affect gameplay
- ⚠️ Raven choice gives +5 Polly - intentional early bond?

---

## 🚪 Arrival Paths

| Scene | Choice/Action | Collaboration | Relationships | Other Stats | Source File |
|-------|---------------|---------------|---------------|-------------|-------------|
| Arrival Method | Confident entrance | +5 | - | - | arrival.txt |
| Arrival Method | Nervous entrance | +5 | izack +5 | - | arrival.txt |
| Arrival Method | Curious entrance | +10 | - | - | arrival.txt |

**Balance Check:**
- ⚠️ Curious gives +10 while others give +5 - verify this is intentional
- ✅ All paths give positive collaboration boost (good opening)
- ✅ Nervous path rewards with mentor relationship (makes sense)

**Recommended Thresholds:**
- Post-arrival: collaboration 5-10 range

---

## 📚 First Lesson (Dimensional Theory)

| Scene | Choice/Action | Collaboration | Relationships | Other Stats | Source File |
|-------|---------------|---------------|---------------|-------------|-------------|
| Magic Approach | Work together | +15 | izack +10 | - | first_lesson.txt |
| Magic Approach | Solo attempt | -5 | - | - | first_lesson.txt |
| Magic Approach | Observe first | +5 | aria +5 | - | first_lesson.txt |
| Practical Exercise | Collaborate | +10 | - | - | first_lesson.txt |
| Practical Exercise | Control attempt | -10 | - | - | first_lesson.txt |
| Response to Izack | Accept guidance | +5 | izack +5 | - | first_lesson.txt |
| Response to Izack | Question method | +0 | zara +5 | - | first_lesson.txt |

**Balance Check:**
- ✅ Clear reward for collaborative choices
- ✅ Control/solo choices reduce collaboration appropriately
- ✅ Observation path rewards Aria (boundary specialist)
- ✅ Questioning rewards Zara (chaos mage) - fits character

**Recommended Thresholds:**
- Post-lesson: collaboration 10-40 range
- Collaborative path: ~30-40
- Neutral path: ~15-25
- Control path: ~0-10

---

## 🏜️ Singing Dunes Expedition

| Scene | Choice/Action | Collaboration | Relationships | Other Stats | Source File |
|-------|---------------|---------------|-------------|-------------|-------------|
| Meet Kael | Respectful greeting | +5 | - | truth +5 | singing_dunes.txt |
| Meet Kael | Cautious approach | +0 | - | - | singing_dunes.txt |
| Meet Kael | Direct challenge | -5 | - | truth -5 | singing_dunes.txt |
| Truth Test 1 | Honest answer | +10 | - | truth +10 | singing_dunes.txt |
| Truth Test 1 | Partial truth | +5 | - | truth +5 | singing_dunes.txt |
| Truth Test 1 | Deception | -15 | - | truth -15 | singing_dunes.txt |
| Oath Magic | Speak oath willingly | +10 | - | truth +15 | singing_dunes.txt |
| Oath Magic | Resist oath | -5 | - | truth -10 | singing_dunes.txt |
| Sand Artifact | Accept bond | +15 | - | truth +20 | singing_dunes.txt |
| Sand Artifact | Decline bond | +0 | - | - | singing_dunes.txt |

**Balance Check:**
- ⚠️ Need to verify these values in actual file
- ✅ Truth stat progression makes sense
- ⚠️ High collaboration gains (+15) may need balancing
- ⚠️ Large truth penalties (-15) could lock out ending

**Recommended Thresholds:**
- Truthbound Mage ending: truth >= 40, collaboration >= 30
- Desert acceptance: truth >= 20
- Mid-range completion: collaboration 25-60

---

## 🌲 Verdant Tithe Expedition

| Scene | Choice/Action | Collaboration | Relationships | Other Stats | Source File |
|-------|---------------|---------------|-------------|-------------|-------------|
| Enter Forest | Open approach | +10 | - | forest +10 | verdant_tithe.txt |
| Enter Forest | Guarded approach | +5 | aria +5 | forest +5 | verdant_tithe.txt |
| Thoughtvine | Listen willingly | +15 | - | forest +15 | verdant_tithe.txt |
| Thoughtvine | Resist thoughts | -5 | - | forest -5 | verdant_tithe.txt |
| Dreamwillow Vision | Accept vision | +10 | - | forest +20 | verdant_tithe.txt |
| Dreamwillow Vision | Question vision | +5 | zara +5 | forest +5 | verdant_tithe.txt |
| Heartwood Tree | Full connection | +20 | - | forest +30 | verdant_tithe.txt |
| Heartwood Tree | Moderate bond | +10 | - | forest +15 | verdant_tithe.txt |
| Heartwood Tree | Minimal contact | +0 | - | forest +5 | verdant_tithe.txt |

**Balance Check:**
- ⚠️ CRITICAL: File is only 183 lines - verify these choices exist!
- ⚠️ High stat gains (+20, +30) may need verification
- ✅ Three-tier Heartwood choice provides good differentiation

**Recommended Thresholds:**
- Heartwood Guardian ending: forest >= 60, collaboration >= 50
- Forestbound Guardian ending: forest >= 40, collaboration >= 30
- Mid-range: collaboration 35-65

**ACTION REQUIRED:** Compare to HTML version - verdant_tithe.txt may be incomplete!

---

## ❄️ Rune Glacier Expedition

| Scene | Choice/Action | Collaboration | Relationships | Other Stats | Source File |
|-------|---------------|---------------|-------------|-------------|-------------|
| Glacier Entrance | Harmony approach | +15 | aria +10 | rune_mastery +10 | rune_glacier.txt |
| Glacier Entrance | Control approach | -10 | - | rune_mastery +5 | rune_glacier.txt |
| Ice Interaction | Partner with ice | +20 | - | rune_mastery +15 | rune_glacier.txt |
| Ice Interaction | Command ice | -15 | - | rune_mastery +10 | rune_glacier.txt |
| Aria's Lesson | Embrace teaching | +10 | aria +15 | rune_mastery +10 | rune_glacier.txt |
| Aria's Lesson | Independent study | +0 | - | rune_mastery +5 | rune_glacier.txt |
| Partnership Path | Accept glacier bond | +25 | - | glacier_bond +50 | rune_glacier.txt |
| Partnership Path | Maintain distance | +5 | aria +5 | - | rune_glacier.txt |

**Balance Check:**
- ⚠️ Large swings (+25, -15) need verification
- ⚠️ Need to verify glacier_bond stat exists/is used
- ✅ Aria relationship gains fit her role as glacier specialist
- ✅ Control path penalties align with game philosophy

**Recommended Thresholds:**
- Glacier Partner ending: glacier_bond >= 40 OR rune_mastery >= 50 + collaboration >= 40
- Runeweaver ending: rune_mastery >= 40, collaboration < 40
- Mid-range: collaboration 30-70

---

## 🏫 Academy Life & Optional Scenes

### Dorm Room Events
| Scene | Choice/Action | Collaboration | Relationships | Other Stats | Source File |
|-------|---------------|---------------|-------------|-------------|-------------|
| TBD | TBD | TBD | TBD | TBD | dorm_room.txt |

### Character Bonds
| Scene | Choice/Action | Collaboration | Relationships | Other Stats | Source File |
|-------|---------------|---------------|-------------|-------------|-------------|
| TBD | TBD | TBD | TBD | TBD | character_bonds.txt |

### Romance Scenes
| Scene | Choice/Action | Collaboration | Relationships | Other Stats | Source File |
|-------|---------------|---------------|-------------|-------------|-------------|
| TBD | TBD | TBD | TBD | TBD | romance_scenes.txt |

**ACTION REQUIRED:** Review HTML game.js to see if these scenes existed or are new additions.

---

## 🏁 Ending Requirements

### High Collaboration Endings (60+)
| Ending Name | Required Stats | Source File | Verified |
|-------------|----------------|-------------|----------|
| Collaborative Master | collaboration >= 80, all_relationships >= 50 | endings.txt | ⏳ |
| Collaborative Scholar | collaboration >= 60, collaboration < 80 | endings.txt | ⏳ |

### Realm-Specific Endings
| Ending Name | Required Stats | Source File | Verified |
|-------------|----------------|-------------|----------|
| Truthbound Mage | truth >= 40, collaboration >= 30 | endings.txt | ⏳ |
| Forestbound Guardian | forest >= 40, collaboration >= 30 | endings.txt | ⏳ |
| Heartwood Guardian | forest >= 60, collaboration >= 50 | endings.txt | ⏳ |
| Runeweaver | rune_mastery >= 40, collaboration < 40 | endings.txt | ⏳ |
| Glacier Partner | glacier_bond >= 40 OR (rune_mastery >= 50, collaboration >= 40) | endings.txt | ⏳ |

### Balanced/Neutral Endings
| Ending Name | Required Stats | Source File | Verified |
|-------------|----------------|-------------|----------|
| Balanced Mage | collaboration 40-60, no extreme stats | endings.txt | ⏳ |
| Boundary Specialist | aria >= 60 | endings.txt | ⏳ |
| Standard Path | No special requirements | endings.txt | ⏳ |

### Low/Failure Endings
| Ending Name | Required Stats | Source File | Verified |
|-------------|----------------|-------------|----------|
| Humble Seeker | collaboration < 30, good_intent = true | endings.txt | ⏳ |
| Humbled Student | collaboration < 20 | endings.txt | ⏳ |
| Second Chance | failed_once = true, recovered | endings.txt | ⏳ |
| Expelled | critical_failures >= 3 OR collaboration < 0 | endings.txt | ⏳ |

**ACTION REQUIRED:** Extract actual stat requirements from endings.txt file.

---

## 📈 Stat Progression Paths

### Collaborative Path (Target: 70-90 collaboration)
```
Startup: +0
Arrival (Curious): +10 → 10
First Lesson (Collaborate x2): +25 → 35
Expedition (High collaboration choices): +35 → 70
Final choices: +15 → 85
= Collaborative Master ending ✅
```

### Balanced Path (Target: 40-60 collaboration)
```
Startup: +0
Arrival (Confident): +5 → 5
First Lesson (Mixed): +15 → 20
Expedition (Moderate choices): +25 → 45
Final choices: +10 → 55
= Balanced Mage ending ✅
```

### Specialist Path (Target: Realm stat 60+, collaboration 30+)
```
Startup: +0
Arrival (Nervous): +5 → 5
First Lesson (Observe): +5 → 10
Forest (Full Heartwood): forest +65, collaboration +30 → 40
= Heartwood Guardian ending ✅
```

### Control Path (Target: < 30 collaboration, high skill)
```
Startup: +0
Arrival (Confident): +5 → 5
First Lesson (Solo): -5 → 0
Glacier (Control route): -15, rune +40 → -15 collaboration
Need recovery or locked to failure endings
= Need balancing! ⚠️
```

---

## ⚖️ Balance Analysis

### Current Issues
1. ⚠️ **Control path may be punitive** - Can you recover from negative collaboration?
2. ⚠️ **Realm stats may be too easy** - Getting 60+ forest in one expedition?
3. ⚠️ **Verdant Tithe file size** - Only 183 lines vs 931 (Dunes) and 1266 (Glacier)
4. ⏳ **Ending requirements unknown** - Need to extract from endings.txt

### Recommended Balancing
1. **Add recovery opportunities** - Allow control-path players to learn collaboration
2. **Spread realm stat gains** - Make 60+ require multiple good choices
3. **Verify stat ranges** - Check startup.txt for min/max values
4. **Test all paths** - Ensure each ending is reachable

---

## 🎯 Difficulty Curve Goals

### Target Stat Distributions (End of Game)
- **Easy path (collaborative):** 70-90 collaboration
- **Medium path (balanced):** 40-60 collaboration  
- **Hard path (specialist):** High realm stat (60+), moderate collaboration (30-50)
- **Expert path (control):** High skill stats, low collaboration (with recovery options)

### Required Passes Per Ending
- Common endings (Standard, Balanced): 1-2 playthroughs
- Specialized endings (Realm-specific): 2-3 targeted playthroughs
- Secret endings (Glacier Partner, Heartwood Guardian): 3-4 playthroughs with knowledge
- Failure endings: Natural consequence of poor choices

---

## 🔍 Verification Checklist

### For Each Scene File:
- [ ] Extract all *set collaboration commands
- [ ] Extract all *set relationship commands  
- [ ] Extract all *set realm/special stat commands
- [ ] Calculate maximum possible stat gain
- [ ] Calculate minimum possible stat outcome
- [ ] Verify choices have meaningful differentiation (not all +5)
- [ ] Check for negative stat possibilities and recovery paths

### For Complete Game:
- [ ] Map one path to each of 14 endings
- [ ] Verify no impossible stat requirements
- [ ] Ensure no "trap" choices that lock out all good endings
- [ ] Test that skill requirements feel fair
- [ ] Balance difficulty across all paths

---

## 📝 Notes for Quality Balancer

### Philosophy
- **Collaboration is the core stat** - Should affect most endings
- **Realm stats are specializations** - High reward but narrow focus
- **Relationships enhance endings** - Should provide flavor, not gate content
- **Failure should be hard to achieve** - Players should feel competent

### Balancing Priorities
1. Make collaborative path rewarding but not easy mode
2. Make control path challenging but viable with skill
3. Make specialist paths feel distinct and powerful
4. Ensure failure endings require genuine mistakes, not bad luck

---

## 🚀 Next Actions

### Immediate (This Session)
1. Extract actual stat changes from all scene files
2. Count stat modifications per scene
3. Flag scenes with extreme values (+20, -15, etc.)
4. Verify verdant_tithe.txt completeness

### Short-Term (Next Session)
1. Test one complete playthrough per ending category
2. Document actual vs intended stat requirements
3. Identify unbalanced choices
4. Propose stat adjustments

### Medium-Term
1. Implement balancing changes
2. Re-test all paths
3. Adjust ending thresholds if needed
4. Final balance pass before beta

---

**Maintained By:** Quality Balancer AI  
**Update After:** Each scene verification, each stat change, each test playthrough  
**Format:** Table-based tracking with analysis notes
