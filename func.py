import re
from token import Token
class Function:
    def __init__(self, func):
        self.special_expressions = ['sin(x)','cos(x)','tan(x)']
        self.variable = self.determine_variable(func)
        self.func = eval('lambda ' + self.variable + ':' + self.parse(func))

    def determine_variable(self,expression):
        for character in expression:
            if character in 'abcdefghijklmnopqrstuvwxyz':
                return character
        return '0'

    def parse(self, func):
        tokens = self.tokenify(func)
        # convert tokens into function that can be evaluated
       
    def tokenify(self, text):
        # convert function text into tokens
        # search for operators and operands
        tokens = []
        for i in range(0,len(text)):
            ch = text[i]
            if ch == '+' or ch == '*'
                tokens.append(Token(text[i],self.variable))
            temp = text[i] + text[i+1] + text[i+2] + text[i+3]
            expression = search_special_expressions(temp)
            if expression not == 'No match':
                tokens.append(Token(text[i],self.variable))
                i = i + 3

    def search_special_expressions(self,text):
        for expression in self.special_expressions:
            if text == expression:
                return expression
        return 'No match'


            





        
        

