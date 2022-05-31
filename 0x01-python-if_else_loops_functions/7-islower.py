#!/usr/bin/python3
def islower(c):
    """This is a function that check for lower character."""
    num = ord(c)
    if num >= 97 and num < 123:
        return (True)
    else:
        return (False)
