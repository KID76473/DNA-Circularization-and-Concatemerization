import random as rand
from numba import jit, clear_cache
import numpy as np

clear_cache()

#this can be generalized to 2d as well using numpy

#self circularization can be represented as a 2d or 3d random walk

num_dir = 6

total_cir = 0

num_trials = 100000000

len_list = [500, 1000, 1500, 2000]

x_vals = []
y_vals = []

start_pos = [0, 0, 0] #[x, y, z]

def random_walk(pos, dir):
    if dir == 0: #east
        pos[0] += 1
    elif dir == 1: #west
        pos[0] -= 1
    elif dir == 2: #up
        pos[1] += 1
    elif dir == 3: #down
        pos[1] -= 1
    elif dir == 4: #z up
        pos[2] += 1
    elif dir == 5: #z down
        pos[2] -= 1
    return pos


# @jit(target_backend='cuda')
def main():
    with open("data/completed_3d_rand_walk_100_mil_trials", "w") as file_output:
        for num in len_list:
            total_cir = 0
            for i in range(num_trials + 1):
                pos = [0, 0, 0]
                for j in range(0, num):
                    direction = rand.randint(0, 5)
                    pos = random_walk(pos, direction)
                if pos == start_pos:
                    total_cir += 1
                if i % 1000000:
                    print(f"length: {num} total_cir: {total_cir} total: {i} \n")
            x_vals.append(num)
            y_vals.append(total_cir)
            # print(f"length: {num} total_cir: {total_cir} total: {num_trials} \n")
            file_output.write(f"length: {num} total_cir: {total_cir} total: {num_trials} \n")


    #print(f"circularized: {total_cir}; total trials: {num_trials}")

    print(x_vals)
    print(y_vals)


if __name__ == '__main__':
    main()
