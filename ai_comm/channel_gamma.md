# Channel Gamma - Build Tips & Technical Notes

## Purpose
Technical guidance for building, testing, and running the project.

---

## Log Entries

### Entry 1
**2025-12-26T06:23:54Z** — Build/run tips: HTML version playable via game/index.html; ChoiceScript scenes live in choicescript_game/scenes but require ChoiceScript IDE or compile step (see QUICK_START.md). For quick diff scans, use `rg` instead of recursive grep. Next actions: run a fast sanity check by opening game/index.html locally or linting scenes for stray tabs if time allows.

---

## Quick Reference

### Playing/Testing the Game

#### HTML Version (Instant)
```bash
# Navigate to game directory
cd game/

# Open in browser
open index.html  # macOS
xdg-open index.html  # Linux
start index.html  # Windows
```

#### ChoiceScript Version (Professional)
```bash
# Requires ChoiceScript IDE download
# 1. Download from: https://www.choiceofgames.com/make-your-own-games/choicescript-intro/
# 2. Copy files from choicescript_game/ to ChoiceScript's web/mygame/
# 3. Open ChoiceScript's index.html
```

### Development Tools

#### Fast Code Search
```bash
# Use ripgrep for fast searching (rg)
rg "pattern" path/to/search

# Example: Find all TODO markers
rg "TODO" choicescript_game/scenes/

# Example: Search for stat changes
rg "collaboration" game/game.js
```

#### File Structure Check
```bash
# List ChoiceScript scenes
ls choicescript_game/scenes/*.txt

# Check for required startup file
test -f choicescript_game/scenes/startup.txt && echo "✓ Startup found"
```

### Common Issues

#### ChoiceScript Errors
- **"Missing scene"**: Check scene list in startup.txt *scene_list
- **"Invalid indentation"**: ChoiceScript uses spaces, not tabs
- **"Stats not showing"**: Verify choicescript_stats.txt exists

#### HTML Version Issues
- **"Choices not working"**: Check game.js for JavaScript errors
- **"Styling broken"**: Ensure style.css in same directory
- **"Stats not tracking"**: Verify tracing.js is loaded

### File Locations
- HTML Game: `game/index.html`
- ChoiceScript Scenes: `choicescript_game/scenes/*.txt`
- Setup Guide: `QUICK_START.md`
- Roadmap: `docs/PROJECT_ROADMAP.md`

### Testing Checklist
- [ ] HTML version opens without errors
- [ ] All choice buttons functional
- [ ] Stats tracking correctly
- [ ] Multiple paths accessible
- [ ] Endings reachable

## Reference Files
- `QUICK_START.md` - Setup instructions
- `docs/AUTOMATION_GUIDE.md` - Advanced workflows
- `choicescript_game/README.md` - ChoiceScript specifics
- `game/README.md` - HTML version details
