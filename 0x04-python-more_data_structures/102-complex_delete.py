#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dic = list(filter(lambda x: a_dictionary[x] == value, list(a_dictionary)))
    for i in dic:
        del a_dictionary[i]
    return a_dictionary
