#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number < 0:
    number1 = ((number * -1) % 10) * -1
else:
    number1 = number % 10
if number1 > 5:
    print('Last digit of {:d} is {:d} and is greater than 5'
          .format(number, number1))
elif number1 == 0:
    print('Last digit of {:d} is {:d} and is 0'.format(number, number1))
elif number1 < 6 and number1 != 0:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'
          .format(number, number1))
