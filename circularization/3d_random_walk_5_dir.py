# cannot go back to the previous step
# if previously went right, cannot go left on current turn
# does not mean that it cannot go back to all other positions it has visited

import random as rand
import time
from numba import jit

num_trials = 10000

len_list = [10000]

dir_list = [-3, -2, -1, 1, 2, 3]

x_vals = []
y_vals = []

start_pos = [0, 0, 0] #[x, y, z]

file_output = open("jit_3d_rand_walk_5_dir_50_to_50k", "w")

t0 = time.time()


@jit
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

@jit
def run(len_listi, dir_listi, num_trialsi):
    for num in len_listi:
        total_cir = 0
        for i in range(num_trialsi):
            pos = [0, 0, 0]
            not_allowed = 0

            for j in range(0, num):
                direction = rand.choice(dir_listi)
                while direction == not_allowed:
                    direction = rand.choice(dir_listi)
                not_allowed = -direction
                pos = random_walk(pos, direction)

            if pos == start_pos:
                total_cir += 1

            if i % 100000 == 0:
                print(num, i, total_cir)

        x_vals.append(num)
        y_vals.append(total_cir)


run(len_list, dir_list, num_trials)

t1 = time.time()

print(f"time taken: {t1 - t0}")
file_output.write(f"time taken: {t1 - t0}\n")

file_output.close()

print(x_vals)
print(y_vals)