# Scripts Directory

This directory contains standalone utility scripts and automation tools for The Avalon Codex project.

## Available Scripts

### ai_pr_agent.py

**AI-Powered Pull Request Review Agent**

Automatically reviews pull requests using OpenAI's GPT-4 model to provide intelligent, context-aware code reviews.

#### Features
- 🤖 AI-generated code reviews using OpenAI GPT-4
- 📝 Analyzes changed files and diffs
- 🎮 Context-aware for ChoiceScript game development
- 🔒 Checks for security issues and best practices
- 💬 Posts review comments directly to PRs

#### Requirements
- Python 3.11+
- `openai` package (`pip install openai`)
- `requests` package (`pip install requests`)
- `OPENAI_API_KEY` environment variable or repository secret
- `GITHUB_TOKEN` for posting comments

#### Usage

**Command Line:**
```bash
export OPENAI_API_KEY="your-key-here"
export GITHUB_TOKEN="your-github-token"
export PR_NUMBER="123"

python scripts/ai_pr_agent.py
```

**Or with argument:**
```bash
python scripts/ai_pr_agent.py 123
```

**In GitHub Actions:**
```yaml
- name: Run AI PR Review
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    PR_NUMBER: ${{ github.event.pull_request.number }}
  run: python scripts/ai_pr_agent.py
```

#### Review Focus Areas
1. **Code Quality**: Syntax errors, best practices, organization
2. **ChoiceScript Conventions**: Proper game scripting syntax
3. **Narrative Consistency**: Character voices and lore accuracy
4. **Game Mechanics**: Stat tracking and player choices
5. **Security**: Sensitive data and error handling

#### Configuration

The script uses GPT-4 by default. To use GPT-3.5-turbo (faster/cheaper), modify line 187 in `ai_pr_agent.py`:
```python
model="gpt-3.5-turbo",  # Changed from gpt-4
```

#### Integration with Auto-Review System

This AI PR agent complements the existing auto-review-fix-merge system:
- **Auto-Review**: Basic syntax and structure validation
- **AI PR Agent**: Deep semantic and contextual review
- **Auto-Fixer**: Automated fixes for common issues
- **Auto-Merger**: Risk-based automatic merging

Use both for comprehensive PR review coverage.

## Directory Structure

```
scripts/
├── README.md           # This file
└── ai_pr_agent.py     # OpenAI-powered PR review agent
```

## vs .github/scripts/

- **`scripts/`**: Standalone utility scripts (this directory)
- **`.github/scripts/`**: GitHub Actions workflow-specific scripts

Both directories serve automation purposes but are organized separately for clarity.

## Adding New Scripts

When adding new scripts to this directory:

1. Make them executable: `chmod +x scripts/your_script.py`
2. Add proper error handling for missing dependencies
3. Include usage documentation in this README
4. Follow the existing code style and patterns
5. Test locally before committing

## Support

For issues or questions:
- Check existing documentation in `/docs`
- Review workflow files in `.github/workflows/`
- See `AGENT_QUICK_REFERENCE.md` for AI system overview
