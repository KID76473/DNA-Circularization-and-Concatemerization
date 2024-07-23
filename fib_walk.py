import numpy as np
import direction_functions
from numba import jit, njit


@jit
def walk(position, last):
    next_dir, upper_bound = direction_functions.fibonacci_sphere(last, deg)
    next_dir = next_dir[np.random.choice(upper_bound)]
    position += next_dir
    last = next_dir
    return position, last


num_trails = 1000000
length_list = [500, 1000, 2000, 5000, 10000, 20000, 50000]
length_size = len(length_list)
variance = 1
deg = np.pi / 5
filename = "fib_walk.txt"
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


cir = np.zeros(length_size)
concat = np.zeros([len(dna_num), length_size])
for n in range(num_trails):
    for i in range(len(density)):  # loop through concentration
        head = np.array([0, 0, 0], dtype='float32')
        last_dir = np.array([0, 0, 0], dtype='float32')
        for j in range(1, length_list[-1] + 1):  # loop through length
            head, last_dir = walk(head, last_dir)

            if j in length_list:
                length_index = length_list.index(j)
                # print(density[i])
                if (np.abs(head) < 1).all():  # check circularization
                    cir[length_index] += 1
                elif (np.abs(head) % density[i][length_index] < 1).all():  # check concatemerization
                    concat[i][length_index] += 1
    print(n)
cir /= num_trails
concat /= num_trails


print(cir, concat)
