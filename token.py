class Token:
	def __init__(self,text,indeterminate):
		self.value = text
		self.indeterminate = indeterminate
		self.type = self.find_type()
		self.len = len(text)

	def find_type(self):
		if self.value in '*+/-':
			return 'operator'
		if self.value in '0123456789':
			return 'operand'
		elif self.value == self.indeterminate:
			return 'operand'
		elif self.value in ['sin','cos','tan','exp']:
			print('trig operator')
			return 'operand'
		elif self.value == ')' or self.value == '(':
			return 'punc'
	def setArgs(self,exp):
		self.args = Token(exp,self.indeterminate)

		