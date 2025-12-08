#!/usr/bin/env python3
"""
AI PR Agent - OpenAI-Powered Pull Request Review
Automatically reviews pull requests using OpenAI's GPT models
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

# Try importing openai with graceful degradation
try:
    import openai
except ImportError:
    print("❌ Error: openai package not installed")
    print("Install with: pip install openai")
    sys.exit(1)

# Try importing requests for GitHub API
try:
    import requests
except ImportError:
    print("❌ Error: requests package not installed")
    print("Install with: pip install requests")
    sys.exit(1)


class AIPRAgent:
    """OpenAI-powered PR review agent"""
    
    def __init__(self, pr_number: str, github_token: str, openai_api_key: str):
        self.pr_number = pr_number
        self.github_token = github_token
        self.repo_root = Path.cwd()
        
        # Initialize OpenAI client
        openai.api_key = openai_api_key
        self.client = openai
        
        # GitHub API setup
        self.github_api = "https://api.github.com"
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "")
        self.headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
    def review_pr(self) -> Dict:
        """Main review logic using OpenAI"""
        print(f"🤖 AI PR Agent reviewing PR #{self.pr_number}...")
        
        # Get PR details from GitHub
        pr_info = self._get_pr_info()
        if not pr_info:
            return {"error": "Could not fetch PR information"}
        
        # Get changed files and diff
        changed_files = self._get_changed_files()
        diff_content = self._get_pr_diff()
        
        print(f"📝 Analyzing {len(changed_files)} changed files")
        
        # Generate AI review
        review_comment = self._generate_ai_review(pr_info, changed_files, diff_content)
        
        # Post review comment
        self._post_review_comment(review_comment)
        
        return {
            "success": True,
            "files_reviewed": len(changed_files),
            "comment_posted": True
        }
    
    def _get_pr_info(self) -> Optional[Dict]:
        """Fetch PR information from GitHub API"""
        try:
            url = f"{self.github_api}/repos/{self.repo_name}/pulls/{self.pr_number}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"⚠️ Error fetching PR info: {e}")
            return None
    
    def _get_changed_files(self) -> List[str]:
        """Get list of changed files in PR"""
        try:
            result = subprocess.run(
                ['git', 'diff', '--name-only', 'origin/main...HEAD'],
                capture_output=True,
                text=True,
                check=True
            )
            files = [f.strip() for f in result.stdout.split('\n') if f.strip()]
            return files
        except subprocess.CalledProcessError:
            # Fallback method
            try:
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
    
    def _get_pr_diff(self) -> str:
        """Get the full diff for the PR"""
        try:
            result = subprocess.run(
                ['git', 'diff', 'origin/main...HEAD'],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError:
            # Fallback
            try:
                result = subprocess.run(
                    ['git', 'diff', 'HEAD^', 'HEAD'],
                    capture_output=True,
                    text=True,
                    check=True
                )
                return result.stdout
            except subprocess.CalledProcessError:
                return ""
    
    def _generate_ai_review(self, pr_info: Dict, changed_files: List[str], diff_content: str) -> str:
        """Use OpenAI to generate a code review"""
        
        # Prepare context for OpenAI
        pr_title = pr_info.get('title', 'Untitled PR')
        pr_description = pr_info.get('body', 'No description provided')
        
        # Truncate diff if too long (OpenAI has token limits)
        max_diff_length = 8000
        if len(diff_content) > max_diff_length:
            diff_content = diff_content[:max_diff_length] + "\n\n... (diff truncated for length)"
        
        # Create the review prompt
        system_prompt = """You are an expert code reviewer for The Avalon Codex project - a fantasy narrative game built with ChoiceScript.

Your review should consider:
1. **Code Quality**: Syntax errors, best practices, code organization
2. **ChoiceScript Conventions**: Proper use of *label, *goto, *choice, *set commands
3. **Narrative Consistency**: Character voices, lore accuracy, stat tracking
4. **Game Mechanics**: Proper stat modifications (Collaboration, relationships)
5. **Security**: No sensitive data, proper error handling

Be constructive, specific, and helpful. Focus on meaningful issues, not nitpicks.
Format your response in markdown with clear sections."""

        user_prompt = f"""Please review this pull request:

**PR Title**: {pr_title}

**Description**: {pr_description}

**Changed Files** ({len(changed_files)}):
{chr(10).join(f'- {f}' for f in changed_files[:20])}

**Diff**:
```diff
{diff_content}
```

Provide a thorough but concise review."""

        try:
            # Use OpenAI Chat API
            response = self.client.chat.completions.create(
                model="gpt-4",  # or gpt-3.5-turbo for faster/cheaper reviews
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,  # Lower temperature for more consistent reviews
                max_tokens=1500
            )
            
            review_text = response.choices[0].message.content
            
            # Add metadata footer
            footer = f"\n\n---\n🤖 *AI-generated review using OpenAI GPT-4*\n📊 Files reviewed: {len(changed_files)}"
            
            return review_text + footer
            
        except Exception as e:
            error_msg = f"⚠️ AI review generation failed: {str(e)}"
            print(error_msg)
            return f"## AI Review Error\n\n{error_msg}\n\nPlease review manually."
    
    def _post_review_comment(self, comment: str) -> bool:
        """Post the review as a PR comment"""
        try:
            url = f"{self.github_api}/repos/{self.repo_name}/issues/{self.pr_number}/comments"
            data = {"body": comment}
            
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            
            print("✅ Review comment posted successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error posting comment: {e}")
            return False


def main():
    """Main entry point"""
    
    # Get required environment variables
    pr_number = os.environ.get("PR_NUMBER") or sys.argv[1] if len(sys.argv) > 1 else None
    github_token = os.environ.get("GITHUB_TOKEN")
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    
    if not pr_number:
        print("❌ Error: PR_NUMBER not provided")
        print("Usage: python ai_pr_agent.py <PR_NUMBER>")
        print("   or: PR_NUMBER=123 python ai_pr_agent.py")
        sys.exit(1)
    
    if not github_token:
        print("❌ Error: GITHUB_TOKEN environment variable not set")
        sys.exit(1)
    
    if not openai_api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please configure the OPENAI_API_KEY secret in your repository")
        sys.exit(1)
    
    # Run the review
    agent = AIPRAgent(pr_number, github_token, openai_api_key)
    result = agent.review_pr()
    
    if result.get("success"):
        print("✨ PR review completed successfully!")
        sys.exit(0)
    else:
        print("⚠️ PR review completed with warnings")
        sys.exit(0)  # Don't fail the workflow


if __name__ == "__main__":
    main()
