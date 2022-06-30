#!/usr/bin/python3
from hidden_4 import *
if __name__ == '__main__':
    names = dir()
    for i in names:
        if i[0] == '_':
            continue
        else:
            print('{}'.format(i))
