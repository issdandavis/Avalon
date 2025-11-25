#!/usr/bin/env python3
"""
ChoiceScript Syntax Validator
Checks for common syntax errors before committing
"""

import re
import sys
from pathlib import Path

def validate_choicescript_file(file_path):
    """Validate a single ChoiceScript file"""
    errors = []
    warnings = []
    
    try:
        content = Path(file_path).read_text()
    except Exception as e:
        return [f"ERROR: Cannot read file: {e}"], []
    
    lines = content.split('\n')
    
    # Track labels for goto validation
    labels = set()
    gotos = []
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Skip comments and blank lines
        if not stripped or stripped.startswith('*comment'):
            continue
        
        # Check for common syntax errors
        
        # 1. Unclosed quotes
        if stripped.startswith('*') and '"' in stripped:
            quotes = stripped.count('"')
            if quotes % 2 != 0:
                errors.append(f"Line {i}: Unclosed quote: {line[:50]}")
        
        # 2. Label syntax (no spaces)
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
            # Should be *set variable value or *set variable +value
            parts = stripped.split(None, 2)
            if len(parts) < 3:
                errors.append(f"Line {i}: Invalid *set syntax: {stripped}")
        
        # 5. Choice indentation
        if stripped.startswith('#'):
            # Should be indented under *choice
            if i > 1 and '*choice' not in lines[i-2]:
                # Look back a few lines for *choice
                found_choice = False
                for j in range(max(0, i-5), i):
                    if '*choice' in lines[j]:
                        found_choice = True
                        break
                if not found_choice:
                    warnings.append(f"Line {i}: Choice option outside *choice block")
        
        # 6. Unmatched *if/*else
        if stripped.startswith('*else') or stripped.startswith('*elseif'):
            # Should have *if before it
            found_if = False
            for j in range(max(0, i-10), i):
                if lines[j].strip().startswith('*if '):
                    found_if = True
                    break
            if not found_if:
                warnings.append(f"Line {i}: *else without matching *if")
    
    # Validate gotos reference existing labels
    for goto_target, line_num in gotos:
        if goto_target not in labels and '_' in goto_target:  # Allow scene references
            # This might be a scene reference, not an error
            pass
        elif goto_target not in labels:
            warnings.append(f"Line {line_num}: *goto {goto_target} references undefined label")
    
    return errors, warnings

def main():
    """Validate all provided files"""
    if len(sys.argv) < 2:
        print("Usage: validate_choicescript.py <file1.txt> [file2.txt ...]")
        sys.exit(1)
    
    total_errors = 0
    total_warnings = 0
    
    for file_path in sys.argv[1:]:
        if not Path(file_path).exists():
            print(f"⚠️ File not found: {file_path}")
            continue
        
        errors, warnings = validate_choicescript_file(file_path)
        
        if errors:
            print(f"\n❌ {Path(file_path).name}: {len(errors)} errors")
            for error in errors:
                print(f"  {error}")
            total_errors += len(errors)
        
        if warnings:
            print(f"\n⚠️ {Path(file_path).name}: {len(warnings)} warnings")
            for warning in warnings:
                print(f"  {warning}")
            total_warnings += len(warnings)
        
        if not errors and not warnings:
            print(f"✅ {Path(file_path).name}: Valid")
    
    print(f"\n{'='*60}")
    print(f"Total: {total_errors} errors, {total_warnings} warnings")
    
    if total_errors > 0:
        print("❌ Validation failed - fix errors before committing")
        sys.exit(1)
    else:
        print("✅ All files passed validation")
        sys.exit(0)

if __name__ == "__main__":
    main()
