#!/usr/bin/python3
def print_last_digit(number):
	"""This function prints the last digit of a number."""
	if number < 0:
		number1 = number * -1
		number2 = number1 % 10
	else:
		number1 = number * 1
		number2 = number1 % 10
	return (number2)
