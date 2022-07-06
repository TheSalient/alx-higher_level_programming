#!/usr/bin/python3
"""
write file function
"""


def append_write(filename="", text=""):
    """The write file function"""

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return (len(text))
