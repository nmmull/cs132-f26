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

u[1] += u[0]

e = np.eye(4)
e[1] += e[0]

l = l @ np.linalg.inv(e)

u[2] -= 2 * u[0]

e = np.eye(4)
e[2] -= 2 * e[0]

l = l @ np.linalg.inv(e)

u[3] += 3 * u[0]

e = np.eye(4)
e[3] += 3 * e[0]

l = l @ np.linalg.inv(e)

u[2] += 5 * u[1]
l[2, 1] = -5

u[3] -= 8 * u[1]
l[3, 1] = 8

u[3] -= 3 * u[2]
l[3, 2] = 3

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
