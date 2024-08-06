import time
import numpy as np
import direction_functions


s = 1000
all_directions, length, _ = direction_functions.fibonacci_sphere(np.zeros(3), 0, samples=s)
direction_set = []
indices = []

t0 = time.time()
print(f"Started to generate directions. samples = {s}")
for i in range(length):
    print(f"the {i}th loop")
    last = -all_directions[i]
    indices.append(last)
    d, l, _ = direction_functions.fibonacci_sphere(last, np.pi / 5)
    direction_set.append([])
    direction_set[i].append(l)
    direction_set[i].append(d)
t1 = time.time()
print(f"Finished to generate directions. samples = {s}")
print(f"It takes {t1 - t0}s.")

# # print(direction_set)
# for x in direction_set:
#     print(x[0])
#     print("-------------------------------")

direction_set = np.array(direction_set, dtype='object')
# print(direction_set)
np.save('./data/direction_set', direction_set)
indices = np.array(indices)
# print(indices)
np.save('./data/indices', indices)
