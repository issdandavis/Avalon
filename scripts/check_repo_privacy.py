#!/usr/bin/env python3
"""
Repository Privacy Checker
Checks if your GitHub repositories are public or private
"""

import json
import sys
import urllib.request
import urllib.error

def check_repo_privacy(username="issdandavis"):
    """Check privacy status of GitHub repositories"""
    
    print("=" * 50)
    print("GitHub Repository Privacy Checker")
    print("=" * 50)
    print()
    print(f"Checking repositories for user: {username}")
    print()
    
    # GitHub API endpoint
    api_url = f"https://api.github.com/users/{username}/repos?per_page=100"
    
    try:
        # Make API request
        with urllib.request.urlopen(api_url) as response:
            repos = json.loads(response.read().decode())
        
        if not repos:
            print(f"No public repositories found for user: {username}")
            print()
            print("Note: The public API only shows public repositories.")
            print("Private repositories are not visible without authentication.")
            return
        
        print("Public Repositories Found:")
        print("-" * 50)
        
        public_count = 0
        for repo in repos:
            name = repo.get('name', 'Unknown')
            private = repo.get('private', False)
            url = repo.get('html_url', '')
            
            if not private:
                public_count += 1
                print(f"  🌐 {name}")
                print(f"     → {url}")
                print()
        
        print("=" * 50)
        print("Summary:")
        print("-" * 50)
        print(f"  ✅ Public repositories: {public_count}")
        print(f"  ⚠️  Private repositories: Not visible via public API")
        print()
        print("To see ALL your repositories (including private):")
        print("  1. Visit: https://github.com/issdandavis?tab=repositories")
        print("  2. Install GitHub CLI: https://cli.github.com/")
        print()
        
    except urllib.error.HTTPError as e:
        print(f"❌ Error fetching repositories: {e.code} {e.reason}")
        print()
        if e.code == 404:
            print(f"User '{username}' not found on GitHub")
        elif e.code == 403:
            print("API rate limit exceeded. Try again later or use authentication.")
        print()
        return
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return
    
    # Check current repository
    print("=" * 50)
    print("Current Repository Status:")
    print("-" * 50)
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'config', '--get', 'remote.origin.url'],
            capture_output=True,
            text=True,
            check=True
        )
        origin_url = result.stdout.strip()
        
        # Extract repo path from URL
        if 'github.com' in origin_url:
            repo_path = origin_url.split('github.com')[-1].strip('/:').replace('.git', '')
            print(f"  📁 Current repository: {repo_path}")
            print()
            print(f"  To check privacy status:")
            print(f"    Visit: https://github.com/{repo_path}/settings")
            print(f"    Look for: 'Danger Zone' → 'Change repository visibility'")
            print()
    except (subprocess.CalledProcessError, FileNotFoundError, Exception) as e:
        print("  Not in a git repository or git not available")
        print()
    
    print("=" * 50)
    print("Next Steps:")
    print("-" * 50)
    print("  1. Review your repositories online:")
    print(f"     https://github.com/{username}?tab=repositories")
    print()
    print("  2. For detailed instructions, see:")
    print("     REPOSITORY_PRIVACY_GUIDE.md")
    print()
    print("  3. Before making any repo public:")
    print("     ⚠️  Check for exposed API keys/secrets")
    print("     ⚠️  Review commit history")
    print("     ⚠️  Verify .gitignore excludes sensitive files")
    print()

if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) > 1 else "issdandavis"
    check_repo_privacy(username)
