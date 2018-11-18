import math
from calculus import Calculus


def findWord(word, arr):
    for i in range(len(arr)):
        if arr[i] == word:
            return i
    return -1

calc = Calculus(5)
while(1):
    inp = input(">> ")
    if inp == 'exit':
        break
    else:
        words = inp.split(" ")
        if words[0] == 'integrate':
            startFunc = 1
            endFunc = findWord('between',words) 
            if endFunc == -1:
                print("Error, wrong syntax")
                break

            func = 'lambda x:'
            for word in range(startFunc,endFunc):
                func = func + words[word]
            lowerBound = float(words[findWord('and',words) - 1])
            upperBound = float(words[findWord('and',words) + 1])
            print(calc.integrate(eval(func))(lowerBound,upperBound))
        elif words[0] == 'differentiate':
            func = 'lambda x:'
            for word in range(1,findWord('at',words)):
                func = func + words[word]
            value = float(words[len(words) - 1])
            print(calc.derivative_operator(eval(func))(value))



          


