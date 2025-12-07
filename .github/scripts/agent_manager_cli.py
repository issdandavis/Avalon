#!/usr/bin/env python3
"""
Agent Management CLI
Simple command-line interface for managing AI workers

Usage:
    python agent_manager_cli.py status          # Show system status
    python agent_manager_cli.py workers         # List all workers
    python agent_manager_cli.py tasks           # Show task queue summary
    python agent_manager_cli.py health          # Show health score only
    python agent_manager_cli.py recommend       # Show recommendations
    python agent_manager_cli.py report          # Generate full report
"""

import sys
import json
from pathlib import Path
from typing import NoReturn

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from agent_orchestrator import AgentOrchestrator

def main() -> NoReturn:
    """
    Main entry point for the agent management CLI.
    
    Processes command-line arguments and executes the appropriate command.
    """
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    try:
        orchestrator = AgentOrchestrator()
    except Exception as e:
        print(f"❌ Error initializing orchestrator: {e}")
        sys.exit(1)
    
    if command == 'status':
        print("🎯 Generating status report...")
        try:
            report = orchestrator.generate_status_report()
            orchestrator.print_report(report)
        except Exception as e:
            print(f"❌ Error generating status report: {e}")
            sys.exit(1)
        
    elif command == 'workers':
        print("🤖 AI WORKERS STATUS\n")
        try:
            report = orchestrator.generate_status_report()
            for worker, info in report['workers'].items():
                status = "✅ Active" if info.get('exists') else "⚠️ Not initialized"
                print(f"{worker.upper():<20} {status}")
                if info.get('exists'):
                    print(f"  └─ Last activity: {info.get('last_commit_time', 'unknown')}")
        except Exception as e:
            print(f"❌ Error getting worker status: {e}")
            sys.exit(1)
        
    elif command == 'tasks':
        print("📋 TASK QUEUE SUMMARY\n")
        try:
            report = orchestrator.generate_status_report()
            tasks = report['task_queue']
            
            if 'error' not in tasks:
                total = tasks.get('total', 0)
                completed = tasks.get('completed', 0)
                progress = int((completed / total * 100)) if total > 0 else 0
                
                print(f"Total Tasks:     {total}")
                print(f"Completed:       {completed} ({progress}%)")
                print(f"In Progress:     {tasks.get('in_progress', 0)}")
                print(f"Pending:         {tasks.get('total_pending', 0)}")
                print(f"Needs Review:    {tasks.get('needs_review', 0)}")
                
                # Progress bar
                bar_width = 50
                filled = int(bar_width * progress / 100)
                bar = '█' * filled + '░' * (bar_width - filled)
                print(f"\n[{bar}] {progress}%")
            else:
                print(f"Error: {tasks.get('error')}")
        except Exception as e:
            print(f"❌ Error analyzing tasks: {e}")
            sys.exit(1)
    
    elif command == 'health':
        try:
            report = orchestrator.generate_status_report()
            health = report['health_score']
            
            if health >= 80:
                status = "✅ HEALTHY"
            elif health >= 50:
                status = "⚠️ WARNING"
            else:
                status = "🔴 CRITICAL"
            
            print(f"\n{'='*50}")
            print(f"  SYSTEM HEALTH: {health}/100")
            print(f"  STATUS: {status}")
            print(f"{'='*50}\n")
        except Exception as e:
            print(f"❌ Error checking health: {e}")
            sys.exit(1)
        
    elif command == 'recommend':
        print("💡 RECOMMENDATIONS\n")
        try:
            report = orchestrator.generate_status_report()
            recommendations = orchestrator.generate_recommendations(report)
            
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec}")
        except Exception as e:
            print(f"❌ Error generating recommendations: {e}")
            sys.exit(1)
        
    elif command == 'report':
        print("📊 Generating full report...")
        try:
            report = orchestrator.generate_status_report()
            orchestrator.print_report(report)
            orchestrator.save_report(report)
            print("\n✅ Report generated and saved")
        except Exception as e:
            print(f"❌ Error generating report: {e}")
            sys.exit(1)
        
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)

if __name__ == '__main__':
    main()
