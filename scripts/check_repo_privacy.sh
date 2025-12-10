#!/bin/bash
# Repository Privacy Checker Script
# Helps you quickly check if your GitHub repositories are public or private

set -e

echo "=========================================="
echo "GitHub Repository Privacy Checker"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get GitHub username
USERNAME="${1:-issdandavis}"

echo "Checking repositories for user: $USERNAME"
echo ""

# Check if gh CLI is installed
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI detected - using authenticated API"
    echo ""
    
    # List repositories with visibility
    echo "Your repositories and their privacy status:"
    echo "--------------------------------------------"
    
    gh repo list "$USERNAME" --limit 100 --json name,visibility,isPrivate,url | \
        jq -r '.[] | "\(.name): \(if .isPrivate then "🔒 PRIVATE" else "🌐 PUBLIC" end) - \(.url)"'
    
    echo ""
    echo "Summary:"
    echo "--------"
    
    # Count public and private
    PUBLIC_COUNT=$(gh repo list "$USERNAME" --limit 100 --json isPrivate | jq '[.[] | select(.isPrivate == false)] | length')
    PRIVATE_COUNT=$(gh repo list "$USERNAME" --limit 100 --json isPrivate | jq '[.[] | select(.isPrivate == true)] | length')
    
    echo -e "${GREEN}Public repositories: $PUBLIC_COUNT${NC}"
    echo -e "${YELLOW}Private repositories: $PRIVATE_COUNT${NC}"
    
elif command -v curl &> /dev/null; then
    echo "⚠️  GitHub CLI not found - using public API (shows public repos only)"
    echo "   To see ALL repos, install GitHub CLI: https://cli.github.com/"
    echo ""
    
    # Use public API (only shows public repos)
    echo "Public repositories for $USERNAME:"
    echo "----------------------------------"
    
    REPOS_JSON=$(curl -s "https://api.github.com/users/$USERNAME/repos?per_page=100")
    
    echo "$REPOS_JSON" | \
        jq -r '.[] | "\(.name): 🌐 PUBLIC - \(.html_url)"' 2>/dev/null || {
            echo "Error: Failed to fetch repositories"
            echo "This could mean:"
            echo "  1. Username doesn't exist"
            echo "  2. API rate limit reached"
            echo "  3. Network connectivity issue"
            exit 1
        }
    
    echo ""
    PUBLIC_COUNT=$(echo "$REPOS_JSON" | jq '. | length')
    echo -e "${GREEN}Public repositories found: $PUBLIC_COUNT${NC}"
    echo -e "${YELLOW}Private repositories: Not visible via public API${NC}"
    echo ""
    echo "💡 Install GitHub CLI to see private repositories:"
    echo "   Visit: https://cli.github.com/"
    
else
    echo "❌ Neither GitHub CLI nor curl is available"
    echo ""
    echo "Please install one of the following:"
    echo "  1. GitHub CLI: https://cli.github.com/ (recommended)"
    echo "  2. curl: Usually pre-installed on most systems"
    exit 1
fi

echo ""
echo "=========================================="
echo "Current Repository Status"
echo "=========================================="

# Check current repository
if [ -d ".git" ]; then
    CURRENT_REPO=$(git config --get remote.origin.url | sed -E 's/.*github.com[:\/](.*)\.git/\1/' | sed 's/\.git$//')
    echo "Current repository: $CURRENT_REPO"
    echo ""
    echo "To check privacy status of this repository:"
    echo "  Visit: https://github.com/$CURRENT_REPO/settings"
    echo "  Look for 'Danger Zone' → 'Change repository visibility'"
else
    echo "Not in a git repository"
fi

echo ""
echo "=========================================="
echo "Next Steps"
echo "=========================================="
echo "1. Review the list above"
echo "2. For detailed guide, see: REPOSITORY_PRIVACY_GUIDE.md"
echo "3. To change visibility, visit repository settings on GitHub"
echo "4. Always audit for secrets before making repositories public"
echo ""
