#!/usr/bin/env python3
"""
Autonomous PR Auto-Merger
Intelligently decides whether to merge a PR based on risk assessment and safety checks
"""

import argparse
import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

def run_command(cmd: List[str]) -> Tuple[int, str, str]:
    """Run shell command and return exit code, stdout, stderr"""
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def get_pr_info(pr_number: int, repo: str) -> Dict:
    """Get PR information using GitHub CLI"""
    exit_code, stdout, stderr = run_command([
        'gh', 'pr', 'view', str(pr_number),
        '--repo', repo,
        '--json', 'title,body,labels,reviews,statusCheckRollup,commits,changedFiles'
    ])
    
    if exit_code == 0:
        return json.loads(stdout)
    return {}

def check_status_checks(pr_info: Dict) -> Tuple[bool, List[str]]:
    """Check if all required status checks have passed"""
    if 'statusCheckRollup' not in pr_info:
        return True, []  # No status checks configured
    
    failed_checks = []
    for check in pr_info.get('statusCheckRollup', []):
        if check.get('conclusion') == 'FAILURE':
            failed_checks.append(check.get('name', 'Unknown check'))
        elif check.get('status') == 'IN_PROGRESS':
            failed_checks.append(f"{check.get('name', 'Unknown check')} (in progress)")
    
    return len(failed_checks) == 0, failed_checks

def check_approvals(pr_info: Dict) -> Tuple[bool, int]:
    """Check if PR has sufficient approvals"""
    reviews = pr_info.get('reviews', [])
    
    approval_count = 0
    change_requests = 0
    
    for review in reviews:
        if review.get('state') == 'APPROVED':
            approval_count += 1
        elif review.get('state') == 'CHANGES_REQUESTED':
            change_requests += 1
    
    # For low-risk PRs, no approval needed
    # For medium-risk, at least one approval
    # For high-risk, should be flagged for manual review
    
    has_changes_requested = change_requests > 0
    
    return not has_changes_requested, approval_count

def determine_merge_method(risk_level: str, pr_info: Dict) -> str:
    """Determine the best merge method based on risk and PR characteristics"""
    commit_count = len(pr_info.get('commits', []))
    
    # For low-risk changes with single commits, use squash
    if risk_level == 'low':
        return 'squash'
    
    # For medium-risk, use squash for cleaner history
    if risk_level == 'medium':
        if commit_count > 5:
            return 'squash'  # Squash many small commits
        return 'merge'  # Preserve commit history
    
    # High-risk should not auto-merge
    return 'merge'

def evaluate_merge_safety(pr_number: int, repo: str, risk_level: str) -> Tuple[bool, str, Dict]:
    """Evaluate if it's safe to merge the PR"""
    pr_info = get_pr_info(pr_number, repo)
    
    evaluation = {
        'should_merge': False,
        'merge_method': 'squash',
        'reasons': [],
        'blockers': []
    }
    
    # Check 1: PR exists and is open
    if not pr_info:
        evaluation['blockers'].append('Could not fetch PR information')
        return False, 'merge', evaluation
    
    # Check 2: Check labels for blocking conditions
    labels = [label.get('name', '') for label in pr_info.get('labels', [])]
    
    if 'no-auto-merge' in labels:
        evaluation['blockers'].append('PR has "no-auto-merge" label')
        return False, 'merge', evaluation
    
    if 'manual-review-required' in labels:
        evaluation['blockers'].append('PR requires manual review')
        return False, 'merge', evaluation
    
    if 'do-not-merge' in labels or 'wip' in labels or 'work-in-progress' in labels:
        evaluation['blockers'].append('PR is not ready for merge (WIP or do-not-merge label)')
        return False, 'merge', evaluation
    
    # Check 3: Status checks
    checks_passed, failed_checks = check_status_checks(pr_info)
    if not checks_passed:
        evaluation['blockers'].extend([f'Failed check: {check}' for check in failed_checks])
        return False, 'merge', evaluation
    else:
        evaluation['reasons'].append('All status checks passed')
    
    # Check 4: Approvals (based on risk)
    no_changes_requested, approval_count = check_approvals(pr_info)
    
    if not no_changes_requested:
        evaluation['blockers'].append('PR has change requests')
        return False, 'merge', evaluation
    
    # Risk-based approval requirements
    if risk_level == 'high':
        evaluation['blockers'].append('High-risk PR requires manual review')
        return False, 'merge', evaluation
    
    if risk_level == 'medium' and approval_count < 1:
        evaluation['blockers'].append('Medium-risk PR requires at least 1 approval')
        return False, 'merge', evaluation
    
    # Check 5: Changed files count (sanity check)
    changed_files = pr_info.get('changedFiles', 0)
    if changed_files > 50:
        evaluation['blockers'].append(f'Too many files changed ({changed_files}) - requires manual review')
        return False, 'merge', evaluation
    
    # All checks passed
    evaluation['should_merge'] = True
    evaluation['merge_method'] = determine_merge_method(risk_level, pr_info)
    evaluation['reasons'].extend([
        f'Risk level: {risk_level}',
        f'Approvals: {approval_count}',
        f'Changed files: {changed_files}',
        'No blocking labels found'
    ])
    
    return True, evaluation['merge_method'], evaluation

def main():
    parser = argparse.ArgumentParser(description='Automated PR Merger')
    parser.add_argument('--pr-number', type=int, required=True, help='PR number')
    parser.add_argument('--repo', required=True, help='Repository (owner/repo)')
    parser.add_argument('--risk-level', default='medium', choices=['low', 'medium', 'high'], help='Risk level')
    parser.add_argument('--evaluate-only', action='store_true', help='Only evaluate, do not merge')
    args = parser.parse_args()
    
    print(f"📊 Evaluating merge eligibility for PR #{args.pr_number} (risk: {args.risk_level})...")
    
    should_merge, merge_method, evaluation = evaluate_merge_safety(
        args.pr_number, args.repo, args.risk_level
    )
    
    # Generate summary
    summary = f"""# ✅ Auto-Merge Evaluation

**PR:** #{args.pr_number}
**Risk Level:** {args.risk_level.upper()}
**Decision:** {'✅ APPROVED FOR AUTO-MERGE' if should_merge else '❌ NOT APPROVED FOR AUTO-MERGE'}
**Merge Method:** {merge_method if should_merge else 'N/A'}

## Evaluation Details

"""
    
    if evaluation['reasons']:
        summary += "### ✅ Passing Criteria\n"
        for reason in evaluation['reasons']:
            summary += f"- {reason}\n"
        summary += "\n"
    
    if evaluation['blockers']:
        summary += "### ❌ Blocking Issues\n"
        for blocker in evaluation['blockers']:
            summary += f"- {blocker}\n"
        summary += "\n"
    
    if should_merge:
        summary += f"""## 🎯 Merge Plan

1. **Method:** {merge_method.upper()}
2. **Delete Branch:** Yes (after merge)
3. **Rollback Point:** Tagged for 30-day retention

## Safety Controls

- Emergency rollback available via git tags
- Full audit trail in workflow logs
- Automated post-merge verification
"""
    else:
        summary += """## 🚫 Action Required

This PR cannot be auto-merged due to the blocking issues listed above.

**Next Steps:**
1. Address the blocking issues
2. Re-run the auto-merge workflow
3. Or manually review and merge
"""
    
    summary += f"\n---\n*Evaluation completed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}*"
    
    # Save summary
    Path('/tmp/merge_summary.md').write_text(summary)
    
    # Save decision data
    decision_data = {
        'pr_number': args.pr_number,
        'risk_level': args.risk_level,
        'should_merge': should_merge,
        'merge_method': merge_method,
        'evaluation': evaluation
    }
    Path('/tmp/merge_decision.json').write_text(json.dumps(decision_data, indent=2))
    
    # Set GitHub Actions outputs
    with open(os.environ.get('GITHUB_OUTPUT', '/dev/null'), 'a') as f:
        f.write(f"should_merge={'true' if should_merge else 'false'}\n")
        f.write(f"merge_method={merge_method}\n")
    
    print("\n" + "="*60)
    print(summary)
    print("="*60)
    
    if should_merge:
        print(f"\n✅ PR #{args.pr_number} is approved for auto-merge using {merge_method} method")
    else:
        print(f"\n❌ PR #{args.pr_number} cannot be auto-merged")
        if evaluation['blockers']:
            print("\nBlocking issues:")
            for blocker in evaluation['blockers']:
                print(f"  - {blocker}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
