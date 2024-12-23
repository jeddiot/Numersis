import math as mt
import pandas as pd
import numpy as np

def simpson_double_integral(f, m, n):
    #let a = 0, b = 1, c = 0, d = mt.sqrt(1-x**2)
    if m % 2 == 0 and n % 2 == 0:
        h = 1/n
        J_1 = 0; J_2 = 0; J_3 = 0 # J_1 is end terms; J_2 is even terms; J_3 is odd terms

        for i in range(n): # integrate by Composite Simpson's method from a to b
            x = i*h
            HX = (mt.sqrt(1-x**2))/m
            K_1 = f(x,0)+f(x,mt.sqrt(1-x**2)) # K_1 is end terms
            K_2 = 0; K_3 = 0 # K_2 is even terms; K_3 is odd terms
      
            for j in range(1,m): # integrate from c(x) to d(x)
                y = 0 + j*HX
                Q = f(x,y)

                if j%2 == 0:
                    K_2 += Q
                else:
                    K_3 += Q
            L =  ((K_1+2*K_2+4*K_3)*HX)/3

            if i==0 or i==n:
                J_1 += L
            elif i%2==0:
                J_2 += L
            else:
                J_3 += L
        J = h*(J_1+2*J_2+4*J_3)/3
        return J
    else:
        return 'n should be even positive integer'
        
f = lambda x, y: mt.exp(-(x**2+y**2))
x_f = lambda x, y: x*mt.exp(-(x**2+y**2))
y_f = lambda x, y: y*mt.exp(-(x**2+y**2))

double_f = simpson_double_integral(f, 14, 14)
double_x_f = simpson_double_integral(x_f, 14, 14)
double_y_f = simpson_double_integral(y_f, 14, 14)
print(double_x_f/double_f, double_y_f/double_f)
