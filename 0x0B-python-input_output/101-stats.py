#!/usr/bin/python3
""" Script to read stdin and compute metrics
"""
import sys


def status_print(tally, size):
    """ Printing function
        Args:
            tally (dict): tally of status
            file_size (int): size of the file
        Return: nothing
    """
    print("File size: {:d}".format(size))
    for key in sorted(tally.keys()):
        if tally[key]:
            print("{:s}: {:d}".format(key, tally[key]))


def main():
    """ Main: Entry point
        Args: none
        Return: nothing
    """
    file_size = 0
    status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1
            tokens = line.split()
            if len(tokens) < 7:
                continue
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
            file_size += int(tokens[-1])
            if line_count % 10 == 0:
                status_print(status_tally, file_size)
        status_print(status_tally, file_size)
    except KeyboardInterrupt as e:
        status_print(status_tally, file_size)
        print(e)


if __name__ == "__main__":
    main()
