#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    if my_list:
        a = set(my_list)
        for x in a:
            res += x
    return res
