#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>'.format())
        exit(1)
    if sys.argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /'.format())
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op == '+':
        print('{} {} {} = {}'.format(a, op, b, add(a, b)))
    elif op == '-':
        print('{} {} {} = {}'.format(a, op, b, sub(a, b)))
    elif op == '*':
        print('{} {} {} = {}'.format(a, op, b, mul(a, b)))
    else:
        print('{} {} {} = {}'.format(a, op, b, div(a, b)))
