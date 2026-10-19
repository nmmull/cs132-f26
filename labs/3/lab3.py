import time
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def benchmark_random(num_exp, step_size, num_eqs, process, low=-100, hi=100):
    """Benchmark a process using random matrix equations.

    Parameters
    ----------
    num_exp : int
        The number of experiments to be run.
    step_size : int
        This value dictates the size of each experiment to run.  For
        example, if experiments with step size `10`, then the i-th
        experiment should use a matrix of size `(10 * i)` by `(10 * i)`
    num_eqs : int
        This value dictates the number of experiments that `process`
        needs to solve, if `num_eqs` is `100`, then the length of the
        vectors `bs` passed into `process` should be `100`.
    process
        The function to benchmark.  In this lab, it will be `solve`,
        `lu_solve`, or `inv_solve`, as defined in the lab spec.
    low : int, default=-100
        The lowest value that should appear in a random matrix/vector
    high : int, default=100
        The highest value that should appear in a random matrix/vector

    Returns
    -------
    tuple[np.ndarray, np.ndarry]
        The output `x_axis, y_axis` should be the `x_axis` of the
        experiment, which should be of the form:
            `np.array([1 * step_size, 2 * step_size,..., num_exp * step_size])`
        and `y_axis` should be the times it takes to run each experiment.

    Notes
    -----
    An experiment is comprised of the following:

    * Generate a random matrix `a` of the appropriate size with values
      between `low` and `high`.

    * Generate a list of vectors `bs` of the appropriate size, of
      length `num_eqs`.

    * Time `process(a, bs)`.  Be careful not to include the matrix
      generation as part of the timing.

    """
    pass # TODO

def banded_matrix(k):
    n = 2 * k
    d = 4 * np.eye(n)
    d -= np.eye(n, k=2) + np.eye(n, k=-2)
    a = [-1 * (n % 2) for n in range(1, n)]
    d += np.diag(a, k=-1) + np.diag(a, k=1)
    return d

def benchmark_banded(num_exp, step_size, num_eqs, process, low=-100, hi=100):
    """Benchmake a process using a banded matrix equation.

    This function is *identical* to `benchmark_random` except that `a`
    in the experiment described above, should be replaced with the
    output of `banded_matrix` on the appropriate argument

    Note that `banded_matrix` takes a parameter `k` and produces a
    matrix with shape `(2 * k, 2 * k)`, so be careful about what
    parameter you use.

    """
    pass # TODO

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

# TODO

# Experiment 3

# TODO
