t = [1.00, 1.01, 1.02, 1.03, 1.04]
i = [3.10, 3.12, 3.14, 3.18, 3.24]
di = [0, 0, 0, 0, 0]

def three_midpoint_differentiate(x0, h):
    vprime = 0.142 * (i[t.index(x0 + h)] - i[t.index(x0 - h)]) / (2 * h)
    return vprime
        
def three_endpoint_differentiate(x0, h):
    vprime = 0.142 * (-3 * i[t.index(x0)] + 4 * i[t.index(x0 + h)] - i[t.index(x0 + 2 * h)])/(2 * h)
    return vprime
    
    v = [0, 0, 0, 0, 0]
di[0] = three_endpoint_differentiate(t[0], 0.01)/0.142
di[1] = three_midpoint_differentiate(t[1], 0.01)/0.142
di[2] = three_midpoint_differentiate(t[2], 0.01)/0.142
di[3] = three_midpoint_differentiate(t[3], 0.01)/0.142
di[4] = three_endpoint_differentiate(t[4], -0.01)/0.142
#python 不能 float 互乘

v[0] = 0.98 * di[0] + 0.142 * i[0]
v[1] = 0.98 * di[1] + 0.142 * i[1]
v[2] = 0.98 * di[2] + 0.142 * i[2]
v[3] = 0.98 * di[3] + 0.142 * i[3]
v[4] = 0.98 * di[4] + 0.142 * i[4]
print(v)
