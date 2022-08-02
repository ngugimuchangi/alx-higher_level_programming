#!/usr/bin/python3
""" JSON serialization and deserialization module
"""
import sys
import json
dump = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def main():
    """ Main function
    """
    try:
        my_list = load('add_item.json')
    except Exception:
        my_list = []
    my_list += [sys.argv[i] for i in range(1, len(sys.argv))]
    dump(my_list, 'add_item.json')


main()
