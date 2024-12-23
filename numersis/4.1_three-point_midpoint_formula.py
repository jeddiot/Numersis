from sympy import *
import numpy as np
x = Symbol('x')
y = x*exp(x)
# 第一步，寫出函數 f(x) = x*exp(x)。

deriv1 = y.diff(x)
deriv2 = deriv1.diff(x)
deriv3 = deriv2.diff(x)
deriv4 = deriv3.diff(x)
deriv5 = deriv4.diff(x)
print("The 1st derivative is", deriv1, "\nThe 2nd derivative is", deriv2, "\nThe 3rd derivative is", deriv3)
# 第二步，先找到函數微分的形式，f'、f^(2) 以及 f^(3)。

d = lambda x: x*np.exp(x)
d1 = lambda x: x*np.exp(x)+ np.exp(x)
d3 = lambda x: x*np.exp(x)+ 3*np.exp(x)
d5 = lambda x: x*np.exp(x)+ 5*np.exp(x)
# 第三步，再把找到的函數微分形式寫成可以計算的資料結構。
def inf(x0, h):
  return 1/(2*h)*(d(x0+h)-d(x0-h))-(h**2)/6*d3(x0)-(h**4)/120*d5(x0)
# 第四步，寫出 Three-Point Midpoint Formula 到 O(h^4) 的公式。
print("Approximations of order O(h4) for f’(2.0) using h = 0.2 is", inf(2.0, 0.2))
print("Approximations of order O(h4) for f’(2.0) using h = 0.1 is", inf(2.0, 0.1))
# 第五步，帶入數字。
