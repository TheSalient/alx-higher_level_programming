#!/usr/bin/python3
"""
this is the function to returns bool, based on if an object is an
instance of the provided class.
"""


def is_same_class(obj, a_class):
    """returns True or False"""
    return (type(obj) == a_class)
