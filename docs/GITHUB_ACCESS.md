# Accessing the GitHub Repository

Use this guide to connect to the Avalon repository, authenticate safely, and keep your local copy in sync.

## 1. Prerequisites
- Install [Git](https://git-scm.com/) and confirm it's available: `git --version`.
- Ensure you have a GitHub account with access to the repository.

## 2. Clone the Repository
Choose the transport that matches your authentication method:
- **HTTPS (recommended for personal access tokens):**
  ```bash
  git clone https://github.com/USER/Aethromoor.git
  ```
- **SSH (recommended if you already use SSH keys):**
  ```bash
  git clone git@github.com:USER/Aethromoor.git
  ```
Replace `USER` with the organization or account that hosts the repo.

## 3. Authenticate
### HTTPS + Personal Access Token (PAT)
1. Create a PAT with `repo` scope from **Settings → Developer settings → Personal access tokens**.
2. When prompted for a password during `git clone`, paste the PAT instead of your GitHub password.

### SSH Keys
1. Generate a key if needed: `ssh-keygen -t ed25519 -C "your_email@example.com"`.
2. Add the public key to **Settings → SSH and GPG keys** on GitHub.
3. Test the connection: `ssh -T git@github.com`.

### GitHub CLI (gh)
1. Install the [GitHub CLI](https://cli.github.com/).
2. Run `gh auth login` and follow the prompts to log in.

## 4. Keep Your Fork in Sync
1. Add the upstream remote if you're working from a fork:
   ```bash
   git remote add upstream https://github.com/ORGANIZATION/Aethromoor.git
   ```
2. Update your local main branch:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```
3. Push updates back to your fork:
   ```bash
   git push origin main
   ```

## 5. Working With Branches
- Create a feature branch before making changes:
  ```bash
  git checkout -b feature/short-description
  ```
- Commit frequently with clear messages:
  ```bash
  git commit -am "Summarize the change in the imperative mood"
  ```

## 6. Troubleshooting
- **Permission denied (publickey):** Regenerate your SSH key and re-add it to GitHub.
- **Invalid username or password:** Ensure you're using a PAT (not a password) for HTTPS.
- **Two-factor authentication enabled:** Use a PAT or GitHub CLI instead of a password.

## 7. Helpful References
- [GitHub: Connecting to GitHub](https://docs.github.com/en/authentication/connecting-to-github)
- [GitHub: About remote repositories](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories)
