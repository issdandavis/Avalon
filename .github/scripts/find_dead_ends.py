#!/usr/bin/env python3
"""
Find dead ends - scenes that don't properly terminate
"""

import re
from pathlib import Path

def find_dead_ends():
    """Find scenes that might be dead ends"""
    scenes_dir = Path("choicescript_game/scenes")
    issues = []
    
    for scene_file in scenes_dir.glob("*.txt"):
        if "stats" in scene_file.name:
            continue
        
        content = scene_file.read_text()
        
        # Check if scene ends properly
        has_finish = bool(re.search(r'\*finish\s*$', content, re.MULTILINE))
        has_goto = bool(re.search(r'\*goto(?:_scene)?\s+\w+', content))
        
        if not has_finish and not has_goto:
            issues.append(f"⚠️ {scene_file.name}: No *finish or *goto found - potential dead end")
        
        # Check for choices without outcomes
        choice_blocks = re.findall(r'\*choice(.*?)(?=\*(?:choice|label|finish|goto_scene)|$)', content, re.DOTALL)
        for i, block in enumerate(choice_blocks):
            options = re.findall(r'#[^\n]+', block)
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
