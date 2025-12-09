# 🎓 Codex Connector Example Workflow

## Real-World Example: Converting a Scene Using the Codex Connector

This example shows how to use the Codex Connector to convert `singing_dunes.txt` from HTML to ChoiceScript using multiple AI assistants.

---

## Scenario

**Goal:** Convert the Singing Dunes expedition from the HTML game to ChoiceScript  
**Participants:** 4 different AI assistants  
**Time:** ~30 minutes with coordination

---

## Step-by-Step Workflow

### Step 1: Lore Curator Reviews (AI #1)

**You say to the Lore Curator AI:**
```
You're the Lore Curator for The Avalon Codex project.

Please review the Singing Dunes content in game/game.js 
and validate it against the established lore in the lore/ directory.

Check:
- Is Kael's character consistent?
- Does the desert magic match established rules?
- Are there any timeline conflicts?

Update STATUS_CONTEXT.md with your findings.
```

**Lore Curator Response:**
```
✅ Reviewed Singing Dunes content

Findings:
- Kael's character is consistent with desert sage archetype
- Truth-testing sand aligns with oath magic in lore/magic_systems.txt
- No timeline conflicts detected
- Suggested enhancement: Reference the "Sunscarred Accords" 
  mentioned in lore/historical_events.txt

Updated STATUS_CONTEXT.md:
- Added: "Singing Dunes ready for conversion - lore approved"
- Noted: Enhancement suggestion for Sunscarred Accords reference

Commit: `Lore: Validated Singing Dunes against desert lore canon`
```

---

### Step 2: Conversion Engineer Drafts (AI #2)

**You say to the Conversion Engineer AI:**
```
You're the Conversion Engineer for The Avalon Codex project.

The Lore Curator approved the Singing Dunes content.
Please convert it from game/game.js to ChoiceScript format
in choicescript_game/scenes/singing_dunes.txt

Follow the template in .github/COPILOT_INSTRUCTIONS.md
Use first_lesson.txt as a formatting reference.

Mark the scene as 🚧 Draft in SCENE_PARITY_CHECKLIST.md
```

**Conversion Engineer Response:**
```
✅ Drafted singing_dunes.txt (487 lines)

Implemented:
- 15 scene labels as specified in requirements
- Kael introduction with proper characterization
- Truth-testing mechanics with stat tracking
- Polly's sarcastic commentary throughout
- Branching paths based on honesty choices
- Integration with Sunscarred Accords lore

Stats added:
- *set truth_level tracking
- *set collaboration modifications
- *set kael_relationship tracking

Updated SCENE_PARITY_CHECKLIST.md:
- singing_dunes.txt: ❌ Missing → 🚧 Draft

Commit: `Convert: Drafted singing_dunes.txt from HTML source`
```

---

### Step 3: Structural Reviewer Verifies (AI #3)

**You say to the Structural Reviewer AI:**
```
You're the Structural Reviewer for The Avalon Codex project.

Please verify choicescript_game/scenes/singing_dunes.txt 
matches the HTML source in game/game.js

Check:
- All choice paths lead somewhere
- Scene count matches original
- No dead ends
- Proper *goto connections
- All endings are reachable

Update SCENE_PARITY_CHECKLIST.md with findings.
```

**Structural Reviewer Response:**
```
✅ Verified singing_dunes.txt structure

Verification Results:
- Scene count: 15/15 ✅
- All *goto targets exist ✅
- No dead ends detected ✅
- Branching logic preserved ✅
- 3 possible outcomes lead correctly to final_trial.txt ✅

Minor Issues Found:
- Line 247: *goto dunes_kael_wisdom should be *goto_scene character_bonds
- Line 389: Missing *line_break before Polly commentary

Fixed both issues in commit.

Updated SCENE_PARITY_CHECKLIST.md:
- singing_dunes.txt: 🚧 Draft → ✅ Verified (with minor fixes)

Commit: `Struct: Verified singing_dunes.txt parity and fixed gotos`
```

---

### Step 4: Quality Balancer Tunes Stats (AI #4)

**You say to the Quality Balancer AI:**
```
You're the Quality Balancer for The Avalon Codex project.

Please analyze stat modifications in singing_dunes.txt
and ensure they're balanced relative to other expeditions.

Extract all stat changes to STATS_MATRIX.md
Check if endings are still reachable with these values.
Recommend adjustments if needed.
```

**Quality Balancer Response:**
```
✅ Balanced singing_dunes.txt stats

Analysis:
- Total collaboration available: +45 (honest path) / -15 (deceptive path)
- Kael relationship: -10 to +30 range
- Truth level: 0 to 100 tracking

Comparison to other expeditions:
- Verdant Tithe: +50 collaboration available
- Rune Glacier: +40 collaboration available
- ✅ Singing Dunes is well-balanced

Adjustments Made:
- Increased collaboration bonus for "dunes_truthbound_success" from +15 to +20
- This ensures honest path players can reach Collaborative Master ending
- All 14 endings remain reachable ✅

Updated STATS_MATRIX.md:
- Added all 23 stat-modifying choices from singing_dunes.txt
- Documented balance rationale
- Verified ending thresholds

Commit: `Balance: Tuned singing_dunes.txt collaboration rewards`
```

---

## Final Result

**✅ Complete Scene Ready for Play Testing**

**What We Accomplished:**
- Converted 1 HTML expedition to professional ChoiceScript
- Validated lore consistency
- Ensured structural integrity
- Balanced gameplay difficulty
- All in ~30 minutes with 4 AI assistants

**Updated Files:**
- ✅ `choicescript_game/scenes/singing_dunes.txt` (new, 487 lines)
- ✅ `STATUS_CONTEXT.md` (progress tracked)
- ✅ `SCENE_PARITY_CHECKLIST.md` (scene verified)
- ✅ `STATS_MATRIX.md` (stats documented)

**Git History:**
```
Balance: Tuned singing_dunes.txt collaboration rewards
Struct: Verified singing_dunes.txt parity and fixed gotos
Convert: Drafted singing_dunes.txt from HTML source
Lore: Validated Singing Dunes against desert lore canon
```

---

## Key Takeaways

### Why This Worked Well

1. **Clear Role Division**
   - Each AI had a specific expertise area
   - No overlap or conflicting edits
   - Each built on the previous work

2. **Shared Context Files**
   - All AIs updated the same tracking files
   - Progress was visible to everyone
   - Easy to see what's done vs. what's next

3. **Structured Hand-offs**
   - Each AI knew what to expect from the previous one
   - Clear completion criteria
   - Commit messages showed progression

4. **Quality Preserved**
   - Multiple review passes
   - Specialized expertise at each stage
   - No loss of quality from delegation

---

## Try It Yourself!

### Quick Test (5 minutes)

1. **Pick a small task:** "Update Polly's dialogue in first_lesson.txt to be more sarcastic"

2. **Assign roles:**
   - Lore Curator: Review proposed changes
   - Conversion Engineer: Make the edits
   - Structural Reviewer: Verify nothing broke

3. **Use the workflow:**
   - Each AI reads `STATUS_CONTEXT.md`
   - Each AI does their part
   - Each AI updates the shared files

4. **Check the result:**
   - Did the dialogue improve?
   - Did everyone know what happened?
   - Could you hand this off to another AI?

---

## Common Patterns

### Pattern 1: Solo AI Can Use It Too
Even if you're working with just one AI, you can use the system:
- Have the AI read the status files
- Update the checklists as you work
- Leave clear notes for your next session
- Your future self (or another AI) can pick up seamlessly

### Pattern 2: Asynchronous Collaboration
AIs don't have to work at the same time:
- Morning: Lore Curator validates 3 scenes
- Afternoon: Conversion Engineer converts 1 of them
- Evening: You review the result
- Next day: Structural Reviewer verifies it

The shared files keep everyone synchronized.

### Pattern 3: Parallel Work
Multiple AIs can work on different scenes simultaneously:
- AI #1 converts `singing_dunes.txt`
- AI #2 converts `verdant_tithe.txt`
- AI #3 balances stats for completed scenes
- All update their own sections of the checklists

No conflicts because each works on different files.

---

## Troubleshooting

### "The AI didn't update the status files"
**Fix:** Explicitly remind them:
```
Before you finish, please update STATUS_CONTEXT.md 
with what you accomplished.
```

### "Two AIs edited the same thing"
**Fix:** Use the role system:
```
You're the Lore Curator. 
Only make lore validation changes, not code changes.
Leave code changes for the Conversion Engineer.
```

### "I lost track of what's done"
**Fix:** Check the checklists:
```
Read SCENE_PARITY_CHECKLIST.md
What scenes are marked ✅ Verified?
```

---

## Next Steps

1. **Try the example workflow** with your own AIs
2. **Adapt the roles** to your specific needs
3. **Customize the shared files** for your project
4. **Share your results** - what worked? what didn't?

---

**The Codex Connector makes multi-AI collaboration effortless.**

*Ready to start? Read [CODEX_CONNECTOR_USAGE.md](CODEX_CONNECTOR_USAGE.md)*
