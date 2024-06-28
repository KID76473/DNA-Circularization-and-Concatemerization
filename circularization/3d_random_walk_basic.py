import random as rand
import time

#this can be generalized to 2d as well using numpy

#self circularization can be represented as a 2d or 3d random walk

num_trials = 10

len_list = [500, 1000, 1500, 2000]

x_vals = []
y_vals = []

start_pos = [0, 0, 0] #[x, y, z]

file_output = open("basic_3d_rand_walk_output", "w")

t0 = time.time()

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

for num in len_list:
    total_cir = 0
    for i in range(num_trials + 1):
        pos = [0, 0, 0]

        for j in range(0, num):
            direction = rand.randint(0, 5)
            pos = random_walk(pos, direction)

        if pos == start_pos:
            total_cir += 1
        
        # if i % 100000 == 0: #making sure the file is running
        #     print(f"length: {num} total_cir: {total_cir} total: {num_trials} \n")
        
    x_vals.append(num)
    y_vals.append(total_cir)
    file_output.write(f"length: {num} total_cir: {total_cir} total: {num_trials} \n")

t1 = time.time()

print(f"time taken: {t1 - t0}")
file_output.write(f"time taken: {t1 - t0}\n")

file_output.close

print(x_vals)
print(y_vals)