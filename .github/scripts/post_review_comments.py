#!/usr/bin/env python3
"""
Post Review Comments
Posts automated review comments to PRs
"""

import argparse
import json
import sys
import subprocess
from pathlib import Path
from typing import List, Dict

def run_command(cmd: List[str]) -> tuple:
    """Run shell command and return exit code, stdout, stderr"""
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def post_pr_comment(pr_number: int, repo: str, body: str) -> bool:
    """Post a comment to a PR"""
    exit_code, stdout, stderr = run_command([
        'gh', 'pr', 'comment', str(pr_number),
        '--repo', repo,
        '--body', body
    ])
    
    return exit_code == 0

def main():
    parser = argparse.ArgumentParser(description='Post review comments to PR')
    parser.add_argument('--pr-number', type=int, required=True, help='PR number')
    parser.add_argument('--repo', required=True, help='Repository (owner/repo)')
    parser.add_argument('--comments-file', required=True, help='Path to comments JSON file')
    args = parser.parse_args()
    
    # Load comments
    try:
        comments = json.loads(Path(args.comments_file).read_text())
    except Exception as e:
        print(f"Error loading comments file: {e}")
        return 1
    
    if not comments:
        print("No comments to post")
        return 0
    
    # Post general comments (those without specific file/line references)
    for comment in comments:
        if comment.get('path') is None:
            body = comment.get('body', '')
            if body:
                if post_pr_comment(args.pr_number, args.repo, body):
                    print(f"✅ Posted comment to PR #{args.pr_number}")
                else:
                    print(f"❌ Failed to post comment to PR #{args.pr_number}")
    
    print(f"Posted {len(comments)} comment(s) to PR #{args.pr_number}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
