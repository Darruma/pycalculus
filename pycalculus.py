import math as Math
from Classes.calculus import Calculus
from Classes.func import Function
from functools import reduce
storedFunctions = {}
calc = Calculus(6)

def parseFunctionExpression(declaration):
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
	if user_input[0] == 'integrate':
		betweenPosition = -1
		if 'between' in user_input:
			betweenPosition = user_input.index('between')
			integrable_input = user_input[1:betweenPosition]
			integrablefunc = parseFunctionExpression(integrable_input)
			if integrablefunc is not None:
				lowerBound = float(user_input[user_input.index('and')-1])
				upperBound = float(user_input[user_input.index('and') + 1]) 
				func_obj = eval('lambda x:' + integrablefunc.func)
				integrate_between = str(calc.integrate(func_obj)(lowerBound,upperBound))
				print(">> " + integrate_between)
		elif betweenPosition == -1:
			print(">> Error")
		else:
			print(">> Error")
			
	elif user_input[0] == 'differentiate':
		atPosition = -1
		if 'at' in user_input:
			atPosition = user_input.index('at')
		if atPosition == -1:
			identifier = user_input[1]
			function = storedFunctions[identifier]
			identifier = identifier.insert(indentifier.find('(') - 1,'\'')
			differentiated_function = calc.derivative_operator(eval('lambda x:' + function))
			storedFunctions.update({identifier:differentiated_function})	
		else:
			diffble_input = user_input[1:atPosition]
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

