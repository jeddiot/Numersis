import numpy
import math
def euler_method(f, a, b, N, y0):
    # f is function, here is di/dt
    # a is the starting time, b, ending time
    # N is how many sections we dividie time
    # y0 is the initial current
    h = ( b - a ) / N # h is step size
    t = a
    w = y0

    for i in range( 1 , N + 1 ):
        w = w + h * f ( t , w ) # from the formula  (5.8)
        t = a + i * h
        
        rt = round(t, 1)
        rw = round(w, 5)
        print('j' + str(i) + ',t_' + str(i) + '=', rt, ',w_' + str(i) + '=', rw)

    return w
test_f = lambda t, it: (math.exp(-0.06*math.pi*t))*(0.73574*math.sin(2*t)-1.20238*math.cos(2*t)) #上面寫的公式 (6)
# ref.1: https://ithelp.ithome.com.tw/articles/10250101
# ref.2: https://blog.finxter.com/solved-typeerror-method-takes-1-positional-argument-but-2-were-given/
ans = euler_method(test_f, 0, 10, 100, 0)
print(ans)
