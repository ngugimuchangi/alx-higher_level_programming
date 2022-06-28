#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Output string
output = "Last digit of {} is {} {}"
# Compute the last digit of number
if number < 0:
    last = (number * -1) % 10
    last = last * -1
else:
    last = number % 10
if last > 5:
    print(output.format(number, last, 'and is greater than 5'))
elif last == 0:
    print(output.format(number, last, 'and is 0'))
else:
    print(output.format(number, last, 'and is less than 6 and not 0'))
