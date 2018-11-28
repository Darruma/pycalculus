import math
from calculus import Calculus
from func import Function
from functools import reduce
storedFunctions = {}
calc = Calculus(6)
while 1:
	user_input = input(">> ")
	equalsPosition = user_input.find('=')
	if not equalsPosition == -1:
		identifier = user_input[0:equalsPosition]
		expression = Function(user_input[equalsPosition:])
		# if the expressions is a literal function , add it to the dictionary,
		# e.g f(x) = sin(3x) or g(x) = cos(2x)
		# else, evaluate the expression then add it to the dictionary
		# e.g g(x) = f(x)+g(x)
		storedFunctions.update({identifier:expression})
	elif user_input[:3] == 'add':
		print(user_input[3:])

	elif user_input == 'functions':
		for function in list(storedFunctions.keys()):
			print(function + ":= " + storedFunctions[function].func)
	elif user_input == 'exit':
		break
	else:
		print("Error")

