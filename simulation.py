import sys
import time
import numpy as np
import matplotlib.pyplot as plt


# dimension = 3 N = 64 length = 1000 concentration = 10 num_dir = 360 error = 0.0001

# # check
# dimension = 3
# N = 3  # number of molecules = N^3
# length = 2
# concentration = 2  # distance between every pair of adjacent points
# heads = np.zeros((N, N, N, dimension))
# furthest = np.zeros((N, N, N, dimension))
# error = 1
# num_dir = 4  # number of angles
# furthest_avg = 0

# test
dimension = 3
N = 32  # number of molecules = N^3
length = 10000
concentration = 2  # distance between every pair of adjacent points
heads = np.zeros((N, N, N, dimension))
furthest = np.zeros((N, N, N, dimension))
error = 1
num_dir = 90  # number of angles
furthest_avg = 0

# set up all directions
angles = np.linspace(0, 2 * np.pi, num_dir, endpoint=False)
directions = np.zeros((num_dir ** 2, dimension))
# print(np.shape(directions))
for i in range(num_dir):  # angle of xy plane
    for j in range(num_dir):  # angle of z plane
        directions[i * num_dir + j, 2] = np.sin(angles[j])
        directions[i * num_dir + j, 1] = np.cos(angles[j]) * np.sin(angles[i])
        directions[i * num_dir + j, 0] = np.cos(angles[j]) * np.cos(angles[i])
# print(len(directions))

# # test whether the length is 1 or not
# for i in range(num_dir ** 2):  # determine precision
#     print(np.abs(directions[i, 0] ** 2 + directions[i, 1] ** 2 + directions[i, 2] ** 2 - 1) < 0.001)

t0 = time.time()

for i in range(length):  # length
    # let heads move
    random_directions = directions[np.random.choice(num_dir ** 2, size=(N, N, N))]
    heads += random_directions

    # record if heads reach the furthest distance from tail
    heads_squared_dist = np.sum(heads ** 2, axis=-1)
    furthest_squared_dist = np.sum(furthest ** 2, axis=-1)
    mask = heads_squared_dist > furthest_squared_dist
    furthest[mask] = heads[mask]

    # print("-------------------------------")
    # print(f"the {i}th step")
    # print(f"heads: {heads}")

t1 = time.time()

np.save('heads.npy', heads)
np.save('furthest.npy', furthest)

# furthest_squared_dist = np.sum(furthest ** 2, axis=-1)
# furthest_dist = np.sqrt(furthest_squared_dist)
# total_distance = np.sum(furthest_dist)
# furthest_avg = total_distance / (N ** 3)
for x in range(N):
    for y in range(N):
        for z in range(N):
            furthest_avg += (furthest[x, y, z, 0] ** 2 + furthest[x, y, z, 1] ** 2 + furthest[x, y, z, 2] ** 2) ** 1 / 2
furthest_avg /= N ** 3

circular = np.sum((np.abs(heads) < error).all(axis=-1))
concatemer = np.sum((np.abs(heads) % concentration < error).all(axis=-1)) - circular

# plt.plot(np.array(range(length)), leftover)
# plt.show()

output = sys.stdout
with open('output.txt', 'w') as f:
    sys.stdout = f
    print(f"The program started running at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t0))}")
    print(f"Dimension: {dimension}")
    print(f"Number of molecule: {N ** 3}")
    print(f"Length of DNA: {length}")
    print(f"Each extension | distance between two adjacent molecules | radius of error: 1 | {concentration} | {error}")
    print(f"Amount of directions: {num_dir}")

    if concatemer == 0:
        print(f"Number of circularization is {circular}, and 0 concatemerization")
    else:
        print(f"Number of circularization is {circular}")
        print(f"Number of concatemerization is {concatemer}")
        print(f"circularization / concatemerization is {circular / concatemer}")
    print(f"average of furthest distance from tail / length = {furthest_avg} / {length}")
    print(f"It takes {t1 - t0} seconds")
    print(f"The program finished at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t1))}")
    sys.stdout = output
