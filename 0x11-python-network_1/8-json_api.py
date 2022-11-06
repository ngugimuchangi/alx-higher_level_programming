#!/usr/bin/python3
""" Script to send a post request and get data
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    key = ""
    if len(argv) > 1:
        key = argv[1]
    data = {'q': key}

    search = post(url, data=data)
    try:
        result = search.json()
    except Exception as e:
        print("Not a valid JSON")
    else:
        if len(result) > 0:
            print("[{}] {}".format(result.get('id'),
                  result.get('name')))
        else:
            print("No result")
