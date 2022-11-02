import math
test_f = lambda x: - 10 / pow(x, 3/2)
def composite_simpson_integral(f, a, b, n):
  if n%2 == 0:
    h = (b-a)/n
    XI_0 = f(a) + f(b)
    XI_1 = 0
    XI_2 = 0

    for i in range(n-1):
      X = a + i*h

      if i%2==0:
        XI_2 += f(X)
      else:
        XI_1 += f(X)
    XI = (XI_0 + 2*XI_2 +4*XI_1)
    return XI * (h / 3)
  else:
    return 'n should be even positive integer'

ans = composite_simpson_integral(test_f, 10, 5, 1000000)
print(ans)
