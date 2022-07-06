#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    if my_list:
        weighted_scores = []
        weights = []
        for tup in my_list:
            weighted_scores.append(tup[0] * tup[1])
            weights.append(tup[1])
        avg = float(sum(weighted_scores) / sum(weights))
    return avg
