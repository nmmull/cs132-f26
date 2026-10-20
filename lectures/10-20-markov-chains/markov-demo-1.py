import numpy as np

a = np.array(
    [[0.95, 0.03],
     [0.05, 0.97]])

p = np.array([600000,400000])
p2 = np.array([200000, 800000])
p3 = np.array([1000000,0])
p4 = np.array([8000, 3100])

for i in range(10):
    print()
    print(f'a to the {10 ** i} times p: ')
    print(np.linalg.matrix_power(a, 10 ** i) @ p)
