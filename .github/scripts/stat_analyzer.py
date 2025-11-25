#!/usr/bin/env python3
"""
Stat Analyzer - Analyzes stat distribution across all scenes
Provides balance recommendations
"""

import re
from pathlib import Path
from collections import defaultdict

def analyze_stats():
    """Analyze stat changes across all scenes"""
    repo_path = Path.cwd()
    scenes_dir = repo_path / "choicescript_game" / "scenes"
    
    # Track stat changes
    stat_changes = defaultdict(lambda: {"increases": [], "decreases": [], "total": 0})
    scenes_with_stats = []
    scenes_without_stats = []
    
    print("# Stat Balance Analysis Report\n")
    print(f"**Generated:** {Path.cwd()}\n")
    
    for scene_file in sorted(scenes_dir.glob("*.txt")):
        if "choicescript_stats" in scene_file.name:
            continue
        
        content = scene_file.read_text()
        scene_name = scene_file.stem
        
        # Find all *set commands
        set_commands = re.findall(r'\*set\s+(\w+)\s+([+-]?\d+|true|false)', content)
        
        if set_commands:
            scenes_with_stats.append(scene_name)
            
            for stat, value in set_commands:
                if value.startswith('+'):
                    stat_changes[stat]["increases"].append((scene_name, int(value)))
                    stat_changes[stat]["total"] += int(value)
                elif value.startswith('-'):
                    stat_changes[stat]["decreases"].append((scene_name, int(value)))
                    stat_changes[stat]["total"] += int(value)
        else:
            scenes_without_stats.append(scene_name)
    
    # Print summary
    print(f"## Summary\n")
    print(f"- **Total scenes analyzed:** {len(list(scenes_dir.glob('*.txt')))-1}")
    print(f"- **Scenes with stat changes:** {len(scenes_with_stats)}")
    print(f"- **Scenes without stats:** {len(scenes_without_stats)}")
    print(f"- **Unique stats used:** {len(stat_changes)}\n")
    
    # Print stat details
    print(f"## Stat Distribution\n")
    
    for stat, data in sorted(stat_changes.items()):
        inc_count = len(data["increases"])
        dec_count = len(data["decreases"])
        total = data["total"]
        
        print(f"### {stat}")
        print(f"- **Total change potential:** {total:+d}")
        print(f"- **Increase opportunities:** {inc_count}")
        print(f"- **Decrease opportunities:** {dec_count}")
        print(f"- **Balance:** {'⚖️ Balanced' if abs(total) < 50 else '⚠️ Unbalanced'}\n")
    
    # Print recommendations
    print(f"## Recommendations\n")
    
    if scenes_without_stats:
        print(f"### Scenes Needing Stat Integration")
        print(f"These scenes have no stat changes and should be reviewed:")
        for scene in scenes_without_stats[:5]:
            print(f"- {scene}")
        print()
    
    # Check for imbalanced stats
    unbalanced = []
    for stat, data in stat_changes.items():
        if abs(data["total"]) > 100:
            unbalanced.append((stat, data["total"]))
    
    if unbalanced:
        print(f"### Unbalanced Stats")
        print(f"These stats have extreme total changes:")
        for stat, total in unbalanced:
            print(f"- **{stat}:** {total:+d} (recommend rebalancing)")
        print()
    
    # Check for underused stats
    print(f"### Stat Usage Health")
    for stat, data in sorted(stat_changes.items(), key=lambda x: len(x[1]["increases"]) + len(x[1]["decreases"])):
        usage = len(data["increases"]) + len(data["decreases"])
        if usage < 3:
            print(f"- ⚠️ **{stat}:** Only {usage} opportunities (consider adding more)")
    
    print("\n---\n")
    print("💡 **Next Steps:**")
    print("1. Review scenes without stat changes")
    print("2. Balance extreme stat totals")
    print("3. Add more opportunities for underused stats")
    print("4. Ensure meaningful choices in all scenes")

if __name__ == "__main__":
    analyze_stats()
