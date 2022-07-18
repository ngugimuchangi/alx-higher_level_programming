#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: ".format(), end="")
        if res == 0:
            print("None")
        else:
            print("{:.1f}".format(res))
            return res
