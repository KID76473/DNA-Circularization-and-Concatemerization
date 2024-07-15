# cannot go back to the previous step
# if previously went right, cannot go left on current turn
# does not mean that it cannot go back to all other positions it has visited

import numpy as np
import time
from numba import njit, types

len_list = np.array([50000])

dir_list = np.array([-3, -2, -1, 1, 2, 3])

file_output = open("jit_3d_rand_walk_5_dir_50_to_50k", "w")

@njit
def random_walk(pos, dir):
    if dir == -3: #east
        pos[0] += 1
    elif dir == -2: # y up
        pos[1] += 1
    elif dir == -1: #z up
        pos[2] += 1
    elif dir == 3: #west
        pos[0] -= 1
    elif dir == 2: # y down
        pos[1] -= 1
    elif dir == 1: #z down
        pos[2] -= 1
    return pos

@njit(types.Tuple([types.List(types.int64), types.List(types.int64)])(types.int64[:]))
def run(len_listi):
    dir_listi = np.array([-3, -2, -1, 1, 2, 3])
    start_pos = np.array([0, 0, 0]) #[x, y, z]
    x_vals = list([500, 1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000])
    y_vals = list([0, 0, 0, 0, 0, 0, 0, 0, 0])
    for num in len_listi:
        for i in range(1000000000): # num_trails
            pos = np.array([0, 0, 0], dtype=np.int64)
            not_allowed = 0

            for j in range(1, num + 1):
                direction = np.random.choice(dir_listi, 1)[0]
                while direction == not_allowed:
                    direction = np.random.choice(dir_listi, 1)[0]
                not_allowed = -direction
                pos = random_walk(pos, direction)
                if j in x_vals:
                    if np.array_equal(pos, start_pos):
                        y_vals[x_vals.index(j)] += 1

            if i % 100000 == 0:
                print(i, x_vals, y_vals)

    print(x_vals)
    print(y_vals)
    return x_vals, y_vals

t0 = time.time()

out_x, out_y = run(len_list)

t1 = time.time()

print(f"time taken: {t1 - t0}")
file_output.write(f"time taken: {t1 - t0}\n")

file_output.write(f"lengths {out_x} \n cir_probs {out_y}")

file_output.close()

print(out_x)
print(out_y)