import numpy as np
from scipy.linalg import ldl
a = np.array([[2, -1, 3], [0, 2, 0], [0, 0, 1]])
lu, d, perm = ldl(a, lower=0) # Use the upper part
lu
# ref: https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.ldl.html
