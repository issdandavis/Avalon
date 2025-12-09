# Scripts Directory

This directory contains standalone utility scripts for repository automation and tooling.

## AI PR Review Agent

### Overview

The AI PR Review Agent (`ai_pr_agent.py`) provides automated code reviews for pull requests using OpenAI's GPT-4o-mini model. It fetches the PR diff, analyzes the changes, and posts a structured review comment.

### Features

- **Automatic Reviews**: Triggers on PR open, synchronize, and reopen events
- **Structured Feedback**: Provides consistent review format with:
  - Summary of changes
  - Issues found (with file locations and line numbers)
  - Risk assessment (Low/Medium/High)
- **Safe Truncation**: Large diffs (>100KB) are automatically truncated
- **Error Handling**: Graceful failure with detailed error logging

### Setup

#### 1. Add OpenAI API Key

The AI PR agent requires an OpenAI API key to be configured as a repository secret:

1. Go to your repository settings
2. Navigate to **Settings → Secrets and variables → Actions**
3. Click **New repository secret**
4. Name: `OPENAI_API_KEY`
5. Value: Your OpenAI API key (from https://platform.openai.com/api-keys)

#### 2. Workflow Configuration

The workflow is automatically configured in `.github/workflows/ai-pr-review.yml` and will:
- Run on every pull request (opened, synchronize, reopened)
- Install required dependencies (openai-agents, requests)
- Execute the review script with proper environment variables

### Usage

Once configured, the agent automatically:
1. Detects new PRs or updates to existing PRs
2. Fetches the unified diff from GitHub API
3. Sends the diff to OpenAI GPT-4o-mini for review
4. Posts a formatted comment on the PR

### Environment Variables

The script requires these environment variables (automatically provided by GitHub Actions):

- `GITHUB_REPOSITORY`: The repository in `owner/repo` format
- `PR_NUMBER`: The pull request number
- `GITHUB_TOKEN`: GitHub token for API access (automatically provided)
- `OPENAI_API_KEY`: OpenAI API key (must be configured as a secret)

### Manual Execution

To run the script manually (for testing):

```bash
export GITHUB_REPOSITORY="owner/repo"
export PR_NUMBER="123"
export GITHUB_TOKEN="ghp_..."
export OPENAI_API_KEY="sk-..."
python scripts/ai_pr_agent.py
```

### Troubleshooting

#### Missing OpenAI API Key

If you see an error about missing `OPENAI_API_KEY`, ensure you've added it as a repository secret (see Setup section).

#### API Rate Limits

- GitHub API: The workflow uses the standard `GITHUB_TOKEN` which has generous rate limits
- OpenAI API: Ensure your OpenAI account has sufficient credits and rate limits

#### Large Diffs

Diffs larger than 100KB are automatically truncated to prevent token limit issues. The truncation is noted in the review.

#### Failed to Post Comment

If the workflow runs but no comment appears:
1. Check that the workflow has `pull-requests: write` permission
2. Verify the `GITHUB_TOKEN` is working correctly
3. Check the workflow logs for detailed error messages

### Dependencies

- `openai-agents`: OpenAI Agents SDK for AI interactions
- `requests`: HTTP library for GitHub API calls

### Cost Considerations

Each PR review consumes OpenAI API credits. With GPT-4o-mini:
- Typical cost: $0.01-0.05 per review
- Configurable via model selection and token limits

To reduce costs:
- Limit reviews to specific branches
- Adjust `max_output_tokens` in the script
- Switch to a cheaper model if needed

## Contributing

When adding new scripts to this directory:
1. Include proper error handling
2. Add documentation to this README
3. Use environment variables for configuration
4. Follow existing code style patterns
