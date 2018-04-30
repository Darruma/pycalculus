def axiom1(s,topology):
    x = 0
    for i in range(0,len(topology)):
        
        if topology[i] == s:
            
            x = x + 1
        
        if topology[i] == []:
            
            x = x + 1           
            
    if x == 2:
        print('Axiom 1 satisfied')
        return True
    else:
        print('Axiom 1 not satisfied')
        return False

def axiom2(s,topology):
        for i in range(0,len(topology)):
            for j in range(0,len(topology)):
                u = union(topology[i],topology[j])
                if elementOf(topology,u) == False:
                    print('Axiom 2 not satisfied')
                    return False
        print('Axiom 2 satisfied')
        return True

def axiom3(s,topology):
        for i in range(0,len(topology)):
            for j in range(0,len(topology)):
                inter = intersection(topology[i],topology[j])
                if elementOf(topology,inter) == False:
                    print('Axiom 3 not satisfied')
                    return False
        print('Axiom 3 satisfied')
        return True


def intersection(a,b):
    intersectionArray = []
    for x in range(0,len(a)):
        for y in range(0,len(b)):
            if a[x] == b[y]:
                intersectionArray.append(a[x])
    return intersectionArray

def union(a,b):
    unionArray = a
    for x in range(0,len(b)):
        if elementOf(a,b[x]) == False:
            unionArray.append(b[x])
    return unionArray
        
def elementOf(a,element):
    for i in range(0,len(a)):
        if a[i] == element:
            return True
    return False;

topology = []
open_set_str = input("Enter elements of open set with commas between each element ").split(",")
open_set = [int(val) for val in open_set_str]
print(open_set)

t_amount = int(input("How many elements of the topology are there? "))
for i in range(0,t_amount):
    topology_element_str = input("Enter elements of the topology (Type 'empty' for an empty set) ").split(",")
    
    if topology_element_str[0] == "empty":
        topology_element = []
    else:
        topology_element = [int(s) for s in topology_element_str]
    topology.append(topology_element)
    print(topology)
print("Checking axioms")
if(axiom1(open_set,topology) and axiom2(open_set,topology) and axiom3(open_set,topology)):
    print(open_set)
    print(topology)
    print("This is a topological space")



