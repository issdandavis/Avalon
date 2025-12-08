# Scripts Directory

This directory contains utility scripts for repository automation and AI-powered workflows.

## AI PR Agent

### `ai_pr_agent.py`

An OpenAI-powered GitHub PR review agent that automatically fetches pull request diffs and posts AI-generated code reviews.

#### Features

- Fetches PR diffs using GitHub API
- Uses OpenAI agents SDK for intelligent code review
- Posts formatted review comments to PRs
- Provides summary, concrete issues, and risk assessment

#### Requirements

```bash
pip install requests openai-agents
```

#### Environment Variables

The script requires the following environment variables:

- `GITHUB_REPOSITORY_OWNER` - Repository owner (username or organization)
- `GITHUB_REPOSITORY` - Full repository name (owner/repo)
- `PR_NUMBER` - Pull request number to review
- `GITHUB_TOKEN` - GitHub authentication token
- `OPENAI_API_KEY` - OpenAI API key for the agent

#### Usage

```bash
export GITHUB_REPOSITORY_OWNER="issdandavis"
export GITHUB_REPOSITORY="issdandavis/Aethromoor"
export PR_NUMBER="123"
export GITHUB_TOKEN="ghp_..."
export OPENAI_API_KEY="sk-..."

python3 scripts/ai_pr_agent.py
```

#### Integration with GitHub Actions

This script can be integrated into GitHub Actions workflows:

```yaml
name: AI PR Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install requests openai-agents
      
      - name: Run AI Review
        env:
          GITHUB_REPOSITORY_OWNER: ${{ github.repository_owner }}
          GITHUB_REPOSITORY: ${{ github.repository }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python3 scripts/ai_pr_agent.py
```

#### Review Output

The agent generates a structured review with:

1. **Summary** - Brief overview of changes
2. **Issues** - Concrete problems with code examples
3. **Risk Rating** - Low/Medium/High assessment

All reviews are posted as PR comments with clear formatting and attribution.
