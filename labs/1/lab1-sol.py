import numpy as np
import scipy as sp

import matplotlib.pyplot as plt
import time

def is_inconsistent(a):
    a = sp.linalg.lu(a)[2]
    row = a[~np.all(np.isclose(a, 0), axis=1)][-1]
    return np.allclose(row[:-1], 0) and not np.isclose(row[-1], 0)

def split_aug(aug):
    return (aug[:,:-1], aug[:,-1])

def mk_aug(cfs, b):
    # return np.hstack((cfs, b.reshape((2, 1))))
    return np.column_stack((cfs, b))

def benchmark(n, step_size=10, low=-100, hi=100):
    rng = np.random.default_rng()

    x_axis = np.arange(1, n + 1) * step_size
    y_axis_con = np.zeros(n)
    y_axis_getrf = np.zeros(n)

    for i in range(n):
        x = x_axis[i]
        print(f'benchmarking: {x}')
        times_con = []
        times_getrf = []
        for _ in range(10):
            # create a random augmented matrix
            aug = (hi - low) * rng.random((x, x + 1)) + low
            augf = np.asfortranarray(aug)

            # time is_inconsistent
            start = time.time()
            is_inconsistent(aug)
            times_con.append(time.time() - start)

            # time getrf
            start = time.time()
            sp.linalg.lapack.get_lapack_funcs(('getrf',), (augf,))[0](augf)
            times_getrf.append(time.time() - start)

        # average the runs
        y_axis_con[i] = np.average(times_con)
        y_axis_getrf[i] = np.average(times_getrf)

    data_con, = plt.plot(x_axis, y_axis_con, 'ro', label='is_inconsistent')
    data_getrf, = plt.plot(x_axis, y_axis_getrf, 'bo', label='getrf')
    plt.xlabel('# rows/cols')
    plt.ylabel('time (sec)')
    plt.legend(handles=[data_getrf, data_con])
    plt.show()

# benchmark(150)
