#!/usr/bin/env python3
"""
Autonomous PR Reviewer
Analyzes PRs for ChoiceScript syntax, merge conflicts, security issues, and code quality
"""

import argparse
import json
import os
import re
import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

def run_command(cmd: List[str]) -> Tuple[int, str, str]:
    """Run shell command and return exit code, stdout, stderr"""
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def check_merge_conflicts() -> Tuple[bool, List[str]]:
    """Check if PR has merge conflicts with main branch"""
    # Fetch latest main
    run_command(['git', 'fetch', 'origin', 'main'])
    
    # Try to merge main into current branch (dry run)
    exit_code, stdout, stderr = run_command([
        'git', 'merge-tree',
        'HEAD',
        'origin/main'
    ])
    
    conflicts = []
    if 'conflict' in stdout.lower() or 'conflict' in stderr.lower():
        # Parse conflict files
        for line in stdout.split('\n') + stderr.split('\n'):
            if 'CONFLICT' in line:
                conflicts.append(line.strip())
    
    has_conflicts = len(conflicts) > 0
    return has_conflicts, conflicts

def validate_choicescript_files() -> Tuple[int, int, List[Dict]]:
    """Validate all ChoiceScript files in the PR"""
    errors = 0
    warnings = 0
    issues = []
    
    # Find all .txt files in choicescript_game/scenes/
    scene_dir = Path('choicescript_game/scenes')
    if not scene_dir.exists():
        return errors, warnings, issues
    
    for txt_file in scene_dir.glob('*.txt'):
        file_errors, file_warnings = validate_choicescript_file(txt_file)
        errors += len(file_errors)
        warnings += len(file_warnings)
        
        for error in file_errors:
            issues.append({
                'file': str(txt_file),
                'type': 'error',
                'message': error
            })
        
        for warning in file_warnings:
            issues.append({
                'file': str(txt_file),
                'type': 'warning',
                'message': warning
            })
    
    return errors, warnings, issues

def validate_choicescript_file(file_path: Path) -> Tuple[List[str], List[str]]:
    """Validate a single ChoiceScript file (reusing existing validator logic)"""
    errors = []
    warnings = []
    
    try:
        content = file_path.read_text()
    except Exception as e:
        return [f"Cannot read file: {e}"], []
    
    lines = content.split('\n')
    labels = set()
    gotos = []
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Skip comments and blank lines
        if not stripped or stripped.startswith('*comment'):
            continue
        
        # 1. Unclosed quotes
        if stripped.startswith('*') and '"' in stripped:
            quotes = stripped.count('"')
            if quotes % 2 != 0:
                errors.append(f"Line {i}: Unclosed quote")
        
        # 2. Label syntax
        if stripped.startswith('*label '):
            label_name = stripped.split('*label ', 1)[1].strip()
            if ' ' in label_name:
                errors.append(f"Line {i}: Label name cannot contain spaces: {label_name}")
            else:
                labels.add(label_name)
        
        # 3. Goto references
        if '*goto ' in stripped or '*goto_scene ' in stripped:
            match = re.search(r'\*goto(?:_scene)?\s+(\w+)', stripped)
            if match:
                gotos.append((match.group(1), i))
        
        # 4. Set command syntax
        if stripped.startswith('*set '):
            parts = stripped.split(None, 2)
            if len(parts) < 3:
                errors.append(f"Line {i}: Invalid *set syntax")
        
        # 5. Choice indentation
        if stripped.startswith('#'):
            found_choice = False
            for j in range(max(0, i-10), i):
                if '*choice' in lines[j]:
                    found_choice = True
                    break
            if not found_choice:
                warnings.append(f"Line {i}: Choice option outside *choice block")
        
        # 6. *if/*else matching
        if stripped.startswith('*else') or stripped.startswith('*elseif'):
            found_if = False
            for j in range(max(0, i-15), i):
                if lines[j].strip().startswith('*if '):
                    found_if = True
                    break
            if not found_if:
                warnings.append(f"Line {i}: *else without matching *if")
    
    # Validate gotos reference existing labels
    for goto_target, line_num in gotos:
        if goto_target not in labels and '_' not in goto_target:
            warnings.append(f"Line {line_num}: *goto {goto_target} references undefined label")
    
    return errors, warnings

def check_security_issues() -> List[Dict]:
    """Basic security checks for common issues"""
    issues = []
    
    # Check for potential secrets in code
    secret_patterns = [
        (r'(password|passwd|pwd)\s*=\s*["\'][\w]+["\']', 'Hardcoded password detected'),
        (r'(api[_-]?key|apikey)\s*=\s*["\'][\w]+["\']', 'Hardcoded API key detected'),
        (r'(secret|token)\s*=\s*["\'][^"\']+["\']', 'Hardcoded secret/token detected'),
    ]
    
    # Search in all files (excluding .git)
    for file_path in Path('.').rglob('*'):
        if file_path.is_file() and '.git' not in str(file_path):
            try:
                content = file_path.read_text()
                for pattern, message in secret_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        issues.append({
                            'file': str(file_path),
                            'type': 'security',
                            'message': message
                        })
            except:
                pass  # Skip binary files
    
    return issues

def assess_risk_level(pr_files: List[str]) -> str:
    """Assess risk level based on changed files"""
    high_risk_patterns = [
        r'\.github/workflows/',
        r'\.github/scripts/.*\.py$',
        r'package\.json$',
        r'requirements\.txt$',
    ]
    
    medium_risk_patterns = [
        r'choicescript_game/scenes/.*\.txt$',
        r'game/.*\.js$',
        r'game/.*\.html$',
    ]
    
    low_risk_patterns = [
        r'\.md$',
        r'docs/',
        r'README',
        r'lore/',
    ]
    
    high_risk_count = 0
    medium_risk_count = 0
    low_risk_count = 0
    
    for file in pr_files:
        if any(re.search(pattern, file) for pattern in high_risk_patterns):
            high_risk_count += 1
        elif any(re.search(pattern, file) for pattern in medium_risk_patterns):
            medium_risk_count += 1
        elif any(re.search(pattern, file) for pattern in low_risk_patterns):
            low_risk_count += 1
    
    # Risk assessment logic
    if high_risk_count > 0:
        return 'high'
    elif medium_risk_count > 3:
        return 'medium'
    elif low_risk_count > 0 and medium_risk_count == 0:
        return 'low'
    else:
        return 'medium'

def get_pr_files(pr_number: int, repo: str) -> List[str]:
    """Get list of files changed in PR using GitHub CLI"""
    exit_code, stdout, stderr = run_command([
        'gh', 'pr', 'view', str(pr_number),
        '--repo', repo,
        '--json', 'files',
        '--jq', '.files[].path'
    ])
    
    if exit_code == 0:
        return [f.strip() for f in stdout.split('\n') if f.strip()]
    return []

def main():
    parser = argparse.ArgumentParser(description='Automated PR Reviewer')
    parser.add_argument('--pr-number', type=int, required=True, help='PR number')
    parser.add_argument('--repo', required=True, help='Repository (owner/repo)')
    args = parser.parse_args()
    
    print(f"🔍 Reviewing PR #{args.pr_number}...")
    
    review_results = {
        'pr_number': args.pr_number,
        'checks': {},
        'needs_fixes': False,
        'can_merge': True,
        'risk_level': 'medium'
    }
    
    # 1. Check for merge conflicts
    print("Checking for merge conflicts...")
    has_conflicts, conflicts = check_merge_conflicts()
    review_results['checks']['merge_conflicts'] = {
        'passed': not has_conflicts,
        'issues': conflicts
    }
    if has_conflicts:
        review_results['needs_fixes'] = True
        review_results['can_merge'] = False
        print(f"❌ Merge conflicts detected: {len(conflicts)}")
    else:
        print("✅ No merge conflicts")
    
    # 2. Validate ChoiceScript syntax
    print("Validating ChoiceScript files...")
    cs_errors, cs_warnings, cs_issues = validate_choicescript_files()
    review_results['checks']['choicescript'] = {
        'errors': cs_errors,
        'warnings': cs_warnings,
        'issues': cs_issues
    }
    if cs_errors > 0:
        review_results['needs_fixes'] = True
        review_results['can_merge'] = False
        print(f"❌ ChoiceScript errors: {cs_errors}")
    else:
        print(f"✅ ChoiceScript validation passed (warnings: {cs_warnings})")
    
    # 3. Check for security issues
    print("Scanning for security issues...")
    security_issues = check_security_issues()
    review_results['checks']['security'] = {
        'issues': security_issues
    }
    if security_issues:
        review_results['can_merge'] = False
        print(f"⚠️ Security issues found: {len(security_issues)}")
    else:
        print("✅ No security issues detected")
    
    # 4. Assess risk level
    print("Assessing risk level...")
    pr_files = get_pr_files(args.pr_number, args.repo)
    risk_level = assess_risk_level(pr_files)
    review_results['risk_level'] = risk_level
    print(f"📊 Risk level: {risk_level.upper()}")
    
    # Generate review report
    report = f"""# 🤖 Automated PR Review Report

**PR:** #{args.pr_number}
**Risk Level:** {risk_level.upper()}

## Summary
- **Merge Conflicts:** {'❌ Found' if has_conflicts else '✅ None'}
- **ChoiceScript Errors:** {cs_errors}
- **ChoiceScript Warnings:** {cs_warnings}
- **Security Issues:** {len(security_issues)}
- **Can Auto-Merge:** {'✅ Yes' if review_results['can_merge'] else '❌ No'}
- **Needs Fixes:** {'✅ Yes' if review_results['needs_fixes'] else '❌ No'}

## Details

### Merge Conflicts
"""
    
    if has_conflicts:
        for conflict in conflicts:
            report += f"- {conflict}\n"
    else:
        report += "No merge conflicts detected.\n"
    
    report += "\n### ChoiceScript Validation\n"
    if cs_issues:
        for issue in cs_issues[:10]:  # Limit to first 10
            report += f"- **{issue['type'].upper()}** in `{issue['file']}`: {issue['message']}\n"
        if len(cs_issues) > 10:
            report += f"\n...and {len(cs_issues) - 10} more issues.\n"
    else:
        report += "All ChoiceScript files passed validation.\n"
    
    report += "\n### Security Scan\n"
    if security_issues:
        for issue in security_issues:
            report += f"- **{issue['type'].upper()}** in `{issue['file']}`: {issue['message']}\n"
    else:
        report += "No security issues detected.\n"
    
    report += f"\n---\n*Auto-Review completed at {subprocess.check_output(['date', '-u']).decode().strip()}*"
    
    # Save report
    Path('/tmp/review_report.md').write_text(report)
    
    # Save structured data for downstream jobs
    Path('/tmp/review_results.json').write_text(json.dumps(review_results, indent=2))
    
    # Set GitHub Actions outputs
    with open(os.environ.get('GITHUB_OUTPUT', '/dev/null'), 'a') as f:
        f.write(f"needs_fixes={'true' if review_results['needs_fixes'] else 'false'}\n")
        f.write(f"can_merge={'true' if review_results['can_merge'] else 'false'}\n")
        f.write(f"risk_level={review_results['risk_level']}\n")
    
    print("\n" + "="*60)
    print(report)
    print("="*60)
    
    # Generate review comments for posting
    comments = []
    if has_conflicts:
        comments.append({
            'body': '## ⚠️ Merge Conflicts Detected\n\nThis PR has merge conflicts with the base branch. The auto-fix system will attempt to resolve them.',
            'path': None,
            'line': None
        })
    
    if cs_errors > 0:
        comments.append({
            'body': f'## ❌ ChoiceScript Errors\n\nFound {cs_errors} syntax errors. Please review the validation report.',
            'path': None,
            'line': None
        })
    
    Path('/tmp/review_comments.json').write_text(json.dumps(comments, indent=2))
    
    print(f"\n✅ Review complete: needs_fixes={review_results['needs_fixes']}, can_merge={review_results['can_merge']}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
