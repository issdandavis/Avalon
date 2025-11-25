#!/usr/bin/env python3
"""
Agent Management Orchestrator
Coordinates and monitors all AI workers in the Avalon autonomous system
"""

import os
import sys
import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import yaml

class AgentOrchestrator:
    """Manages coordination between multiple AI workers"""
    
    def __init__(self):
        self.repo_root = Path(__file__).parent.parent.parent
        self.config_file = self.repo_root / "config" / "automation-settings.json"
        self.task_queue_file = self.repo_root / "docs" / "AI_TASK_QUEUE.md"
        self.worker_status = {}
        
    def load_config(self):
        """Load automation configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {}
    
    def get_worker_status(self):
        """Check status of all AI workers via git branches"""
        workers = {
            'scene-writer': 'ai-scene-development',
            'content-polisher': 'ai-content-polish',
            'stat-balancer': 'ai-stat-balance',
            'autonomous-worker': 'ai-autonomous-work'
        }
        
        status = {}
        for worker_name, branch_name in workers.items():
            try:
                # Check if branch exists
                result = subprocess.run(
                    ['git', 'rev-parse', '--verify', f'origin/{branch_name}'],
                    cwd=self.repo_root,
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    # Get last commit info
                    commit_info = subprocess.run(
                        ['git', 'log', '-1', '--format=%H|%an|%ar|%s', f'origin/{branch_name}'],
                        cwd=self.repo_root,
                        capture_output=True,
                        text=True
                    ).stdout.strip().split('|')
                    
                    status[worker_name] = {
                        'branch': branch_name,
                        'exists': True,
                        'last_commit_sha': commit_info[0] if len(commit_info) > 0 else 'unknown',
                        'last_commit_author': commit_info[1] if len(commit_info) > 1 else 'unknown',
                        'last_commit_time': commit_info[2] if len(commit_info) > 2 else 'unknown',
                        'last_commit_msg': commit_info[3] if len(commit_info) > 3 else 'unknown'
                    }
                else:
                    status[worker_name] = {
                        'branch': branch_name,
                        'exists': False,
                        'status': 'Not yet initialized'
                    }
            except Exception as e:
                status[worker_name] = {
                    'branch': branch_name,
                    'exists': False,
                    'error': str(e)
                }
        
        return status
    
    def analyze_task_queue(self):
        """Parse and analyze the task queue"""
        if not self.task_queue_file.exists():
            return {'error': 'Task queue file not found'}
        
        with open(self.task_queue_file, 'r') as f:
            content = f.read()
        
        # Count task statuses
        total_tasks = content.count('- [ ]')  # Not started
        in_progress = content.count('- [→]')   # In progress
        needs_review = content.count('- [?]')  # Needs review
        completed = content.count('- [x]')     # Completed
        
        return {
            'total_pending': total_tasks,
            'in_progress': in_progress,
            'needs_review': needs_review,
            'completed': completed,
            'total': total_tasks + in_progress + needs_review + completed
        }
    
    def check_merge_conflicts(self):
        """Check for merge conflicts between AI worker branches"""
        conflicts = []
        workers = ['ai-scene-development', 'ai-content-polish', 'ai-stat-balance', 'ai-autonomous-work']
        
        for branch in workers:
            try:
                # Check if branch can merge cleanly into main
                result = subprocess.run(
                    ['git', 'merge-tree', 'origin/main', f'origin/{branch}'],
                    cwd=self.repo_root,
                    capture_output=True,
                    text=True
                )
                
                if '<<<<<<<' in result.stdout:
                    conflicts.append({
                        'branch': branch,
                        'has_conflicts': True
                    })
                else:
                    conflicts.append({
                        'branch': branch,
                        'has_conflicts': False
                    })
            except Exception as e:
                conflicts.append({
                    'branch': branch,
                    'error': str(e)
                })
        
        return conflicts
    
    def get_scene_completion_status(self):
        """Analyze scene completion across expeditions"""
        scenes_dir = self.repo_root / "choicescript_game" / "scenes"
        
        if not scenes_dir.exists():
            return {'error': 'Scenes directory not found'}
        
        expeditions = {
            'singing_dunes.txt': 'Singing Dunes',
            'verdant_tithe.txt': 'Verdant Tithe',
            'rune_glacier.txt': 'Rune Glacier'
        }
        
        status = {}
        for filename, name in expeditions.items():
            filepath = scenes_dir / filename
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = len(content.splitlines())
                    placeholders = content.count('PLACEHOLDER') + content.count('TODO') + content.count('STUB')
                    
                    status[name] = {
                        'lines': lines,
                        'placeholders': placeholders,
                        'estimated_complete': min(100, int((lines / 1000) * 100))  # Assume 1000 lines = complete
                    }
            else:
                status[name] = {
                    'exists': False
                }
        
        return status
    
    def generate_status_report(self):
        """Generate comprehensive status report"""
        config = self.load_config()
        worker_status = self.get_worker_status()
        task_analysis = self.analyze_task_queue()
        scene_status = self.get_scene_completion_status()
        conflicts = self.check_merge_conflicts()
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'configuration': {
                'silent_mode': config.get('silent_mode', {}).get('enabled', False),
                'api_key_configured': bool(os.getenv('ANTHROPIC_API_KEY'))
            },
            'workers': worker_status,
            'task_queue': task_analysis,
            'scene_completion': scene_status,
            'merge_conflicts': conflicts,
            'health_score': self.calculate_health_score(worker_status, task_analysis, conflicts)
        }
        
        return report
    
    def calculate_health_score(self, workers, tasks, conflicts):
        """Calculate overall system health (0-100)"""
        score = 100
        
        # Deduct for non-existent worker branches
        for worker, info in workers.items():
            if not info.get('exists', False):
                score -= 10
        
        # Deduct for merge conflicts
        conflict_count = sum(1 for c in conflicts if c.get('has_conflicts', False))
        score -= conflict_count * 15
        
        # Deduct if too many tasks in progress (bottleneck)
        if tasks.get('in_progress', 0) > 5:
            score -= 10
        
        # Deduct if no completed tasks
        if tasks.get('completed', 0) == 0:
            score -= 5
        
        return max(0, score)
    
    def print_report(self, report):
        """Print formatted status report"""
        print("=" * 80)
        print("🎯 AGENT MANAGEMENT SYSTEM - STATUS REPORT")
        print("=" * 80)
        print(f"\n⏰ Timestamp: {report['timestamp']}")
        print(f"\n📊 System Health: {report['health_score']}/100")
        
        # Configuration
        print("\n🔧 CONFIGURATION")
        print(f"  • Silent Mode: {'✅ Enabled' if report['configuration']['silent_mode'] else '❌ Disabled'}")
        print(f"  • API Key: {'✅ Configured' if report['configuration']['api_key_configured'] else '⚠️ Missing (workers won\'t run)'}")
        
        # Workers
        print("\n🤖 AI WORKERS")
        for worker, info in report['workers'].items():
            if info.get('exists'):
                print(f"  ✅ {worker.upper()}")
                print(f"     Branch: {info['branch']}")
                print(f"     Last Commit: {info.get('last_commit_time', 'unknown')}")
                print(f"     Message: {info.get('last_commit_msg', 'unknown')[:60]}")
            else:
                print(f"  ⚠️ {worker.upper()} - Not initialized")
        
        # Tasks
        print("\n📋 TASK QUEUE")
        tasks = report['task_queue']
        if 'error' not in tasks:
            total = tasks.get('total', 0)
            completed = tasks.get('completed', 0)
            progress = int((completed / total * 100)) if total > 0 else 0
            
            print(f"  • Total Tasks: {total}")
            print(f"  • Completed: {completed} ({progress}%)")
            print(f"  • In Progress: {tasks.get('in_progress', 0)}")
            print(f"  • Pending: {tasks.get('total_pending', 0)}")
            print(f"  • Needs Review: {tasks.get('needs_review', 0)}")
        
        # Scene Status
        print("\n🎭 EXPEDITION SCENE COMPLETION")
        for expedition, status in report['scene_completion'].items():
            if status.get('exists', True):
                print(f"  • {expedition}: {status['lines']} lines ({status['estimated_complete']}% complete)")
                if status['placeholders'] > 0:
                    print(f"    ⚠️ {status['placeholders']} placeholders remaining")
        
        # Conflicts
        print("\n⚠️ MERGE CONFLICTS")
        has_conflicts = any(c.get('has_conflicts', False) for c in report['merge_conflicts'])
        if has_conflicts:
            for conflict in report['merge_conflicts']:
                if conflict.get('has_conflicts'):
                    print(f"  ⚠️ {conflict['branch']} has merge conflicts with main")
        else:
            print("  ✅ No merge conflicts detected")
        
        print("\n" + "=" * 80)
        
        # Recommendations
        print("\n💡 RECOMMENDATIONS")
        recommendations = self.generate_recommendations(report)
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec}")
        
        print("\n" + "=" * 80)
    
    def generate_recommendations(self, report):
        """Generate actionable recommendations based on status"""
        recommendations = []
        
        # API key check
        if not report['configuration']['api_key_configured']:
            recommendations.append("🔴 CRITICAL: Add ANTHROPIC_API_KEY to repository secrets to activate workers")
        
        # Worker initialization
        for worker, info in report['workers'].items():
            if not info.get('exists'):
                recommendations.append(f"Initialize {worker} by running its workflow manually")
        
        # Merge conflicts
        conflict_branches = [c['branch'] for c in report['merge_conflicts'] if c.get('has_conflicts')]
        if conflict_branches:
            recommendations.append(f"Resolve merge conflicts in: {', '.join(conflict_branches)}")
        
        # Task queue
        if report['task_queue'].get('in_progress', 0) > 5:
            recommendations.append("Too many tasks in progress - focus on completing existing work")
        
        if report['task_queue'].get('needs_review', 0) > 3:
            recommendations.append(f"{report['task_queue']['needs_review']} tasks need human review")
        
        # Scene completion
        for expedition, status in report['scene_completion'].items():
            if status.get('placeholders', 0) > 10:
                recommendations.append(f"{expedition} has {status['placeholders']} placeholders - prioritize completion")
        
        # Health score
        if report['health_score'] < 70:
            recommendations.append("⚠️ System health below 70% - review and address issues")
        
        if not recommendations:
            recommendations.append("✅ System healthy - workers can continue autonomous operation")
        
        return recommendations
    
    def save_report(self, report):
        """Save status report to file"""
        reports_dir = self.repo_root / "logs" / "agent-management"
        reports_dir.mkdir(parents=True, exist_ok=True)
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        report_file = reports_dir / f"status-{date_str}.json"
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Full report saved to: {report_file}")
        
        # Also create markdown summary
        md_file = reports_dir / f"status-{date_str}.md"
        self.create_markdown_summary(report, md_file)
        print(f"📄 Markdown summary: {md_file}")
    
    def create_markdown_summary(self, report, filepath):
        """Create human-readable markdown summary"""
        with open(filepath, 'w') as f:
            f.write(f"# Agent Management Status Report\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Health Score:** {report['health_score']}/100\n\n")
            
            f.write("## Configuration\n\n")
            f.write(f"- Silent Mode: {'Enabled' if report['configuration']['silent_mode'] else 'Disabled'}\n")
            f.write(f"- API Key: {'Configured' if report['configuration']['api_key_configured'] else 'Missing'}\n\n")
            
            f.write("## Worker Status\n\n")
            for worker, info in report['workers'].items():
                status_icon = "✅" if info.get('exists') else "⚠️"
                f.write(f"### {status_icon} {worker.replace('-', ' ').title()}\n\n")
                if info.get('exists'):
                    f.write(f"- **Branch:** `{info['branch']}`\n")
                    f.write(f"- **Last Activity:** {info.get('last_commit_time', 'unknown')}\n")
                    f.write(f"- **Last Commit:** {info.get('last_commit_msg', 'unknown')}\n\n")
                else:
                    f.write(f"- **Status:** Not initialized\n\n")
            
            f.write("## Task Queue Summary\n\n")
            tasks = report['task_queue']
            if 'error' not in tasks:
                f.write(f"- Total Tasks: {tasks.get('total', 0)}\n")
                f.write(f"- Completed: {tasks.get('completed', 0)}\n")
                f.write(f"- In Progress: {tasks.get('in_progress', 0)}\n")
                f.write(f"- Pending: {tasks.get('total_pending', 0)}\n")
                f.write(f"- Needs Review: {tasks.get('needs_review', 0)}\n\n")
            
            f.write("## Scene Completion\n\n")
            for expedition, status in report['scene_completion'].items():
                if status.get('exists', True):
                    f.write(f"- **{expedition}:** {status['lines']} lines ({status['estimated_complete']}% complete)\n")
                    if status['placeholders'] > 0:
                        f.write(f"  - ⚠️ {status['placeholders']} placeholders remaining\n")
            
            f.write("\n## Recommendations\n\n")
            for i, rec in enumerate(self.generate_recommendations(report), 1):
                f.write(f"{i}. {rec}\n")

def main():
    """Main execution"""
    orchestrator = AgentOrchestrator()
    
    print("🎯 Avalon Agent Management Orchestrator")
    print("Analyzing AI worker system...\n")
    
    # Generate status report
    report = orchestrator.generate_status_report()
    
    # Print to console
    orchestrator.print_report(report)
    
    # Save to file
    orchestrator.save_report(report)
    
    # Exit code based on health
    health = report['health_score']
    if health >= 80:
        sys.exit(0)  # Healthy
    elif health >= 50:
        sys.exit(1)  # Warning
    else:
        sys.exit(2)  # Critical

if __name__ == '__main__':
    main()
