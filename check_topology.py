from topologicalspace import Topological_Space
main = input('Enter the set for your topological space')
topology = input('Enter your topology')

T = Topological_Space(eval(main),eval(topology))

if(T.axiom1()):
    print("axiom 1 is satisfied")

if(T.axiom2()):
    print("axiom 2 is satisfied")

if(T.axiom3() ):
    print("axiom 3 is satisfied")