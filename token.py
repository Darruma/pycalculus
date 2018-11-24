class Token:
    def __init__(self,text,indeterminate):
    	self.indeterminate = indeterminate
        self.value = text
    	self.type = self.find_type()

    def find_type(self):
    	if self.value in '0123456789':
    		return 'num'
    	if self.value == self.type:
    		return 'var'
    	if self.value == 'sin(x)' or self.value == 'cos(x)' or self.value == 'tan(x)':
    		return 'trig'
    	if self.value == '(' or self.value == ')':
    		return 'punc'

