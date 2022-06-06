#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        list_a = list(tuple_a)
        while(len(list_a) != 2):
            list_a.append(0)
        tuple_a = tuple(list_a)
    elif len(tuple_b) < 2:
        list_b = list(tuple_b)
        while(len(list_b) != 2):
            list_b.append(0)
        tuple_b = tuple(list_b)
    res = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return res
