#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    else:
        large_int = my_list[0]
        for i in my_list:
            if i > large_int:
                large_int = i
        return large_int
