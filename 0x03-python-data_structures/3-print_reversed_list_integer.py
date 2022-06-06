#!/usr/bin/python3
def print_list_integer(my_list=[]):
    m = len(my_list) - 1
    for i in range(m, -1, -1):
        print("{:d}".format(my_list[i]))
