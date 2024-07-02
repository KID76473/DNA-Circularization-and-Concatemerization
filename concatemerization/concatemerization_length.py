import time
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'parent_dir')))
import direction_functions


num = 1000000000000
length = 2000
num_dir = 360
cirs = np.zeros(4)
heads = np.zeros((4, 3))
error = 1
directions = direction_functions.get_directions(num_dir)
distance = 30
deg = np.pi / 2

output_filename = sys.argv[1]
with open("data/" + str(output_filename), 'w') as f:
    f.write("Starting new run concatemerization\n")

t0 = time.time()
i = 0
while i < num:
    # every case
    head = np.zeros(3)
    last = np.array([0, 0, 0])
    for j in range(length):
        # # any random direction
        # head += directions[np.random.choice(num_dir ** 2)]

        # choose random direction based on the last step
        temp = direction_functions.get_propelled_directions(num_dir, last, deg)
        head += temp
        last = temp

        if j in [499, 999, 1499, 1999]:
            index = int(j / 500)
            heads[index] = head
        if j in [499, 999, 1499, 1999]:
            index = int(j / 500)
            heads[index] = head
    # count number of circularization
    for j in range(len(heads)):
        if (np.abs(heads[j]) % distance < error).all():
            cirs[j] += 1
        i += 1
    n = 10000
    # write the result to file every 100000 loops
    if i % n == 0:
        with open("data/" + str(output_filename), 'a') as f:
            f.write(f"{i} loops\n")
            for k in range(len(cirs)):
                if cirs[k] == 0:
                    f.write(f"i: {(k + 1) * 500}, head: {heads[k]}, no cir\n")
                else:
                    f.write(f"i: {(k + 1) * 500}, head: {heads[k]}, cir: {cirs[k]}, cir / num: {cirs[k] / i}\n")
