import re
from token import Token
class Function:
    def __init__(self, func):
        self.variable = self.determine_variable(func)
        self.func = eval('lambda ' + self.variable + ':' + self.parse(func))

    def determine_variable(self,expression):
        for character in expression:
            if character in 'abcdefghijklmnopqrstuvwxyz':
                return character
        return '0'

    def parse(self, func):
        tokens = self.tokenify(func)
        function = ""
        for tokenArray in tokens:
            function = function + '+'
            for token in tokenArray:
                function = function + token.val
        print(function[1:])
        return function[1:]

    def tokenify(self, text):
        text = text.replace("^","**")
        expressions = text.split("+")
        expressions = list(map(lambda exp: exp.lower(),expressions))
        print(expressions)
        tokens = []
        for expression in expressions:
            tokenArray = []
            for character in expression:
                new_token = Token(character,self.variable)
                tokenArray.append(new_token)
            tokens.append(tokenArray)
        return self.convert(tokens)

    def convert(self,tokens):
        for exp in tokens:
            for i in range(0,len(exp) - 1):
                if exp[i].isOperand() and exp[i+1].isOperand():
                    newToken = Token('*',self.variable)
                    exp.insert(i+1,newToken)
        return tokens
       

