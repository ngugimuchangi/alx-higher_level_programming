#!/usr/bin/python3
"""Script that manages HTTP errors
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = get(url)
    if req.status_code < 400:
        print(req.content.decode())
    else:
        print("Error code: {}".format(req.status_code))
