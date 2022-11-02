from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
x = [ 0, 3, 5, 8, 13]
y = [0,225,383,623,993]

f = CubicSpline(x, y, bc_type=((1, 75), (1, 72)))
# 用表去查一階微分值，也就是那個時間對應的速度
# reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html
# 值得注意的是 bc_type = 'clamped' 去把 boundary condition 設成 'clamped'，但裏頭
# 設定的 'clamped' 是設成 S'(endpoint)=0，跟課本上 S'(endpoint)=f'(endpoint) 不同，
# 所以另外特別指定 boundary condition 為 ((1, 75), (1, 72))，1 指的是一階微分，後面
# 接的數字 75 和 72 分別指的是起點的一階微分和終點的一階微分。
print('The distance at 10 second is ', f(10), 'ft.')

x_new = np.linspace(0, 13, 100)
y_new = f(x_new)

plt.figure(figsize = (10,8))
plt.plot(x_new, y_new, 'b')
plt.plot(x, y, 'ro')
plt.title('Clamped Cubic Spline Interpolation')
plt.xlabel('t(s)')
plt.ylabel('Distance(ft)')
plt.show()
