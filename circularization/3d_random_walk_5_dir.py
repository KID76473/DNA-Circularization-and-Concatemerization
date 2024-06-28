# cannot go back to the previous step
# if previously went right, cannot go left on current turn
# does not mean that it cannot go back to all other positions it has visited

import random as rand
import time

num_trials = 100000

len_list = [500, 1000, 1500, 2000]

dir_list = [-3, -2, -1, 1, 2, 3]

x_vals = []
y_vals = []

start_pos = [0, 0, 0] #[x, y, z]

file_output = open("data/basic_3d_rand_walk_output", "w")

t0 = time.time()

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

for num in len_list:
    total_cir = 0
    for i in range(num_trials + 1):
        pos = [0, 0, 0]
        not_allowed = 0

        for j in range(0, num):
            direction = rand.choice(dir_list)
            while direction == not_allowed:
                direction = rand.choice(dir_list)
            not_allowed = -direction
            pos = random_walk(pos, direction)

        if pos == start_pos:
            total_cir += 1
        
    x_vals.append(num)
    y_vals.append(total_cir)
    file_output.write(f"length: {num} total_cir: {total_cir} total: {num_trials} \n")

t1 = time.time()

print(f"time taken: {t1 - t0}")
file_output.write(f"time taken: {t1 - t0}\n")

file_output.close

print(x_vals)
print(y_vals)