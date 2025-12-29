#!/usr/bin/env python3
"""
Find dead ends - scenes that don't properly terminate
"""

import re
from pathlib import Path

# Pre-compile regex patterns for better performance
FINISH_PATTERN = re.compile(r'\*finish\s*$', re.MULTILINE)
GOTO_PATTERN = re.compile(r'\*goto(?:_scene)?\s+\w+')
CHOICE_PATTERN = re.compile(r'\*choice(.*?)(?=\*(?:choice|label|finish|goto_scene)|$)', re.DOTALL)
OPTION_PATTERN = re.compile(r'#[^\n]+')

def find_dead_ends():
    """Find scenes that might be dead ends"""
    scenes_dir = Path("choicescript_game/scenes")
    issues = []
    
    for scene_file in scenes_dir.glob("*.txt"):
        if "stats" in scene_file.name:
            continue
        
        content = scene_file.read_text()
        
        # Check if scene ends properly using pre-compiled patterns
        has_finish = bool(FINISH_PATTERN.search(content))
        has_goto = bool(GOTO_PATTERN.search(content))
        
        if not has_finish and not has_goto:
            issues.append(f"⚠️ {scene_file.name}: No *finish or *goto found - potential dead end")
        
        # Check for choices without outcomes using pre-compiled patterns
        choice_blocks = CHOICE_PATTERN.findall(content)
        for i, block in enumerate(choice_blocks):
            options = OPTION_PATTERN.findall(block)
            if len(options) < 2:
                issues.append(f"⚠️ {scene_file.name}: Choice block {i+1} has fewer than 2 options")
    
    if issues:
        print("\n🔍 Dead End Detection Results:\n")
        for issue in issues:
            print(issue)
        print(f"\n{len(issues)} potential issues found")
    else:
        print("✅ No dead ends detected")

if __name__ == "__main__":
    find_dead_ends()
