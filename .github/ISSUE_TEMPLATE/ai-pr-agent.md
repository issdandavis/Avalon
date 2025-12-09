---
name: AI-Powered PR Review Agent
about: Set up automated AI code reviews using OpenAI and GitHub Actions
title: 'Set up AI-powered PR review agent (GitHub Actions + OpenAI)'
labels: automation, enhancement
assignees: ''
---

## Summary

Add an automated AI PR reviewer that comments on every pull request using OpenAI and the `openai-agents` SDK. The bot fetches the diff, generates a structured review, and posts it as a PR comment.

## Motivation

- Faster, more consistent reviews
- Early feedback on style, safety, and potential bugs  
- Lightweight to maintain (one script + one workflow)

## Acceptance Criteria

- [ ] Workflow runs on every `pull_request` event (opened, synchronize, reopened)
- [ ] AI bot posts a single comment on the PR with:
  - [ ] **Summary** section
  - [ ] **Issues Found** section (with file locations and code snippets)
  - [ ] **Risk Assessment** section (Low/Medium/High with justification)
- [ ] Large diffs (>100KB) are safely truncated
- [ ] Errors (GitHub API / OpenAI) are logged in workflow logs instead of failing silently
- [ ] `OPENAI_API_KEY` is configured as a repository secret

## Implementation Checklist

- [ ] Create `scripts/ai_pr_agent.py`
- [ ] Create `.github/workflows/ai-pr-review.yml`
- [ ] Add `OPENAI_API_KEY` in repository secrets
- [ ] Test on a sample PR
- [ ] Document setup in `scripts/README.md`

## Setup Instructions

### 1. Add Python Script

Create `scripts/ai_pr_agent.py` with the AI review logic.

### 2. Add GitHub Workflow

Create `.github/workflows/ai-pr-review.yml` to trigger on PR events.

### 3. Configure Secrets

1. Go to **Settings → Secrets and variables → Actions**
2. Click **New repository secret**
3. Name: `OPENAI_API_KEY`
4. Value: Your OpenAI API key from https://platform.openai.com/api-keys

### 4. Test

Open a test PR to verify the agent posts a review comment.

## Notes

- Uses GPT-4o-mini model (~$0.01-0.05 per review)
- Automatically truncates large diffs to prevent token limit issues
- Requires OpenAI API access with sufficient credits

## Resources

- [OpenAI Agents SDK](https://github.com/openai/agents)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [OpenAI API Keys](https://platform.openai.com/api-keys)
