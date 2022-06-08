#!/usr/bin/python3
def search_replace(my_list, search, replace):
    hi = []
    for i in my_list:
        if i == search:
            hi.append(replace)
        else:
            hi.append(i)
    return hi
