#!/usr/bin/python3
""" Script to HTTP request header
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = get(url)
    print(req.headers.get('X-Request-Id'))
