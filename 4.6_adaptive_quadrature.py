import math as mt
fun = lambda x: (1/5)*(mt.cos(2*x)- mt.cos(3*x))

def compositeSimpson(fun, a, b, n):
    if n%2 is not 0:
        return None
    h = (b-a)/n
    first = fun(a)
    last = fun(b)

    x = a
    sum = 0
    for i in range(n-1):
        x += h
        value = fun(x)
        if i%2 == 0:
            sum += 4*value
        else:
            sum += 2*value
    total = (h/3)*(first + sum + last)
    return total
    
    def adaptiveCompositeSimpson(fun, a, b, tol):
  stack = []
  stack.append(a)
  stack.append(b)
  I = 0
  iter = 0
  while len(stack) is not 0:
      bb = stack.pop()
      aa = stack.pop()
      I1 = compositeSimpson(fun, aa, bb, 2)
      m = (aa + bb)/2
      I2 = compositeSimpson(fun, aa, m, 2) + compositeSimpson(fun, m, bb, 2)
      iter += 1
      if abs(I2 - I1)/15 < ((bb - aa)*tol):
            I += I2
      else:
          stack.append(m)
          stack.append(bb)
          stack.append(aa)
          stack.append(m)
      if iter > 1000:
          break
  return I

print(adaptiveCompositeSimpson(fun, 0, 2*mt.pi, 1e-4))
