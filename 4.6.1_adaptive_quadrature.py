import numpy as np
from matplotlib import pyplot as plt
import math as mt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

f = lambda t: 2*(np.cos(2*t)-np.cos(np.sqrt(9/2)*t))

t = np.linspace(0, 2*mt.pi, 100)

plt.plot(t, f(t), color='red')
plt.show()

import math as mt
from scipy import integrate
testf = lambda t: 2*(np.cos(2*t)-np.cos(np.sqrt(9/2)*t))
integrate.quadrature(testf, 0, mt.pi, args=(), tol=1e-04, rtol=1e-04, maxiter=50, vec_func=True, miniter=1)
# ref: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quadrature.html#scipy.integrate.quadrature

testf= lambda x: (1/5)*(np.cos(2*x)- np.cos(3*x))
integrate.quadrature(testf, 0, mt.pi, args=(), tol=1e-04, rtol=1e-04, maxiter=50, vec_func=True, miniter=1)
