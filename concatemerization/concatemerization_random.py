import numpy as np
import sys


def get_directions(num_dir):
    d = np.zeros((num_dir * num_dir, 3))
    angles = np.linspace(0, 2 * np.pi, num_dir, endpoint=False)  # xy
    phi_angles = np.linspace(0, 2 * np.pi, num_dir, endpoint=False)  # z
    for i in range(num_dir):  # angle of xy plane
        for j in range(num_dir):  # angle of z plane
            d[i * num_dir + j, 2] = np.sin(phi_angles[j])
            d[i * num_dir + j, 1] = np.cos(phi_angles[j]) * np.sin(angles[i])
            d[i * num_dir + j, 0] = np.cos(phi_angles[j]) * np.cos(angles[i])
    return d


def get_6_directions():
    return [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], ]


num = 1000000000000
length = 2000
num_dir = 360
cirs = np.zeros(4)
concentrations = np.linspace(2, 20, 19)
cons = np.zeros(19)
heads = np.zeros((4, 3))
error = 1
directions = get_directions(num_dir)

output_filename = sys.argv[1]
with open("data/" + str(output_filename), 'w') as f:
    f.write("Starting new run circularization\n")

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
        if (np.abs(heads[j]) < error).all():
            cirs[j] += 1
    # count number of concatemerization
    for c in range(len(concentrations)):
        tail = np.random.uniform(0, concentrations[c], size=3)
        if (np.abs(heads[-1]) % concentrations[c] - tail < error).all():
            cons[c] += 1
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
            f.write("concatemerization:\n")
            f.write(f"concentrations   : {range(2, 21)}\n")
            f.write(f"concatemerization: {concentrations}\n")
