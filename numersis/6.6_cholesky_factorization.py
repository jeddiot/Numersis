import numpy as np
A = np.array([[1,-2j],[2j,5]])
print(A)
L = np.linalg.cholesky(A)
print(L)
# ref: https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html
