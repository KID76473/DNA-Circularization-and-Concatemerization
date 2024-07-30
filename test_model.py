import numpy as np
import direction_functions
from numba import jit, njit
import time


# @jit(nopython=False)
def walk(position, last):
    directions, upper_bound, _ = direction_functions.fibonacci_sphere(last, deg, samples=2000)
    next_dir = directions[np.random.choice(upper_bound)]
    position += next_dir
    last = -next_dir
    return position, last


num_trails = 100000000
length = 10000
deg = np.pi / 5
concentration = 953.715332748677  # unit is length of nucleotide
cir = 0
concat = 0

with open("data/test_model_sum.txt", 'w') as f:
    t = time.time()
    f.write(f"The program started at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}\n")

for n in range(num_trails):
    head = np.array([0, 0, 0], dtype='float64')
    last_dir = np.array([0, 0, 0], dtype='float64')
    for _ in range(length):  # loop through length
        head, last_dir = walk(head, last_dir)
    if (np.abs(head) < 1).all(axis=-1):  # check circularization
        cir += 1
    elif (np.abs(head) % concentration < 1).all(axis=-1):  # check concatemerization
        concat += 1
    t = time.time()
    with open("data/test_model_sum.txt", 'a') as f:
        f.write(f"{n + 1}th loop at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}\n")
        if n % 100 == 0:
            temp1, temp2 = cir / (n + 1), concat / (n + 1)
            f.write(f"circularization: {temp1}\n")
            f.write(f"concatemerization: {temp2}\n")

with open("data/test_model_sum.txt", 'a') as f:
    f.write(f"circularization: {cir / num_trails}\n")
    f.write(f"concatemerization: {concat / num_trails}\n")
    t = time.time()
    f.write(f"The program finished at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}")