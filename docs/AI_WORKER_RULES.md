# 🤖 RULES FOR AUTONOMOUS AI WORKERS
## Guidelines for AI Agents Working Independently on Avalon

**Purpose:** Ensure AI workers make safe, high-quality contributions  
**Audience:** Autonomous AI agents, GitHub Actions, API-driven workers

---

## ✅ ALWAYS DO

### Code Quality
- **Make small, incremental changes** - One feature or scene at a time
- **Test changes before committing** - Verify ChoiceScript syntax
- **Follow existing patterns** - Match the style of surrounding code
- **Preserve working code** - Don't delete or break existing functionality
- **Add descriptive comments** - Explain complex logic or choices

### Version Control
- **Write meaningful commit messages** - Describe what and why
- **Commit frequently** - After each completed task
- **Work on feature branches** - Use `ai-autonomous-work` branch
- **Tag commits with [AI-AUTO]** - Make AI work clearly identifiable
- **Update task queue** - Mark tasks complete as you finish them

### Documentation
- **Log all decisions** - Document reasoning in commit messages
- **Update progress reports** - Keep AI_TASK_QUEUE.md current
- **Flag uncertainties** - Create AI_QUESTIONS.md entries when unsure
- **Maintain audit trail** - Track what you changed and why

### Content Quality (Spiralverse Specific)
- **Follow sensory rule** - Every scene needs taste OR smell
- **Preserve character voices:**
  - Izack: Nervous, wondering, self-deprecating
  - Polly: Sarcastic, wise, caws frequently  
  - Aria: Precise, quiet, boundary-focused
  - Zara: Warm, dragon-blooded, naturalist
  - Alexander: Curious, questioning, diplomatic
- **Use collaborative magic philosophy** - Magic is about partnership, not domination
- **Maintain lore consistency** - Check IZACK_MASTER_CHRONICLE_UPDATED.txt

---

## ❌ NEVER DO

### Dangerous Actions
- **Delete working code** - Unless explicitly instructed to remove it
- **Make breaking changes** - Don't modify public APIs or published features
- **Commit secrets** - No API keys, passwords, or credentials
- **Override human changes** - If a human edited recently, pause and flag
- **Work on multiple tasks simultaneously** - Focus on one thing at a time
- **Push directly to main branch** - Always use feature branches

### Quality Violations
- **Ship broken code** - Always verify syntax before committing
- **Ignore test failures** - Fix failing tests, don't ignore them
- **Break character voice** - Stay true to established personalities
- **Violate lore** - Check canon before inventing new rules
- **Skip sensory details** - Every scene must engage the senses

### Process Violations
- **Skip the task queue** - Work in priority order
- **Forget to log work** - Update task queue and commit messages
- **Work without context** - Read related files before changing them
- **Assume unstated requirements** - Flag ambiguities for review

---

## 🤔 WHEN UNCERTAIN

### Decision Framework

**If you're unsure about:**

#### **Lore or Story Decisions**
1. ✅ Check IZACK_MASTER_CHRONICLE_UPDATED.txt
2. ✅ Review existing scenes for patterns
3. ✅ Choose the most conservative option
4. ✅ Flag for human review in AI_QUESTIONS.md
5. ❌ Don't invent new canon without approval

#### **Technical Decisions**
1. ✅ Look at similar code elsewhere in the project
2. ✅ Choose the simplest solution
3. ✅ Add a comment explaining your reasoning
4. ✅ Create a draft PR for review if complex
5. ❌ Don't refactor large sections without approval

#### **Writing Style Decisions**
1. ✅ Match the tone of surrounding scenes
2. ✅ Prioritize clarity over cleverness
3. ✅ Include sensory details (taste/smell rule)
4. ✅ Keep Polly sarcastic and wise
5. ❌ Don't experiment with radically different styles

### When to Pause and Ask

**STOP AND FLAG FOR REVIEW IF:**
- Lore conflicts with itself
- Character voice feels wrong
- Technical solution seems risky
- Task requires deleting substantial code
- Multiple valid approaches exist
- Human input would save time
- You're repeating the same fix multiple times

**How to Flag:**
Create entry in `docs/AI_QUESTIONS.md`:
```markdown
## Question: [Brief description]
**Date:** 2025-11-25  
**Task:** Singing Dunes Scene 4  
**Issue:** Unsure if sand should reject player or give warning  
**Options:**
1. Outright rejection (player fails expedition)
2. Warning + second chance (player can try again)
3. Partial acceptance (player gets lesser artifact)

**Recommendation:** Option 2 (matches game's forgiving tone)  
**Needs:** Human decision on difficulty curve
```

---

## 📏 QUALITY STANDARDS

### ChoiceScript Syntax
```choicescript
✅ GOOD:
*comment Clear comment explaining what follows
*label scene_name
*if (collaboration > 70)
  *set artifact_earned "Truth-Sworn Sand"
  The sand swirls around your hand, warm and approving.
*goto next_scene

❌ BAD:
*label scene name  # Spaces in label names not allowed
*if collaboration>70  # Missing parentheses
  artifact_earned = "Truth-Sworn Sand"  # Wrong syntax for *set
  # Missing descriptive text
*goto next scene  # Spaces in scene names not allowed
```

### Sensory Writing
```
✅ GOOD (includes taste):
The sand swirls around your hand. When you speak your truth, 
the air tastes of honey and distant starlight.

✅ GOOD (includes smell):
Kael approaches, robes carrying the scent of sun-baked stone 
and cinnamon.

❌ BAD (no sensory detail):
The sand swirls around your hand. You feel it judging you.
```

### Character Voice
```
✅ GOOD (Polly's voice):
"Caw! Truth-telling in a truth-testing desert? How delightfully 
redundant. Like being wet in the ocean. Still, try not to lie."

✅ GOOD (Izack's voice):
"I, um, once tried to lie to the Singing Dunes," Izack says 
nervously. "My hand burned for three days. The sand remembers 
grudges better than I remember breakfast."

❌ BAD (generic voice):
"Be careful in the desert," the character says. "It can detect lies."
```

---

## 🎯 TASK EXECUTION CHECKLIST

Before starting any task:
- [ ] Read task description in AI_TASK_QUEUE.md
- [ ] Understand success criteria
- [ ] Review related existing code
- [ ] Check lore documents if needed
- [ ] Note any uncertainties

While working:
- [ ] Make changes incrementally
- [ ] Test syntax frequently
- [ ] Preserve character voices
- [ ] Add sensory details
- [ ] Follow ChoiceScript best practices

Before committing:
- [ ] Verify ChoiceScript syntax is valid
- [ ] Check that all labels are referenced
- [ ] Ensure all scenes have *goto or *finish
- [ ] Confirm character voices match canon
- [ ] Include taste OR smell in new scenes
- [ ] Write descriptive commit message

After committing:
- [ ] Update AI_TASK_QUEUE.md
- [ ] Mark task as complete
- [ ] Log any decisions made
- [ ] Note any questions for humans

---

## 🚨 ERROR HANDLING

### If You Encounter an Error

**Syntax Error:**
1. Read error message carefully
2. Check ChoiceScript documentation
3. Look at similar working code
4. Fix and test again
5. If still failing, flag for review

**Lore Conflict:**
1. Document the conflict
2. Check master chronicle
3. Choose most canon option
4. Flag discrepancy for review
5. Continue with conservative choice

**Merge Conflict:**
1. **STOP immediately**
2. Do not attempt to resolve automatically
3. Flag for human review
4. Document what you were trying to do
5. Wait for human intervention

**Unexpected Behavior:**
1. Document what happened vs. what you expected
2. Check recent changes
3. Roll back if necessary
4. Flag for review
5. Pause work on that task

---

## 🔄 CONTINUOUS IMPROVEMENT

### Learning from Each Task

**After completing a task, reflect:**
- What went well?
- What was challenging?
- What would you do differently?
- What patterns did you learn?

**Update your knowledge:**
- Note successful patterns
- Document common pitfalls
- Refine your approach
- Share insights in commit messages

---

## 📋 EXAMPLE WORKFLOW

### Complete Task: "Add Scene 1-3 to singing_dunes.txt"

**Step 1: Preparation**
```bash
# Read task requirements
# Check AI_TASK_QUEUE.md for success criteria
# Review existing singing_dunes.txt structure
# Read lore about Singing Dunes
```

**Step 2: Implementation**
```bash
# Create draft of Scene 1 (desert arrival)
# Add sensory details (taste of copper, smell of hot sand)
# Include Polly commentary
# Test ChoiceScript syntax
# Commit: "[AI-AUTO] Add singing_dunes.txt Scene 1 - Desert arrival"

# Repeat for Scenes 2 and 3
```

**Step 3: Verification**
```bash
# Re-read all three scenes
# Verify character voices
# Check for sensory details in each
# Ensure proper *goto flow
# Test that stats update correctly
```

**Step 4: Completion**
```bash
# Update AI_TASK_QUEUE.md - mark task [x]
# Final commit: "[AI-AUTO] Complete singing_dunes.txt Scenes 1-3"
# Create summary in logs/ai-work-YYYY-MM-DD.md
```

---

## 🎨 SPIRALVERSE-SPECIFIC GUIDELINES

### Magic System Rules
- **Collaborative magic** > Hierarchical magic
- Magic tastes of copper, mint, or starlight
- Dimensional barriers respond to emotion
- Polly appears when dimensionally relevant

### Avalon Academy Culture
- Students learn through collaboration
- Failure is a teaching tool, not punishment
- Multiple valid paths to mastery
- Balance of tradition and innovation

### Narrative Tone
- Whimsical but with emotional depth
- Sarcastic (via Polly) but kind
- Wonder balanced with practicality
- Hope even in difficult moments

---

## 🌟 ASPIRATIONAL GOALS

Strive to make work that:
- Makes players feel seen and valued
- Balances humor with emotional impact
- Rewards curiosity and exploration
- Respects player agency
- Ships quality over quantity

---

**Remember:** You are not just writing code.  
You are weaving stories that taste of starlight and tomorrow.

**The spiral turns. The code compiles. The players choose.**

**Caw.** 🪶
