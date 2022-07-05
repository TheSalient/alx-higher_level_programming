#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle
(9-rectangle.py):
"""

BaseGeometry = __import__("9-base_geometry").BaseGeometry


class Square(BaseGeometry):
    """the square attributes in here."""
    def __init__(self, size):
        """to valid the size"""
        if size > 0:
            self.interger_validator("size", size)
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """to compute and return the area"""
        return (self.__size ** 2)

    def __str__(self):
        """for str output."""
        return ("[Rectangle] {:d}/{:d}".format(self.__size, self.__size))
