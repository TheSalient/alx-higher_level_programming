#!/usr/bin/python3
def weight_average(my_list=[]):
    c = 0
    d = 0
    if my_list:
        dic = dict(my_list)
        for i in dic:
            c = c + (i * dic[i])
            d += dic[i]
            i = i + 1
        e = c / d
        return (e)
    else:
        return (0)
