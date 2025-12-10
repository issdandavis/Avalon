# 🚨 CRITICAL SECURITY ALERT - EXPOSED API KEYS

## ⚠️ IMMEDIATE ACTION REQUIRED

**Exposed API Keys Found in Repository:**
- File: `archive/Open Ai and Claudie.txt`
- Contains: OpenAI API Key + Anthropic API Key
- Status: **PUBLICLY VISIBLE** (if repository is public)

---

## 🔴 STOP - Do This RIGHT NOW

### Step 1: Rotate Your API Keys IMMEDIATELY

#### OpenAI API Key
1. Go to: https://platform.openai.com/api-keys
2. Find the key starting with `sk-proj-jhVvo...`
3. Click **Revoke** or **Delete**
4. Create a new API key
5. Store it ONLY in `config/.env` (NOT in git)

#### Anthropic API Key
1. Go to: https://console.anthropic.com/settings/keys
2. Find the key starting with `sk-ant-api03-MFGHI...`
3. Click **Revoke** or **Delete**
4. Create a new API key
5. Store it ONLY in `config/.env` (NOT in git)

### Step 2: Check for Unauthorized Usage

#### OpenAI
1. Visit: https://platform.openai.com/usage
2. Check for unexpected API calls
3. Review usage dates and amounts
4. Look for suspicious activity

#### Anthropic
1. Visit: https://console.anthropic.com/settings/usage
2. Review recent API usage
3. Check for unexpected patterns
4. Monitor your billing

### Step 3: Secure Your Repository

#### Option A: If Repository is Currently Public
**Make it private IMMEDIATELY:**
1. Go to: https://github.com/issdandavis/Aethromoor/settings
2. Scroll to "Danger Zone"
3. Click "Change visibility"
4. Select "Make private"
5. Confirm by typing repository name

#### Option B: If You Want to Keep it Public
1. Remove the exposed keys from git history (see below)
2. Rotate all API keys
3. Verify .gitignore is correct
4. Then make public again

---

## 🔧 Remove Secrets from Git History

### Quick Method (Recommended)

```bash
# Navigate to repository
cd /home/runner/work/Aethromoor/Aethromoor

# Remove the file from git history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch 'archive/Open Ai and Claudie.txt'" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (WARNING: This rewrites history)
git push origin --force --all
```

### Alternative: Use BFG Repo-Cleaner (Easier)

```bash
# Install BFG
# Download from: https://rtyley.github.io/bfg-repo-cleaner/

# Run BFG to remove the file
bfg --delete-files "Open Ai and Claudie.txt"

# Clean up
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Force push
git push origin --force --all
```

---

## ✅ Proper API Key Storage

### DO ✅

**Store in `config/.env`** (this file is gitignored):
```bash
# config/.env
OPENAI_API_KEY=sk-proj-YOUR_NEW_KEY_HERE
ANTHROPIC_API_KEY=sk-ant-api03-YOUR_NEW_KEY_HERE
```

**Or use GitHub Secrets** for workflows:
1. Go to: https://github.com/issdandavis/Aethromoor/settings/secrets/actions
2. Click "New repository secret"
3. Name: `OPENAI_API_KEY`
4. Value: Your new key
5. Repeat for `ANTHROPIC_API_KEY`

### DON'T ❌

- ❌ Put keys in ANY file tracked by git
- ❌ Commit `.env` files
- ❌ Store keys in code files
- ❌ Share keys in text files
- ❌ Email keys
- ❌ Post keys in issues/PRs/comments

---

## 🔍 Check for Other Exposed Secrets

```bash
# Search for common secret patterns
cd /home/runner/work/Aethromoor/Aethromoor

# Check current files
grep -r -iE "sk-[a-zA-Z0-9-]+" . --exclude-dir=.git | grep -v ".md:"

# Check API keys
grep -r -iE "api[_-]?key\s*=\s*['\"]?[a-zA-Z0-9-]+" . --exclude-dir=.git

# Check tokens
grep -r -iE "token\s*=\s*['\"]?[a-zA-Z0-9-]+" . --exclude-dir=.git

# Check passwords
grep -r -iE "password\s*=\s*['\"]?[a-zA-Z0-9-]+" . --exclude-dir=.git
```

---

## 📋 Security Checklist

- [ ] Revoked OpenAI API key
- [ ] Revoked Anthropic API key
- [ ] Created new OpenAI API key
- [ ] Created new Anthropic API key
- [ ] Stored new keys in `config/.env` ONLY
- [ ] Verified `config/.env` is in `.gitignore`
- [ ] Checked OpenAI usage dashboard for suspicious activity
- [ ] Checked Anthropic usage dashboard for suspicious activity
- [ ] Reviewed recent charges/billing
- [ ] Removed `archive/Open Ai and Claudie.txt` from git history
- [ ] Force pushed to remove history
- [ ] Scanned for other exposed secrets
- [ ] Made repository private (or cleaned before making public)
- [ ] Set up GitHub secret scanning (if available)
- [ ] Enabled 2FA on OpenAI account
- [ ] Enabled 2FA on Anthropic account

---

## 🆘 If You See Unauthorized Charges

### OpenAI
- Email: support@openai.com
- Report: Unauthorized API usage
- Request: Refund for unauthorized charges
- Provide: Dates, amounts, and explanation

### Anthropic
- Email: support@anthropic.com
- Report: Exposed API key and unauthorized usage
- Request: Investigation and potential refund
- Provide: Timeline of exposure

---

## 📚 Resources

- **GitHub - Removing Sensitive Data**: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- **BFG Repo-Cleaner**: https://rtyley.github.io/bfg-repo-cleaner/
- **git-filter-branch**: https://git-scm.com/docs/git-filter-branch
- **OpenAI Security Best Practices**: https://platform.openai.com/docs/guides/safety-best-practices
- **GitHub Secret Scanning**: https://docs.github.com/en/code-security/secret-scanning

---

## 🔐 Prevention for the Future

### 1. Use Environment Variables
Always store secrets in environment variables, never in code.

### 2. Use .gitignore
Verify `.gitignore` includes:
```
.env
.env.*
*.key
*.pem
config/.env
secrets/
```

### 3. Use git-secrets
Install pre-commit hooks to prevent committing secrets:
```bash
# Install git-secrets
brew install git-secrets  # macOS
# or download from: https://github.com/awslabs/git-secrets

# Set up for repository
git secrets --install
git secrets --register-aws
```

### 4. Regular Audits
- Review repository monthly for exposed secrets
- Rotate API keys quarterly
- Monitor usage dashboards weekly

---

## ⏰ Timeline

**What you should do and when:**

### Right Now (Next 10 minutes)
1. Revoke both API keys
2. Check usage dashboards
3. Make repository private (if currently public)

### Today
1. Create new API keys
2. Store in `config/.env` properly
3. Remove file from git history
4. Scan for other secrets

### This Week
1. Set up GitHub secret scanning
2. Enable 2FA on all accounts
3. Audit other repositories
4. Document security practices

---

## ❓ Questions?

**Q: Is this really that serious?**
A: **YES.** Exposed API keys can lead to:
- Thousands of dollars in unauthorized charges
- Account suspension
- Data theft
- Service abuse

**Q: How do I know if someone used my keys?**
A: Check the usage dashboards:
- OpenAI: https://platform.openai.com/usage
- Anthropic: https://console.anthropic.com/settings/usage

**Q: Can I just delete the file?**
A: **NO.** Deleting the file doesn't remove it from git history. You must use `git filter-branch` or BFG to rewrite history.

**Q: What if my repository is already public?**
A: The keys are likely compromised. Rotate immediately and monitor usage closely.

---

**🚨 DO NOT IGNORE THIS. ACT NOW. 🚨**

