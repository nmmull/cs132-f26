import numpy as np
import sympy

def problem_4_1():
  v1 = np.array([1, -1])
  v2 = np.array([-1, 2])
  a = np.column_stack((v1, v2))
  num_pivs = np.linalg.matrix_rank(a)
  num_cols = a.shape[1]
  assert(num_pivs == num_cols)

problem_4_1()

def problem_4_2():
  v1 = np.array([1, -1, 2])
  v2 = np.array([-1, 4, -3])
  v3 = np.array([-3, 9, -8])
  a = np.column_stack((v1, v2, v3))
  num_pivs = np.linalg.matrix_rank(a)
  num_cols = a.shape[1]
  assert(num_pivs == 2)
  assert(num_cols == 3)
  assert(num_pivs != num_cols)
  assert(np.allclose(v1 - 2 * v2 + v3, np.zeros(3)))

problem_4_2()

def problem_4_7():
  v1 = np.array([2, 0, 0, 0])
  v2 = np.array([-3, -2, 0, 0])
  v3 = np.array([3, -2, 0, 0])
  v4 = np.array([8, 7, 6, 0])
  assert(np.allclose(3 * v1 + v2 - v3, np.zeros(4)))

problem_4_7()

def problem_5_10():
  T_v1 = np.array([-6, 3, -2, -10])
  T_v2 = np.array([-5, 1, -2, 9])
  T_v3 = np.array([8, -7, 6, 6])
  out = np.array([7, 4, -4, 9])
  assert(np.allclose(-3 * T_v1 - T_v2 - 2 * T_v3, out))

problem_5_10()

def problem_5_12():
  a = np.array([
    [3, -3],
    [2, 1],
  ])
  b = np.array([21, 8])
  v = np.linalg.solve(a, b)
  expected = np.array([5, -2])
  assert(np.allclose(v, expected))
  assert(np.allclose(a @ expected, b))

problem_5_12()

def problem_5_13():
  a = np.array([
    [1, -1, 2],
    [2, -1, 3],
    [-2, 2, -3],
  ])
  b = np.array([6, 12, -10])
  v = np.linalg.solve(a, b)
  expected = np.array([4, 2, 2])
  assert(np.allclose(v, expected))
  assert(np.allclose(a @ expected, b))

problem_5_13()

def problem_5_15():
  v1 = np.array([-3, 9, 5, -4])
  v2 = np.array([-9, -5, 0, -7])
  v3 = np.array([9, -1, -2, 4])
  u = np.array([30, 0, -7, 22])
  aug = sympy.Matrix(np.column_stack((v1, v2, v3, u)))
  # sympy.pprint(aug.rref()[0])
  assert(np.allclose(-v1 - 2 * v2 + v3, u))

  T_v1 = np.array([-4, 3, 4])
  T_v2 = np.array([0, 1, 2])
  T_v3 = np.array([3, -3, 7])
  expected = np.array([7, -8, -1])
  assert(np.allclose(-T_v1 - 2 * T_v2 + T_v3, expected))

problem_5_15()

def problem_4_22():
  v1 = np.array([1, 0, 0, 0])
  v2 = np.array([1, 4, 0, 0])
  v3 = np.array([3, -4, 3, 0])
  v4 = np.array([-2, 12, 3, 0])

  # part (a)
  assert(np.allclose(-9 * v1 + 4 * v2 + v3, v4))

  # part (b)
  a = np.column_stack((v2, v3, v4))
  num_pivs = np.linalg.matrix_rank(a)
  num_cols = a.shape[1]
  assert(num_pivs == num_cols)

problem_4_22()
