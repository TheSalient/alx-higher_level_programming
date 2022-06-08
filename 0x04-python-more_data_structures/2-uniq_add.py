#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    my_list1 = list(set(my_list))
    for i in my_list1:
        num += i
    return num
