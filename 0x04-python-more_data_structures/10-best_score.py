#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        fin_max = max(a_dictionary, key=a_dictionary.get)
        return fin_max
    else:
        return (None)
