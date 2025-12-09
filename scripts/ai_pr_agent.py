import os
import sys
from pathlib import Path

import requests
from agents import Agent, Runner, ModelSettings  # openai-agents SDK

GITHUB_API = "https://api.github.com"


def get_pr_diff(owner: str, repo: str, pr_number: int, token: str) -> str:
    """
    Get the PR diff in unified diff format.
    Uses the correct media type: application/vnd.github.v3.diff
    """
    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.diff",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    diff = resp.text

    if len(diff) > 100_000:
        diff = diff[:100_000] + "\n\n... (diff truncated for review) ...\n"
    return diff


def post_pr_comment(owner: str, repo: str, pr_number: int, token: str, body: str) -> None:
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = {"body": body}
    resp = requests.post(url, headers=headers, json=data, timeout=30)
    resp.raise_for_status()


def build_review_prompt(diff: str) -> str:
    return f"""
You are a senior software engineer performing a thorough code review.

Here is the pull request diff:

```diff
{diff}
```

Please provide a concise but actionable review with exactly this structure (no extra headings):

Summary

<1-3 sentence summary of what the PR does>

Issues Found

File: path/to/file.ext (lines X-Y)

```
problematic code block
```

→ Explanation and suggested fix.


(Repeat as needed. If no issues, write "None found – the change looks solid.")

Risk Assessment

Level: Low / Medium / High

Reason: Brief justification


Only comment on the code shown in the diff.
"""


def main():
    required_env = ["GITHUB_REPOSITORY", "PR_NUMBER", "GITHUB_TOKEN", "OPENAI_API_KEY"]
    missing = [var for var in required_env if not os.getenv(var)]
    if missing:
        print(f"Missing environment variables: {', '.join(missing)}")
        sys.exit(1)

    owner, repo = os.environ["GITHUB_REPOSITORY"].split("/")
    pr_number = int(os.environ["PR_NUMBER"])
    gh_token = os.environ["GITHUB_TOKEN"]
    openai_key = os.environ["OPENAI_API_KEY"]

    print(f"Reviewing PR #{pr_number} in {owner}/{repo}")

    try:
        diff = get_pr_diff(owner, repo, pr_number, gh_token)
    except requests.HTTPError as e:
        print(f"Failed to fetch diff: {e.response.status_code} {e.response.text}")
        sys.exit(1)

    review_agent = Agent(
        name="PR_Reviewer",
        instructions="You are an expert code reviewer. Always follow the exact response template given in the user message.",
        model="gpt-4o-mini",
        model_settings=ModelSettings(
            temperature=0.2,
            max_output_tokens=1500,
        ),
    )

    runner = Runner(api_key=openai_key)

    try:
        result = runner.run_sync(
            starting_agent=review_agent,
            input=build_review_prompt(diff),
        )
        review_text = result.final_output_text.strip()
    except Exception as e:
        review_text = f"AI review failed: {str(e)}"
        print(review_text)

    markdown_body = f"""## AI Code Review (gpt-4o-mini)

{review_text}

---

*Generated automatically by ai_pr_agent.py • {Path(__file__).name}*
"""

    try:
        post_pr_comment(owner, repo, pr_number, gh_token, markdown_body)
        print("Review comment posted successfully!")
    except requests.HTTPError as e:
        print(f"Failed to post comment: {e.response.status_code} {e.response.text}")


if __name__ == "__main__":
    main()
