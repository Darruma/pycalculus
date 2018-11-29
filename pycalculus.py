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
		declaration = user_input[equals_index+1:]
		if len(declaration) == 1:
			storedFunctions.update({identifier:Function(declaration[0])});
			print(">> Stored function with name " + identifier)
		else:
			operator = declaration[1]
			if declaration[0] in list(storedFunctions.keys()):
				if declaration[2] in list(storedFunctions.keys()):
					leftFunc = storedFunctions[declaration[0]]
					rightFunc = storedFunctions[declaration[2]]
					if operator == '+':
						storedFunctions.update({identifier:leftFunc + rightFunc})
					elif operator == '*':
						storedFunctions.update({identifier:leftFunc * rightFunc})
					elif operator == '-':
						storedFunctions.update({identifier:leftFunc - rightFunc})
					elif operator == '.':
						storedFunctions.update({identifier:leftFunc.compose(rightFunc)})
				else:
					print(">> " +  declaration[2] + " not found")
			else:
				print(">> "  + declaration[0] + " not found")

			


			# perform operations on functions
	elif 'functions' in user_input:
		for function in list(storedFunctions.keys()):
			print(">> " + function + ":= " + storedFunctions[function].readable_func)
	elif 'exit' in user_input:
		break
	else:
		print("Error")

