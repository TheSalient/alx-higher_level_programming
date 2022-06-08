#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = sorted(a_dictionary)
    for i in lst:
        print("{}: {}". format(i, a_dictionary[i]))
