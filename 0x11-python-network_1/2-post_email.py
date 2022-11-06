#!/usr/bin/python3
""" Script to send a post request
"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == "__main__":
    url, email = argv[1:3]
    data = urlencode({'email': email}).encode('utf8')
    with urlopen(Request(url, data)) as req:
        print("Your email is: {}".format(req.msg))
