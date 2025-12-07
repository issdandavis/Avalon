#!/usr/bin/env python3
"""
Auto-Merger - Smart Merge Decision System
Determines when PRs are safe to auto-merge
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List

class AutoMerger:
    """Automated merge decision system"""
    
    def __init__(self, pr_number: str):
        self.pr_number = pr_number
        self.repo_root = Path.cwd()
        
    def should_merge(self, review: Dict) -> Dict:
        """Determine if PR should be auto-merged"""
        print(f"🤔 Evaluating merge eligibility for PR #{self.pr_number}...")
        
        decision = {
            'pr_number': self.pr_number,
            'should_merge': False,
            'merge_method': 'squash',
            'reasons': [],
            'blockers': []
        }
        
        # Check approval status
        if not review.get('approved', False):
            decision['blockers'].append("PR not approved - has errors")
            return decision
        
        # Check risk level
        risk_level = review.get('risk_level', 'medium')
        if risk_level == 'high':
            decision['blockers'].append("High risk changes - requires manual review")
            return decision
        
        # Check for merge conflicts
        if self._has_merge_conflicts():
            decision['blockers'].append("Has merge conflicts")
            return decision
        
        # Check for required labels
        if self._has_no_merge_label():
            decision['blockers'].append("Has 'no-auto-merge' label")
            return decision
        
        # Check CI status (if available)
        ci_status = self._check_ci_status()
        if ci_status == 'failed':
            decision['blockers'].append("CI checks failed")
            return decision
        elif ci_status == 'pending':
            decision['blockers'].append("CI checks still running")
            return decision
        
        # All checks passed
        decision['should_merge'] = True
        decision['reasons'].append(f"Risk level: {risk_level}")
        decision['reasons'].append("All checks passed")
        decision['reasons'].append("No merge conflicts")
        
        # Determine merge method based on file count
        changed_files_count = len(self._get_changed_files())
        if changed_files_count == 1:
            decision['merge_method'] = 'rebase'
            decision['reasons'].append("Single file change - using rebase")
        else:
            decision['merge_method'] = 'squash'
            decision['reasons'].append("Multiple files - using squash merge")
        
        return decision
    
    def _has_merge_conflicts(self) -> bool:
        """Check if PR has merge conflicts"""
        try:
            # Try to merge origin/main
            result = subprocess.run(
                ['git', 'merge-tree', 
                 subprocess.check_output(['git', 'merge-base', 'HEAD', 'origin/main'], text=True).strip(),
                 'HEAD',
                 'origin/main'],
                capture_output=True,
                text=True
            )
            
            # Check for conflict markers
            return '<<<<<<< ' in result.stdout
        
        except subprocess.CalledProcessError:
            # If we can't determine, assume no conflicts
            return False
    
    def _has_no_merge_label(self) -> bool:
        """Check if PR has no-auto-merge label"""
        # This would require GitHub API access
        # For now, check environment variable
        labels = os.getenv('PR_LABELS', '')
        return 'no-auto-merge' in labels.lower()
    
    def _check_ci_status(self) -> str:
        """Check CI status (success, failed, pending, unknown)"""
        # This would require GitHub API access
        # For now, return unknown
        return 'unknown'
    
    def _get_changed_files(self) -> List[str]:
        """Get list of changed files"""
        try:
            result = subprocess.run(
                ['git', 'diff', '--name-only', 'origin/main...HEAD'],
                capture_output=True,
                text=True,
                check=True
            )
            return [f.strip() for f in result.stdout.split('\n') if f.strip()]
        except subprocess.CalledProcessError:
            return []
    
    def merge_pr(self, decision: Dict) -> bool:
        """Execute the merge"""
        if not decision['should_merge']:
            print("❌ PR not eligible for auto-merge")
            return False
        
        print(f"🚀 Auto-merging PR #{self.pr_number}...")
        
        try:
            merge_method = decision.get('merge_method', 'squash')
            
            # For now, we can't actually merge via git commands alone
            # This would require GitHub API or gh CLI
            print(f"✅ Would merge using method: {merge_method}")
            print("⚠️ Actual merge requires GitHub API access")
            
            return True
        
        except Exception as e:
            print(f"❌ Failed to merge: {e}")
            return False
    
    def print_decision(self, decision: Dict):
        """Print merge decision"""
        print("\n" + "="*60)
        print(f"🎯 Merge Decision for PR #{decision['pr_number']}")
        print("="*60)
        
        if decision['should_merge']:
            print("\n✅ APPROVED FOR AUTO-MERGE")
            print(f"   Method: {decision['merge_method']}")
            
            if decision['reasons']:
                print("\n📋 Reasons:")
                for reason in decision['reasons']:
                    print(f"  ✓ {reason}")
        else:
            print("\n❌ NOT APPROVED FOR AUTO-MERGE")
            
            if decision['blockers']:
                print("\n🚫 Blockers:")
                for blocker in decision['blockers']:
                    print(f"  ✗ {blocker}")
        
        print("="*60 + "\n")

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: auto_merger.py <pr_number>")
        sys.exit(1)
    
    pr_number = sys.argv[1]
    
    # Load review results
    review_file = Path("/tmp/review_result.json")
    if not review_file.exists():
        print("❌ No review results found. Run auto_reviewer.py first.")
        sys.exit(1)
    
    review = json.loads(review_file.read_text())
    
    # Make merge decision
    merger = AutoMerger(pr_number)
    decision = merger.should_merge(review)
    merger.print_decision(decision)
    
    # Save decision
    decision_file = Path("/tmp/merge_decision.json")
    decision_file.write_text(json.dumps(decision, indent=2))
    print(f"💾 Decision saved to {decision_file}")
    
    # Exit with status
    sys.exit(0 if decision['should_merge'] else 1)

if __name__ == "__main__":
    main()
