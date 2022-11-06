#!/usr/bin/python3
""" Script to send a post request
"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

url, email = argv[1:3]
data = urlencode({'email': email}).encode('utf8')
with urlopen(url, data) as req:
    print(req.msg)
