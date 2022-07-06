#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if isinstance(roman_string, str):
        if roman_string:
            for i in range(len(roman_string)):
                if roman_string[i] not in 'IVXLCDM':
                    res = 0
                    break
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
                    if (i + 1) < len(roman_string):
                        if roman_string[i + 1] in 'LC':
                            res -= 10
                        else:
                            res += 10
                    else:
                        res += 10
                if roman_string[i] == 'L':
                    res += 50
                if roman_string[i] == 'C':
                    if (i + 1) < len(roman_string):
                        if roman_string[i + 1] in 'DM':
                            res -= 100
                        else:
                            res += 100
                    else:
                        res += 100
                if roman_string[i] == 'D':
                    res += 500
                if roman_string[i] == 'M':
                    res += 1000
    return res
