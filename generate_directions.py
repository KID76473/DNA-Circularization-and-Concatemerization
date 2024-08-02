import numpy as np
import direction_functions


all_directions, length, _ = direction_functions.fibonacci_sphere(np.zeros(3), 0, samples=10)
direction_set = [[]] * length
print(direction_set)

for i in range(length):
    d, l, _ = direction_functions.fibonacci_sphere(-all_directions[i], np.pi / 5)
    direction_set[i].append(l)
    direction_set[i].append(d)

# # print(direction_set)
# for x in direction_set:
#     print(x[0])
#     print("-------------------------------")

np.asarray(direction_set, dtype='object')
print(direction_set)
np.save('./data/direction_set.npy', direction_set)
