#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if roman_string:
        for i in range(len(roman_string)):
            if roman_string[i] not in 'IiVvXxLlCcDdMm':
                return None
            if roman_string[i] in 'Ii':
                if (i + 1) < len(roman_string):
                    if roman_string[i + 1] in 'VvXx':
                        res -= 1
                    else:
                        res += 1
                else:
                    res += 1
            if roman_string[i] in 'Vv':
                res += 5
            if roman_string[i] in 'Xx':
                res += 10
            if roman_string[i] in 'Ll':
                res += 50
            if roman_string[i] in 'Cc':
                res += 100
            if roman_string[i] in 'Dd':
                res += 500
            if roman_string[i] in 'Mm':
                res += 1000
        return res
