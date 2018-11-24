class Token:
	def __init__(self,text,indeterminate):
		self.value = text
		self.indeterminate = indeterminate
		self.type = self.find_type()
		self.len = len(text)

	def find_type(self):
		if self.value in '0123456789':
			return 'num'
		elif self.value == self.indeterminate:
			return 'var'
		elif self.value == 'sin(x)' or self.value == 'cos(x)' or self.value == 'tan(x)':
			return 'trig'
		elif self.value == ')' or self.value == '(':
			return 'punc'
