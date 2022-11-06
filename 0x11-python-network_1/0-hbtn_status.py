#!/usr/bin/python3
""" Script to send a get request
"""
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as req:
        content = req.read()
        print("Body response:\n\t{}: {}\n\t{}: {}\n\t{}: {}".format(
            "- type", type(content), "- content", content, "- utf8 content",
            content.decode('utf8')))
