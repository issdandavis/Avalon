# Scripts Directory

This directory contains standalone utility scripts and automation tools for the Aethromoor project.

## 📁 Directory Purpose

The `scripts/` directory at the repository root contains general-purpose scripts and tools that are separate from the GitHub Actions automation scripts in `.github/scripts/`. These scripts can be run manually or integrated into external workflows.

## 🤖 AI PR Agent

### Overview

The **AI PR Agent** (`ai_pr_agent.py`) is an advanced AI-powered pull request review system that uses OpenAI's GPT models to provide intelligent code analysis and recommendations.

### Features

- 🧠 **AI-Powered Analysis**: Uses GPT-4 for deep code understanding
- 🎯 **Specialized Knowledge**: Trained on ChoiceScript, Python, GitHub Actions, and game development
- 🔍 **Comprehensive Reviews**: Analyzes code quality, security, performance, and best practices
- 📝 **Automated Comments**: Posts detailed review feedback directly to PRs
- 🎮 **Game Development Focus**: Special attention to narrative branching and ChoiceScript syntax

### Usage

#### Basic Usage

```bash
python scripts/ai_pr_agent.py \
  --repo issdandavis/Aethromoor \
  --pr 123 \
  --github-token $GITHUB_TOKEN \
  --openai-key $OPENAI_API_KEY
```

#### With Output File

```bash
python scripts/ai_pr_agent.py \
  --repo issdandavis/Aethromoor \
  --pr 123 \
  --output review-results.json
```

#### Using Environment Variables

```bash
# Set environment variables
export GITHUB_TOKEN="your-github-token"
export OPENAI_API_KEY="your-openai-key"

# Run without explicit tokens
python scripts/ai_pr_agent.py --repo issdandavis/Aethromoor --pr 123
```

### Requirements

Install required Python packages:

```bash
pip install openai requests
```

### Environment Variables

- `GITHUB_TOKEN`: GitHub personal access token with repo permissions
- `OPENAI_API_KEY`: OpenAI API key for GPT-4 access

### Integration with GitHub Actions

The AI PR Agent is automatically triggered via GitHub Actions workflow (`.github/workflows/ai-pr-agent.yml`) when pull requests are created or updated.

### Review Focus Areas

The AI agent specializes in:

1. **Code Quality**: Maintainability, readability, structure
2. **Security**: Vulnerability detection, best practices
3. **Performance**: Optimization opportunities
4. **ChoiceScript**: Syntax validation, narrative flow, branching logic
5. **Python**: Script quality, error handling, documentation
6. **GitHub Actions**: Workflow efficiency, security, best practices

### Output Format

The agent posts markdown-formatted reviews with:

- Overall code quality assessment
- Specific issues with file/line references
- Security concerns
- Improvement suggestions
- Positive aspects

### Example Review Output

```markdown
## 🤖 AI Code Review

### Overall Assessment: Good

### Specific Findings:

**File: choicescript_game/scenes/expedition.txt**
- Line 45: Consider adding error handling for undefined variables
- Line 67: Excellent use of conditional branching

**File: .github/scripts/helper.py**
- Security: Input validation recommended for user-provided data
- Performance: Consider caching this operation

### Suggestions:
1. Add unit tests for new functions
2. Update documentation for changed behavior

### Positive Aspects:
- Clean code structure
- Good variable naming
- Comprehensive error messages

---
*Reviewed by AI PR Agent using gpt-4-turbo-preview*
*Timestamp: 2025-12-08T02:37:00Z*
```

## 🔄 Relationship with .github/scripts

- **`.github/scripts/`**: GitHub Actions automation scripts (auto-reviewer, auto-fixer, etc.)
- **`scripts/`**: General-purpose tools that can be run independently

The AI PR Agent in `scripts/` complements the existing auto-review system by providing deeper AI analysis using advanced language models.

## 📚 Additional Scripts

As more standalone utilities are added to this directory, they will be documented here.

## 🆘 Troubleshooting

### "requests package not found"
```bash
pip install requests
```

### "openai package not found"
```bash
pip install openai
```

### "GitHub token not provided"
Set the `GITHUB_TOKEN` environment variable or use `--github-token` flag.

### "OpenAI API key not provided"
Set the `OPENAI_API_KEY` environment variable or use `--openai-key` flag.

## 📖 More Information

- See `.github/workflows/ai-pr-agent.yml` for automated workflow configuration
- See `docs/AUTO_MERGE_SYSTEM.md` for the complete PR automation system
- See `AI_SYSTEM_INDEX.md` for all AI agents and tools
