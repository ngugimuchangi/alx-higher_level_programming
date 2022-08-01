#!/usr/bin/python3
""" List module
"""


class MyList(list):
    """ List subclass
    """

    def print_sorted(self):
        """ List printing method
        """
        if isinstance(self, list):
            res = self[:]
            res.sort()
            print(res)
