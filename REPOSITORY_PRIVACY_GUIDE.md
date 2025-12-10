# Repository Privacy Status Guide

## Quick Answer: How to Check if Your Repositories Are Private

This guide helps you verify whether your GitHub repositories are public or private.

---

## Current Repository (Aethromoor)

**Based on the fact that this GitHub Actions workflow is running**, this repository (`issdandavis/Aethromoor`) is **likely PUBLIC**. Here's why:

- GitHub Actions workflows in this runner environment typically indicate a public repository
- Private repositories have different execution contexts and limitations
- The workflow has access to standard public API endpoints

---

## How to Check Privacy Status for ALL Your Repositories

### Method 1: GitHub Web Interface (Easiest)

1. **Go to Your Profile**
   - Navigate to: `https://github.com/issdandavis`
   - Or click your profile icon → "Your profile"

2. **View Your Repositories**
   - Click the "Repositories" tab
   - Look for visibility indicators:
     - **Public** repositories show a "Public" badge
     - **Private** repositories show a "Private" badge (lock icon 🔒)

3. **Quick Filter**
   - Use the repository search box
   - Click "Type" dropdown → Select "Public" or "Private"
   - This shows only repositories of that visibility type

### Method 2: GitHub Settings Page

1. Go to: `https://github.com/issdandavis?tab=repositories`
2. Each repository will display either:
   - **Public** - visible to everyone
   - **Private** - only visible to you and collaborators you've invited

### Method 3: Using GitHub CLI (Command Line)

If you have GitHub CLI installed:

```bash
# List all your repositories with privacy status
gh repo list issdandavis --limit 100 --json name,visibility

# Count public vs private
gh repo list issdandavis --limit 100 --json visibility -q '.[] | .visibility' | sort | uniq -c
```

### Method 4: Using Git Commands (Current Repository Only)

To check just this repository:

```bash
# Check the repository URL
git remote get-url origin

# If it's public, you'll see:
# https://github.com/issdandavis/Aethromoor

# Then visit:
# https://github.com/issdandavis/Aethromoor/settings

# Look for the "Danger Zone" section at the bottom
# It will show "Change repository visibility" with current status
```

---

## Understanding Repository Visibility

### Public Repositories
- ✅ Visible to everyone on the internet
- ✅ Searchable on GitHub and search engines
- ✅ Anyone can clone/fork (unless you disable)
- ✅ Free unlimited collaborators
- ✅ Shows on your public profile
- ⚠️ **All code, issues, and commits are public**

### Private Repositories
- 🔒 Only visible to you and invited collaborators
- 🔒 Not searchable publicly
- 🔒 Cannot be forked by others (unless you allow)
- 🔒 Limited collaborators on free plans
- 🔒 Does NOT show on your public profile (unless you're a collaborator viewing)
- ✅ **Code and history are hidden from public**

---

## How to Change Repository Visibility

### Make a Public Repository Private

1. Go to repository Settings: `https://github.com/issdandavis/Aethromoor/settings`
2. Scroll to "Danger Zone" (bottom of page)
3. Click "Change visibility"
4. Select "Make private"
5. Type the repository name to confirm
6. Click "I understand, make this repository private"

⚠️ **Warning**: Making a repository private will:
- Remove it from search engines
- Hide all issues, PRs, and discussions from public view
- Disable public GitHub Pages (if enabled)
- Remove public forks (they become detached)

### Make a Private Repository Public

1. Go to repository Settings
2. Scroll to "Danger Zone"
3. Click "Change visibility"
4. Select "Make public"
5. Type the repository name to confirm
6. Click "I understand, make this repository public"

⚠️ **Warning**: Making a repository public will:
- Expose ALL code, commits, and history
- Make issues and PRs searchable
- Allow anyone to clone the repository
- **Check for exposed secrets/API keys first!**

---

## Security Best Practices

### Before Making Any Repository Public

✅ **Check for exposed secrets:**
```bash
# Search for common secret patterns
git log -p | grep -iE "api[_-]?key|password|secret|token|private[_-]?key"

# Check current files
grep -r -iE "api[_-]?key|password|secret|token" . --exclude-dir=.git
```

✅ **Review .gitignore:**
- Ensure `.env` files are listed
- Ensure `config/.env` is ignored (not tracked)
- Ensure sensitive configuration files are excluded

✅ **Check commit history:**
- Even deleted files can be found in Git history
- If secrets were committed, they need to be removed from history
- Consider using `git filter-branch` or BFG Repo-Cleaner

### After Making a Repository Public

🔄 **Rotate all credentials:**
- API keys
- Tokens
- Passwords
- SSH keys
- Database credentials

📝 **Document security:**
- Add security policy (SECURITY.md)
- Set up Dependabot alerts
- Enable secret scanning (if available)

---

## Quick Checklist for Repository Privacy

- [ ] I know the current visibility of this repository (Aethromoor)
- [ ] I've checked the visibility of all my repositories
- [ ] I understand the difference between public and private
- [ ] I've reviewed my repositories for exposed secrets
- [ ] I've verified my `.gitignore` excludes sensitive files
- [ ] I know how to change repository visibility if needed
- [ ] I've documented which repositories should stay private
- [ ] I've rotated any credentials if I made repositories public

---

## Additional Resources

- **GitHub Docs - Repository Visibility**: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
- **GitHub Docs - About Private Repositories**: https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility
- **GitHub Security Best Practices**: https://docs.github.com/en/code-security/getting-started/github-security-features

---

## Next Steps

1. **Verify Current Status**
   - Visit: https://github.com/issdandavis?tab=repositories
   - Note which repositories are public vs private

2. **Audit for Secrets** (if planning to make anything public)
   - Review commit history
   - Check for API keys, tokens, passwords
   - Verify `.gitignore` is properly configured

3. **Make Informed Decisions**
   - Decide which repositories should be public
   - Keep private: personal projects, work code, anything with secrets
   - Make public: open-source projects, portfolios, learning projects

4. **Document Your Decision**
   - Add notes to repository README files
   - Create a personal inventory of your repositories
   - Set calendar reminders to audit repository visibility quarterly

---

**Need Help?**
- GitHub Support: https://support.github.com/
- GitHub Community: https://github.community/
- Repository Settings: https://github.com/issdandavis/Aethromoor/settings

