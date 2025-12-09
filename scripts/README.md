# Scripts Directory

This directory contains standalone utility scripts for the Aethromoor project.

## AI PR Agent (`ai_pr_agent.py`)

Automated AI-powered code review bot that analyzes pull requests and provides structured feedback using OpenAI's GPT-4o-mini model.

### Features

- **Automatic PR Analysis**: Fetches PR diff and analyzes code changes
- **Structured Reviews**: Provides consistent review format with:
  - Summary of changes
  - Issues found with specific file locations and line numbers
  - Risk assessment (Low/Medium/High)
- **Smart Diff Handling**: Automatically truncates large diffs (>100KB) to stay within API limits
- **Error Handling**: Gracefully handles GitHub API and OpenAI API failures

### Setup

#### 1. Add OpenAI API Key Secret

Go to your repository settings:

1. Navigate to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `OPENAI_API_KEY`
4. Value: Your OpenAI API key
5. Click **Add secret**

#### 2. Workflow Configuration

The workflow (`.github/workflows/ai-pr-review.yml`) is triggered automatically on:
- Pull request opened
- Pull request synchronized (new commits pushed)
- Pull request reopened

### Environment Variables

The script requires these environment variables (automatically set by GitHub Actions):

- `GITHUB_REPOSITORY`: Repository in format `owner/repo`
- `PR_NUMBER`: Pull request number
- `GITHUB_TOKEN`: GitHub token for API authentication
- `OPENAI_API_KEY`: OpenAI API key (must be added as a repository secret)

### Usage

The script runs automatically via GitHub Actions. You can also run it manually:

```bash
export GITHUB_REPOSITORY="owner/repo"
export PR_NUMBER="123"
export GITHUB_TOKEN="ghp_..."
export OPENAI_API_KEY="sk-..."

python scripts/ai_pr_agent.py
```

### Review Output Format

The AI reviewer posts a comment on each PR with:

```markdown
## AI Code Review (gpt-4o-mini)

**Summary**
Brief description of what the PR does

**Issues Found**
File: path/to/file.ext (lines X-Y)
\```
code snippet
\```
→ Explanation and suggested fix

**Risk Assessment**
Level: Low/Medium/High
Reason: Brief justification

---
Generated automatically by ai_pr_agent.py
```

### Customization

To customize the review behavior, edit these parameters in `ai_pr_agent.py`:

- **Model**: Change `model="gpt-4o-mini"` to use a different OpenAI model
- **Temperature**: Adjust `temperature=0.2` for more/less creative responses
- **Max Tokens**: Change `max_output_tokens=1500` to allow longer/shorter reviews
- **Diff Size Limit**: Modify the 100,000 character limit in `get_pr_diff()`

### Troubleshooting

**Missing OPENAI_API_KEY**
- Ensure the secret is added in repository settings
- Check the workflow run logs for the exact error

**API Rate Limits**
- GitHub API: Limited to 1000 requests/hour for authenticated requests
- OpenAI API: Depends on your account tier and model

**Large Diffs**
- Diffs over 100KB are automatically truncated
- Consider breaking large PRs into smaller ones for better reviews

### Dependencies

- `requests`: HTTP library for GitHub API calls
- `openai-agents`: OpenAI's agent SDK for structured AI interactions

Install with:
```bash
pip install openai-agents requests
```
