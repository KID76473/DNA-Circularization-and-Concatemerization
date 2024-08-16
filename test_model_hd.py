import numpy as np
import direction_functions
from numba import jit, njit
import time
import sys


@jit(forceobj=True, cache=True, parallel=True, fastmath=True)
# @njit
def walk(position, last):
    next_directions = np.zeros((N, N, N, 3))

    # # one way
    # for i in range(N):
    #     for j in range(N):
    #         for k in range(N):
    #             candidates, upper_bound, _ = direction_functions.fibonacci_sphere(last[i, j, k], np.pi / 5, samples=100)
    #             next_directions[i, j, k] = candidates[np.random.choice(upper_bound)]

    # another way
    for i in range(N):
        for j in range(N):
            for k in range(N):
                # print("---------------------------------------")
                # print(f"the {k}th loop")
                index_last = -1
                # p1 = np.arccos(last[i, j, k][2])
                # t1 = np.arctan2(last[i, j, k][1], last[i, j, k][0])
                if (last[i, j, k] == 0).all():  # first time
                    index_last = 0
                    num = 100  # revise the number here if try different samples
                    next_directions[i, j, k] = direction_set[index_last][1][np.random.choice(num)]
                    # print("last all 0")
                else:  # non-first time
                    for n in range(1, len(indices)):
                        # p2 = np.arccos(indices[n][2])
                        # t2 = np.arctan2(indices[n][1], indices[n][0])
                        # print(last[i, j, k], indices[n])
                        # print(np.sum(np.abs(last[i, j, k] - indices[n])))
                        # if (last[i, j, k][0] == indices[n][0] and
                        #     last[i, j, k][1] == indices[n][1] and
                        #     last[i, j, k][2] == indices[n][2]):
                        if (last[i, j, k] == indices[n]).all():
                        # if np.sum(np.abs(last[i, j, k] - indices[n])) < 0.3:
                        # if True:
                        #     print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                            index_last = n
                            break
                    if index_last == -1:
                        print("Cannot find direction!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        # raise ValueError("Cannot find direction!")
                    # print(f"index_last: {index_last}")
                    # print(f"ergsfd: {direction_set[index_last][1]}")
                    # print(f"index_last: {np.random.choice(direction_set[index_last][0])}")
                    temp = direction_set[index_last]
                    num = temp[0]
                    next_directions[i, j, k] = direction_set[index_last][1][np.random.choice(num)]

    position += next_directions
    last = -next_directions
    return position, last


num_trails = 100000000
length = 10000
N = 4
deg = np.pi / 5
concentration = 953.715332748677  # unit is length of nucleotide
cir = 0
concat = 0
direction_set = np.load('./data/direction_set.npy', allow_pickle=True)
indices = np.load('./data/indices.npy')

output_filename = "./test_model_output/" + str(sys.argv[1])
# output_filename = "./data/test_model_hd_sum.txt"
with open(output_filename, 'w') as f:
    t = time.time()
    f.write(f"The program started at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}\n")

for n in range(num_trails):
    print(f"{n}th trail")
    # head = np.array([0, 0, 0], dtype='float64')
    # last_dir = np.array([0, 0, 0], dtype='float64')
    head = np.zeros((N, N, N, 3))
    last_dir = np.zeros((N, N, N, 3))
    for _ in range(length):  # loop through length
        head, last_dir = walk(head, last_dir)
    cir = np.sum((np.abs(head) < 1).all(axis=-1))
    concat = np.sum((np.abs(head) % concentration < 1).all(axis=-1)) - cir
    t = time.time()
    with open(output_filename, 'a') as f:
        f.write(f"{n + 1}th loop at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}\n")
        if n % 1 == 0:
            f.write(f"circularization: {cir / ((n + 1) * N ** 3)}\n")
            f.write(f"concatemerization: {concat / ((n + 1) * N ** 3)}\n")
            f.write(f"# of molecules: {N ** 3 * (n + 1)}\n")

with open(output_filename, 'a') as f:
    f.write(f"circularization: {cir / (num_trails * N ** 3)}\n")
    f.write(f"concatemerization: {concat / (num_trails * N ** 3)}\n")
    t = time.time()
    f.write(f"The program finished at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))}")
    f.write(f"# of molecules: {N ** 3 * num_trails}\n")
