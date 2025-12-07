#!/usr/bin/env python3
"""
Content Polisher - Enhances existing scenes with sensory details
Actually improves content quality
"""

import os
import re
from pathlib import Path
from typing import Optional
import anthropic

class ContentPolisher:
    """
    Polishes existing scenes by adding sensory details and improving prose.
    
    This class uses AI to enhance ChoiceScript game scenes while preserving
    all game logic, character voices, and structural elements.
    """
    
    SYSTEM_PROMPT = """You are a content polish specialist for ChoiceScript games.

Your job is to take existing scene content and enhance it by:
1. Adding vivid sensory details (taste and smell particularly)
2. Enriching atmospheric descriptions
3. Preserving exact character voices and dialogue
4. Maintaining all ChoiceScript syntax perfectly
5. Keeping all *label names, *goto targets, and stat changes EXACTLY the same

You DO NOT:
- Change the story or plot
- Modify character dialogue significantly  
- Add or remove choices
- Change stat adjustments
- Alter *goto flow

You DO:
- Add sensory details where missing
- Enrich scene-setting descriptions
- Add atmospheric touches
- Polish prose for better flow
- Ensure every scene has taste OR smell

Output the COMPLETE polished scene with all original code intact."""

    def __init__(self):
        """Initialize the ContentPolisher with API client and repository paths."""
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable must be set")
        self.client = anthropic.Anthropic(api_key=api_key)
        self.repo_path = Path.cwd()
    
    def find_scene_needing_polish(self, polish_type: str = "sensory-details") -> Optional[Path]:
        """
        Find a scene that lacks sensory details.
        
        Args:
            polish_type: Type of polishing needed (default: "sensory-details")
            
        Returns:
            Path to scene file needing polish, or None if all scenes are polished
        """
        scenes_dir = self.repo_path / "choicescript_game" / "scenes"
        
        if not scenes_dir.exists():
            print(f"❌ Error: Scenes directory not found at {scenes_dir}")
            return None
        
        for scene_file in sorted(scenes_dir.glob("*.txt")):
            if "choicescript_stats" in scene_file.name:
                continue
            
            try:
                content = scene_file.read_text(encoding='utf-8').lower()
            except Exception as e:
                print(f"⚠️ Warning: Could not read {scene_file.name}: {e}")
                continue
            
            # Look for scenes without taste or smell
            has_taste = any(word in content for word in ["taste", "tasted", "tasting", "flavor", "flavour"])
            has_smell = any(word in content for word in ["smell", "scent", "aroma", "odor", "fragrance"])
            
            if not has_taste and not has_smell:
                return scene_file
        
        return None
    
    def polish_scene(self, scene_path: Path) -> bool:
        """
        Polish a scene with AI-powered enhancements.
        
        Args:
            scene_path: Path to the scene file to polish
            
        Returns:
            True if polishing succeeded, False otherwise
        """
        try:
            original_content = scene_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"❌ Error reading {scene_path.name}: {e}")
            return False
        
        # Don't polish very short scenes (under 500 chars) - they need writing, not polish
        if len(original_content) < 500:
            print(f"⏭️ Skipping {scene_path.name} - too short for polish")
            return False
        
        prompt = f"""Polish this ChoiceScript scene by adding sensory details (especially taste and smell).

ORIGINAL SCENE:
{original_content}

REQUIREMENTS:
- Add at least ONE taste or smell description
- Enhance atmospheric descriptions
- Keep ALL *labels, *gotos, *set statements EXACTLY the same
- Preserve character voices perfectly
- Maintain all ChoiceScript syntax
- Don't change the plot or choices

Output the complete polished scene."""

        print(f"✨ Polishing {scene_path.name}...")
        
        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=8000,
                temperature=0.75,
                system=self.SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}]
            )
        except Exception as e:
            print(f"❌ Error calling AI: {e}")
            return False
        
        polished_content = response.content[0].text
        
        # Extract just the code if wrapped in markdown
        if "```" in polished_content:
            polished_content = re.search(r'```(?:choicescript)?\n(.*?)\n```', polished_content, re.DOTALL)
            if polished_content:
                polished_content = polished_content.group(1)
        
        # Verify labels haven't changed
        original_labels = set(re.findall(r'\*label (\w+)', original_content))
        polished_labels = set(re.findall(r'\*label (\w+)', polished_content))
        
        if original_labels != polished_labels:
            print(f"⚠️ Warning: Labels changed in polish, reverting")
            return False
        
        # Write polished version
        try:
            scene_path.write_text(polished_content, encoding='utf-8')
        except Exception as e:
            print(f"❌ Error writing file: {e}")
            return False
        
        # Show diff stats
        orig_lines = len(original_content.split('\n'))
        new_lines = len(polished_content.split('\n'))
        print(f"✅ Polished: {orig_lines} → {new_lines} lines")
        
        return True
    
    def run(self) -> None:
        """
        Main execution method for the content polisher.
        
        Finds scenes needing polish and applies AI-powered enhancements.
        """
        print("✨ Content Polisher Starting...")
        
        polish_type = os.environ.get("POLISH_TYPE", "sensory-details")
        
        # Find scene needing work
        scene = self.find_scene_needing_polish(polish_type)
        if not scene:
            print("ℹ️ All scenes have sensory details!")
            return
        
        print(f"🎨 Target: {scene.name}")
        
        # Polish it
        success = self.polish_scene(scene)
        
        if success:
            print(f"✅ Successfully polished {scene.name}")
        else:
            print(f"⏭️ Skipped {scene.name}")

if __name__ == "__main__":
    polisher = ContentPolisher()
    polisher.run()
