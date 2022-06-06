#!/usr/bin/python3
def no_c(my_string):
    The = my_string.translate({ord(c): None for c in "cC"})
    return The
