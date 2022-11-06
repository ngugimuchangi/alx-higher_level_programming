#!/usr/bin/python3
""" Script that takes in a URL, sends a request and displays
    the value of the X-Rquest-Id variable in the header of the response
"""
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as req:
        print(req.headers.get('X-Request-Id'))
