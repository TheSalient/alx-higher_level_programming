#!/usr/bin/python3
def uppercase(str):
    """this function prints a string in uppercase followed by a new line."""
    for i in str:
        num = ord(i)
        if num > 90:
            num = num - 32
            print("{:c}".format(num), end="")
        else:
            print("{:c}".format(num), end="")
