#!/usr/bin/env python3
"""
SpiralVerse Autonomous AI Worker
A self-directed agent that reads the task queue and makes progress on the game.

This is a DEMONSTRATION version. For production use, enhance error handling
and add more sophisticated task parsing.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
import re

try:
    import anthropic
except ImportError:
    print("❌ Error: anthropic package not installed")
    print("Install with: pip install anthropic")
    sys.exit(1)

class AutonomousAIWorker:
    """
    The SpiralVerse AI worker that breathes ChoiceScript and ships games.
    """
    
    SYSTEM_PROMPT = """You are the SpiralVerse-Omnifeather-Terminal — an autonomous AI agent working on "Polly's Wingscroll: The First Thread", a ChoiceScript game.

You are working independently to make progress on the game. You have access to:
- The full repository code
- Task queue with priorities
- Lore documents and character information
- Style guidelines and rules

Your current task is: {task_description}

Core principles:
1. Make small, incremental changes
2. Preserve character voices (Polly is sarcastic, Izack is nervous, etc.)
3. Every scene needs at least one taste or smell
4. Follow ChoiceScript syntax perfectly
5. Test your changes before completing

You should provide your changes as a detailed plan of file edits.
Be specific about what to add, modify, or remove.
"""

    def __init__(self):
        self.repo_path = Path.cwd()
        self.api_key = os.environ.get("ANTHROPIC_API_KEY")
        
        if not self.api_key:
            print("❌ Error: ANTHROPIC_API_KEY environment variable not set")
            sys.exit(1)
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.task_queue_path = self.repo_path / "docs" / "AI_TASK_QUEUE.md"
        self.rules_path = self.repo_path / "docs" / "AI_WORKER_RULES.md"
    
    def log(self, message, level="INFO"):
        """Log a message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prefix = {
            "INFO": "ℹ️",
            "SUCCESS": "✅",
            "ERROR": "❌",
            "WORKING": "🔄"
        }.get(level, "ℹ️")
        print(f"{prefix} [{timestamp}] {message}")
    
    def read_task_queue(self):
        """Read and parse the task queue"""
        if not self.task_queue_path.exists():
            self.log("Task queue file not found", "ERROR")
            return []
        
        content = self.task_queue_path.read_text()
        
        # Find unchecked tasks ([ ]) in priority order
        tasks = []
        current_priority = None
        
        for line in content.split('\n'):
            # Detect priority headers
            if line.startswith('## 🔥 PRIORITY 1:') or line.startswith('## PRIORITY 1'):
                current_priority = 1
            elif line.startswith('## ⭐ PRIORITY 2:') or line.startswith('## PRIORITY 2'):
                current_priority = 2
            elif line.startswith('## 📝 PRIORITY 3:') or line.startswith('## PRIORITY 3'):
                current_priority = 3
            
            # Find unchecked tasks
            if '- [ ]' in line and current_priority:
                # Extract task description
                task_text = line.split('- [ ]', 1)[1].strip()
                tasks.append({
                    'priority': current_priority,
                    'description': task_text,
                    'line': line
                })
        
        return tasks
    
    def get_next_task(self, priority_filter=None):
        """Get the next task to work on"""
        tasks = self.read_task_queue()
        
        if priority_filter:
            tasks = [t for t in tasks if t['priority'] == int(priority_filter)]
        
        if not tasks:
            self.log("No unchecked tasks found in queue")
            return None
        
        # Return highest priority task (lowest number = highest priority)
        next_task = min(tasks, key=lambda t: t['priority'])
        self.log(f"Next task (P{next_task['priority']}): {next_task['description'][:60]}...")
        return next_task
    
    def execute_task(self, task):
        """
        Use Claude to analyze and execute a task.
        
        This is a DEMO implementation. In production, you would:
        1. Use more sophisticated prompting
        2. Implement actual file editing
        3. Add verification steps
        4. Include rollback mechanisms
        """
        self.log(f"Executing task: {task['description'][:50]}...", "WORKING")
        
        # For demo purposes, we'll just log that we would work on it
        self.log("This is a DEMONSTRATION version", "INFO")
        self.log("In production, this would:", "INFO")
        self.log("  1. Analyze the task requirements", "INFO")
        self.log("  2. Read relevant files", "INFO")
        self.log("  3. Generate new content", "INFO")
        self.log("  4. Edit files appropriately", "INFO")
        self.log("  5. Test ChoiceScript syntax", "INFO")
        self.log("  6. Commit changes", "INFO")
        
        # Create a demonstration log file
        log_dir = self.repo_path / "logs"
        log_dir.mkdir(exist_ok=True)
        
        log_file = log_dir / f"ai-work-{datetime.now().strftime('%Y-%m-%d')}.md"
        log_content = f"""# AI Worker Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Task Attempted
**Priority:** {task['priority']}  
**Description:** {task['description']}

## Status
This was a DEMONSTRATION run. No actual changes were made.

## What Would Happen in Production
1. AI would read task requirements from AI_TASK_QUEUE.md
2. AI would review related files and lore documents
3. AI would generate content matching Spiralverse style
4. AI would edit files with new content
5. AI would verify ChoiceScript syntax
6. AI would commit changes with meaningful message
7. AI would update task queue to mark task complete

## Next Steps
To enable full autonomous operation:
1. Add ANTHROPIC_API_KEY to repository secrets
2. Review and approve the AI worker implementation
3. Enable the GitHub Actions workflow
4. Monitor first few runs closely
5. Gradually increase autonomy as confidence grows

---

**The spiral turns. The code waits to be written.**
"""
        
        log_file.write_text(log_content)
        self.log(f"Created log file: {log_file}", "SUCCESS")
        
        return True
    
    def update_task_queue(self, task, status="completed"):
        """Update task queue to mark task as complete"""
        # For demo, we don't actually modify the queue
        self.log(f"Would mark task as {status} in task queue", "INFO")
    
    def run_work_cycle(self):
        """Execute one complete work cycle"""
        self.log("Starting autonomous work cycle", "INFO")
        
        # Get priority from environment or default to 1
        priority = os.environ.get("TASK_PRIORITY", "1")
        
        # Get next task
        task = self.get_next_task(priority_filter=priority)
        
        if not task:
            self.log("No tasks available for current priority", "INFO")
            return False
        
        # Execute task
        success = self.execute_task(task)
        
        if success:
            self.update_task_queue(task)
            self.log("Work cycle completed successfully", "SUCCESS")
        else:
            self.log("Work cycle encountered issues", "ERROR")
        
        return success

def main():
    """Main entry point"""
    print("=" * 60)
    print("🌀 SpiralVerse Autonomous AI Worker")
    print("=" * 60)
    print()
    
    worker = AutonomousAIWorker()
    worker.run_work_cycle()
    
    print()
    print("=" * 60)
    print("Caw. 🪶")
    print("=" * 60)

if __name__ == "__main__":
    main()
