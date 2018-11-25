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
        tokens = self.explicit_multiply(tokens)
        return list(map(lambda token : token.value,tokens))
        # convert tokens into function that can be evaluated

    def explicit_multiply(self,tokens):
        for i in range(len(tokens)-1):
            if tokens[i].type == 'operand' and tokens[i+1].type == 'operand':
                tokens.insert(i+1,Token('*',self.variable))
        return tokens

    def multiply_brackets(self,tokens):
        pass

    def search_special_expression(self,text,position):
        keyword_search = text[position:position + 3]
        if keyword_search in self.special_functions:
            argIndex = position+4
            print('argument index:'+text[argIndex])
            arg = ''
            while not text[argIndex] == ')':
                arg += text[argIndex]
                argIndex += 1
                return {
                    'success':True,
                    'special_func':keyword_search,
                    'argument':arg,
                    'nextIndex':argIndex+1
                 }
        return {
        'success':False
        }
        
       
    def tokenify(self, text):

        tokens = []
        i = 0
        while i < len(text):
            temp = ''
            ch = text[i]
            if ch in '+-/*012345678()^':
                print('added token:' + ch)
                tokens.append(Token(text[i],self.variable))
            if ch == self.variable:
                print('added x')
                tokens.append(Token(self.variable,self.variable))
            special_exp_data = self.search_special_expression(text,i)
            print(i)
            print(special_exp_data)
            if special_exp_data.get('success'):
                print(special_exp_data.get('special_func'))
                tok = Token(special_exp_data.get('special_func'),self.variable)
                tok.setArgs(special_exp_data.get('argument'))
                tokens.append(tok)
                i = special_exp_data.get('nextIndex')
            i = i + 1 
        return tokens



            





        
        

