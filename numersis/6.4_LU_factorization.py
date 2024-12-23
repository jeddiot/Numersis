import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = scipy.array([ [1, 2, -1], [2, 4, 0], [0, 1, -1] ])
P, L, U = scipy.linalg.lu(A)

print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)
