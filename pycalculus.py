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
		name = user_input[0:equalsPosition].strip(" ")
		function = Function(user_input[equalsPosition:])
		storedFunctions.update({name:function})
	elif user_input[:3] == 'add':
		plusFunctions = user_input[3:].split(" ")[1:]
		
	elif user_input == 'functions':
		for function in list(storedFunctions.keys()):
			print(function + " := " + storedFunctions[function].func)
	elif user_input == 'exit':
		break
	else:
		print("Error")

