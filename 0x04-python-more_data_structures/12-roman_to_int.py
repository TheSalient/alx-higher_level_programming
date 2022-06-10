#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        hi = 0
        boy = 0
        roman1 = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in roman_string[::-1]:
            hello = roman1[i]
            if hello >= hi:
                boy = boy + hello
                hi = hello
            else:
                boy = boy - hello
        return (boy)
    else:
        return (0)
