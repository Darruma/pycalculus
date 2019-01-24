class UniversalRegisterMachine:
    def __init__(self):
        self.registers = []
        self.currentInstruction = 0
    def compute(self,program):
            current = program.instructions[self.currentInstruction]
            while current:
                self.execute(current)
        
    def execute(self,instruction):
        if instruction.name == 'Z':
            n = instruction.argument[0]
            self.registers[n] = 0
            self.currentInstruction = self.currentInstruction + 1
        elif instruction.name == 'S':
            n = instruction.argument[0]
            self.registers[n] = self.registers[n] + 1
            self.currentInstruction = self.currentInstruction + 1
        elif instruction.name == 'T':
            m = instruction.argument[0]
            n = instruction.argument[1]
            self.registers[n] = self.registers[m]
            self.currentInstruction = self.currentInstruction + 1 
        elif instruction.name == 'J':
            m = instruction.argument[0]
            n = instruction.argument[1]
            q = instruction.argument[2]
            if self.registers[m] == self.registers[n]:
                self.currentInstruction = q
            else:
                 self.currentInstruction = self.currentInstruction + 1
            
