# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability in this project, please follow these guidelines:

### For Security Issues

**DO NOT** open a public GitHub issue for security vulnerabilities.

Instead, please report security issues by:

1. Using GitHub's private security advisory feature:
   - Go to the repository's Security tab
   - Click "Report a vulnerability"
   - Fill out the form with details

2. Or contact the repository maintainers directly through GitHub

### What to Include

When reporting a vulnerability, please include:

- **Description** - Clear description of the vulnerability
- **Impact** - Potential impact and severity assessment
- **Steps to Reproduce** - Detailed steps to reproduce the issue
- **Affected Versions** - Which versions are affected
- **Suggested Fix** - If you have ideas for fixing it (optional)
- **Your Contact** - How we can reach you for follow-up

### Response Timeline

- **Initial Response:** Within 48 hours of report
- **Status Update:** Within 7 days with assessment and action plan
- **Resolution:** Timeline depends on severity and complexity

### Severity Levels

We classify vulnerabilities as:

- **Critical** - Immediate action required (e.g., credential exposure, RCE)
- **High** - Significant security issue (e.g., XSS, data leak)
- **Medium** - Moderate security concern
- **Low** - Minor security improvement

## Security Best Practices

### For Contributors

- Never commit API keys, passwords, or other credentials
- Use `.env` files (which are gitignored) for sensitive data
- Review code for common security issues before submitting PRs
- Keep dependencies updated
- Follow secure coding practices

### For Users

- Always use the `.env.example` template and create your own `.env` file
- Never share your API keys or credentials
- Keep your local repository clone secure
- Report suspicious behavior or unexpected requests for credentials

## Known Security Considerations

### API Keys

This project uses external APIs (Anthropic, OpenAI) for AI automation features. These keys should:

- ✅ Be stored in `.env` files (gitignored)
- ✅ Be added to GitHub Secrets for automated workflows
- ✅ Never be committed to the repository
- ✅ Be rotated if exposed

### Previous Exposure

**Note:** Previous commits in this repository's history may have contained plaintext API keys. These have been:

- Removed from tracked files
- Added to `.gitignore`
- Recommended for rotation in documentation

**Action Required:** If you cloned this repository before December 2025, ensure you:
- Rotate any API keys that may have been visible
- Pull the latest changes
- Use proper `.env` file setup

### Content Safety

The game content is designed for general audiences (teens and adults). No sensitive personal data is collected or stored by the game itself.

### Third-Party Dependencies

We use:
- **ChoiceScript** - Interactive fiction framework (Choice of Games LLC)
- **Node.js** - For local development server
- **Python** - For automation scripts

Keep these dependencies updated and review their security advisories.

## Security Features

### Current Protections

- ✅ `.gitignore` excludes sensitive files
- ✅ `.env.example` template for safe configuration
- ✅ No hardcoded credentials in code
- ✅ GitHub Secrets for automation credentials
- ✅ Code review required for sensitive changes

### Planned Enhancements

- 🔄 Automated dependency vulnerability scanning
- 🔄 Secret scanning alerts enabled
- 🔄 Branch protection rules for main branch

## Disclosure Policy

- We follow **coordinated disclosure** practices
- Security issues will be disclosed after a fix is available
- Credit will be given to reporters (unless they prefer anonymity)
- CVE IDs will be requested for serious vulnerabilities

## Contact

For security-related questions that aren't vulnerabilities, you can:
- Open a GitHub discussion
- Contact maintainers through GitHub
- Review our public documentation

---

**Remember:** Security is everyone's responsibility. Thank you for helping keep this project secure! 🔒

*Last Updated: December 2025*
