import numpy as np
import scipy as sp

a = np.array(
    [[0.95, 0.03],
     [0.05, 0.97]])

b = np.array(
    [[0.7, 0.1, 0.3],
     [0.2, 0.8, 0.3],
     [0.1, 0.1, 0.4]])

def rref(a):
    ef = np.vectorize(lambda x: 0. if np.isclose(x, 0.) else x)(sp.linalg.lu(a)[2])
    for i in range(ef.shape[0]):
        lead = next(iter(np.nonzero(ef[i])[0]), None)
        if lead is not None:
            ef[i] /= ef[i, lead]
            for k in range(i):
                ef[k] -= ef[i] * ef[k, lead]
    return ef


print(rref(a - np.eye(2)))
print()
print(f'x1 = {0.6 * (1 / 1.6)}')
print(f'x2 = {1/1.6}')

# print(rref(b - np.eye(3)))
# sol = np.array(sp.linalg.null_space(b - np.eye(3))[:,0])
# sol /= sum(sol)
# print(sol)
