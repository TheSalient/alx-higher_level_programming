#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry
(8-base_geometry.py)
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """my rectangle class"""

    def __init__(self, width, height):
        """my public initialised class"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """to compute and return the area"""

        ans = self.__width * self.__height
        return ans

    def __str__(self):
        """for str output."""

        tring = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
