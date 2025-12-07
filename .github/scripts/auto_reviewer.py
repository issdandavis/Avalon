#!/usr/bin/env python3
"""
Auto-Reviewer - AI-Powered PR Review System
Automatically reviews pull requests and provides feedback
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

class AutoReviewer:
    """Automated PR review system"""
    
    def __init__(self, pr_number: str):
        self.pr_number = pr_number
        self.repo_root = Path.cwd()
        self.errors = []
        self.warnings = []
        self.suggestions = []
        self.risk_level = "low"
        
    def review_pr(self) -> Dict:
        """Main review logic"""
        print(f"🔍 Reviewing PR #{self.pr_number}...")
        
        # Get changed files
        changed_files = self._get_changed_files()
        print(f"📝 Found {len(changed_files)} changed files")
        
        # Analyze files
        for file_path in changed_files:
            self._analyze_file(file_path)
        
        # Determine risk level
        self._assess_risk(changed_files)
        
        # Generate review summary
        return self._generate_review()
    
    def _get_changed_files(self) -> List[str]:
        """Get list of changed files in PR"""
        try:
            result = subprocess.run(
                ['git', 'diff', '--name-only', 'main...HEAD'],
                capture_output=True,
                text=True,
                check=True
            )
            files = [f.strip() for f in result.stdout.split('\n') if f.strip()]
            return files
        except subprocess.CalledProcessError:
            print("⚠️ Could not get changed files, trying alternative")
            try:
                # Try without origin prefix
                result = subprocess.run(
                    ['git', 'diff', '--name-only', 'HEAD^', 'HEAD'],
                    capture_output=True,
                    text=True,
                    check=True
                )
                files = [f.strip() for f in result.stdout.split('\n') if f.strip()]
                return files
            except subprocess.CalledProcessError:
                return []
    
    def _analyze_file(self, file_path: str):
        """Analyze a single file for issues"""
        path = Path(file_path)
        
        # Skip deleted files
        if not path.exists():
            return
        
        # Check file extension
        if path.suffix == '.txt' and 'choicescript_game/scenes' in file_path:
            self._check_choicescript_file(path)
        elif path.suffix == '.py':
            self._check_python_file(path)
        elif path.suffix in ['.yml', '.yaml']:
            self._check_yaml_file(path)
        elif path.suffix == '.md':
            self._check_markdown_file(path)
    
    def _check_choicescript_file(self, path: Path):
        """Check ChoiceScript syntax"""
        try:
            content = path.read_text()
            lines = content.split('\n')
            
            # Basic syntax checks
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                
                # Check for unclosed quotes
                if stripped.startswith('*') and '"' in stripped:
                    if stripped.count('"') % 2 != 0:
                        self.errors.append(f"{path.name}:{i} - Unclosed quote")
                
                # Check for invalid label names
                if stripped.startswith('*label '):
                    label = stripped.split('*label ', 1)[1].strip()
                    if ' ' in label:
                        self.errors.append(f"{path.name}:{i} - Label contains spaces: {label}")
                
                # Check for *create in non-startup files
                if stripped.startswith('*create ') and path.name != 'startup.txt':
                    self.errors.append(f"{path.name}:{i} - *create only allowed in startup.txt")
            
            # Check for required *choice structure
            if '*choice' in content:
                if not any(line.strip().startswith('#') for line in lines):
                    self.warnings.append(f"{path.name} - *choice without options")
        
        except Exception as e:
            self.errors.append(f"{path.name} - Error reading file: {e}")
    
    def _check_python_file(self, path: Path):
        """Check Python file quality"""
        try:
            # Check for basic syntax
            compile(path.read_text(), str(path), 'exec')
            
            # Check for security patterns
            content = path.read_text()
            if 'eval(' in content:
                self.warnings.append(f"{path.name} - Uses eval() which can be unsafe")
            if 'exec(' in content:
                self.warnings.append(f"{path.name} - Uses exec() which can be unsafe")
            
            # Check for shebang
            first_line = path.read_text().split('\n')[0]
            if not first_line.startswith('#!'):
                self.suggestions.append(f"{path.name} - Consider adding shebang (#!/usr/bin/env python3)")
        
        except SyntaxError as e:
            self.errors.append(f"{path.name}:{e.lineno} - Syntax error: {e.msg}")
        except Exception as e:
            self.errors.append(f"{path.name} - Error checking file: {e}")
    
    def _check_yaml_file(self, path: Path):
        """Check YAML file syntax"""
        try:
            import yaml
            content = path.read_text()
            yaml.safe_load(content)
        except ImportError:
            # yaml not available, skip detailed check
            pass
        except Exception as e:
            self.errors.append(f"{path.name} - YAML syntax error: {e}")
    
    def _check_markdown_file(self, path: Path):
        """Check Markdown file for common issues"""
        try:
            content = path.read_text()
            
            # Check for broken links
            import re
            links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
            for text, url in links:
                if url.startswith('/') or url.startswith('./'):
                    link_path = self.repo_root / url.lstrip('./')
                    if not link_path.exists():
                        self.warnings.append(f"{path.name} - Broken link: {url}")
        
        except Exception as e:
            self.warnings.append(f"{path.name} - Error checking markdown: {e}")
    
    def _assess_risk(self, changed_files: List[str]):
        """Assess overall risk level of changes"""
        high_risk_patterns = [
            '.github/workflows/',
            'config/',
            '.github/scripts/',
            'startup.txt'
        ]
        
        medium_risk_patterns = [
            'choicescript_game/scenes/',
            'game/scenes/',
            '.py'
        ]
        
        # Check for high-risk changes
        for file in changed_files:
            if any(pattern in file for pattern in high_risk_patterns):
                self.risk_level = "high"
                return
        
        # Check for medium-risk changes
        for file in changed_files:
            if any(pattern in file for pattern in medium_risk_patterns):
                self.risk_level = "medium"
                # Don't return, might find high-risk later
        
        # Default is low risk (docs, etc.)
        if self.risk_level != "medium":
            self.risk_level = "low"
    
    def _generate_review(self) -> Dict:
        """Generate review summary"""
        review = {
            'pr_number': self.pr_number,
            'risk_level': self.risk_level,
            'errors': self.errors,
            'warnings': self.warnings,
            'suggestions': self.suggestions,
            'approved': len(self.errors) == 0,
            'can_auto_merge': len(self.errors) == 0 and self.risk_level in ['low', 'medium']
        }
        
        return review
    
    def print_review(self, review: Dict):
        """Print review results"""
        print("\n" + "="*60)
        print(f"📊 Review Summary for PR #{review['pr_number']}")
        print("="*60)
        
        print(f"\n🎯 Risk Level: {review['risk_level'].upper()}")
        
        if review['errors']:
            print(f"\n❌ Errors ({len(review['errors'])}):")
            for error in review['errors']:
                print(f"  - {error}")
        else:
            print("\n✅ No errors found")
        
        if review['warnings']:
            print(f"\n⚠️ Warnings ({len(review['warnings'])}):")
            for warning in review['warnings']:
                print(f"  - {warning}")
        
        if review['suggestions']:
            print(f"\n💡 Suggestions ({len(review['suggestions'])}):")
            for suggestion in review['suggestions']:
                print(f"  - {suggestion}")
        
        print(f"\n{'='*60}")
        if review['approved']:
            print("✅ APPROVED - No blocking issues found")
        else:
            print("❌ CHANGES REQUESTED - Fix errors before merging")
        
        if review['can_auto_merge']:
            print("🤖 AUTO-MERGE: Eligible")
        else:
            print("👤 MANUAL REVIEW: Required")
        
        print("="*60 + "\n")

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: auto_reviewer.py <pr_number>")
        sys.exit(1)
    
    pr_number = sys.argv[1]
    reviewer = AutoReviewer(pr_number)
    review = reviewer.review_pr()
    reviewer.print_review(review)
    
    # Write review to file for other scripts
    output_file = Path("/tmp/review_result.json")
    output_file.write_text(json.dumps(review, indent=2))
    print(f"💾 Review saved to {output_file}")
    
    # Exit with error code if not approved
    sys.exit(0 if review['approved'] else 1)

if __name__ == "__main__":
    main()
