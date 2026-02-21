# INSTRUCTIONS FOR GITHUB COPILOT AND AI ASSISTANTS

**Project:** Polly's Wingscroll: The First Thread
**Goal:** Expand ChoiceScript game from placeholders to 100+ fully-written scenes
**Priority:** HIGH - This is the main development focus

---

## WHAT THIS PROJECT IS

A choice-based interactive fiction game built in **ChoiceScript** (the engine used by Choice of Games/Hosted Games). The game follows a new student at Avalon Academy, guided by Polly - a sarcastic immortal raven.

**Current State:** Foundation complete, but expedition scenes are PLACEHOLDERS
**Target State:** Professional-quality game with 100+ scenes, each with meaningful depth

---

## YOUR TASK (FOR ANY AI WORKING ON THIS)

### Primary Goal
Expand the ChoiceScript files in `choicescript_game/scenes/` to match the quality of published Choice of Games titles.

### Files That Need Expansion

| File | Current State | Target |
|------|---------------|--------|
| `singing_dunes.txt` | ~12 lines placeholder | 500+ lines, 15-20 scenes |
| `verdant_tithe.txt` | ~12 lines placeholder | 500+ lines, 15-20 scenes |
| `rune_glacier.txt` | ~12 lines placeholder | 500+ lines, 15-20 scenes |
| `endings.txt` | ~12 lines placeholder | 300+ lines, 14 endings |

### Reference Material
- `game/game.js` - Contains ALL the story content to convert (use this as source)
- `choicescript_game/scenes/first_lesson.txt` - Example of proper ChoiceScript formatting

---

## CHOICESCRIPT SYNTAX GUIDE

### Basic Structure
```choicescript
*comment Scene header
*label scene_name

Narrative text here. Use [i]italics[/i] for emphasis.
Use [b]bold[/b] for important terms.

*line_break

More text after a visual break.

*choice
    #First choice option
        Result of choosing this.
        *set collaboration +5
        *goto next_scene
    #Second choice option
        Different result.
        *set some_stat -3
        *goto other_scene

*label next_scene
Continue the story here...
```

### Stat Modifications
```choicescript
*set collaboration +10
*set izack_relationship +5
*set aria_relationship -3
```

### Conditionals
```choicescript
*if collaboration > 60
    High collaboration text.
*elseif collaboration > 30
    Medium collaboration text.
*else
    Low collaboration text.
```

### Polly's Commentary
Always use italics for Polly's sarcastic narrator voice:
```choicescript
[i]"And here we go again. Another student about to learn the hard way."[/i]
```

### Scene Transitions
```choicescript
*goto_scene singing_dunes
*goto label_name
*finish
```

---

## SCENE EXPANSION TEMPLATE

Each major location should have this structure:

```
1. ARRIVAL (1-2 scenes)
   - Initial description of the location
   - First impressions
   - Polly's commentary
   - Introduction to local guide/character

2. EXPLORATION (3-5 scenes)
   - Multiple paths to explore
   - Environmental storytelling
   - Learning about the location's magic
   - Character interactions
   - Stat-based variations

3. CHALLENGE (3-5 scenes)
   - Central test or conflict
   - Multiple approaches (collaboration vs solo)
   - Consequences of choices
   - Character development moments

4. RESOLUTION (2-3 scenes)
   - Outcomes based on earlier choices
   - Lessons learned
   - Rewards/artifacts earned
   - Lead-in to endings

5. BRANCHES (varies)
   - Alternative paths
   - Hidden discoveries
   - Relationship-specific scenes
```

---

## SINGING DUNES EXPANSION GUIDE

### Setting
- Truth-testing desert where sand judges honesty
- Oath-bound sand spirits
- Ironwood oases
- Guide: Kael (desert sage)

### Required Scenes
1. `dunes_arrival` - Portal arrival, first impression of golden sand
2. `dunes_kael_intro` - Meeting Kael, learning desert rules
3. `dunes_sand_test_intro` - Explanation of truth-sworn sand
4. `dunes_first_truth` - Initial truth test (3+ choices)
5. `dunes_honest_path` - Reward for vulnerability
6. `dunes_safe_path` - Result of playing it safe
7. `dunes_rejection` - Consequence of lying
8. `dunes_oasis_discovery` - Finding the Ironwood oasis
9. `dunes_sand_spirits` - Encountering oath-bound spirits
10. `dunes_oath_magic_lesson` - Learning to bind promises
11. `dunes_night_mirages` - Twilight vision sequence
12. `dunes_kael_wisdom` - Deep conversation with guide
13. `dunes_final_test` - Major truth challenge
14. `dunes_truthbound_success` - Earning desert's blessing
15. `dunes_departure` - Leaving with new knowledge

### Key Mechanics
- Truth level tracking (honest choices accumulate)
- Sand's response changes based on truthfulness
- Relationship with Kael affects what you learn
- Multiple ending paths based on honesty

---

## VERDANT TITHE EXPANSION GUIDE

### Setting
- Sentient forest that reads thoughts
- Thoughtvines share consciousness
- Dreamwillows show possible futures
- Heartwood Tree is the forest's heart
- Guide: Izack leads this expedition

### Required Scenes
1. `forest_arrival` - Entering the living forest
2. `forest_first_thoughts` - Thoughtvines react to you
3. `forest_path_choice` - Three paths diverge
4. `dreamwillow_grove` - Silver tree visions
5. `dreamwillow_vision_good` - Collaborative future
6. `dreamwillow_vision_bad` - Isolated future
7. `dreamwillow_vision_crisis` - World-shaking choice
8. `thoughtvine_deep` - Merging with forest mind
9. `thoughtvine_memory` - Forest shares its history
10. `thoughtvine_question` - Forest asks for promise
11. `heartwood_approach` - Nearing the ancient tree
12. `heartwood_test` - The Tithe demands payment
13. `heartwood_communion` - Becoming forest-bound
14. `heartwood_rejection` - Forest finds you wanting
15. `forest_departure` - Leaving with new connection

### Key Mechanics
- Thoughts are visible to the forest
- Quieting your mind affects outcomes
- Memory sharing with ancient consciousness
- Different paths lead to different endings

---

## RUNE GLACIER EXPANSION GUIDE

### Setting
- Living ice inscribed with adaptive runes
- Frozen spell library
- Ice responds to magical intention
- Guide: Aria teaches boundary magic here

### Required Scenes
1. `glacier_arrival` - Stepping onto living ice
2. `glacier_runes_awaken` - Runes respond to your presence
3. `glacier_aria_lesson` - Boundary magic introduction
4. `glacier_approach_choice` - Control vs Harmony
5. `glacier_control_attempt` - Trying to dominate ice
6. `glacier_control_success` - Mastering ice through force
7. `glacier_control_backlash` - Ice resists domination
8. `glacier_harmony_attempt` - Partnering with ice
9. `glacier_harmony_deep` - Ice accepts partnership
10. `glacier_spell_library` - Discovering frozen knowledge
11. `glacier_ancient_runes` - Reading the oldest inscriptions
12. `glacier_boundary_test` - Testing magical limits
13. `glacier_partnership_bond` - Forming lasting connection
14. `glacier_runeweaver_path` - Control mastery ending
15. `glacier_departure` - Leaving with ice's blessing

### Key Mechanics
- Control vs Harmony stat tracking
- Ice responds differently to each approach
- Aria's approval affects what you learn
- Hidden paths for high-collaboration players

---

## ENDINGS EXPANSION GUIDE

### All 14 Endings Required

Each ending needs:
- 30-50 lines of text
- Personalized based on journey
- Polly's final commentary
- Achievement unlock
- `*ending` command

### Ending List
1. `ending_collaborative_master` - Highest collaboration
2. `ending_truthbound_mage` - Desert blessing
3. `ending_forestbound_guardian` - Forest connection
4. `ending_heartwood_guardian` - Deepest forest bond (rare)
5. `ending_runeweaver` - Glacier control master
6. `ending_glacier_partner` - Ice partnership
7. `ending_balanced_mage` - Middle path
8. `ending_boundary_specialist` - Aria's protege
9. `ending_collaborative_scholar` - Teaching focus
10. `ending_humble_seeker` - Wisdom through humility
11. `ending_second_chance` - Recovery from failure
12. `ending_humbled_student` - Learned through rejection
13. `ending_expelled` - Failed completely (dramatic)
14. `ending_standard_path` - Neutral completion

---

## QUALITY STANDARDS

### Every Scene Must Have:
- [ ] Vivid environmental description (2-3 sentences minimum)
- [ ] Polly commentary (at least once per scene)
- [ ] Meaningful choice with consequences
- [ ] Stat modifications that matter
- [ ] Connection to overall narrative

### Polly's Voice Guidelines
- Sarcastic but caring
- 3000+ years old, seen everything
- Fourth-wall aware
- Actually wants students to succeed
- Never cruel, but brutally honest

Example:
```
[i]"Oh good, you're about to do the thing. You know, the thing where you think you're smarter than the ancient magical desert. This always ends well."[/i]
```

### Prose Quality
- Literary but accessible
- Show don't tell
- Sensory details (sight, sound, smell, feel)
- Emotional resonance
- Consistent tone throughout

---

## CONVERSION PROCESS

When converting from `game/game.js` to ChoiceScript:

1. **Find the scene** in game.js (search for the node name)
2. **Extract the narrative** from the `text` property
3. **Remove HTML tags** and convert to ChoiceScript formatting
4. **Expand the content** - add 2-3x more detail
5. **Add Polly commentary** if missing
6. **Convert choices** to `*choice` blocks
7. **Add stat effects** with `*set` commands
8. **Add conditionals** for stat-based variations
9. **Test the flow** with `*goto` statements

---

## EXAMPLE CONVERSION

### Original (game.js):
```javascript
singing_dunes_journey: {
    text: `
        <p>The portal opens onto endless golden sand...</p>
        <p><span class="polly-comment">"Welcome to the truth desert..."</span></p>
    `,
    choices: [
        { text: "Speak a vulnerable truth", next: 'dunes_honest_truth' },
        { text: "Share something safe", next: 'dunes_safe_truth' }
    ]
}
```

### Expanded (ChoiceScript):
```choicescript
*label dunes_arrival

The portal deposits you onto golden sand that gleams with crystalline fragments. Each grain catches the light differently, creating a landscape that seems to shimmer with hidden meaning.

The heat is immediate but not oppressive—the desert's warmth feels almost welcoming, like it's been waiting for you.

*line_break

In the distance, dunes rise like frozen waves, their crests singing in the wind. The sound is haunting—a harmony that seems to carry words just beyond understanding.

[i]"Welcome to the Sunscarred Dunes, where the sand itself passes judgment. Every lie you've ever told? The desert remembers. Every truth you've avoided? It knows. Sleep well tonight."[/i]

*line_break

Your expedition guide, a weathered man named Kael, steps forward. His robes are the color of sunset sand, and his eyes hold the patience of someone who has watched the desert for decades.

"The Singing Dunes test all who enter," he says, his voice carrying the dry rasp of wind over stone. "They seek truth—not facts, but the truth of who you are. Are you prepared to be known?"

*page_break

He produces small vials of sand, one for each student.

"These will be your witnesses. The sand will react to your words. Gold for truth, red for deception. The desert is patient, but it does not forget."

[i]"Pro tip: the desert has been doing this for about ten thousand years. It's very, very good at spotting lies. Even the ones you tell yourself."[/i]

*choice
    #"I'm ready. I have nothing to hide."
        Kael's eyes crinkle with something between amusement and respect.

        "Bold. The desert appreciates directness, even if it later proves... optimistic."

        *set collaboration +5
        *goto dunes_first_test

    #"What happens if the sand turns red?"
        "The desert's displeasure," Kael says simply. "Minor deceptions bring minor consequences—a burned hand, a night of troubled dreams. Major lies..."

        He doesn't finish, but Polly does.

        [i]"Let's just say the desert has been known to swallow people whole. Not often! But, you know. It happens."[/i]

        *goto dunes_first_test

    #"Can we just... observe? See how others do it first?"
        *set collaboration -3

        Kael shakes his head slowly.

        "The desert does not permit spectators. You enter, you are tested. There is no middle ground in the Singing Dunes."

        [i]"Translation: no hiding at the back of the class here. The desert is about to get very personal with you whether you like it or not."[/i]

        *goto dunes_first_test
```

---

## VERIFICATION CHECKLIST

Before submitting any scene expansion:

- [ ] All `*goto` targets exist
- [ ] All `*label` names are unique
- [ ] Stats are properly modified
- [ ] Polly has at least one comment per major scene
- [ ] Choices lead to meaningful different outcomes
- [ ] No dead ends (every path continues or ends properly)
- [ ] Tone matches established style
- [ ] Environmental details are vivid
- [ ] Character voices are consistent

---

## HOW TO HELP

### If you're Copilot/AI assistant:
1. Read this document fully
2. Check `game/game.js` for source content
3. Use `first_lesson.txt` as formatting reference
4. Expand one scene file at a time
5. Follow the templates above
6. Maintain quality standards
7. Test that all gotos resolve

### Priority Order:
1. `singing_dunes.txt` (most developed in game.js)
2. `verdant_tithe.txt` (complex branching)
3. `rune_glacier.txt` (needs control/harmony mechanics)
4. `endings.txt` (requires all paths to exist first)

---

## CONTACT

This project is maintained by @issdandavis on GitHub.
AI session handoff documentation: `docs/AI_SESSION_HANDOFF.md`
Task queue: `docs/NEXT_TASKS.md`

---

*"The spiral continues. Every scene you write adds another thread."*

**Last Updated:** November 22, 2025
**By:** Claude Code Session (teleport-session-recovery)
