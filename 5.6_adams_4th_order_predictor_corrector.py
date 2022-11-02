def AB_Predictor_Corrector(def_fn, a, b, ya, N):
    f = def_fn          #intakes function to method to approximate 
    h = (b-a)/N         #creates step size based on input values of a, b, N 
    t = np.arange(a, b+h, h) #array intialized to hold mesh points t
    y = np.zeros((N+1,)) #array to hold Midpoint Method approximated y values
    y[0] = ya           #intial condition 
    
    #using RK4 to obtain the first 3 points
    for i in range(0,N):
        if i in range(0,3):
            k1 = h * f(t[i],y[i])
            k2 = h * f(t[i] + (h/2.0), y[i] +(k1/2.0))
            k3 = h * f(t[i] + (h/2.0), y[i] + (k2/2.0))
            k4 = h * f(t[i] + h, y[i] + k3)
        
            y[i + 1] = y[i] + (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
            
        else:
             y[i + 1] = y[i] + h*(55.0 * f(t[i],y[i]) - 59.0 * f(t[i-1],y[i-1]) + 37.0 * f(t[i-2],y[i-2]) - 9.0 * f(t[i-3],y[i-3]))/24.0
             y[i + 1] = y[i] + h*(9.0 * f(t[i+1], y[i + 1]) + 19.0 * f(t[i],y[i]) - 5.0 * f(t[i-1],y[i-1]) + f(t[i-2],y[i-2]))/24.0
    lis = []
    for i in range(-10, 0):
        lis.append((t[i], y[i]))
    return lis
    
import numpy as np
test_f = lambda y, self: 0.0439*np.log(12000/(y+1e-9))*y
# because it occurs divided by 0, so we add a small number to the y at the denominator
AB_Predictor_Corrector(test_f, 0, 275, 4000, 550)
