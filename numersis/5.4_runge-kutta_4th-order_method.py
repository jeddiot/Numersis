import math
def runge_kutta(f,a,b,N,x0):
    # f is the function
    # a is the starting time, b , the ending time.
    # N is how many sections we devide the time
    # x0 is the initial height
    h = (b-a)/N # h is the step size
    t, w = a, x0
    print('Initial Value (t0,y0) = ',t,',',w)

    for i in range(1, N + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * f(t, w)
        k2 = h * f(t + 0.5 * h, w + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, w + 0.5 * k2)
        k4 = h * f(t + h, w + k3) # from the formula in p.288 in the textbook

        t = a + i*h
        w += (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        
        rt = round(t, 1)
        rw = round(w, 5)
        print('i = ' + str(i) + ', t_' + str(i) + ' =', rt, ',w_' + str(i) + ' =', rw)
    return t, w
  
test_f = lambda it, x : - 0.006 * math.sqrt(64.2)* x**(-1.5) 
runge_kutta(test_f, 0, 1600, 80, 8)

import numpy as np
test_f = lambda y, self: 0.0439*np.log(12000/(y+1e-4))*y
runge_kutta(test_f, 0, 1.5, 3, 4000)
