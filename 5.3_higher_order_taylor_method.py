def taylor_method (T, a, b, N, y0):
    # T is Taylor expansion
    # a is the starting time, b , ending time
    # N is how many sections we divide the time
    # y0 is initial velocity
    h = ( b - a ) / N # h is step size
    t = a
    w = y0

    for i in range( 1 , N + 1 ):
        w = w + h * T ( w, h ) # from the formula (5.17) in textbook
        t = a + i * h
        
        rt = round(t, 1)
        rw = round(w, 5)
        print('i = ' + str(i) + ', t_' + str(i) + ' =', rt, ',w_' + str(i) + ' =', rw)

    return w
  
test_f = lambda v, x:-9.8-0.01818*v*abs(v)+(x/2)*(0.35633*abs(v)+6.61025*(10**-4)*v**3)+(x**2/6)*(0.35633-0.01943*v**2-3.60523*10**-5*v**3*abs(v))+(x**3/12)*(-0.03886*v+1.41325*10**-3*v**3+2.262712*10**-6*v**5)
taylor_method(test_f, 0, 1, 10, 8)
