#!/usr/bin/python3
""" Script to send get request and manage HTTPError
"""
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as req:
            print(req.read().decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
