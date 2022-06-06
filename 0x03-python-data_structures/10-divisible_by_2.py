#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    secondList = []
    for i in my_list:
        if i % 2 == 0:
            secondList.append(True)
        else:
            secondList.append(False)
    return secondList
