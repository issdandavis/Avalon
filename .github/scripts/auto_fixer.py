#!/usr/bin/env python3
"""
Auto-Fixer - Automated Issue Resolution
Automatically fixes common issues in PRs
"""

import os
import sys
import json
import subprocess
import re
from pathlib import Path
from typing import Dict, List

class AutoFixer:
    """Automated issue fixing system"""
    
    def __init__(self, pr_number: str):
        self.pr_number = pr_number
        self.repo_root = Path.cwd()
        self.fixes_applied = []
        
    def fix_issues(self, review: Dict) -> bool:
        """Attempt to fix issues found in review"""
        print(f"🔧 Auto-fixing issues in PR #{self.pr_number}...")
        
        # Load review results
        errors = review.get('errors', [])
        warnings = review.get('warnings', [])
        
        if not errors and not warnings:
            print("✅ No issues to fix")
            return True
        
        # Try to fix each error
        for error in errors:
            self._fix_error(error)
        
        # Try to fix warnings
        for warning in warnings:
            self._fix_warning(warning)
        
        # Report fixes
        if self.fixes_applied:
            print(f"\n✅ Applied {len(self.fixes_applied)} fixes:")
            for fix in self.fixes_applied:
                print(f"  - {fix}")
            return True
        else:
            print("\n⚠️ Could not auto-fix issues")
            return False
    
    def _fix_error(self, error: str):
        """Try to fix a specific error"""
        # Parse error format: "filename:line - description"
        match = re.match(r'(.+?):(\d+) - (.+)', error)
        if not match:
            return
        
        filename, line_num, description = match.groups()
        line_num = int(line_num)
        
        # Find the file
        file_path = self._find_file(filename)
        if not file_path:
            return
        
        # Fix based on error type
        if "Unclosed quote" in description:
            self._fix_unclosed_quote(file_path, line_num)
        elif "Label contains spaces" in description:
            self._fix_label_spaces(file_path, line_num)
        elif "*create only allowed in startup.txt" in description:
            self._fix_misplaced_create(file_path, line_num)
    
    def _fix_warning(self, warning: str):
        """Try to fix a specific warning"""
        # Most warnings are informational and don't need auto-fix
        pass
    
    def _find_file(self, filename: str) -> Path:
        """Find a file in the repository"""
        # Try common locations
        candidates = [
            self.repo_root / filename,
            self.repo_root / 'choicescript_game' / 'scenes' / filename,
            self.repo_root / 'game' / 'scenes' / filename,
            self.repo_root / '.github' / 'scripts' / filename,
        ]
        
        for candidate in candidates:
            if candidate.exists():
                return candidate
        
        # Search recursively
        for path in self.repo_root.rglob(filename):
            return path
        
        return None
    
    def _fix_unclosed_quote(self, file_path: Path, line_num: int):
        """Fix unclosed quote in a line"""
        try:
            lines = file_path.read_text().split('\n')
            if line_num > len(lines):
                return
            
            line = lines[line_num - 1]
            
            # Count quotes
            if line.count('"') % 2 != 0:
                # Add closing quote before any trailing comment or at end
                # Check for comment markers
                comment_pos = line.find('*comment')
                if comment_pos > 0:
                    # Insert quote before comment
                    lines[line_num - 1] = line[:comment_pos].rstrip() + '" ' + line[comment_pos:]
                else:
                    # Add closing quote at end of content
                    lines[line_num - 1] = line.rstrip() + '"'
                
                file_path.write_text('\n'.join(lines))
                self.fixes_applied.append(f"Fixed unclosed quote in {file_path.name}:{line_num}")
        
        except Exception as e:
            print(f"⚠️ Could not fix unclosed quote: {e}")
    
    def _fix_label_spaces(self, file_path: Path, line_num: int):
        """Fix label with spaces by replacing spaces with underscores"""
        try:
            lines = file_path.read_text().split('\n')
            if line_num > len(lines):
                return
            
            line = lines[line_num - 1]
            
            # Replace spaces in label name
            if '*label ' in line:
                parts = line.split('*label ', 1)
                label = parts[1].strip()
                new_label = label.replace(' ', '_')
                lines[line_num - 1] = parts[0] + '*label ' + new_label
                file_path.write_text('\n'.join(lines))
                self.fixes_applied.append(f"Fixed label spaces in {file_path.name}:{line_num}")
        
        except Exception as e:
            print(f"⚠️ Could not fix label spaces: {e}")
    
    def _fix_misplaced_create(self, file_path: Path, line_num: int):
        """Remove *create from non-startup files"""
        try:
            lines = file_path.read_text().split('\n')
            if line_num > len(lines):
                return
            
            line = lines[line_num - 1]
            
            # Comment out the *create line properly
            if '*create ' in line:
                # Replace *create with *comment about the variable
                var_name = line.split('*create ', 1)[1].split()[0] if ' ' in line.split('*create ', 1)[1] else 'variable'
                lines[line_num - 1] = f'*comment Variable {var_name} should be defined in startup.txt'
                file_path.write_text('\n'.join(lines))
                self.fixes_applied.append(f"Commented out misplaced *create in {file_path.name}:{line_num}")
        
        except Exception as e:
            print(f"⚠️ Could not fix misplaced *create: {e}")
    
    def update_branch(self) -> bool:
        """Update branch with upstream changes"""
        try:
            print("🔄 Updating branch with latest changes...")
            
            # Fetch latest
            subprocess.run(['git', 'fetch', 'origin', 'main'], check=True)
            
            # Try to rebase
            result = subprocess.run(
                ['git', 'rebase', 'origin/main'],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print("⚠️ Rebase failed, trying merge instead...")
                subprocess.run(['git', 'rebase', '--abort'], check=False)
                subprocess.run(['git', 'merge', 'origin/main'], check=True)
            
            print("✅ Branch updated successfully")
            return True
        
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to update branch: {e}")
            return False
    
    def commit_fixes(self) -> bool:
        """Commit applied fixes"""
        if not self.fixes_applied:
            return False
        
        try:
            # Stage all changes
            subprocess.run(['git', 'add', '-A'], check=True)
            
            # Create commit message
            commit_msg = f"🤖 Auto-fix: Applied {len(self.fixes_applied)} fixes\n\n"
            commit_msg += '\n'.join(f"- {fix}" for fix in self.fixes_applied)
            
            # Commit
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
            print(f"✅ Committed {len(self.fixes_applied)} fixes")
            return True
        
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to commit fixes: {e}")
            return False

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: auto_fixer.py <pr_number>")
        sys.exit(1)
    
    pr_number = sys.argv[1]
    
    # Load review results
    review_file = Path("/tmp/review_result.json")
    if not review_file.exists():
        print("❌ No review results found. Run auto_reviewer.py first.")
        sys.exit(1)
    
    review = json.loads(review_file.read_text())
    
    # Apply fixes
    fixer = AutoFixer(pr_number)
    success = fixer.fix_issues(review)
    
    if success and fixer.fixes_applied:
        # Commit fixes
        fixer.commit_fixes()
        print("\n✅ Fixes applied and committed")
        sys.exit(0)
    else:
        print("\n⚠️ No fixes could be applied")
        sys.exit(1)

if __name__ == "__main__":
    main()
