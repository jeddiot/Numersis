import math
test_f = lambda x: - 10 / pow(x, 3/2)
def romberg_integration(f, a, b, n):
  h = b - a
  R = [ [ 0 for i in range(n) ] for j in range(n) ]
  R[0][0] = (h / 2) * ( -10 / f(a) + f(b))
  return R


def summation(f, x, n):
  temp_sum = 0
  for i in range(n):
    temp_sum += f(x)
    return temp_sum

temp = romberg_integration(test_f, 10, 5, 4)

print(temp)

import numpy
test_f = lambda x: - 10 / pow( x, 3 / 2)

def trapezoidal(f, a, b, n):
  h = float(b - a) / n
  s = 0.0
  s += f(a)/2.0
  for i in range(1, n):
    s += f(a + i*h)
  s += f(b)/2.0
  return s * h

def romberg(f, a, b, n):
  RArray = numpy.zeros(shape = ( n, n ))
  for i in range( 0, n ):
    RArray[ i, 0 ] = trapezoidal( f, a, b, pow(2, i) )
  for k in range( 1, n ):
    for j in range(1, k+1):
      RArray[k,j] = RArray[ k, j-1 ] + (( RArray[ k, j-1 ] - RArray[ k-1, j-1 ]) / (pow(4,j) - 1))
  return RArray

ans =  romberg(test_f, 10, 5, 4)
print(ans)  
print(ans[-1][-1])
