#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number < 0:
	number1 = number * -1
	number2 = -(number1 % 10)
else:
	number1 = number * 1
	number2 = number1 % 10
str = f"Last digit of {number:d} is {number2} "
if number2 == 0:
	print(str + "and is 0")
elif number2 < 6 and number2 != 0:
	print(str + "and is less than 6 and not 0")
else:
	print(str + "and is greater than 5")
