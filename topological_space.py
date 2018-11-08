class Topological_Space:
    def __init__(self,topology,main):
        self.main = main
        self.topology = topology
    
    def axiom1(self):
        return(self.main in topology and [] in topology)
    
    def axiom2(self):
        for i,j in topology:
            if(!i.intersection(j) in topology):
                return false
        return true
        
    def axiom3(self):
        for i,j in topology:
            if(!i.union(j) in topology):
                return false