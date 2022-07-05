#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle
(9-rectangle.py):
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """the square attributes in here."""
    def __init__(self, size):
        """to valid the size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """to compute and return the area"""
        return (self.__size ** 2)

    def __str__(self):
        """for str output."""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))

s = Square(13)

print(s)
print(s.area())