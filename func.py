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
        # convert tokens into function that can be evaluated
        tokens = self.tokenify(func)
        tokens = self.explicit_multiply(tokens)
        return self.evaluate(tokens)

    def evaluate(self,tokens):
        function = ''
        for token in tokens:
            if token.type == 'func_operand':
                arg_as_func = Function(token.args.value)
                function = "Math." +token.value + '(' + arg_as_func.func +")"
            else:
                function = function + token.value
        return function


    def explicit_multiply(self,tokens):
        i = 0
        while i < len(tokens)-1:
            if 'operand' in tokens[i].type and 'operand' in tokens[i+1].type:
                tokens.insert(i+1,Token('*',self.variable))
            if tokens[i].value == '(':
                tokens.insert(i,Token('*',self.variable))
                i = i + 1
            i = i + 1
        return tokens

    def search_special_expression(self,text,position):
        keyword_search = text[position:position + 3]
        #look for special expression
        if keyword_search in self.special_functions:
            # if the keyword is a special function , search for the arguments
            argIndex = position+4
            arg = ''

            while not text[argIndex] == ')':
                # until the end bracket is found , concantenate to characters to arg
                arg += text[argIndex]
                argIndex += 1
                # calcualte argIndex so we know where to continue from
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
                tokens.append(Token(text[i],self.variable))
            if ch == self.variable:
                tokens.append(Token(self.variable,self.variable))
            special_exp_data = self.search_special_expression(text,i)
            if special_exp_data.get('success'):
                tok = Token(special_exp_data.get('special_func'),self.variable)
                tok.setArgs(special_exp_data.get('argument'))

                tokens.append(tok)
                i = special_exp_data.get('nextIndex')
            i = i + 1
        return tokens
