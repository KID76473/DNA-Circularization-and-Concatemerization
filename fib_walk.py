import numpy as np
import direction_functions
from numba import jit, njit
import time


@njit
def walk(position, last):
    directions, upper_bound, _ = direction_functions.fibonacci_sphere(last, deg)
    next_dir = directions[np.random.choice(upper_bound)]
    position += next_dir
    last = -next_dir
    return position, last


num_trails = 100000000
length_list = [500, 1000, 2000, 5000, 10000, 20000, 50000]
length_size = len(length_list)
variance = 1
deg = np.pi / 5
# reactor_length = 3.4e-7
reactor_length = 1.365e7  # length of big cube in nucleotide
reactor_volume = reactor_length ** 3
dna_num = [
    [1.95e+10, 9.77e+09, 4.89e+09, 1.95e+09, 9.77e+08, 4.89e+08, 1.95e+08],
    [1.95e+11, 9.77e+10, 4.89e+10, 1.95e+10, 9.77e+09, 4.89e+09, 1.95e+09],
    [1.95e+12, 9.77e+11, 4.89e+11, 1.95e+11, 9.77e+10, 4.89e+10, 1.95e+10],
    [1.95e+13, 9.77e+12, 4.89e+12, 1.95e+12, 9.77e+11, 4.89e+11, 1.95e+11],
    [1.95e+14, 9.77e+13, 4.89e+13, 1.95e+13, 9.77e+12, 4.89e+12, 1.95e+12]
]
density = reactor_volume / np.array(dna_num)  # each row has length of small cube for same concentration but different dna length
density = density ** (1 / 3)
print(density)
cir = np.zeros(length_size, dtype='float64')
# print(cir.flags.writeable)
concat = np.zeros([len(dna_num), len(dna_num[0])], dtype='float64')

with open("data/fib_walk_sum.txt", 'w') as f:
    t = time.time()
    f.write(f"The program started at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}\n")

for n in range(num_trails):
    head = np.array([0, 0, 0], dtype='float64')
    last_dir = np.array([0, 0, 0], dtype='float64')
    for j in range(1, length_list[-1] + 1):  # loop through length
        head, last_dir = walk(head, last_dir)
        if j in length_list:
            length_index = length_list.index(j)
            # print(density[i])
            if (np.abs(head) < 1).all(axis=-1):  # check circularization
                cir[length_index] += 1
            else:
                for i in range(len(density)):  # loop through concentration
                    # print("!!")
                    if (np.abs(head) % density[i][length_index] < 1).all(axis=-1):  # check concatemerization
                        # print(density[i][length_index])
                        concat[i][length_index] += 1

    t = time.time()
    with open("data/fib_walk_sum.txt", 'a') as f:
        f.write(f"{n + 1}th loop at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}\n")
        if n % 10 == 0:
            temp1, temp2 = cir / (n + 1), concat / (n + 1)
            f.write(f"circularization: \n{temp1}\n")
            f.write(f"concatemerization: \n{temp2}\n")

with open("data/fib_walk_sum.txt", 'a') as f:
    f.write(f"circularization: \n{cir / num_trails}\n")
    f.write(f"concatemerization: \n{concat / num_trails}\n")
    t = time.time()
    f.write(f"The program finished at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}")
