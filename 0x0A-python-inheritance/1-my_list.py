#!/usr/bin/python3
"""
This is the first inheritance task, it inherit from class list
"""


class MyList(list):
    """all the attribute of list inherited"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        return (sorted(self))
