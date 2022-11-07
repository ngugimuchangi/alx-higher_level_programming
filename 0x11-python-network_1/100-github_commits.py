#!/usr/bin/python3
""" Script that gets most recent 10 commits
    from a specified github repository
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    repo, owner = argv[1:3]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    params = {"per_page": 10, "sort": "author-date", "order": "desc"}
    req = get(url, params=params)
    if req.status_code == 200:
        results = req.json()
        for i in results:
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
