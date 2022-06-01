#!/usr/bin/python3
def uppercase(str):
    """this function prints a string in uppercase followed by a new line."""
    for i in str:
        num = ord(i)
        if num >= 97 and num <= 122:
            num = num - 32
        print("{:c}".format(num), end="")
    print()

uppercase("best")
uppercase("Best School 98 Battery street")