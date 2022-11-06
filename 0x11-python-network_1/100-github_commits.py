#!/usr/bin/python3
""" Script that gets last 10 commits

"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/search/commits"
    repo, owner = argv[1:3]
    header = {"accept": "application/vnd.github+json"}
    q = "repo:{}/{}".format(owner, repo)
    data = {"q": q, "per_page": 100, "sort": "author-date"}
    req = get(url, params=data headers=header)
    if req.status_code == 200:
        results = req.json()['items']
        for commit in results:
            print("{}: {}".format(commit.get('sha'), commit.get('author')))
