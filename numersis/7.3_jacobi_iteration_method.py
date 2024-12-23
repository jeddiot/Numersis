from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(a,x,b):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    n = len(a)  
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(a)
    R = a - diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(0,n):
        x = (b - dot(R,x)) / D
    return x

# int(input())input as number of variable to be solved                
n = 4                              
a = []                            
b = []        
# initial solution depending on n(here n=4)                     
x = [0, 0, 0, 0]                        
a = [[10, -1, 2, 0],[-1, 11, -1, 3],[2, -1, 10, -1],[0, 3, -1, 8]]
b = [6, 25, -11, 15]
print(x)
  
#loop run for m times depending on m the error value
for i in range(0, 25):            
    x = jacobi(a, x, b)
    #print each time the updated solution
    print(x)   
