import math as Math
from calculus import Calculus
from func import Function
from functools import reduce
storedFunctions = {}
calc = Calculus(6)
while 1:
	user_input = input(">> ").split(" ")
	if user_input[0] == 'differentiate':
		func = user_input[1]
		val = user_input[len(user_input) -1]
		if func in list(storedFunctions.keys()):
			function = 'lambda x:' + storedFunctions[func].func
			val = float(val)
			print(">> " +calc.derivative_operator(eval(function))(val))
		else:
			print(">> Error entering function")
	elif "=" in user_input: 
		equals_index = user_input.index("=")
		identifier = user_input[equals_index - 1]
		other = user_input[equals_index:]
		storedFunctions.update({identifier:Function(other[1])});
		print(">> Stored function with name " + identifier)
		# perform operations on functions
	elif 'functions' in user_input:
		for function in list(storedFunctions.keys()):
			print(">> " + function + ":= " + storedFunctions[function].func)
	elif 'exit' in user_input:
		break
	else:
		print("Error")

