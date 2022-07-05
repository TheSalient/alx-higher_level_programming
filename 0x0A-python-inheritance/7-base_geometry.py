#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 5-base_geometry.py)
"""


class BaseGeometry:
    """it has one method in it."""
    def area(self):
        """This is just to raise exceptions."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """to validate value."""
        self.name = name
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
