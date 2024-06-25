import time
import numpy as np
import sys

def get_directions(num):
    directions = np.zeros((num ** 2, 3))
    angles = np.linspace(0, 2 * np.pi, num, endpoint=False)
    for i in range(num):  # angle of xy plane
        for j in range(num):  # angle of z plane
            directions[i * num + j, 2] = np.sin(angles[j])
            directions[i * num + j, 1] = np.cos(angles[j]) * np.sin(angles[i])
            directions[i * num + j, 0] = np.cos(angles[j]) * np.cos(angles[i])
    return directions

num = 1000000000000
length = 2000
num_dir = 360
cirs = np.zeros(4)
heads = np.zeros((4, 3))
error = 1
directions = get_directions(num_dir)
distance = 30

output_filename = sys.argv[1]
with open("data/" + str(output_filename), 'w') as f:
    f.write("Starting new run concatemerization\n")

t0 = time.time()
i = 0
while i < num:
    # every case
    head = np.zeros(3)
    for j in range(length):
        head += directions[np.random.choice(num_dir ** 2)]
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
