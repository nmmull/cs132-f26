import numpy as np
import timeit

def triangle_count_naive(a):
    count = 0
    for i in range(a.shape[0]):
        for j in range(i, a.shape[0]):
            for k in range(j, a.shape[0]):
                count += a[i, j] * a[j, k] * a[i, k]
    return count

def triangle_count(a):
    return np.sum((a @ a) * a) / 6

def rand_undir_adj_mat(n):
    a = np.random.randint(0, 3, (n, n))
    sym = np.tril(a) + np.tril(a, -1).T
    np.fill_diagonal(sym, 0)
    return np.ceil(sym / 2)

a = rand_undir_adj_mat(100)
print()
print("--------------------")
print("Quick check that both functions count the same thing:")
print("--------------------")
print(f'triangle_count_naive result: {triangle_count_naive(a)}')
print(f'triangle_count result: {triangle_count(a)}')
print()

def bench(fn, k):
    setup = f'from __main__ import {fn}, rand_undir_adj_mat'
    for i in range(1,k + 1):
        test = f'{fn}(rand_undir_adj_mat({i * 100}))'
        result = timeit.timeit(test, setup=setup, number=5)
        print(f'{fn} on 5 random {i * 100} node graphs: {result:.3f} secs')

print("--------------------")
print("benchmarking triangle_count naive:")
print("--------------------")
bench('triangle_count_naive', 4)
print()
print("--------------------")
print("benchmarking triangle_count:")
print("--------------------")
bench('triangle_count', 40)
