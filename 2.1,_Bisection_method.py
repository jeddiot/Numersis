%matplotlib inline
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    return 10 * (0.5 * 3.141592658 - math.asin(x) - x * (1-x**2)**(1/2)) - 12.4

def bisection(a, b, tol):
  xl = a
  xr = b
  while (np.abs(xl - xr) >= tol):
    c = (xl + xr) / 2.0
    prod = f(xl) * f(c)
    if prod > tol:
      xl = c
    else:
      if prod < tol:
        xr = c
  return c

h = bisection(0, 1, 1e-3)
depth_water = 1 - bisection(0, 1, 1e-3)
print ("Bisection gives root at x = ", h)
print ("And the depth of water is", depth_water)
