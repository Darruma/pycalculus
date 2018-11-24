import re
from token import Token
class Function:
    def __init__(self, func):
        self.special_expressions = ['sin(x)','cos(x)','tan(x)']
        self.variable = self.determine_variable(func)
        self.func = self.parse(func)
    def determine_variable(self,expression):
        return 'x'

    def parse(self, func):
        tokens = self.tokenify(func)
        return list(map(lambda token : token.value,tokens))
        # convert tokens into function that can be evaluated

    def search_special_expressions(self,text):
        for expression in self.special_expressions:
            if text == expression:
                return expression
        return 'No match'
       
    def tokenify(self, text):
        # convert function text into tokens
        # search for operators and operands
        tokens = []
        i = 0
        while i < len(text):
            temp = ''
            ch = text[i]
            if ch == "+" or ch == "*" or ch == self.variable:
                tokens.append(Token(text[i],self.variable))
            if i + 6 <= len(text):
                temp = text[i] + text[i+1] + text[i+2] + text[i+3] + text[i+4] + text[i+5]
            expression = self.search_special_expressions(temp)
            if not expression == 'No match':
                tokens.append(Token(expression,self.variable))
                i = i + 5
                print(i)
            i = i + 1 
        return tokens

    


            





        
        

