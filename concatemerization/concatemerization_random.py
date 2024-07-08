import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'parent_dir')))
import direction_functions


num = 1000000000000
length = 2000
num_dir = 360
cirs = np.zeros(4)
concentrations = np.linspace(2, 20, 19)
cons = np.zeros(19)
heads = np.zeros((4, 3))
error = 1
directions = direction_functions.get_directions(num_dir)
deg = np.pi / 6

output_filename = sys.argv[1]
with open("data/" + str(output_filename), 'w') as f:
    f.write("Starting new run circularization\n")

i = 0
while i < num:
    # every case
    head = np.zeros(3)
    last = np.array([0, 0, 0])
    for j in range(length):
        # # many directions
        # head += directions[np.random.choice(num_dir ** 2)]

        # # 6 directions
        # head += direction_functions.get_6_directions()[np.random.choice(6)]

        # # 5 directions
        # temp = direction_functions.get_5_directions(last)[np.random.choice(6)]
        # head += temp
        # last = temp

        # choose random direction based on the last step
        temp = direction_functions.get_propelled_directions(num_dir, last, deg)
        head += temp
        last = temp

        if j in [499, 999, 1499, 1999]:
            index = int(j / 500)
            heads[index] = head
    # count number of circularization
    for j in range(len(heads)):
        if (np.abs(heads[j]) < error).all():
            # with open("data/" + str(output_filename), 'a') as f:
            #     f.write(f"heads[j]: {heads[j]}\n")
            cirs[j] += 1
    # count number of concatemerization
    for c in range(len(concentrations)):
        tail = np.random.uniform(0, concentrations[c], size=3)
        if not (np.abs(heads[-1]) < error).all() and (np.abs(heads[-1]) % concentrations[c] - tail < error).all():
            cons[c] += 1
    i += 1
    n = 10000
    # write the result to file every 100000 loops
    if i % n == 0:
        with open("data/" + str(output_filename), 'a') as f:
            f.write(f"{i} loops\n")
            f.write("circularization:\n")
            for k in range(len(cirs)):
                if cirs[k] == 0:
                    f.write(f"i: {(k + 1) * 500}, no cir\n")
                else:
                    f.write(f"i: {(k + 1) * 500}, cir: {cirs[k]}, cir / num: {cirs[k] / i}\n")
            f.write("concatemerization(length: 2000):\n")
            f.write(f"number: {cons}\n")
            f.write(f"rate: {cons / i}\n")

# 430000 loops
# circularization:
# i: 500, head: [-9.  8. -5.], cir: 23.0, cir / num: 5.348837209302326e-05
# i: 1000, head: [-23.   5. -12.], cir: 9.0, cir / num: 2.0930232558139536e-05
# i: 1500, head: [-49.   8. -11.], cir: 5.0, cir / num: 1.1627906976744185e-05
# i: 2000, head: [-39.  20.  -5.], cir: 6.0, cir / num: 1.3953488372093024e-05
# concatemerization(length: 2000):
# number: [429994. 303648. 234159. 193770. 167692. 150242. 138543. 129480. 123288.
#  117641. 114116. 110193. 108033. 105530. 104520. 103881. 102293. 101786.
#  101254.]
# rate: [0.99998605 0.70615814 0.54455581 0.45062791 0.3899814  0.3494
#  0.32219302 0.30111628 0.28671628 0.27358372 0.26538605 0.25626279
#  0.25123953 0.2454186  0.24306977 0.24158372 0.2378907  0.23671163
#  0.23547442]

