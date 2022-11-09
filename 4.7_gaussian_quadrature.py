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

# drivers code
def fun(x):
    return np.exp(x**2)

for i in range(1,10):  
    print(gauss(fun,0,1,i))

# another version of gauss quadrature, modified from matlab code by Peter J. Acklam.

def gaussquad(*args): # save the variables in a tuple called "args", in the order of n, b, a
    u = []
    vtsort = []
    a = np.zeros((args[0], args[0]))
    k = 0

    if len(args) == 1:
        # gaussquad(N) assumes the interval is from -1 to 1.
        ba = (1,-1)
        args += ba
    elif len(args) == 2:
        # gaussquad(N, C) assumes the interval is from 0 to C.
        b = (0,)
        args += b

    # Same as in matlab, A = diag(u, -1) + diag(u, 1), but faster (no addition).
    for i in range(args[0] - 1):
        u.append((i+1)/np.sqrt(4*(i+1)**2 - 1))
        a[i + 1,k] = u[i]
        a[k,i + 1] = u[i]
        k += 1

    # Find the base points X and weight factors W for the interval [-1,1].
    vl, vt = np.linalg.eig(np.array(a)) # vl = eigen values of a, the column of vt = eigen vectors of a.
    vlsort = np.sort(vl) # sorted eigen value. Ndarray.
    for i in np.argsort(vl): # get the index for sorting vl
        vtsort.append(vt[0,i]) # get the first element for each eigen vectors
    w = 2 * np.transpose(vtsort)**2
    
    # Linearly transform from [-1,1] to [a,b].
    vlsort = (args[1] - args[2]) / 2 * vlsort + (args[2] + args[1]) / 2

    if len(args) != 0:
        xx = np.transpose(vlsort)
        ww = np.transpose(vtsort)
        return

    return [xx, ww]
