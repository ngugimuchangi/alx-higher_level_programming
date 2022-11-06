#!/usr/bin/python3
""" Script to login into github
    Usage: ./10-my_github.py <username> <token>
"""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username, token = argv[1:3]
    logins = HTTPBasicAuth(username, token)
    req = get(url, auth=logins)
    results = req.json()
    print(results.get('id'))
