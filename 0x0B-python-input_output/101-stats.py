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
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))


if __name__ == "__main__":
    """ Main: Entry point
        Args: none
        Return: nothing
    """
    i = 0
    try:
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) >= 2:
                stay = i
                if tokens[-2] in status_tally:
                    status_tally[tokens[-2]] += 1
                    i += 1
                try:
                    file_size += int(tokens[-1])
                    if stay == i:
                        i += 1
                except Exception:
                    if stay == i:
                        continue
            if i % 10 == 0:
                status_print(status_tally, file_size)

    except KeyboardInterrupt as e:
        status_print(status_tally, file_size)
        print(e)
