#!/usr/bin/python3
""" Script to send a post request
"""
from sys import argv
from urllib.request import urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    url, email = argv[1:3]
    data = urlencode({'email': email}).encode('utf-8')
    with urlopen(url, data) as req:
        print(req.read().decode('utf-8'))
