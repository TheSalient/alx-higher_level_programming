#!/usr/bin/python3
str = ''
for i in range(122, 96, -1):
    if i % 2 != 0:
        str += chr(i - 32)
    else:
        str += chr(i)
print("{}".format(str), end="")
