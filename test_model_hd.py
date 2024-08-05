import numpy as np
import direction_functions
from numba import jit, njit
import
import time


# @jit(nopython=True)
def walk(position, last):
    # # one way
    # next_directions = np.zeros((N, N, N, 3))
    # for i in range(N):
    #     for j in range(N):
    #         for k in range(N):
    #             candidates, upper_bound, _ = direction_functions.fibonacci_sphere(last[i, j, k], np.pi / 5, samples=100)
    #             next_directions[i, j, k] = candidates[np.random.choice(upper_bound)]
    # position += next_directions
    # last = -next_directions

    # another way


    return position, last


num_trails = 100000000
length = 10000
N = 8
deg = np.pi / 5
concentration = 953.715332748677  # unit is length of nucleotide
cir = 0
concat = 0

with open("data/test_model_hd_sum.txt", 'w') as f:
    t = time.time()
    f.write(f"The program started at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}\n")

for n in range(num_trails):
    print(n)
    # head = np.array([0, 0, 0], dtype='float64')
    # last_dir = np.array([0, 0, 0], dtype='float64')
    head = np.zeros((N, N, N, 3))
    last_dir = np.zeros((N, N, N, 3))
    for _ in range(length):  # loop through length
        head, last_dir = walk(head, last_dir)
    cir = np.sum((np.abs(head) < 1).all(axis=-1))
    concat = np.sum((np.abs(head) % concentration < 1).all(axis=-1)) - cir
    t = time.time()
    with open("data/test_model_hd_sum.txt", 'a') as f:
        f.write(f"{n + 1}th loop at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}\n")
        if n % 1 == 0:
            f.write(f"circularization: {cir / ((n + 1) * N ** 3)}\n")
            f.write(f"concatemerization: {concat / ((n + 1) * N ** 3)}\n")

with open("data/test_model_hd_sum.txt", 'a') as f:
    f.write(f"circularization: {cir / (num_trails * N ** 3)}\n")
    f.write(f"concatemerization: {concat / (num_trails * N ** 3)}\n")
    t = time.time()
    f.write(f"The program finished at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}")
