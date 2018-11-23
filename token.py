class Token:
    def __init__(self,text,var):
        self.special_expression = ['sin(x)','cos(x)','tan(x)']
        self.val = text
        self.var = var

    def isOperand(self):
        if self.val in self.var or self.val in '0123456789' ir self.val in special_expression:
            return True
        else:
            return False
