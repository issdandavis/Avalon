#!/usr/bin/env python3
"""
Autonomous PR Auto-Fixer
Automatically fixes common issues in PRs:
- Resolves merge conflicts
- Fixes ChoiceScript syntax errors
- Updates branches
- Formats code
"""

import argparse
import json
import os
import re
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

def run_command(cmd: List[str]) -> Tuple[int, str, str]:
    """Run shell command and return exit code, stdout, stderr"""
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def fix_merge_conflicts() -> Tuple[bool, List[str]]:
    """Attempt to auto-resolve merge conflicts"""
    fixes_applied = []
    
    # Fetch latest main
    run_command(['git', 'fetch', 'origin', 'main'])
    
    # Get list of conflicted files
    exit_code, stdout, stderr = run_command(['git', 'diff', '--name-only', '--diff-filter=U'])
    
    if exit_code != 0 or not stdout.strip():
        # No conflicts or can't detect them, try merge
        exit_code, stdout, stderr = run_command(['git', 'merge', 'origin/main'])
        
        if exit_code == 0:
            return True, ['Successfully merged with main branch']
        
        # Get conflicted files after merge attempt
        exit_code, stdout, stderr = run_command(['git', 'diff', '--name-only', '--diff-filter=U'])
    
    conflicted_files = [f.strip() for f in stdout.split('\n') if f.strip()]
    
    if not conflicted_files:
        return True, ['No merge conflicts to resolve']
    
    # Try to auto-resolve conflicts
    for file_path in conflicted_files:
        if resolve_conflict_in_file(file_path):
            fixes_applied.append(f"Auto-resolved conflicts in {file_path}")
            run_command(['git', 'add', file_path])
    
    if fixes_applied:
        # Commit the conflict resolutions
        run_command(['git', 'commit', '-m', 'Auto-fix: Resolve merge conflicts'])
        return True, fixes_applied
    
    return False, ['Unable to auto-resolve conflicts - manual intervention required']

def resolve_conflict_in_file(file_path: str) -> bool:
    """Attempt to resolve conflicts in a single file"""
    try:
        content = Path(file_path).read_text()
    except:
        return False
    
    # Check if file has conflict markers
    if not ('<<<<<<< HEAD' in content and '=======' in content and '>>>>>>>' in content):
        return False
    
    # For ChoiceScript files and markdown, use simple "ours" strategy for simple conflicts
    if file_path.endswith('.txt') or file_path.endswith('.md'):
        # Try to intelligently merge by keeping both versions when possible
        resolved = resolve_text_conflict(content)
        if resolved != content:
            Path(file_path).write_text(resolved)
            return True
    
    # For other files, try git's auto-merge strategies
    strategies = ['ours', 'theirs', 'union']
    
    for strategy in strategies:
        # Try each strategy
        run_command(['git', 'checkout', '--ours', file_path])
        exit_code, _, _ = run_command(['git', 'merge-file', file_path, file_path, file_path])
        
        if exit_code == 0:
            return True
    
    return False

def resolve_text_conflict(content: str) -> str:
    """Intelligently resolve conflicts in text files"""
    lines = content.split('\n')
    resolved_lines = []
    in_conflict = False
    ours = []
    theirs = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if line.startswith('<<<<<<< HEAD'):
            in_conflict = True
            ours = []
            theirs = []
            i += 1
            continue
        
        if in_conflict:
            if line.startswith('======='):
                # Switch from ours to theirs
                i += 1
                while i < len(lines) and not lines[i].startswith('>>>>>>>'):
                    theirs.append(lines[i])
                    i += 1
                
                # Decide which version to keep
                if not ours and theirs:
                    resolved_lines.extend(theirs)
                elif not theirs and ours:
                    resolved_lines.extend(ours)
                elif ours == theirs:
                    resolved_lines.extend(ours)
                else:
                    # Keep both if they're different and non-empty
                    resolved_lines.extend(ours)
                    if theirs:
                        resolved_lines.append('')
                        resolved_lines.extend(theirs)
                
                in_conflict = False
                i += 1
                continue
            else:
                ours.append(line)
        else:
            resolved_lines.append(line)
        
        i += 1
    
    return '\n'.join(resolved_lines)

def fix_choicescript_syntax() -> Tuple[int, List[str]]:
    """Fix common ChoiceScript syntax errors"""
    fixes_applied = []
    total_fixes = 0
    
    scene_dir = Path('choicescript_game/scenes')
    if not scene_dir.exists():
        return 0, []
    
    for txt_file in scene_dir.glob('*.txt'):
        file_fixes = fix_choicescript_file(txt_file)
        if file_fixes:
            total_fixes += len(file_fixes)
            fixes_applied.extend([f"{txt_file.name}: {fix}" for fix in file_fixes])
    
    return total_fixes, fixes_applied

def fix_choicescript_file(file_path: Path) -> List[str]:
    """Fix syntax errors in a ChoiceScript file"""
    fixes = []
    
    try:
        content = file_path.read_text()
        original_content = content
    except:
        return fixes
    
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        fixed_line = line
        
        # Fix 1: Remove spaces from label names
        if stripped.startswith('*label '):
            label_name = stripped.split('*label ', 1)[1].strip()
            if ' ' in label_name:
                new_label = label_name.replace(' ', '_')
                fixed_line = line.replace(label_name, new_label)
                fixes.append(f"Line {i+1}: Fixed label with spaces: {label_name} -> {new_label}")
        
        # Fix 2: Close unclosed quotes (simple case)
        if stripped.startswith('*') and '"' in stripped:
            quotes = stripped.count('"')
            if quotes % 2 != 0 and not stripped.endswith('"'):
                fixed_line = line + '"'
                fixes.append(f"Line {i+1}: Closed unclosed quote")
        
        # Fix 3: Fix *set command without value
        if stripped.startswith('*set '):
            parts = stripped.split(None, 2)
            if len(parts) == 2:
                # Missing value, add 0 or empty string
                fixed_line = line + ' 0'
                fixes.append(f"Line {i+1}: Added missing value to *set command")
        
        fixed_lines.append(fixed_line)
    
    if fixes:
        # Write back to file
        file_path.write_text('\n'.join(fixed_lines))
    
    return fixes

def update_branch() -> Tuple[bool, str]:
    """Update branch with latest from main"""
    # Fetch latest
    run_command(['git', 'fetch', 'origin', 'main'])
    
    # Try rebase first (cleaner history)
    exit_code, stdout, stderr = run_command(['git', 'rebase', 'origin/main'])
    
    if exit_code == 0:
        return True, "Successfully rebased on main"
    
    # If rebase fails, abort and try merge
    run_command(['git', 'rebase', '--abort'])
    
    exit_code, stdout, stderr = run_command(['git', 'merge', 'origin/main'])
    
    if exit_code == 0:
        return True, "Successfully merged with main"
    
    return False, "Failed to update branch"

def format_code() -> Tuple[int, List[str]]:
    """Basic code formatting fixes"""
    fixes = []
    
    # Fix trailing whitespace in text files
    for file_path in Path('.').rglob('*.txt'):
        if '.git' in str(file_path):
            continue
        
        try:
            content = file_path.read_text()
            lines = content.split('\n')
            fixed_lines = [line.rstrip() for line in lines]
            
            if lines != fixed_lines:
                file_path.write_text('\n'.join(fixed_lines))
                fixes.append(f"Removed trailing whitespace in {file_path}")
        except:
            pass
    
    return len(fixes), fixes

def main():
    parser = argparse.ArgumentParser(description='Automated PR Fixer')
    parser.add_argument('--pr-number', type=int, required=True, help='PR number')
    parser.add_argument('--repo', required=True, help='Repository (owner/repo)')
    args = parser.parse_args()
    
    print(f"🔧 Auto-fixing issues in PR #{args.pr_number}...")
    
    all_fixes = {
        'pr_number': args.pr_number,
        'fixes_applied': [],
        'total_fixes': 0,
        'success': False
    }
    
    # 1. Fix merge conflicts
    print("\n1. Checking for merge conflicts...")
    conflicts_fixed, conflict_fixes = fix_merge_conflicts()
    if conflict_fixes:
        all_fixes['fixes_applied'].extend([f"[Merge] {f}" for f in conflict_fixes])
        all_fixes['total_fixes'] += len(conflict_fixes)
        if conflicts_fixed:
            print(f"✅ Fixed {len(conflict_fixes)} merge conflict(s)")
        else:
            print(f"⚠️ Could not auto-fix merge conflicts")
    
    # 2. Fix ChoiceScript syntax
    print("\n2. Fixing ChoiceScript syntax errors...")
    cs_fixes_count, cs_fixes = fix_choicescript_syntax()
    if cs_fixes_count > 0:
        all_fixes['fixes_applied'].extend([f"[ChoiceScript] {f}" for f in cs_fixes])
        all_fixes['total_fixes'] += cs_fixes_count
        print(f"✅ Fixed {cs_fixes_count} ChoiceScript issue(s)")
        
        # Commit syntax fixes
        run_command(['git', 'add', 'choicescript_game/scenes/'])
        run_command(['git', 'commit', '-m', f'Auto-fix: ChoiceScript syntax ({cs_fixes_count} fixes)'])
    else:
        print("✅ No ChoiceScript syntax errors to fix")
    
    # 3. Format code
    print("\n3. Applying code formatting...")
    format_count, format_fixes = format_code()
    if format_count > 0:
        all_fixes['fixes_applied'].extend([f"[Format] {f}" for f in format_fixes])
        all_fixes['total_fixes'] += format_count
        print(f"✅ Applied {format_count} formatting fix(es)")
        
        # Commit formatting fixes
        run_command(['git', 'add', '.'])
        run_command(['git', 'commit', '-m', f'Auto-fix: Code formatting ({format_count} fixes)'])
    else:
        print("✅ Code formatting is clean")
    
    # 4. Update branch if needed
    print("\n4. Checking branch status...")
    updated, update_msg = update_branch()
    if updated and 'Successfully' in update_msg:
        all_fixes['fixes_applied'].append(f"[Branch] {update_msg}")
        print(f"✅ {update_msg}")
    
    # Generate summary
    all_fixes['success'] = all_fixes['total_fixes'] > 0
    
    summary = f"""# 🔧 Auto-Fix Summary

**PR:** #{args.pr_number}
**Total Fixes Applied:** {all_fixes['total_fixes']}

## Fixes Applied

"""
    
    if all_fixes['fixes_applied']:
        for fix in all_fixes['fixes_applied']:
            summary += f"- {fix}\n"
    else:
        summary += "No fixes were needed - the PR is already in good shape!\n"
    
    summary += f"\n---\n*Auto-fix completed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}*"
    
    # Save summary
    Path('/tmp/fix_summary.md').write_text(summary)
    Path('/tmp/fix_details.json').write_text(json.dumps(all_fixes, indent=2))
    
    # Set GitHub Actions outputs
    with open(os.environ.get('GITHUB_OUTPUT', '/dev/null'), 'a') as f:
        f.write(f"fixed={'true' if all_fixes['success'] else 'false'}\n")
        f.write(f"fix_count={all_fixes['total_fixes']}\n")
        if all_fixes['total_fixes'] > 0:
            # Get the latest commit SHA
            exit_code, stdout, _ = run_command(['git', 'rev-parse', 'HEAD'])
            if exit_code == 0:
                f.write(f"fix_commit={stdout.strip()}\n")
    
    print("\n" + "="*60)
    print(summary)
    print("="*60)
    
    print(f"\n✅ Auto-fix complete: {all_fixes['total_fixes']} fixes applied")
    return 0

if __name__ == '__main__':
    sys.exit(main())
