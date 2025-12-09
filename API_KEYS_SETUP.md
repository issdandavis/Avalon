# 🔑 API Keys Setup Guide

## Where to Add Your ChatGPT/OpenAI API Key

This guide explains **exactly where** to add your OpenAI (ChatGPT) API key and other AI service keys for this project.

---

## 🎯 Quick Answer

**For Local Development:**
1. Copy `config/.env.example` to `config/.env`
2. Add your OpenAI API key to the `OPENAI_API_KEY=` line
3. Save the file
4. You're done!

**For GitHub Actions (Automated Workflows):**
1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `OPENAI_API_KEY`
5. Value: Your API key (starting with `sk-...`)
6. Click **Add secret**

---

## 📝 Detailed Instructions

### Option 1: Local Development (Running Scripts on Your Computer)

#### Step 1: Create Your `.env` File

```bash
# From the repository root directory
cp config/.env.example config/.env
```

Or manually:
1. Navigate to the `config/` folder
2. Copy the file `.env.example`
3. Rename the copy to `.env`

#### Step 2: Get Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Log in to your OpenAI account
3. Click **"Create new secret key"**
4. Copy the key (it starts with `sk-proj-` or `sk-`)
5. **Save it somewhere safe** - you won't be able to see it again!

#### Step 3: Add Your API Key to `.env`

Open `config/.env` in a text editor and add your key:

```bash
# AI Service API Keys
OPENAI_API_KEY=sk-proj-YOUR_KEY_HERE
ANTHROPIC_API_KEY=sk-ant-YOUR_KEY_HERE

# Optional: External integrations
# DISCORD_WEBHOOK=https://discord.com/api/webhooks/...
# GOOGLE_API_KEY=your_key_here
# ZAPIER_WEBHOOK=https://hooks.zapier.com/...
```

**Replace `sk-proj-YOUR_KEY_HERE` with your actual API key!**

#### Step 4: Verify It Works

Test that your API key is set up correctly:

```bash
# Check the file exists
ls -la config/.env

# Test a script that uses the API (if available)
python .github/scripts/ai_autonomous_worker.py
```

---

### Option 2: GitHub Actions (Automated Workflows)

For the AI automation workflows to run, you need to add API keys as **GitHub Secrets**.

#### Step 1: Go to Repository Settings

1. Go to your repository: https://github.com/issdandavis/Aethromoor
2. Click the **Settings** tab (requires admin access)
3. In the left sidebar, click **Secrets and variables** → **Actions**

#### Step 2: Add OpenAI API Key

1. Click **New repository secret**
2. Fill in:
   - **Name:** `OPENAI_API_KEY`
   - **Secret:** Your OpenAI API key (e.g., `sk-proj-abc123...`)
3. Click **Add secret**

#### Step 3: Add Anthropic API Key (Optional)

If you're using Claude AI features:

1. Click **New repository secret** again
2. Fill in:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Secret:** Your Anthropic API key (starts with `sk-ant-`)
3. Click **Add secret**

#### Step 4: Verify in Workflows

Your workflows will now have access to these keys. Check a workflow run:

1. Go to **Actions** tab
2. Click on a recent workflow run
3. Check the logs - you should see successful API authentication

---

## 🔒 Security Best Practices

### ✅ DO:
- ✅ Keep API keys in `config/.env` for local development
- ✅ Add API keys to GitHub Secrets for automated workflows
- ✅ Add `config/.env` to `.gitignore` (already done)
- ✅ Rotate your keys if they're ever exposed
- ✅ Use read-only or rate-limited keys when possible

### ❌ DON'T:
- ❌ **NEVER** commit API keys to git
- ❌ **NEVER** share API keys in issues or pull requests
- ❌ **NEVER** post API keys in screenshots
- ❌ **NEVER** store keys in regular code files

---

## ⚠️ IMPORTANT: Exposed Key Warning

**If you previously stored API keys in the repository:**

There is an exposed OpenAI API key in `archive/Open Ai and Claudie.txt`. This key should be:

1. **Immediately rotated** (deleted and replaced) at https://platform.openai.com/api-keys
2. **Never used again**
3. **Removed from the archive** or the archive excluded from git

To check for exposed keys:

```bash
# Search for potential API keys in tracked files
git log --all --full-history -- "*" | grep -i "sk-"
```

If you find any, follow these steps:
1. Immediately rotate all exposed keys
2. Remove them from git history (use `git filter-repo` or BFG Repo-Cleaner)
3. Add the new keys only to `.env` or GitHub Secrets

---

## 🛠️ Which Scripts Use API Keys?

### OpenAI API Key (`OPENAI_API_KEY`)
- `.github/scripts/ai_pr_agent.py` - AI code review
- Any future OpenAI-powered features

### Anthropic API Key (`ANTHROPIC_API_KEY`)
- `.github/scripts/ai_autonomous_worker.py` - Autonomous development
- `.github/scripts/scene_writer_agent.py` - Scene writing
- `.github/scripts/content_polisher.py` - Content enhancement
- Other Claude AI-powered scripts

### Optional Keys
- `DISCORD_WEBHOOK` - For Discord notifications
- `GOOGLE_API_KEY` - For Google Workspace integration
- `ZAPIER_WEBHOOK` - For Zapier automations

---

## 🧪 Testing Your Setup

### Test Local Environment

```bash
# Test that environment variables load
cd /path/to/Aethromoor
python3 << 'EOF'
import os
from pathlib import Path

# Try to load .env
env_file = Path("config/.env")
if env_file.exists():
    print("✅ .env file exists")
    with open(env_file) as f:
        content = f.read()
        if "OPENAI_API_KEY=" in content:
            print("✅ OPENAI_API_KEY found in .env")
        if "sk-" in content:
            print("✅ API key value appears to be set")
else:
    print("❌ .env file not found")
EOF
```

### Test GitHub Secrets

1. Go to **Actions** tab
2. Click **"AI Autonomous Worker"** workflow
3. Click **"Run workflow"**
4. If it runs successfully, your secrets are set up correctly
5. If it fails with authentication errors, recheck your secrets

---

## 📚 Related Documentation

- **[config/.env.example](config/.env.example)** - Template for local environment
- **[ACCOUNTS_README.md](ACCOUNTS_README.md)** - Account automation setup
- **[.github/README_AI_SYSTEM.md](.github/README_AI_SYSTEM.md)** - AI system overview
- **[AI_SYSTEM_ACTIVATION_GUIDE.md](AI_SYSTEM_ACTIVATION_GUIDE.md)** - Activating AI workers

---

## 🆘 Troubleshooting

### "Module 'openai' not found"

Install the required Python package:

```bash
pip install openai anthropic
```

### "Authentication failed" errors

1. Verify your API key is correct
2. Check it starts with `sk-proj-` or `sk-`
3. Ensure no extra spaces in the `.env` file
4. Try generating a new key

### "Permission denied" on `.env` file

Make sure the file has proper permissions:

```bash
chmod 600 config/.env
```

### GitHub Actions can't find secrets

1. Verify you added secrets in **Settings** → **Secrets and variables** → **Actions**
2. Check secret names match exactly: `OPENAI_API_KEY` (case-sensitive)
3. Make sure you have admin access to the repository

### API key not loading in scripts

Some scripts need explicit environment loading. Check if the script has:

```python
from dotenv import load_dotenv
load_dotenv("config/.env")
```

If not, install and import:

```bash
pip install python-dotenv
```

---

## 💰 API Usage & Costs

### OpenAI Costs (ChatGPT API)
- **GPT-4o**: ~$5 per 1M input tokens, ~$15 per 1M output tokens
- **GPT-3.5 Turbo**: ~$0.50 per 1M input tokens, ~$1.50 per 1M output tokens

### Anthropic Costs (Claude API)
- **Claude 3.5 Sonnet**: ~$3 per 1M input tokens, ~$15 per 1M output tokens
- **Claude 3 Haiku**: ~$0.25 per 1M input tokens, ~$1.25 per 1M output tokens

**Tip:** Set usage limits in your API dashboard to avoid unexpected charges!

---

## ✅ Checklist

Before you finish setup:

- [ ] Created `config/.env` from `config/.env.example`
- [ ] Added OpenAI API key to `.env` file
- [ ] Added Anthropic API key to `.env` file (if using Claude)
- [ ] Verified `.env` is in `.gitignore`
- [ ] Added `OPENAI_API_KEY` to GitHub Secrets
- [ ] Added `ANTHROPIC_API_KEY` to GitHub Secrets (if needed)
- [ ] Tested a script locally to verify it works
- [ ] Checked a GitHub Actions workflow run
- [ ] Rotated any exposed API keys from git history

---

## 🎉 You're All Set!

Your ChatGPT/OpenAI API key is now configured and ready to use!

**Next Steps:**
- Test the AI autonomous workflows
- Explore the AI-powered scripts in `.github/scripts/`
- Read the [AI System Activation Guide](AI_SYSTEM_ACTIVATION_GUIDE.md)

---

*Need more help? Check [ACCOUNTS_README.md](ACCOUNTS_README.md) or create a GitHub issue.*

*Last Updated: 2025-12-09*
