#!/usr/bin/python3
"""
this is the function to returns bool, based on if an object is an
instance of the provided class.
"""


def is_kind_of_class(obj, a_class):
    """returns False or True"""
    return(isinstance(obj, a_class))
