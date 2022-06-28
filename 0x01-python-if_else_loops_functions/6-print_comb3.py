#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if (j < i) | (j == i):
            continue
        if (j == 1) & (i == 0):
            print('{:d}{:d}'.format(i, j), end='')
        else:
            print(', {:d}{:d}'.format(i, j), end='')
print(''.format())
