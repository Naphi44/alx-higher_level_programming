#!/usr/bin/python3
"""
    This script lists 10 commits (from the most recent to oldest)
    of a repository by a user, using the GitHub API
"""
import requests
from sys import argv

if __name__ == "__main__":
    repo, owner = argv[1], argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                  commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
