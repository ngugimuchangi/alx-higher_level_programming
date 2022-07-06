#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for x in a_dictionary:
            if a_dictionary.get(x) == max(a_dictionary.values()):
                return x
