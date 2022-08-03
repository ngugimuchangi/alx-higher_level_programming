#!/usr/bin/python3
""" Script to read stdin and compute metrics
"""
import sys
file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}


def status_print(status_tally, file_size):
    """ Printing function
        Args:
            status_tally: tally of status
            file_size: size of the file
        Return: nothing
    """
    print("File size: {:d}".format(file_size))
    for key in sorted(status_tally.keys()):
        if status_tally[key]:
            print("{:s}: {:d}".format(key, status_tally[key]))


if __name__ == "__main__":
    """ Main: Entry point
        Args: none
        Return: nothing
    """
    i = 0
    try:
        for line in sys.stdin:
            i += 1
            tokens = line.split()
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
            file_size += int(tokens[-1])
            if i % 10 == 0:
                status_print(status_tally, file_size)
    except KeyboardInterrupt as e:
        status_print(status_tally, file_size)
        print(e)
