#!/usr/bin/python3
def uppercase(str):
    s2 = ''
    for i in str:
        if ord(i) in range(97, 123):
            s2 = s2 + chr(ord(i) - 32)
        else:
            s2 = s2 + i
    print('{}'.format(s2))
