import math;
dx = 0.00001

def derivative_operator(f): # define a function that takes a function f
                            # and returns its derivative
    def fPrime(x):         
        value = (f(x + dx) - f(x)) / dx 
        return  "{:-1}\n".format(value)

    return fPrime





def integrate(f): # takes a function f 

    def integral(a,b): # returns a function which integrates between a and b
        rectangleWidth = (b - a) / 1000
        sum = 0;
        index = a
        while(index <= b):
            sum+= f(index) * rectangleWidth
            index += rectangleWidth
            
            
        return int(sum)
    return integral

choice = input('Type I for integration and D for differentiation')
func = input("enter function")

if(choice=='I')
{
    lower = input('input lower bound for integral')
    higher = input('input higher bound for integral')
    print(integrate(eval(func))(lower,higher))
}
if(choice == 'D')
{
    point = input('input the point at which you want to find the derivative');
    print(derivative_operator(eval(func))(point))
}