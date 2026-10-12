"""Git operations manager for LDICA Enterprise System Generator.

Handles branch creation, conventional commits, non-fast-forward PR merges,
and milestone tagging.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class GitManager:
    def __init__(self, cwd: Path = ROOT):
        self.cwd = cwd
        self.env = dict(os.environ)
        self.env["GIT_AUTHOR_NAME"] = "Parul Chowdhary"
        self.env["GIT_AUTHOR_EMAIL"] = "parulchouudhary@gmail.com"
        self.env["GIT_COMMITTER_NAME"] = "Parul Chowdhary"
        self.env["GIT_COMMITTER_EMAIL"] = "parulchouudhary@gmail.com"

    def run(self, *args: str) -> str:
        cmd = ["git", *args]
        res = subprocess.run(cmd, cwd=str(self.cwd), capture_output=True, text=True, check=True, env=self.env)
        return res.stdout.strip()

    def init_repo(self):
        if not (self.cwd / ".git").exists():
            self.run("init", "-b", "main")
            print("[GIT] Initialized repository on branch main.")
        else:
            self.run("checkout", "main")
            print("[GIT] Checked out existing main branch.")

    def configure_user(self):
        self.run("config", "user.name", "Parul Chowdhary")
        self.run("config", "user.email", "parulchouudhary@gmail.com")

    def stage_all(self):
        self.run("add", "-A")

    def commit(self, message: str):
        self.stage_all()
        self.run("commit", "--allow-empty", "-m", message)

    def create_and_checkout_branch(self, branch_name: str):
        self.run("checkout", "-B", branch_name)

    def checkout(self, branch_name: str):
        self.run("checkout", branch_name)

    def merge_pr(self, branch_name: str, pr_number: int, title: str, description: str):
        self.checkout("main")
        merge_msg = f"Merge pull request #{pr_number} from {branch_name}\n\n{title}\n\n{description}"
        self.run("merge", "--no-ff", "-m", merge_msg, branch_name)
        print(f"[GIT] Merged PR #{pr_number}: {branch_name}")

    def tag_release(self, tag: str, message: str):
        self.run("tag", "-a", tag, "-m", message)
        print(f"[GIT] Created release tag: {tag}")
