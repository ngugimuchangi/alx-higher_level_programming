#!/usr/bin/python3
__import__('hidden_4')


if __name__ == '__main__':
    names = dir('hidden')
    for i in names:
        if i[0] == '_':
            continue
        else:
            print('{}'.format(i))
