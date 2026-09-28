import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import time

def pad_with_zeros(a):
    """Add zeros to the bottom or right of matrix until it becomes square.

    Parameters
    ----------
    a : (m × n) 2D numpy array

    Returns
    -------
    a_square : (max(m, n) × max(m, n)) 2D numpy array
               Padded with zeros on the bottom or right


    Examples
    --------
    >>> pad_with_zeros(np.array([[1, 2, 3], [4, 5, 6]]))
    array([[1., 2., 3.],
           [4., 5., 6.],
           [0., 0., 0.]])
    >>> pad_with_zeros(np.array([[1, 2], [3, 4], [5, 6]]))
    array([[1., 2., 0.],
           [3., 4., 0.],
           [5., 6., 0.]])
    """
    pass # TODO

rng = np.random.default_rng()

def benchmark(
        num_trials,
        input_generator,
        test_funcs,
        step_size=10,
        low=-100,
        high=100,
        num_samples_per_trial=10
):
    assert(len(test_funcs) <= 6)
    x_axis = np.arange(1, num_trials + 1) * step_size
    y_axes = [np.zeros(num_trials) for _ in range(len(test_funcs))]

    for i in range(num_trials):
        x = x_axis[i]
        print(f'benchmarking: {x}')
        times = [[] for _ in range(len(test_funcs))]
        for _ in range(num_samples_per_trial):
            inputs = input_generator(rng, low, high, x)

            for j in range(len(test_funcs)):
                start = time.time()
                test_funcs[j][0](*inputs)
                times[j].append(time.time() - start)

        for j in range(len(test_funcs)):
            y_axes[j][i] = np.average(times[j])

        datas = []
        colors = ['ro', 'bo', 'go', 'co', 'mo', 'ko']

    for j in range(len(test_funcs)):
        data, = plt.plot(x_axis, y_axes[j], colors[j], label=test_funcs[j][1])
        datas.append(data)

    plt.xlabel('# rows')
    plt.ylabel('time (sec)')
    plt.legend(handles=datas)
    plt.show()

def random_gen(rng, low, high, n):
    a = rng.uniform(low, high, (n, n))
    b = rng.uniform(low, high, n)
    return (a, b)

# # Benchmark against uniformly random square matrices
# benchmark(
#     300,
#     random_gen,
#     [
#         (np.linalg.solve, "np.linalg.solve"),
#         (sp.linalg.solve, "sp.linalg.solve"),
#     ],
# )

def random_tridiagonal(rng, low, high, n):
    pass # TODO

# # Benchmark against uniformly random tridiagonal matrices
# benchmark(
#     300,
#     random_tridiagonal,
#     [
#         (np.linalg.solve, "np.linalg.solve"),
#         (sp.linalg.solve, "sp.linalg.solve"),
#         (lambda a, b: sp.linalg.solve(a, b, assume_a="tridiagonal"), "sp.linalg.solve(assume_a=\"tridiagonal\")"),
#     ],
# )

def random_sym(rng, low, high, n):
    pass # TODO

# # Benchmark against uniformly random symmetric matrices
# benchmark(
#     300,
#     random_sym,
#     [
#         (np.linalg.solve, "np.linalg.solve"),
#         (sp.linalg.solve, "sp.linalg.solve"),
#         (lambda a, b: sp.linalg.solve(a, b, assume_a="sym"), "sp.linalg.solve(assume_a=\"sym\")"),
#         (lambda a, b: sp.linalg.solve(a, b, assume_a="gen"), "sp.linalg.solve(assume_a=\"gen\")"),
#     ],
# )
