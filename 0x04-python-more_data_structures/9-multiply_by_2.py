#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        dict = {}
        for k in a_dictionary.keys():
            dict[k] = a_dictionary[k] * 2
    return dict
