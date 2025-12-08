#!/usr/bin/env python3
"""
AI PR Agent - OpenAI-Powered GitHub PR Review System
Fetches PR diffs and posts automated code reviews using OpenAI agents SDK
"""

import os
import sys

# Try to import required packages with helpful error messages
try:
    import requests
except ImportError:
    print("❌ Error: requests package not installed")
    print("Install with: pip install requests")
    sys.exit(1)

try:
    from agents import Agent, Runner, ModelSettings
except ImportError:
    print("❌ Error: openai-agents SDK not installed")
    print("Install with: pip install openai-agents")
    sys.exit(1)

GITHUB_API = "https://api.github.com"

def get_pr_diff(owner: str, repo: str, pr_number: int, token: str) -> str:
    """
    Fetch the diff for a specific pull request from GitHub API
    
    Args:
        owner: Repository owner (username or organization)
        repo: Repository name
        pr_number: Pull request number
        token: GitHub authentication token
        
    Returns:
        Raw diff text of the pull request
    """
    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3.diff"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.text  # raw diff

def post_pr_comment(owner: str, repo: str, pr_number: int, token: str, body: str):
    """
    Post a comment on a GitHub pull request
    
    Args:
        owner: Repository owner (username or organization)
        repo: Repository name
        pr_number: Pull request number
        token: GitHub authentication token
        body: Comment body text (supports Markdown)
    """
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    data = {"body": body}
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()

def main():
    """
    Main entry point for the AI PR agent
    
    Expects environment variables:
        GITHUB_REPOSITORY_OWNER: Repository owner
        GITHUB_REPOSITORY: Full repository name (owner/repo)
        PR_NUMBER: Pull request number
        GITHUB_TOKEN: GitHub authentication token
        OPENAI_API_KEY: OpenAI API key for agent
    """
    # Get configuration from environment
    owner = os.environ.get("GITHUB_REPOSITORY_OWNER")
    repo_full = os.environ.get("GITHUB_REPOSITORY")
    pr_number_str = os.environ.get("PR_NUMBER")
    gh_token = os.environ.get("GITHUB_TOKEN")
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    
    # Validate required environment variables
    if not owner:
        print("❌ Error: GITHUB_REPOSITORY_OWNER environment variable not set")
        sys.exit(1)
    if not repo_full:
        print("❌ Error: GITHUB_REPOSITORY environment variable not set")
        sys.exit(1)
    if not pr_number_str:
        print("❌ Error: PR_NUMBER environment variable not set")
        sys.exit(1)
    if not gh_token:
        print("❌ Error: GITHUB_TOKEN environment variable not set")
        sys.exit(1)
    if not openai_api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)
    
    # Parse repository name
    repo_parts = repo_full.split("/")
    if len(repo_parts) != 2:
        print(f"❌ Error: Invalid repository format '{repo_full}'. Expected 'owner/repo'")
        sys.exit(1)
    repo = repo_parts[1]
    
    try:
        pr_number = int(pr_number_str)
    except ValueError:
        print(f"❌ Error: Invalid PR number '{pr_number_str}'. Must be an integer")
        sys.exit(1)
    
    print(f"🔍 Fetching PR #{pr_number} diff from {owner}/{repo}...")
    
    # Fetch the PR diff
    try:
        diff = get_pr_diff(owner, repo, pr_number, gh_token)
    except requests.HTTPError as e:
        print(f"❌ Error fetching PR diff: {e}")
        sys.exit(1)
    
    print(f"📝 Diff size: {len(diff)} characters")
    
    # Define the code review agent
    review_agent = Agent(
        name="github_pr_reviewer",
        instructions=(
            "You are a senior code reviewer. "
            "Given a Git diff, you must:\n"
            "1) Briefly summarize the change.\n"
            "2) List concrete issues with code blocks.\n"
            "3) Rate overall risk as Low/Medium/High.\n"
            "Only comment on the diff shown."
        ),
        model="gpt-4.1-mini",   # or another model you like
        model_settings=ModelSettings(max_output_tokens=1200),
    )

    print("🤖 Running AI code review...")
    
    # Initialize the runner
    runner = Runner(api_key=openai_api_key)

    # Run the review
    result = runner.run_sync(
        starting_agent=review_agent,
        input=(
            "Here is the PR diff. Perform a review.\n\n"
            f"```diff\n{diff}\n```"
        ),
    )

    # Extract the review text from results
    # The openai-agents SDK Result object may use different property names
    # Try common variants to ensure compatibility
    if hasattr(result, 'final_output_text'):
        review_text = result.final_output_text
    elif hasattr(result, 'output'):
        review_text = result.output
    elif hasattr(result, 'text'):
        review_text = result.text
    else:
        print("⚠️  Warning: Unable to extract review text from result object")
        review_text = str(result)

    # Format as a nice GitHub comment
    markdown_body = f"""## 🤖 AI Code Review

{review_text}

---

_This review was generated by an OpenAI-powered GitHub agent._
"""

    print("💬 Posting review comment to PR...")
    
    # Post the comment
    try:
        post_pr_comment(owner, repo, pr_number, gh_token, markdown_body)
        print("✅ Review posted successfully!")
    except requests.HTTPError as e:
        print(f"❌ Error posting comment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
