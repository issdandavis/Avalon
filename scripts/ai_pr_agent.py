#!/usr/bin/env python3
"""
AI PR Agent - Advanced AI-Powered Pull Request Review System
Uses OpenAI Agents SDK for intelligent code analysis and recommendations
"""

import os
import sys
import json
import argparse
import base64
from datetime import datetime
from typing import Dict, List, Optional

# Try importing required packages with helpful error messages
try:
    import requests
except ImportError:
    print("Error: 'requests' package not found.")
    print("Please install it with: pip install requests")
    sys.exit(1)

try:
    from openai import OpenAI
except ImportError:
    print("Error: 'openai' package not found.")
    print("Please install it with: pip install openai")
    sys.exit(1)

# Configuration constants
MAX_CONTENT_LENGTH_PER_FILE = int(os.getenv('AI_PR_MAX_CONTENT_PER_FILE', '1000'))
AI_TEMPERATURE = float(os.getenv('AI_PR_TEMPERATURE', '0.3'))
AI_MAX_TOKENS = int(os.getenv('AI_PR_MAX_TOKENS', '2000'))


class AICodeReviewer:
    """AI-powered code review agent using OpenAI"""
    
    def __init__(self, repo: str, pr_number: int, github_token: str, openai_api_key: str):
        self.repo = repo
        self.pr_number = pr_number
        self.github_token = github_token
        self.github_api_base = "https://api.github.com"
        self.client = OpenAI(api_key=openai_api_key)
        self.headers = {
            "Authorization": f"Bearer {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
    def get_pr_details(self) -> Dict:
        """Fetch PR details from GitHub API"""
        url = f"{self.github_api_base}/repos/{self.repo}/pulls/{self.pr_number}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_pr_files(self) -> List[Dict]:
        """Fetch changed files in the PR"""
        url = f"{self.github_api_base}/repos/{self.repo}/pulls/{self.pr_number}/files"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_file_content(self, filename: str, ref: str) -> Optional[str]:
        """Fetch file content from GitHub"""
        url = f"{self.github_api_base}/repos/{self.repo}/contents/{filename}?ref={ref}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        
        content = response.json().get('content', '')
        if content:
            return base64.b64decode(content).decode('utf-8')
        return None
    
    def analyze_code_with_ai(self, file_changes: List[Dict]) -> Dict:
        """Use OpenAI to analyze code changes"""
        
        # Prepare context for AI analysis
        analysis_context = []
        for file in file_changes:
            filename = file['filename']
            patch = file.get('patch', '')
            status = file['status']
            
            analysis_context.append({
                'filename': filename,
                'status': status,
                'changes': patch,
                'additions': file.get('additions', 0),
                'deletions': file.get('deletions', 0)
            })
        
        # Create AI analysis prompt
        prompt = self._create_analysis_prompt(analysis_context)
        
        try:
            # Use OpenAI's chat completion for code review
            response = self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert code reviewer specializing in:
                        - ChoiceScript game development
                        - Python automation scripts
                        - GitHub Actions workflows
                        - Game narrative and branching logic
                        - Security best practices
                        
                        Provide constructive, actionable feedback focusing on:
                        1. Code quality and maintainability
                        2. Potential bugs or edge cases
                        3. Security vulnerabilities
                        4. Performance improvements
                        5. Best practices and conventions
                        6. ChoiceScript syntax and structure (if applicable)
                        """
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=AI_TEMPERATURE,
                max_tokens=AI_MAX_TOKENS
            )
            
            ai_feedback = response.choices[0].message.content
            
            return {
                'success': True,
                'analysis': ai_feedback,
                'model_used': 'gpt-4-turbo-preview',
                'timestamp': datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }
    
    def _create_analysis_prompt(self, file_changes: List[Dict]) -> str:
        """Create a detailed prompt for AI analysis"""
        prompt = f"""Please review the following pull request changes:

PR Number: {self.pr_number}
Repository: {self.repo}

Files Changed ({len(file_changes)}):
"""
        
        for idx, file in enumerate(file_changes, 1):
            prompt += f"""
--- File {idx}: {file['filename']} ---
Status: {file['status']}
Additions: +{file['additions']} | Deletions: -{file['deletions']}

Changes:
{file['changes'][:MAX_CONTENT_LENGTH_PER_FILE]}
{'...(truncated)' if len(file['changes']) > MAX_CONTENT_LENGTH_PER_FILE else ''}

"""
        
        prompt += """
Please provide:
1. Overall assessment of code quality (Good/Needs Improvement/Critical Issues)
2. Specific issues found (if any), with file and line references
3. Security concerns (if any)
4. Suggestions for improvement
5. Positive aspects worth noting

Format your response in markdown with clear sections.
"""
        return prompt
    
    def post_review_comment(self, review_body: str, event: str = "COMMENT") -> bool:
        """Post review comment to PR"""
        url = f"{self.github_api_base}/repos/{self.repo}/pulls/{self.pr_number}/reviews"
        
        data = {
            "body": review_body,
            "event": event  # APPROVE, REQUEST_CHANGES, or COMMENT
        }
        
        response = requests.post(url, headers=self.headers, json=data)
        
        if response.status_code in [200, 201]:
            print(f"✅ Review posted successfully")
            return True
        else:
            print(f"❌ Failed to post review: {response.status_code}")
            print(response.text)
            return False
    
    def run_review(self) -> Dict:
        """Main review workflow"""
        print(f"🤖 AI PR Agent starting review of PR #{self.pr_number}")
        
        try:
            # Get PR details
            pr_details = self.get_pr_details()
            print(f"📝 PR: {pr_details['title']}")
            print(f"👤 Author: {pr_details['user']['login']}")
            
            # Get changed files
            files = self.get_pr_files()
            print(f"📁 Files changed: {len(files)}")
            
            if not files:
                print("⚠️  No files changed in this PR")
                return {'success': True, 'message': 'No files to review'}
            
            # Analyze with AI
            print("🧠 Running AI analysis...")
            analysis = self.analyze_code_with_ai(files)
            
            if not analysis['success']:
                print(f"❌ AI analysis failed: {analysis.get('error')}")
                return analysis
            
            # Format review comment
            review_comment = f"""## 🤖 AI Code Review

{analysis['analysis']}

---
*Reviewed by AI PR Agent using {analysis['model_used']}*  
*Timestamp: {analysis['timestamp']}*
"""
            
            # Post review
            self.post_review_comment(review_comment)
            
            print("✅ Review complete!")
            return {
                'success': True,
                'pr_number': self.pr_number,
                'files_reviewed': len(files),
                'analysis': analysis
            }
            
        except Exception as e:
            error_msg = f"Error during review: {str(e)}"
            print(f"❌ {error_msg}")
            return {'success': False, 'error': error_msg}


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='AI-powered PR review agent')
    parser.add_argument('--repo', required=True, help='Repository (owner/repo)')
    parser.add_argument('--pr', required=True, type=int, help='PR number')
    parser.add_argument('--github-token', help='GitHub token (or set GITHUB_TOKEN env var)')
    parser.add_argument('--openai-key', help='OpenAI API key (or set OPENAI_API_KEY env var)')
    parser.add_argument('--output', help='Output file for results (JSON)')
    
    args = parser.parse_args()
    
    # Get tokens from args or environment
    github_token = args.github_token or os.getenv('GITHUB_TOKEN')
    openai_key = args.openai_key or os.getenv('OPENAI_API_KEY')
    
    if not github_token:
        print("❌ Error: GitHub token not provided")
        print("Use --github-token or set GITHUB_TOKEN environment variable")
        sys.exit(1)
    
    if not openai_key:
        print("❌ Error: OpenAI API key not provided")
        print("Use --openai-key or set OPENAI_API_KEY environment variable")
        sys.exit(1)
    
    # Create reviewer and run
    reviewer = AICodeReviewer(
        repo=args.repo,
        pr_number=args.pr,
        github_token=github_token,
        openai_api_key=openai_key
    )
    
    result = reviewer.run_review()
    
    # Save results if output file specified
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"📄 Results saved to {args.output}")
    
    # Exit with appropriate code
    sys.exit(0 if result.get('success') else 1)


if __name__ == '__main__':
    main()
