class Topological_Space:
    def __init__(self,topology,main):
        self.main = main
        self.topology = topology
    
    def axiom1(self):
        return(self.main in self.topology and [] in self.topology)
    
    def axiom2(self):
        for i,j in self.topology:
            if i.intersection(j) in self.topology == False:
                return False
        return True
        
    def axiom3(self):
        for i,j in self.topology:
            if i.union(j) in self.topology == False:
                return False
        return True
