import numpy as np

def gauss(f,a,b,n): # f is the function, a and b indicates the interval to integrate [a,b], n is th degree of the Legendre polynomials
    half = float(b-a)/2.
    mid = (a+b)/2.
    [x,w] = np.polynomial.legendre.leggauss(n)
    result =  0.
    for i in range(n):
        result += w[i] * f(half*x[i] + mid)
    result *= half
    return result
  
def fun(x):
    return np.exp(x**2)

for i in range(1,10):  
    print(gauss(fun,0,1,i))
