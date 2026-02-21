#!/usr/bin/env python3
"""
Conflict Resolver - AI-Powered Merge Conflict Resolution
Automatically resolves merge conflicts using intelligent strategies
"""

import os
import sys
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

class ConflictResolver:
    """Automated conflict resolution system"""
    
    def __init__(self):
        self.repo_root = Path.cwd()
        self.conflicts_resolved = []
        
    def detect_conflicts(self) -> List[str]:
        """Detect files with merge conflicts"""
        try:
            result = subprocess.run(
                ['git', 'diff', '--name-only', '--diff-filter=U'],
                capture_output=True,
                text=True,
                check=True
            )
            
            conflicts = [f.strip() for f in result.stdout.split('\n') if f.strip()]
            return conflicts
        
        except subprocess.CalledProcessError:
            return []
    
    def resolve_conflicts(self) -> bool:
        """Attempt to resolve all conflicts"""
        conflicts = self.detect_conflicts()
        
        if not conflicts:
            print("✅ No conflicts detected")
            return True
        
        print(f"🔍 Found {len(conflicts)} conflicted files")
        
        success = True
        for file_path in conflicts:
            if self._resolve_file(file_path):
                self.conflicts_resolved.append(file_path)
            else:
                print(f"❌ Could not auto-resolve: {file_path}")
                success = False
        
        if self.conflicts_resolved:
            print(f"\n✅ Resolved {len(self.conflicts_resolved)} conflicts:")
            for file in self.conflicts_resolved:
                print(f"  - {file}")
        
        return success
    
    def _resolve_file(self, file_path: str) -> bool:
        """Resolve conflicts in a single file"""
        path = Path(file_path)
        
        if not path.exists():
            return False
        
        try:
            content = path.read_text()
            
            # Parse conflict markers
            conflicts = self._parse_conflicts(content)
            
            if not conflicts:
                return False
            
            # Attempt resolution
            resolved_content = self._apply_resolution_strategy(content, conflicts, path.suffix)
            
            if resolved_content:
                path.write_text(resolved_content)
                subprocess.run(['git', 'add', file_path], check=True)
                print(f"✅ Resolved conflicts in {file_path}")
                return True
            
            return False
        
        except Exception as e:
            print(f"⚠️ Error resolving {file_path}: {e}")
            return False
    
    def _parse_conflicts(self, content: str) -> List[Dict]:
        """Parse conflict markers in content"""
        conflicts = []
        lines = content.split('\n')
        
        i = 0
        while i < len(lines):
            if lines[i].startswith('<<<<<<<'):
                # Found conflict start
                conflict = {
                    'start': i,
                    'marker': lines[i],
                    'ours': [],
                    'theirs': [],
                    'base': []
                }
                
                i += 1
                # Collect 'ours' section
                while i < len(lines) and not lines[i].startswith('======='):
                    conflict['ours'].append(lines[i])
                    i += 1
                
                if i < len(lines):
                    i += 1  # Skip =======
                
                # Collect 'theirs' section
                while i < len(lines) and not lines[i].startswith('>>>>>>>'):
                    conflict['theirs'].append(lines[i])
                    i += 1
                
                if i < len(lines):
                    conflict['end'] = i
                    conflicts.append(conflict)
                
            i += 1
        
        return conflicts
    
    def _apply_resolution_strategy(self, content: str, conflicts: List[Dict], file_ext: str) -> str:
        """Apply resolution strategy based on file type"""
        lines = content.split('\n')
        
        for conflict in reversed(conflicts):  # Reverse to maintain line numbers
            resolution = self._resolve_conflict(conflict, file_ext)
            
            if resolution is not None:
                # Replace conflict with resolution
                start = conflict['start']
                end = conflict['end']
                lines = lines[:start] + resolution + lines[end+1:]
            else:
                return None  # Can't resolve
        
        return '\n'.join(lines)
    
    def _resolve_conflict(self, conflict: Dict, file_ext: str) -> List[str]:
        """Resolve a single conflict"""
        ours = conflict['ours']
        theirs = conflict['theirs']
        
        # Strategy 1: If one side is empty, use the other
        if not ours:
            return theirs
        if not theirs:
            return ours
        
        # Strategy 2: If both sides are identical, use either
        if ours == theirs:
            return ours
        
        # Strategy 3: For ChoiceScript files, prefer structural changes
        if file_ext == '.txt':
            return self._resolve_choicescript_conflict(ours, theirs)
        
        # Strategy 4: For Python files, try to combine imports
        if file_ext == '.py':
            return self._resolve_python_conflict(ours, theirs)
        
        # Strategy 5: For YAML, prefer theirs (upstream)
        if file_ext in ['.yml', '.yaml']:
            return theirs
        
        # Strategy 6: For docs, combine both with separator
        if file_ext == '.md':
            return ours + ['', '---', ''] + theirs
        
        # Default: Can't auto-resolve
        return None
    
    def _resolve_choicescript_conflict(self, ours: List[str], theirs: List[str]) -> List[str]:
        """Resolve ChoiceScript-specific conflicts"""
        # If it's just whitespace differences, prefer ours
        ours_stripped = [line.strip() for line in ours if line.strip()]
        theirs_stripped = [line.strip() for line in theirs if line.strip()]
        
        if ours_stripped == theirs_stripped:
            return ours
        
        # If one has more content, prefer the longer version (more complete)
        if len(ours) > len(theirs) * 1.5:
            return ours
        if len(theirs) > len(ours) * 1.5:
            return theirs
        
        # Can't resolve
        return None
    
    def _resolve_python_conflict(self, ours: List[str], theirs: List[str]) -> List[str]:
        """Resolve Python-specific conflicts"""
        # Check if conflict is in imports
        ours_has_import = any(line.strip().startswith(('import ', 'from ')) for line in ours)
        theirs_has_import = any(line.strip().startswith(('import ', 'from ')) for line in theirs)
        
        if ours_has_import and theirs_has_import:
            # Combine imports and deduplicate
            combined = list(dict.fromkeys(ours + theirs))
            return sorted(combined)
        
        # Can't resolve
        return None
    
    def commit_resolutions(self) -> bool:
        """Commit resolved conflicts"""
        if not self.conflicts_resolved:
            return False
        
        try:
            commit_msg = f"🤖 Auto-resolve: Fixed {len(self.conflicts_resolved)} merge conflicts\n\n"
            commit_msg += "Resolved conflicts in:\n"
            commit_msg += '\n'.join(f"- {f}" for f in self.conflicts_resolved)
            
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
            print(f"✅ Committed conflict resolutions")
            return True
        
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to commit: {e}")
            if hasattr(e, 'stderr') and e.stderr:
                print(f"   Error details: {e.stderr}")
            return False

def main():
    """Main entry point"""
    resolver = ConflictResolver()
    
    print("🔍 Checking for merge conflicts...")
    success = resolver.resolve_conflicts()
    
    if success and resolver.conflicts_resolved:
        resolver.commit_resolutions()
        print("\n✅ All conflicts resolved")
        sys.exit(0)
    elif success:
        print("\n✅ No conflicts to resolve")
        sys.exit(0)
    else:
        print("\n❌ Some conflicts could not be auto-resolved")
        sys.exit(1)

if __name__ == "__main__":
    main()
