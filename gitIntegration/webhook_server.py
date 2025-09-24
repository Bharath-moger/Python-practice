import time
from github import Github, Auth

# -----------------------------
# CONFIG
# -----------------------------
ACCESS_TOKEN = "XXXXXXXXXXXXXX"
REPO_NAME = "Bharath-moger/Python-Git-Integration"
POLL_INTERVAL = 10  # seconds

# -----------------------------
# CONNECT
# -----------------------------
auth = Auth.Token(ACCESS_TOKEN)
g = Github(auth=auth)
repo = g.get_repo(REPO_NAME)
print(f"Connected to {repo.full_name}\n")

# -----------------------------
# TRACKERS
# -----------------------------
seen_commits = set()
seen_prs = set()

# -----------------------------
# Show FULL history first
# -----------------------------
print("=== Commit History ===")
for commit in repo.get_commits():
    sha = commit.sha
    author = commit.commit.author.name
    msg = commit.commit.message
    print(f"[COMMIT] {sha[:7]} - {author}: {msg}")
    seen_commits.add(sha)

print("\n=== Pull Request History ===")
for pr in repo.get_pulls(state="all", sort="created", direction="asc"):
    print(f"[PR] #{pr.number} [{pr.state.upper()}] {pr.title} by {pr.user.login}")
    seen_prs.add(pr.id)

# -----------------------------
# LOOP for new events
# -----------------------------
print("\n--- Watching for new activity ---\n")
while True:
    try:
        # --- Check new commits ---
        for commit in repo.get_commits():
            if commit.sha not in seen_commits:
                print(f"\n[NEW COMMIT] {commit.commit.author.name}: {commit.commit.message}")
                seen_commits.add(commit.sha)

        # --- Check new PRs ---
        for pr in repo.get_pulls(state="all", sort="updated", direction="desc"):
            if pr.id not in seen_prs:
                print(f"\n[NEW PR] #{pr.number} [{pr.state.upper()}] {pr.title} by {pr.user.login}")
                seen_prs.add(pr.id)

        time.sleep(POLL_INTERVAL)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(POLL_INTERVAL)