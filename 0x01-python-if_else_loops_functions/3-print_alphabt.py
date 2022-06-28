#!/usr/bin/python3
for x in range(97, 123):
    if chr(x) not in 'qe':
        print('{}'.format(chr(x)), end='')
