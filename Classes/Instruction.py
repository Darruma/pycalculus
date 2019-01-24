

class Instruction:
    def __init__(self):
          self.name = ''
          self.arguments = []

    def __str__(self):
        readable = self.name + '('
        for i in self.arguments:
            readable = readable + i + ','
        return readable[:readable.length - 1] + ')'


