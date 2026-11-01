import time
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def solve(a, bs):
    out = []
    for b in bs:
        out.append(np.linalg.solve(a, b))
    return out

def lu_solve(a, bs):
    lu = sp.linalg.lu_factor(a)
    out = []
    for b in bs:
        out.append(sp.linalg.lu_solve(lu, b))
    return out

def inv_solve(a, bs):
    a_inv = np.linalg.inv(a)
    out = []
    for b in bs:
        out.append(a_inv @ b)
    return out

def benchmark_random(num_exp, step_size, num_eqs, process, low=-100, hi=100):
    rng = np.random.default_rng()

    x_axis = np.arange(1, num_exp + 1) * step_size
    y_axis = np.zeros(num_exp)

    for i in range(num_exp):
        x = x_axis[i]
        print(f'benchmarking: {x}')
        a = (hi - low) * rng.random((x, x)) + low
        bs = [(hi - low) * rng.random(x) + low for _ in range(num_eqs)]
        start = time.time()
        process(a, bs)
        y_axis[i] = time.time() - start

    return x_axis, y_axis

def banded_matrix(k):
    n = 2 * k
    d = 4 * np.eye(n)
    d -= np.eye(n, k=2) + np.eye(n, k=-2)
    a = [-1 * (n % 2) for n in range(1, n)]
    d += np.diag(a, k=-1) + np.diag(a, k=1)
    return d

def benchmark_banded(num_exp, step_size, num_eqs, process, low=-100, hi=100):
    rng = np.random.default_rng()

    x_axis = np.arange(1, num_exp + 1) * step_size
    y_axis = np.zeros(num_exp)

    for i in range(num_exp):
        x = x_axis[i]
        print(f'benchmarking: {x}')
        a = banded_matrix(x // 2)
        bs = [(hi - low) * rng.random(x) + low for _ in range(num_eqs)]
        start = time.time()
        process(a, bs)
        y_axis[i] = time.time() - start

    return x_axis, y_axis

# Experiment 1

# x_axis, y_axis = benchmark_random(100, 10, 100, solve)
# p1, = plt.plot(x_axis, y_axis, 'o', label="numpy.linalg.solve")

# x_axis, y_axis = benchmark_random(100, 10, 100, lu_solve)
# p2, = plt.plot(x_axis, y_axis, 'r^', label="scipy.linalg.lu_solve")

# plt.title('Solve vs. LU Solve')
# plt.xlabel('# rows/cols')
# plt.ylabel('time (sec)')
# plt.legend(handles=[p1, p2])
# plt.show()

# Experiment 2

# x_axis, y_axis = benchmark_random(300, 10, 100, inv_solve)
# p1, = plt.plot(x_axis, y_axis, 'o', label="numpy.linalg.inv")

# x_axis, y_axis = benchmark_random(300, 10, 100, lu_solve)
# p2, = plt.plot(x_axis, y_axis, 'r^', label="scipy.linalg.lu_solve")

# plt.title('Inverse Solve vs. LU Solve (Random)')
# plt.xlabel('# rows/cols')
# plt.ylabel('time (sec)')
# plt.legend(handles=[p1, p2])
# plt.show()

# Experiment 3

x_axis, y_axis = benchmark_banded(12, 1000, 100, inv_solve)
p1, = plt.plot(x_axis, y_axis, 'o', label="numpy.linalg.inv")

x_axis, y_axis = benchmark_banded(12, 1000, 100, lu_solve)
p2, = plt.plot(x_axis, y_axis, 'r^', label="scipy.linalg.lu_solve")

plt.title('Inverse Solve vs. LU Solve (Banded)')
plt.xlabel('# rows/cols')
plt.ylabel('time (sec)')
plt.legend(handles=[p1, p2])
plt.show()
