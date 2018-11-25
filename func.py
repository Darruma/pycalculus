import re
from token import Token
class Function:
    def __init__(self, func):
        self.special_functions = ['sin','cos','tan','exp']
        self.variable = self.determine_variable(func)
        self.func = self.parse(func)

    def determine_variable(self,expression):
        return 'x'

    def parse(self, func):
        tokens = self.tokenify(func)
        print(list(map(lambda token : token.value,tokens)))
        tokens = self.add_multiples(tokens)
        return list(map(lambda token : token.value,tokens))
        # convert tokens into function that can be evaluated

    def add_multiples(self,tokens):
        for i in range(len(tokens)):
            if tokens[i].type == 'operand' and tokens[i+1].type == 'operand':
                tokens.insert(i+1,Token('*',self.variable))
        return tokens

    def search_special_expressions(self,text,position):
        for index in range(position,len(text)):
            keyword_search = text[index:index + 3]
            if keyword_search in self.special_functions:
                argIndex = index+4
                arg = ''
                while not text[argIndex] == ')':
                    arg += text[argIndex]
                    argIndex += 1
                return {
                    'success':True,
                    'special_func':keyword_search,
                    'argument':arg,
                    'nextIndex':argIndex
                 }
        return {
            'success':False
        }
       
    def tokenify(self, text):
        # convert function text into tokens

        tokens = []
        i = 0
        while i < len(text):
            temp = ''
            ch = text[i]
            if ch == "+" or ch == "*" or ch == self.variable or ch in '0123456789()': 
                tokens.append(Token(text[i],self.variable))
            special_exp_data = self.search_special_expressions(text,i)
            print(special_exp_data)
            if special_exp_data.get('success'):
                tok = Token(special_exp_data.get('special_func'),self.variable)
                tok.setArgs(special_exp_data.get('argument'))
                tokens.append(tok)
                i = special_exp_data.get('nextIndex')
            i = i + 1 
        return tokens



            





        
        

