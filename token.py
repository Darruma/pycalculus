class Token:
    def __init__(self,text,var):
        self.val = text
        self.var = var

    def isOperand(self):
        if self.val in self.var or self.val in '0123456789':
            return True
        else:
            return False