import numpy as np
import time

#self circularization can be represented as a 2d or 3d random walk

num_trials = 1000

len_list = [500, 1000, 1500, 2000]

movement = [-1, 1]

x_vals = []
y_vals = []

start_pos = np.zeros(3) #[x, y, z]

file_output = open("data/numpy_3d_rand_walk_output", "w")

t0 = time.time()

def random_walk(pos):
    dir = np.random.choice(3)
    move = np.random.choice(movement)
    pos[dir] += move
    return pos

for num in len_list:
    total_cir = 0

    for i in range(num_trials + 1):
        pos = np.array([0, 0, 0])

        for j in range(0, num):
            pos = random_walk(pos)

        if np.equal(pos, start_pos).all():
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