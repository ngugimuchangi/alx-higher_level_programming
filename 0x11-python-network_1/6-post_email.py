#!/usr/bin/python3
""" Script to send a POST request
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url, email = argv[1:3]
    data = {'email': email}
    req = post(url, data=data)
    print(req.content.decode())
