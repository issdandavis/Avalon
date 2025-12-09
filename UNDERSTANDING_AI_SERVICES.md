# 🤖 Understanding AI Services in This Repository

## Important: What AI Services Are Being Used?

This document clarifies **which AI services** your repository uses and **who is paying** for them.

---

## 🎯 Quick Answer to Your Question

**Question:** "Can you access ChatGPT? I want to make sure you're using my subscription and my ChatGPT can access GitHub."

**Answer:**
1. **I (GitHub Copilot) am NOT ChatGPT** - I'm a different AI service
2. **This repository primarily uses Anthropic Claude**, not ChatGPT/OpenAI
3. **Your automated workflows will use YOUR API keys and YOUR billing**
4. **GitHub Copilot (me) is a separate Microsoft/GitHub service you're already subscribed to**

Let me explain the different AI services involved:

---

## 🤖 Different AI Services Explained

### 1️⃣ GitHub Copilot (Me - The AI Helping You Right Now)

**What it is:**
- I'm GitHub Copilot, made by GitHub/Microsoft
- I'm helping you write code and create documentation RIGHT NOW
- I run in your browser/IDE through GitHub

**Who pays:**
- YOU have a GitHub Copilot subscription (separate from ChatGPT)
- This is already active since I'm talking to you now
- ~$10-20/month depending on your plan

**What I can do:**
- Help you write code
- Create documentation
- Answer questions about your repository
- Make changes to files
- I do NOT call external APIs - I work directly in GitHub

**Access to your repository:**
- ✅ YES - I can already access your GitHub repository
- ✅ I'm working in it right now!

---

### 2️⃣ Anthropic Claude (Primary AI in Your Workflows)

**What it is:**
- Claude is an AI service made by Anthropic (different company)
- Your repository's automated scripts use Claude, not ChatGPT
- It runs when GitHub Actions workflows trigger

**Who pays:**
- YOU will pay Anthropic when you add your API key
- Pay-per-use based on API calls
- ~$3-15 per million tokens (cheaper than ChatGPT for most tasks)

**Where it's used:**
- `.github/workflows/ai-autonomous-worker.yml` - Uses `ANTHROPIC_API_KEY`
- `.github/scripts/ai_autonomous_worker.py` - Calls Claude API
- `.github/scripts/scene_writer_agent.py` - Scene writing with Claude
- `.github/scripts/content_polisher.py` - Content enhancement

**How to set it up:**
1. Get API key from: https://console.anthropic.com/
2. Add to GitHub Secrets as `ANTHROPIC_API_KEY`
3. Workflows will automatically use YOUR key and YOUR billing

---

### 3️⃣ OpenAI ChatGPT API (Optional - Not Currently Used)

**What it is:**
- ChatGPT API by OpenAI
- Different from the ChatGPT web interface you might use
- Currently configured but NOT actively used in your workflows

**Who pays:**
- YOU would pay OpenAI if you enable it
- Pay-per-use based on API calls
- ~$5-15 per million tokens

**Where it COULD be used:**
- There's a placeholder for `OPENAI_API_KEY` in `config/.env.example`
- No workflows currently use it
- Could be added for future features

**Your ChatGPT web subscription:**
- ❌ This is DIFFERENT from the API
- ❌ Your ChatGPT Plus/Pro subscription does NOT give you API access
- ❌ You need a separate OpenAI API account with billing set up

---

## 📊 Comparison Table

| Service | What It Is | Who Pays | Used In This Repo? | Access to GitHub? |
|---------|-----------|----------|-------------------|------------------|
| **GitHub Copilot** (me) | AI coding assistant | You (already subscribed) | ✅ YES - Helping you now | ✅ YES - Native access |
| **Anthropic Claude** | AI API for automation | You (when you add key) | ✅ YES - Main automation | ✅ YES - Via GitHub Actions |
| **OpenAI ChatGPT API** | AI API (alternative) | You (if you enable it) | ⚠️ NO - Placeholder only | ✅ YES - Via GitHub Actions |
| **ChatGPT Web** (ChatGPT Plus) | Web interface | You (separate subscription) | ❌ NO - Not connected | ❌ NO - Cannot connect |

---

## 🔑 How API Keys Work

### For Anthropic Claude (Currently Used)

**Step 1: Get Your API Key**
```
1. Go to: https://console.anthropic.com/
2. Sign up / Log in
3. Go to "API Keys" section
4. Click "Create Key"
5. Copy the key (starts with "sk-ant-")
```

**Step 2: Add to GitHub Secrets**
```
1. Go to your GitHub repository settings
2. Secrets and variables → Actions
3. New repository secret
4. Name: ANTHROPIC_API_KEY
5. Value: sk-ant-your-key-here
6. Add secret
```

**Step 3: It Just Works**
- GitHub Actions workflows will automatically use this key
- Claude API calls will charge YOUR Anthropic account
- You can monitor usage at: https://console.anthropic.com/settings/usage

### For OpenAI (If You Want to Use It)

**Step 1: Get API Key**
```
1. Go to: https://platform.openai.com/api-keys
2. Sign up / Log in (separate from ChatGPT Plus!)
3. Add payment method (required for API)
4. Create new secret key
5. Copy the key (starts with "sk-proj-" or "sk-")
```

**Step 2: Add to GitHub Secrets**
```
Same process as Claude:
- Name: OPENAI_API_KEY
- Value: sk-proj-your-key-here
```

**Step 3: Update Workflows to Use OpenAI**
- Currently, workflows use Anthropic Claude
- You would need to modify Python scripts to use OpenAI instead
- Or add new workflows that use OpenAI

---

## 💰 Cost Breakdown

### What You're Already Paying For

✅ **GitHub Copilot**: $10-20/month (flat rate)
- Unlimited usage in your IDE/browser
- What's helping you RIGHT NOW

### What You'll Pay for When You Enable It

📊 **Anthropic Claude API** (Pay per use):
- **Claude 3.5 Sonnet**: ~$3 per 1M input tokens, ~$15 per 1M output tokens
- **Claude 3 Haiku**: ~$0.25 per 1M input tokens, ~$1.25 per 1M output tokens
- **Estimated**: $1-10/month for typical automation usage

📊 **OpenAI API** (If you enable it - Pay per use):
- **GPT-4o**: ~$5 per 1M input tokens, ~$15 per 1M output tokens  
- **GPT-3.5**: ~$0.50 per 1M input tokens, ~$1.50 per 1M output tokens
- **Estimated**: Similar to Claude

### What Doesn't Work

❌ **Your ChatGPT Plus/Pro subscription**:
- This is for the web interface only
- Does NOT include API access
- Cannot be used for GitHub automation

---

## 🔐 Privacy & Security

### Who Can See Your Code?

**GitHub Copilot (Me):**
- ✅ Can see your repository (you granted access)
- ✅ Microsoft/GitHub processes your code
- ✅ Uses it to help you, following their privacy policy

**Anthropic Claude:**
- ✅ Only sees what your scripts send to it
- ✅ You control what data is sent
- ✅ Anthropic doesn't train on your data (per their policy)

**OpenAI (If you enable it):**
- ⚠️ Only sees what your scripts send to it
- ⚠️ By default, may use data for training (check API settings)
- ✅ Can opt out in API settings

---

## 🚀 What Should You Do?

### To Use the Current AI Automation (Recommended)

1. **Get Anthropic API key** (free tier available)
   - Go to: https://console.anthropic.com/
   - Sign up and get API key

2. **Add to GitHub Secrets**
   - Repository Settings → Secrets → Actions
   - Add `ANTHROPIC_API_KEY`

3. **Workflows will automatically activate**
   - AI Scene Writer runs every 3 hours
   - AI Content Polisher runs every 4 hours
   - Other automation as scheduled

4. **Monitor your usage**
   - Check Anthropic console for API usage
   - Set spending limits if needed

### If You Want to Use OpenAI Instead

1. **Get OpenAI API key** (requires payment method)
   - Go to: https://platform.openai.com/api-keys
   - Add billing information
   - Create API key

2. **Modify the Python scripts**
   - Change from `import anthropic` to `import openai`
   - Update API calls to use OpenAI format
   - Test thoroughly

3. **Add to GitHub Secrets**
   - Add `OPENAI_API_KEY` to secrets

### If You Just Want to Use GitHub Copilot (Me)

✅ **You're already doing this!**
- I'm helping you right now
- No additional setup needed
- I can make all the changes manually without automation

---

## 🤔 Common Misconceptions

### ❌ "My ChatGPT subscription should work with the API"
**Reality:** ChatGPT Plus/Pro is separate from the API. You need a separate API account with billing.

### ❌ "GitHub Copilot can call ChatGPT API for me"
**Reality:** I'm a separate service. I can help you SET UP API calls, but I don't make them myself.

### ❌ "Adding my API key gives GitHub access to my OpenAI account"
**Reality:** The key only lets your workflows call the API. GitHub doesn't access your account.

### ❌ "The automation will cost hundreds of dollars"
**Reality:** Typical usage is $1-10/month. You can set spending limits to protect yourself.

---

## ✅ Summary

**What You Have Now:**
- ✅ GitHub Copilot (me) helping you interactively
- ✅ Automated workflows ready to use Anthropic Claude
- ✅ Optional support for OpenAI if you want it

**What You Need to Do:**
1. Decide: Use Anthropic Claude (current setup) or OpenAI (requires changes)
2. Get the appropriate API key
3. Add to GitHub Secrets
4. Workflows will automatically use YOUR key and YOUR billing
5. Monitor usage and costs

**The Bottom Line:**
- I (GitHub Copilot) am already helping you - no setup needed
- Automated workflows use YOUR API keys and YOUR billing
- You control what runs and how much it costs
- ChatGPT web subscription is NOT the same as API access

---

## 📚 Next Steps

1. **Read:** [API_KEYS_SETUP.md](API_KEYS_SETUP.md) - Step-by-step setup guide
2. **Read:** [AI_SYSTEM_ACTIVATION_GUIDE.md](AI_SYSTEM_ACTIVATION_GUIDE.md) - How automation works
3. **Read:** [.github/README_AI_SYSTEM.md](.github/README_AI_SYSTEM.md) - Technical details

4. **Decide:** Do you want to enable automated AI workflows?
   - If YES: Follow API_KEYS_SETUP.md to add Anthropic key
   - If NO: Just keep using GitHub Copilot (me) for manual help

---

*Questions? Create a GitHub issue or ask me (GitHub Copilot) for help!*

*Last Updated: 2025-12-09*
