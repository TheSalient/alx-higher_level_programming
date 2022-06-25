#!/usr/bin/python3
# 0-add_integer.py


def add_integer(a, b=98):
    """
    Returns c+d
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an interger")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an interger")
    return (int(a) + int(b))
    
    


print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)