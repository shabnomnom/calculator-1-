"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def get_input():
	operation = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
	user_input = input('> ')
	user_input = user_input.split(' ')
	if user_input[0] in operation:
		if len(user_input) == 1:
			return user_input
		if len(user_input) == 2 and user_input[1].isdigit():
			user_input[1] = int(user_input[1])
			return user_input
		elif len(user_input) == 3 and user_input[1].isdigit() and user_input[2].isdigit():
			user_input[1] = int(user_input[1])
			user_input[2] = int(user_input[2])
			return user_input
		else:
			return 'Not a valid option'
	else:
		return 'Not a valid option'

def prefix_calculator():

	print('Enter the operation you\'d like to perform.')

	user_input = get_input()

	while user_input[0] != 'q': 

		if user_input[0] == '+':

			summation = add(user_input[1], user_input[2])
			print(summation)
			
		elif user_input[0] == '-':

			difference = subtract(user_input[1], user_input[2])
			print(difference)

		elif user_input[0] == '*':

			product = multiply(user_input[1], user_input[2])
			print(product)

		elif user_input[0] == '/':

			quotient = divide(user_input[1], user_input[2])
			print(quotient)

		elif user_input[0] == 'square':

			squared = square(user_input[1])
			print(squared)

		elif user_input[0] == 'cube':
			
			cubed = cube(user_input[1])
			print(cubed)

		elif user_input[0] == 'pow':

			power_num = power(user_input[1], user_input[2])
			print(power_num)

		elif user_input[0] == 'mod':

			modulo = mod(user_input[1], user_input[2])
			print(modulo)

		elif user_input == 'Not a valid option':

			print('Enter a valid operation.')

		user_input = get_input()


prefix_calculator()