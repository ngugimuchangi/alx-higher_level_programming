#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) & (i % 5 != 0):
            print('{}'.format('Fizz'), end=' ')
        elif (i % 5 == 0) & (i % 3 != 0):
            print('{}'.format('Buzz'), end=' ')
        elif i % 15 == 0:
            print('{}'.format('FizziBuzz'), end=' ')
        else:
            print('{:d}'.format(i), end=' ')
