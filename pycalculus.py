import math;
dx = 0.00001

def derivative_operator(f): # define a function that takes a function f
                            # and returns its derivative
    def fPrime(x):         
        value = (f(x + dx) - f(x)) / dx 
        return  "{:-1}\n".format(value)

    return fPrime


derivative = derivative_operator(lambda x:x *x)
print(derivative(10))


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

ig = integrate(lambda x:x * x)
print(ig(0,10))
    
    
        
        

