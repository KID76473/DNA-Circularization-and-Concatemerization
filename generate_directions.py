import numpy as np
import direction_functions


all_directions, length, _ = direction_functions.fibonacci_sphere(np.zeros(3), 0, samples=10)
direction_set = []
indices = []

for i in range(length):
    last = -all_directions[i]
    indices.append(last)
    d, l, _ = direction_functions.fibonacci_sphere(last, np.pi / 5)
    direction_set.append([])
    direction_set[i].append(l)
    direction_set[i].append(d)

# # print(direction_set)
# for x in direction_set:
#     print(x[0])
#     print("-------------------------------")

direction_set = np.array(direction_set, dtype='object')
print(direction_set)
np.save('./data/direction_set', direction_set)
indices = np.array(indices)
print(indices)
np.save('./data/indices', indices)
