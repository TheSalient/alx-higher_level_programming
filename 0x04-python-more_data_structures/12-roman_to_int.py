#!/usr/bin/python3
def roman_to_int(roman_string):
    hi = 0
    i = 0
    while (i < len(roman_number)):
        s1 = value(roman_number[i])
        if (i + 1 < len(roman_number)):
            s2 = value(roman_number[i + 1])
            if (s1 >= s2):
                hi += s1
                i += 1
            else:
                hi += s2 - s1
                i += 2
        else:
            hi += s1
            i += 1
    return hi


def value(s):
    if (s == 'I'):
        return 1
    if (s == 'V'):
        return 5
    if (s == 'X'):
        return 10
    if (s == 'L'):
        return 50
    if (s == 'C'):
        return 100
    if (s == 'D'):
        return 500
    if (s == 'M'):
        return 1000
    return 0
