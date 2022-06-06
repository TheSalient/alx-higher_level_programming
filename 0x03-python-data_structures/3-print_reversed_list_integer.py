#!/usr/bin/python3
from audioop import reverse


def print_list_integer(my_list=[]):
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
