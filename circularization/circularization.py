import time
import numpy as np
import sys
import direction_functions


num = 1000000000000
length = 2000
num_dir = 360
cirs = np.zeros(4)
heads = np.zeros((4, 3))
error = 1
directions = direction_functions.get_directions(num_dir)
concentration = 30
deg = np.pi / 2

output_filename = sys.argv[1]
with open("data/" + str(output_filename), 'w') as f:
    f.write("Starting new run circularization\n")

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
        temp, length = direction_functions.fibonacci_sphere(last, deg)
        temp = temp[np.random.choice(length)]
        head += temp
        last = temp
        if j in [499, 999, 1499, 1999]:
            index = int(j / 500)
            heads[index] = head
    # count number of circularization
    for j in range(len(heads)):  # loop thru each length
        if (np.abs(heads[j]) < error).all():
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
