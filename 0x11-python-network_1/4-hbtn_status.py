#!/usr/bin/python3
""" Script to send GET request using request library
"""
from requests import get


if __name__ == "__main__":
    req = get('https://alx-intranet.hbtn.io/status')
    content = req.content.decode()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
