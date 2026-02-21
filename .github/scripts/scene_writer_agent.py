#!/usr/bin/env python3
"""
Scene Writer Agent - Actually writes ChoiceScript scenes
This is a REAL implementation that generates usable content
"""

import os
import sys
import re
from pathlib import Path
import anthropic

class SceneWriterAgent:
    """Writes complete ChoiceScript scenes with proper voice and structure"""
    
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
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        self.repo_path = Path.cwd()
    
    def read_file_safe(self, path):
        """Read file or return empty string"""
        try:
            return Path(path).read_text()
        except:
            return ""
    
    def find_next_scene_to_write(self):
        """Find the most incomplete scene that needs work"""
        scenes_dir = self.repo_path / "choicescript_game" / "scenes"
        
        # Priority: scenes with PLACEHOLDER or very short
        for scene_file in scenes_dir.glob("*.txt"):
            content = scene_file.read_text()
            
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
                content = scene_file.read_text()
                # If under 5KB, needs expansion
                if len(content) < 5000:
                    return scene_file
        
        return None
    
    def get_scene_context(self, scene_path):
        """Gather context for writing this scene"""
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
        
        return {
            "scene_name": scene_name,
            "lore": lore_context,
            "current_content": scene_path.read_text(),
            "available_stats": self.extract_stats(startup_content),
            "requirements": self.extract_requirements(task_queue, scene_name)
        }
    
    def extract_stats(self, startup_content):
        """Extract available stats from startup"""
        stats = []
        for line in startup_content.split('\n'):
            if '*create ' in line and not line.strip().startswith('*comment'):
                stat = line.split('*create ')[1].split()[0]
                stats.append(stat)
        return stats[:20]  # Limit for prompt
    
    def extract_requirements(self, task_queue, scene_name):
        """Find requirements for this scene in task queue"""
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
    
    def write_scene_section(self, context, section="next"):
        """Use AI to write a section of the scene"""
        
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

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            temperature=0.85,
            system=self.SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
    
    def append_to_scene(self, scene_path, new_content):
        """Intelligently append new content to scene"""
        current = scene_path.read_text()
        
        # If scene is very short or placeholder, replace most of it
        if len(current) < 500 or "PLACEHOLDER" in current:
            # Keep the header comment
            header = []
            for line in current.split('\n'):
                if line.strip().startswith('*comment'):
                    header.append(line)
                else:
                    break
            
            scene_path.write_text('\n'.join(header) + '\n\n' + new_content)
        else:
            # Append to existing content
            # Remove any trailing *finish to continue the scene
            current = re.sub(r'\*finish\s*$', '', current.strip())
            scene_path.write_text(current + '\n\n' + new_content)
        
        print(f"✅ Added {len(new_content)} characters to {scene_path.name}")
    
    def run(self):
        """Main execution"""
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
    
    def update_task_queue(self, scene_name):
        """Mark progress in task queue"""
        queue_path = self.repo_path / "docs" / "AI_TASK_QUEUE.md"
        content = queue_path.read_text()
        
        # Find and update related task
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if scene_name.replace('_', ' ') in line.lower() and '- [ ]' in line:
                lines[i] = line.replace('- [ ]', '- [→]')
                break
        
        queue_path.write_text('\n'.join(lines))
        print("📋 Updated task queue")

if __name__ == "__main__":
    agent = SceneWriterAgent()
    agent.run()
