import math as Math
from calculus import Calculus
from func import Function
from functools import reduce
storedFunctions = {}
calc = Calculus(6)

def parseFunctionExpression(declaration):
	print(declaration)
	if len(declaration) == 1:
		if declaration[0] in storedFunctions.keys():
			return storedFunctions[declaration[0]]
		return Function(declaration[0])
	else:
		operator = declaration[1]
		if declaration[0] in list(storedFunctions.keys()):
			if declaration[2] in list(storedFunctions.keys()):
				leftFunc = storedFunctions[declaration[0]]
				rightFunc = storedFunctions[declaration[2]]
				if operator == '+':
					return leftFunc + rightFunc
				elif operator == '*':
					return leftFunc * rightFunc
				elif operator == '-':
					return leftFunc - rightFunc
				elif operator == '.':
					return leftFunc.compose(rightFunc)
			else:
				print(">> " +  declaration[2] + " not found")
		else:
			print(">> "  + declaration[0] + " not found")
	return None

while 1:
	user_input = input(">> ").split(" ")
	if user_input[0] == 'differentiate':
		diffble_input = user_input[1:user_input.index('at')]
		diffblefunc = parseFunctionExpression(diffble_input)
		if diffblefunc is not None:
			val = float(user_input[len(user_input)-1])
			derivative_at_val = str(calc.derivative_operator(eval('lambda x:' + diffblefunc.func))(val))
			print(">> " + derivative_at_val)
	elif "=" in user_input: 
		equals_index = user_input.index("=")
		identifier = user_input[equals_index - 1]
		func = parseFunctionExpression(user_input[equals_index+1:])
		if func is not None:
			storedFunctions.update({identifier:func})
	elif 'functions' in user_input:
		for function in list(storedFunctions.keys()):
			print(">> " + function + ":= " + storedFunctions[function].readable_func)
	elif 'exit' in user_input:
		break
	else:
		print("Error")

