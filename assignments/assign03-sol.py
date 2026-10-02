import numpy as np

def problem_2_2():
  v1 = np.array([-1, 1, 10])
  v2 = np.array([-6, 3, 7])
  v3 = np.array([8, 9, 1])
  sol = 4 * v1 - 5 * v2 + 9 * v3
  print('2.2')
  print('-----')
  print(sol)

problem_2_2()

def problem_2_13():
  aug = np.array([
    [1., -2, -8, 16],
    [-2, 5, 21, -38],
    [0, 2, 10, -12],
  ])
  aug[2] /= 2
  aug[1] += 2 * aug[0]
  aug[2] -= aug[1]
  aug[0] += 2 * aug[1]
  print('2.13')
  print('-----')
  print(aug)
  print()
  print(f'x1 = {aug[0, 3]} - ({aug[0, 2]})x3')
  print(f'x2 = {aug[1, 3]} - ({aug[0, 2]})x3')
  print('x3 is free')

print()
problem_2_13()

def problem_3_1():
  a = np.array([
    [-10, 6, 2, 8],
    [1, 3, 4, 5],
    [0, -2, 0, -9],
  ])
  v = np.array([4, -5, 3, 1])
  print('3.1')
  print('-----')
  print(a @ v)

print()
problem_3_1()

def problem_3_3():
  a = np.array([
    [6, 1, -8, -3],
    [5, 0, -9, -4],
  ])
  v = np.array([-6, 2])
  print('3.3')
  print('-----')
  try:
    a @ v
  except ValueError as e:
    print("not possible")
    print(e)

print()
problem_3_3()

def problem_3_9():
  a = np.array([[1., 2], [2, 5]])
  num_rows = a.shape[0]
  num_pivs = np.linalg.matrix_rank(a) # we'll see later why this works
  print('3.9')
  print('-----')
  print(a)
  print(f'number of rows: {num_rows}')
  print(f'number of pivots: {num_pivs}')
  if num_rows == num_pivs:
    print('full span')

print()
problem_3_9()

def problem_3_12():
  a = np.array([
    [1., 5, -1],
    [2, -4, 5],
    [4, 0, 6],
  ])
  num_rows = a.shape[0]
  num_pivs = np.linalg.matrix_rank(a)
  print('3.12')
  print('-----')
  print(a)
  print(f'number of rows: {num_rows}')
  print(f'number of pivots: {num_pivs}')
  if num_rows > num_pivs:
    print('not full span')

print()
problem_3_12()

def problem_3_31():
  a = np.eye(6) + np.eye(6, k=1)
  e6 = np.eye(6, 1, k=-5)
  aug = np.hstack([a, e6])
  aug[4] -= aug[5]
  aug[3] -= aug[4]
  aug[2] -= aug[3]
  aug[1] -= aug[2]
  aug[0] -= aug[1]
  print('3.31')
  print('-----')
  print(aug[:,6])

print()
problem_3_31()
