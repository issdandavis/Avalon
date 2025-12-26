# AI Communication Channels

This directory contains communication logs between AI agents working on The Avalon Codex project. Each channel serves a specific purpose for cross-agent coordination.

## Channel Guide

### 📌 channel_alpha.md - Priorities & Status
**Purpose:** High-level task prioritization and status updates
**When to update:** After completing major milestones or shifting focus
**Format:** ISO timestamp + priority summary + current status + next actions

### 💡 channel_beta.md - Scene Ideas & Content
**Purpose:** Creative suggestions for game scenes and narrative improvements
**When to update:** When brainstorming new content or identifying gaps
**Format:** ISO timestamp + scene description + implementation notes + action items

### 🔧 channel_gamma.md - Build Tips & Technical Notes
**Purpose:** Technical guidance for building, testing, and running the project
**When to update:** When discovering build issues or documenting setup steps
**Format:** ISO timestamp + technical tip + context + verification steps

### 📚 channel_delta.md - Lore Index & References
**Purpose:** Track location of lore documents and maintain canonical references
**When to update:** When adding new lore or reorganizing documents
**Format:** ISO timestamp + lore location + cross-references + sync actions

## Usage Guidelines

### Adding Entries
1. Use ISO 8601 timestamps (YYYY-MM-DDTHH:MM:SSZ)
2. Format as: `**[timestamp]** — [Topic]: [details]. Next actions: [specific steps].`
3. Number entries sequentially (1., 2., 3., etc.)
4. Keep each entry focused on a single topic
5. Always include "Next actions" for actionable items

### Reading Logs
- **Latest entry is at the bottom** of each numbered list
- Scan for most recent timestamp to get current state
- Look for "Next actions" to see what needs doing
- Cross-reference between channels for related work

### Workflow Example
```
1. Check channel_alpha for current priorities
2. Review channel_gamma for any build/setup notes
3. Consult channel_delta for lore reference locations
4. Add content ideas to channel_beta
5. Update channel_alpha when work is complete
```

## Integration with Repository

### Related Files
- `docs/PROJECT_ROADMAP.md` - Overall development plan
- `QUICK_START.md` - User-facing quick start guide
- `docs/AUTOMATION_GUIDE.md` - Zapier and tool integration

### AI Agent Coordination
These logs enable:
- Handoff between different AI assistants
- Persistent context across sessions
- Avoiding duplicate work
- Maintaining consistent lore and technical decisions

## Best Practices

### ✅ DO:
- Timestamp every entry accurately
- Be specific about file paths and locations
- Include actionable next steps
- Update when completing tasks mentioned in "Next actions"
- Keep entries concise but informative

### ❌ DON'T:
- Add vague or incomplete entries
- Delete old entries (append new ones)
- Mix multiple unrelated topics in one entry
- Forget to update after completing actions
- Use ambiguous file references

## Channel Naming Convention

Channels use Greek letters to maintain clear identity while avoiding confusion with repository folders:
- **Alpha (α)** = First/Primary = Priorities
- **Beta (β)** = Second/Creative = Scene Ideas  
- **Gamma (γ)** = Third/Technical = Build Tips
- **Delta (Δ)** = Fourth/Foundation = Lore Index

---

**Last Updated:** 2025-12-26
**Purpose:** Enable seamless multi-AI collaboration on The Avalon Codex
**Status:** Active and ready for use
