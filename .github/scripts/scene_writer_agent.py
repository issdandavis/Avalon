#!/usr/bin/env python3
"""
Scene Writer Agent - Actually writes ChoiceScript scenes
This is a REAL implementation that generates usable content
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, Optional, List
import anthropic

class SceneWriterAgent:
    """
    Writes complete ChoiceScript scenes with proper voice and structure.
    
    This class uses AI to generate high-quality ChoiceScript content that matches
    the established universe, character voices, and game mechanics.
    """
    
    SYSTEM_PROMPT = """You are an expert ChoiceScript author specializing in the Spiral of Pollyoneth universe.

Your task is to write engaging, high-quality ChoiceScript scenes that:
1. Match the established character voices (Polly: sarcastic, Izack: nervous, Aria: precise, Zara: warm)
2. Include sensory details (at least one taste OR smell per scene)
3. Provide meaningful player choices that affect stats
4. Use proper ChoiceScript syntax
5. Maintain lore consistency with the Avalon universe

Key rules:
- Every scene needs *label at the start
- All choices should affect at least one stat
- Include Polly's commentary when dimensionally relevant
- End scenes with *goto, *goto_scene, or *finish
- Preserve the collaborative magic philosophy
- Make choices matter

You will be given:
- Scene name and purpose
- Context from surrounding scenes
- Lore requirements
- Target length

Produce complete, ready-to-use ChoiceScript code."""

    def __init__(self):
        """Initialize the SceneWriterAgent with API client and repository paths."""
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable must be set")
        self.client = anthropic.Anthropic(api_key=api_key)
        self.repo_path = Path.cwd()
    
    def read_file_safe(self, path: Path) -> str:
        """
        Safely read a file, returning empty string on error.
        
        Args:
            path: Path to the file to read
            
        Returns:
            File contents as string, or empty string if read fails
        """
        try:
            return Path(path).read_text(encoding='utf-8')
        except Exception as e:
            print(f"⚠️ Warning: Could not read {path}: {e}")
            return ""
    
    def find_next_scene_to_write(self) -> Optional[Path]:
        """
        Find the most incomplete scene that needs work.
        
        Returns:
            Path to scene file needing work, or None if all scenes are complete
        """
        scenes_dir = self.repo_path / "choicescript_game" / "scenes"
        
        if not scenes_dir.exists():
            print(f"❌ Error: Scenes directory not found at {scenes_dir}")
            return None
        
        # Priority: scenes with PLACEHOLDER or very short
        for scene_file in scenes_dir.glob("*.txt"):
            try:
                content = scene_file.read_text(encoding='utf-8')
            except Exception as e:
                print(f"⚠️ Warning: Could not read {scene_file.name}: {e}")
                continue
            
            # Skip stats screen
            if "choicescript_stats" in scene_file.name:
                continue
            
            # High priority: has placeholder
            if "PLACEHOLDER" in content or "TODO" in content or "STUB" in content:
                return scene_file
            
            # Medium priority: very short (under 1KB)
            if len(content) < 1000:
                return scene_file
        
        # Look for incomplete expeditions (singing_dunes, verdant_tithe, rune_glacier)
        for name in ["singing_dunes", "verdant_tithe", "rune_glacier"]:
            scene_file = scenes_dir / f"{name}.txt"
            if scene_file.exists():
                try:
                    content = scene_file.read_text(encoding='utf-8')
                    # If under 5KB, needs expansion
                    if len(content) < 5000:
                        return scene_file
                except Exception as e:
                    print(f"⚠️ Warning: Could not read {scene_file.name}: {e}")
                    continue
        
        return None
    
    def get_scene_context(self, scene_path: Path) -> Dict[str, any]:
        """
        Gather context for writing this scene.
        
        Args:
            scene_path: Path to the scene file
            
        Returns:
            Dictionary containing scene context including lore, stats, and requirements
        """
        scene_name = scene_path.stem
        
        # Read related lore
        lore_context = ""
        if "singing_dunes" in scene_name or "dunes" in scene_name:
            lore_context = "Truth-testing desert, oath magic, Kael as guide, sand judges honesty"
        elif "verdant" in scene_name or "forest" in scene_name:
            lore_context = "Sentient forest, Thoughtvines, Dreamwillow, Heartwood Tree"
        elif "glacier" in scene_name or "rune" in scene_name:
            lore_context = "Living ice with adaptive runes, control vs harmony, Aria teaches"
        
        # Read startup for available stats
        startup_content = self.read_file_safe(self.repo_path / "choicescript_game" / "startup.txt")
        
        # Get character info from task queue
        task_queue = self.read_file_safe(self.repo_path / "docs" / "AI_TASK_QUEUE.md")
        
        try:
            current_content = scene_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"⚠️ Warning: Could not read current scene content: {e}")
            current_content = ""
        
        return {
            "scene_name": scene_name,
            "lore": lore_context,
            "current_content": current_content,
            "available_stats": self.extract_stats(startup_content),
            "requirements": self.extract_requirements(task_queue, scene_name)
        }
    
    def extract_stats(self, startup_content: str) -> List[str]:
        """
        Extract available stats from startup file.
        
        Args:
            startup_content: Content of the startup.txt file
            
        Returns:
            List of stat names available in the game
        """
        stats: List[str] = []
        for line in startup_content.split('\n'):
            if '*create ' in line and not line.strip().startswith('*comment'):
                stat = line.split('*create ')[1].split()[0]
                stats.append(stat)
        return stats[:20]  # Limit for prompt
    
    def extract_requirements(self, task_queue: str, scene_name: str) -> str:
        """
        Find requirements for this scene in task queue.
        
        Args:
            task_queue: Content of the task queue file
            scene_name: Name of the scene to find requirements for
            
        Returns:
            Requirements text or default message
        """
        relevant_section = ""
        in_relevant = False
        
        for line in task_queue.split('\n'):
            if scene_name.replace('_', ' ') in line.lower():
                in_relevant = True
            elif in_relevant and line.startswith('## '):
                break
            elif in_relevant:
                relevant_section += line + '\n'
        
        return relevant_section if relevant_section else "Continue the scene naturally with meaningful choices"
    
    def write_scene_section(self, context: Dict[str, any], section: str = "next") -> str:
        """
        Use AI to write a section of the scene.
        
        Args:
            context: Scene context dictionary
            section: Section type to write (default: "next")
            
        Returns:
            Generated ChoiceScript content
        """
        
        prompt = f"""Write the {section} section for the ChoiceScript scene: {context['scene_name']}

LORE CONTEXT:
{context['lore']}

CURRENT CONTENT:
{context['current_content'][:2000]}  
(showing first 2000 chars - continue from where this leaves off)

REQUIREMENTS:
{context['requirements']}

AVAILABLE STATS TO USE:
{', '.join(context['available_stats'][:15])}

INSTRUCTIONS:
1. Write 300-500 lines of ChoiceScript continuing this scene
2. Include at least ONE taste or smell description
3. Create meaningful choices that affect stats
4. Preserve character voices if characters appear
5. Use proper *label, *choice, *set, *goto syntax
6. Make sure all code paths end properly
7. Add atmospheric descriptions

Output ONLY valid ChoiceScript code, no explanations."""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4000,
                temperature=0.85,
                system=self.SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            print(f"❌ Error calling AI: {e}")
            return ""
    
    def append_to_scene(self, scene_path: Path, new_content: str) -> None:
        """
        Intelligently append new content to scene.
        
        Args:
            scene_path: Path to the scene file
            new_content: New content to append
        """
        if not new_content:
            print("⚠️ Warning: No content to append")
            return
            
        try:
            current = scene_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"❌ Error reading scene: {e}")
            return
        
        # If scene is very short or placeholder, replace most of it
        if len(current) < 500 or "PLACEHOLDER" in current:
            # Keep the header comment
            header = []
            for line in current.split('\n'):
                if line.strip().startswith('*comment'):
                    header.append(line)
                else:
                    break
            
            try:
                scene_path.write_text('\n'.join(header) + '\n\n' + new_content, encoding='utf-8')
            except Exception as e:
                print(f"❌ Error writing scene: {e}")
                return
        else:
            # Append to existing content
            # Remove any trailing *finish to continue the scene
            current = re.sub(r'\*finish\s*$', '', current.strip())
            try:
                scene_path.write_text(current + '\n\n' + new_content, encoding='utf-8')
            except Exception as e:
                print(f"❌ Error writing scene: {e}")
                return
        
        print(f"✅ Added {len(new_content)} characters to {scene_path.name}")
    
    def run(self) -> None:
        """
        Main execution method for the scene writer.
        
        Finds scenes needing work and generates AI-powered content.
        """
        print("🎭 Scene Writer Agent Starting...")
        
        # Find scene to work on
        scene = self.find_next_scene_to_write()
        if not scene:
            print("ℹ️ No scenes need work currently")
            return
        
        print(f"📝 Working on: {scene.name}")
        
        # Get context
        context = self.get_scene_context(scene)
        
        # Generate content
        print("🤖 Generating content with AI...")
        new_content = self.write_scene_section(context)
        
        # Append to scene
        self.append_to_scene(scene, new_content)
        
        # Update task queue
        self.update_task_queue(scene.stem)
        
        print(f"✅ Completed work on {scene.name}")
    
    def update_task_queue(self, scene_name: str) -> None:
        """
        Mark progress in task queue.
        
        Args:
            scene_name: Name of the scene that was worked on
        """
        queue_path = self.repo_path / "docs" / "AI_TASK_QUEUE.md"
        
        if not queue_path.exists():
            print("⚠️ Warning: Task queue file not found")
            return
            
        try:
            content = queue_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"⚠️ Warning: Could not read task queue: {e}")
            return
        
        # Find and update related task
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if scene_name.replace('_', ' ') in line.lower() and '- [ ]' in line:
                lines[i] = line.replace('- [ ]', '- [→]')
                break
        
        try:
            queue_path.write_text('\n'.join(lines), encoding='utf-8')
            print("📋 Updated task queue")
        except Exception as e:
            print(f"⚠️ Warning: Could not update task queue: {e}")

if __name__ == "__main__":
    try:
        agent = SceneWriterAgent()
        agent.run()
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)
