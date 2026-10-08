import numpy as np

a = np.array(
    [[3., -7, -2, 2],
     [-3, 5, 1, 0],
     [6, -4, 0, -5],
     [-9, 5, -5, 12]])

# a = np.array(
#     [[2., 4, -1, 5, -2],
#      [-4, -5, 3, -8, 1],
#      [2, -5, -4, 1, 8],
#      [-6, 0, 7, -3, 1]])

l = np.eye(4)
u = np.copy(a)

print()
print("Original matrix:")
print("----------------")
print(a)

print()
print("Lower * Upper:")
print("--------------")
print(l @ u)

print()
print("Lower part:")
print("-----------")
print(l)

print()
print("Upper part:")
print("-----------")
print(u)
