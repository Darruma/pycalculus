import math
from calculus import Calculus
from func import Function

def findWord(word, arr):
    for i in range(len(arr)):
        if arr[i] == word:
            return i
    return -1


calc = Calculus(6)
# while(1):
#     inp = input(">> ")
#     words = list(map(lambda word: word.lower(),inp.split(" ")))
#     if inp == 'exit':
#         break
#     elif words[0] == 'integrate':
#         startFunc = 1
#         endFunc = findWord('between', words)
#         if endFunc == -1:
#             print("Error, wrong syntax")
#         func = 'lambda x:'
#         for word in range(startFunc, endFunc):
#             func = func + words[word]
#         lowerBound = float(words[findWord('and', words) - 1])
#         upperBound = float(words[findWord('and', words) + 1])
#         print(calc.integrate(eval(func))(lowerBound, upperBound))
#     elif words[0] == 'differentiate':
#         print("differentiating")
#         func = 'lambda x:'
#         for word in range(1, findWord('at', words)):
#             func = func + words[word]
#         value = float(words[len(words) - 1])
#         print(calc.derivative_operator(eval(func))(value))
#     else:
#         print("Error please try again")

myFunc = Function("x^2+x")
print(myFunc.func)