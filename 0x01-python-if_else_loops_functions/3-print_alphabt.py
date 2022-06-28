#!/usr/bin/python3
for x in range(97, 123):
    if '{:c}'.format(x) not in 'qe':
        print('{:c}'.format(x), end='')
