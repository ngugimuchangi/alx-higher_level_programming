#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        values = list(a_dictionary.values())
        count = values.count(value)
        if count > 0:
            for i in range(count):
                for x in a_dictionary:
                    if a_dictionary.get(x) == value:
                        del a_dictionary[x]
                        break
    return a_dictionary
