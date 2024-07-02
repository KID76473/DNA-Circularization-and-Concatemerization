import numpy as np
from numba import jit


@jit
def func():
    N = 64
    dimensions = 3
    concentrations = np.arange(2, 21, 19)
    positions = np.zeros((N, N, N, dimensions))
    num = 100000000000
    concat = np.zeros(19)
    error = 1

    i = 0
    while i < num:
        for c in range(len(concentrations)):
            positions = np.random.uniform(concentrations[c] * 10, size=(N, N, N, dimensions))
            concat[c] = np.sum((positions < error).all(axis=-1))
        n = 10000
        # write the result to file every 100000 loops
        if i % n == 0:
            # write_file(i, concat)
            print(f"{i} loops")
            print(str(concat / i) + "\n")
        i += 1

func()

def write_file(i, concat):
    with open("../data/big_cube", 'a') as f:
        f.write(f"{i} loops\n")
        # f.write(str(positions) + "\n")
        f.write(str(concat / i) + "\n")
