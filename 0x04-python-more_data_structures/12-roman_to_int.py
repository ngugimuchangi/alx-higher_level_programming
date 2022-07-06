#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if roman_string:
        for i in range(len(roman_string)):
            if roman_string[i] not in 'IVXLCDM':
                return None;
            if roman_string[i] == 'I':
                if (i + 1) < len(roman_string):
                    if roman_string[i + 1] in 'VX':
                        res -= 1
                    else:
                        res += 1
                else:
                    res += 1
            if roman_string[i] == 'V':
                res += 5
            if roman_string[i] == 'X':
                res += 10
            if roman_string[i] == 'L':
                res += 50
            if roman_string[i] == 'C':
                res += 100
            if roman_string[i] == 'D':
                res += 500
            if roman_string[i] == 'M':
                res += 1000
        return res