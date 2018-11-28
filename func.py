import re
from token import Token
class Function:
    def __init__(self, func):
        self.special_functions = ['sin','cos','tan','exp']
        self.variable = self.determine_variable(func)
        self.func = self.parse(func)

    def determine_variable(self,expression): #rewrite to work with functions of more than one variable
        return 'x'

    def __add__(self,other):
        self.func + '+' + other.func
    def __mul__(self,other):
        self.func+ '*' + other.func
    def __mul__(self,other):
        self.func + '-' + other.func

    def compose(self,other):
        composed = ''
        for i in range(len(self.func)):
            if self.func[i] == self.variable:
                composed = composed + other.func
            else:
                composed = composed + self.func[i]
        return composed
    def parse(self, func):
        # convert tokens into function that can be evaluated
        tokens = self.tokenify(func)
        tokens = self.explicit_multiply(tokens)
        return self.evaluate(tokens)

    def evaluate(self,tokens):
        function = ''
        for token in tokens:
            if token.value == '^':
                function = function + '**';
            elif token.type == 'func_operand':
                arg_as_func = Function(token.args.value)
                function = "Math." +token.value + '(' + arg_as_func.func +")"
            else:
                function = function + token.value
        return function

    def explicit_multiply(self,tokens):
        i = 0
        print(tokens)
        while i < len(tokens)-1:
            print(tokens[i].type);
            if 'operand' in tokens[i].type and 'operand' in tokens[i+1].type:
                tokens.insert(i+1,Token('*',self.variable))
            if tokens[i].value == '(':
                tokens.insert(i,Token('*',self.variable))
                i = i + 1
            i = i + 1
        return tokens

    def search_special_expression(self,text,position):
        keyword_search = text[position:position + 3]
        if keyword_search in self.special_functions:
            # if the keyword is a special function , search for the arguments
            argIndex = position+4 #special functions have 3 characters , change this for extra functions
            arg = ''
            parens = 1 
            while not parens == 0: # if the parens are equal to zero that means we found the end of the expression
                # Check for balanced parens to allow nested expressions.
                if text[argIndex] == '(':
                    parens = parens + 1
                elif text[argIndex] == ')':
                    if parens == 1: # if we are at the end of the expression dont add the final end paren
                        break
                    else:
                        parens = parens - 1
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
        # convert a input string into a set of tokens that can be used to create a function.
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
