import numpy as np

# invertible matrix
a = np.array(
    [[1., 2, 5],
     [0, 1, 3],
     [1, 0, 0]])

# inverse of a
ainv = np.linalg.inv(a)

# a with the identity on the right + (plus extra column for b)
aid = np.hstack([a, np.eye(3), np.array([[5, -1, 6]]).T])

# row reductions
aid[2] -= aid[0]
aid[2] += 2 * aid[1]
aid[0] -= 5 * aid[2]
aid[1] -= 3 * aid[2]
aid[0] -= 2 * aid[1]

print()
print("------------------------------")
print("The matrix [ A I ]:")
print("------------------------------")
print(aid[:,:6])

print()
print("------------------------------")
print("Augmented matrix for Ax = e1:")
print("------------------------------")
print(aid[:,:4])

print()
print("------------------------------")
print("Augmented matrix for Ax = e2:")
print("------------------------------")
print(aid[:,[0, 1, 2, 4]])

print()
print("------------------------------")
print("Augmented matrix for Ax = e3:")
print("------------------------------")
print(aid[:,[0, 1, 2, 5]])

print()
print("------------------------------")
print("Augmented matrix for Ax = b:")
print("------------------------------")
print(aid[:,[0, 1, 2, 6]])

print()
print("------------------------------")
print("A^{-1}:")
print("------------------------------")
print(aid[:,3:6])

print()
print("------------------------------")
print("A^{-1} b:")
print("------------------------------")
print(aid[:,3:6] @ np.array([[5, -1, 6]]).T)
