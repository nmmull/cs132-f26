import numpy as np

# Gaussian elimination for 2 by n matrices
def gauss(A):
    A[1,:] -= A[1,0] / A[0,0] * A[0,:]
    if not np.isclose(A[1,1], 0):
        A[1,:] /= A[1, 1]
        A[0,:] -= A[0, 1] * A[1,:]
        A[0,:] /= A[0, 0]
    else:
        A[1,1] = 0
        A[1,2] = 1
        A[0,2] = 0

# carfully chosen very large number
c = 100000000000000010241

B = np.array([
    [1/7, 1/70, 1],
    [  1, 1/10, 2],
])

gauss(B)
print()
print("Solving well-conditioned problem with NumPy (gives correct solution):")
print()
print(B)

C = np.array([
    [1/7, c/70, 1],
    [  1, c/10, 2],
])

gauss(C)
print()
print("Solving ill-conditioned problem with NumPy (gives incorrect solution):")
print()
print(C)
