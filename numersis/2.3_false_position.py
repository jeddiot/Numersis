import math 

def func( t ):
    return 290228 * math.exp(-0.65123 * math.exp(-0.0302 * t))

def dfunc( t ):
    return 5707.956449 * math.exp(-0.65123 * math.exp(-0.0302 * t) - 0.0302 * t)
 
# Function to find the root
def NewtonRaphson( t ):
    h = func(t)/dfunc(t)
    N = int(input("Enter a number: "))
    tol = abs(t - N)
    while tol >= 0.1:
        h = func(t)/dfunc(t)
        t -= h
        # x(i+1) = x(i) - f(x) / f'(x)
    func(t)

def main():
    t0 = 28 # Initial values assumed
    NewtonRaphson(t0)
    print("The population is : ", func(t))

if __name__ == '__main__': main()
