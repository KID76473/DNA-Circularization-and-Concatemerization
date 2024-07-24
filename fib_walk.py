import numpy as np
import direction_functions
from numba import jit, njit
import time


@njit
def walk():
    position = np.array([0, 0, 0], dtype='float64')
    last = np.array([0, 0, 0], dtype='float64')
    for j in range(1, length_list[-1] + 1):  # loop through length
        next_dir, upper_bound = direction_functions.fibonacci_sphere(last, deg)
        next_dir = next_dir[np.random.choice(upper_bound)]
        position += next_dir
        last = next_dir

        if j in length_list:
            length_index = length_list.index(j)
            # print(density[i])
            if (np.abs(position) < 1).all():  # check circularization
                cir[length_index] += 1
            else:
                for i in range(len(density)):  # loop through concentration
                    if (np.abs(position) % density[i][length_index] < 1).all():  # check concatemerization
                        concat[i][length_index] += 1
    return position, last


num_trails = 1000
length_list = [500, 1000, 2000, 5000, 10000, 20000, 50000]
length_size = len(length_list)
variance = 1
deg = np.pi / 5
reactor_length = 3.4e-7
reactor_volume = reactor_length ** 3
dna_num = [
    [1.95e+10, 9.77e+09, 4.89e+09, 1.95e+09, 9.77e+08, 4.89e+08, 1.95e+08],
    [1.95e+11, 9.77e+10, 4.89e+10, 1.95e+10, 9.77e+09, 4.89e+09, 1.95e+09],
    [1.95e+12, 9.77e+11, 4.89e+11, 1.95e+11, 9.77e+10, 4.89e+10, 1.95e+10],
    [1.95e+13, 9.77e+12, 4.89e+12, 1.95e+12, 9.77e+11, 4.89e+11, 1.95e+11],
    [1.95e+14, 9.77e+13, 4.89e+13, 1.95e+13, 9.77e+12, 4.89e+12, 1.95e+12]
]
density = reactor_volume / np.array(dna_num)  # each row has length of small cube for same concentration but different dna length
cir = np.zeros(length_size, dtype='float64')
concat = np.zeros([len(dna_num), len(dna_num[0])], dtype='float64')

with open("data/fib_walk_sum.txt", 'w') as f:
    t = time.time()
    f.write(f"The program started at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}")

for n in range(num_trails):
    cir, concat = walk()

    t = time.time()
    with open("data/fib_walk_sum.txt", 'a') as f:
        f.write(f"{n + 1}th loop at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}")
        if (n + 1) % 100 == 0:
            f.write(f"the {n + 1}the loop")
            f.write(f"circularization: \n{cir / (n + 1)}")
            f.write(f"concatemerization: \n{concat / (n + 1)}")

with open("data/fib_walk_sum.txt", 'a') as f:
    f.write(f"circularization: \n{cir / num_trails}")
    f.write("\n")
    f.write(f"concatemerization: \n{concat / num_trails}")
    t = time.time()
    f.write(f"The program finished at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}")
