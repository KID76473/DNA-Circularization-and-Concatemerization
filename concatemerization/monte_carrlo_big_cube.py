import numpy as np
from numba import jit


# @jit
def func():
    N = 64
    dimensions = 3
    concentrations = np.arange(2, 21)
    num = 10000000
    concat = np.zeros(19)
    error = 1

    with open("../data/big_cube", 'w') as f:
        f.write("Started running\n")

    i = 0
    while i < num:
        for c in range(len(concentrations)):
            positions = np.random.uniform(0, concentrations[c] * 10, size=(N, N, N, dimensions))
            concat[c] += np.sum((positions < error).all(axis=-1))
        n = 10000
        # write the result to file every 100000 loops
        if i % n == 0:
            write_file(i, concat, concentrations)
            # print(f"{i} loops")
            # print(str(concat / i) + "\n")
        i += 1


def write_file(i, concat, concentrations):
    with open("../data/big_cube", 'a') as f:
        f.write(f"{i} loops\n")
        # f.write(str(positions) + "\n")
        for c in range(len(concentrations)):
            f.write(str(concentrations[c]) + ": " + str(concat[c] / ((i + 1) * 64 ^ 3)) + "\n")


func()
