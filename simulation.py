import sys
import time
import numpy as np
import matplotlib.pyplot as plt


# dimension = 3 N = 64 length = 1000 concentration = 10 num_dir = 360 error = 0.0001

# # check
# dimension = 3
# N = 3  # number of molecules = N^3
# length = 1000
# concentration = 2  # distance between every pair of adjacent points
# heads = np.zeros((N, N, N, dimension))
# # terminate = np.ones((N, N, N, dimension))
# error = 0.01
# num_dir = 4  # number of angles
# furthest_avg = 0

# test
dimension = 3
N = 32  # number of molecules = N^3
length = 10000
concentration = 2  # distance between every pair of adjacent points
heads = np.zeros((N, N, N, dimension))
furthest = np.zeros((N, N, N, dimension))
# terminate = np.ones((N, N, N, dimension))
error = 0.5
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
    # # old
    # for x in range(N):
    #     for y in range(N):
    #         for z in range(N):
    #             heads[x, y, z] +=  directions[np.random.choice(range(num_dir ** 2))]

    # new
    random_directions = directions[np.random.choice(num_dir ** 2, size=(N, N, N))]
    heads += random_directions

    # # old
    # for x in range(N):
    #     for y in range(N):
    #         for z in range(N):
    #             if heads[x, y, z, 0] ** 2 + heads[x, y, z, 1] ** 2 + heads[x, y, z, 2] ** 2 > \
    #                     furthest[x, y, z, 0] ** 2 + furthest[x, y, z, 1] ** 2 + furthest[x, y, z, 2] ** 2:
    #                 furthest[x, y, z, :] = heads[x, y, z, :]

    # new
    heads_squared_dist = np.sum(heads ** 2, axis=-1)
    furthest_squared_dist = np.sum(furthest ** 2, axis=-1)
    mask = heads_squared_dist > furthest_squared_dist
    furthest[mask] = heads[mask]

    # print("-------------------------------")
    # print(f"the {i}th step")
    # print(f"heads: {heads}")

    # count # of circularization

    # # old
    # circular = (np.abs(heads) < error)
    # circular = circular[:, :, :, 0] * circular[:, :, :, 1] * circular[:, :, :, 2]
    # num_cir.append(np.sum(circular))

    # new
    # circular = (np.abs(heads) < error).all(axis=-1)
    # num_cir.append(np.sum(circular))

    # print(f"circular: {num_cir[i]}")
    # print(f"circular: {circular.astype(int)}")

    # count # of concatemerization

    # # old
    # concatemer = (np.abs(heads) % concentration) < error
    # concatemer = concatemer[:, :, :, 0] * concatemer[:, :, :, 1] * concatemer[:, :, :, 2]
    # for x in range(N):
    #     for y in range(N):
    #         for z in range(N):
    #             if np.abs(heads[x, y, z, 0]) < error and np.abs(heads[x, y, z, 1]) < error and np.abs(heads[x, y, z, 2]) < error:
    #                 concatemer[x, y, z] = False
    # num_con.append(np.sum(concatemer))

    # # new
    # concatemer = (np.abs(heads) % concentration < error).all(axis=-1)
    # concatemer &= ~circular
    # num_con.append(np.sum(concatemer))

    # print(f"concatemer: {num_con[i]}")
    # print(f"concatemer: {concatemer.astype(int)}")

    # terminate = (np.ones((N, N, N), dtype=np.int8) - concatemer - circular)[..., np.newaxis]

t1 = time.time()

np.save('heads.npy', heads)
np.save('furthest.npy', furthest)

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
    print(f"The program started running at {t0}")
    print(f"Dimension: {dimension}")
    print(f"Number of molecule: {N ** 3}")
    print(f"Length of DNA: {length}")
    print(f"Each extension / distance between two adjacent molecules: 1 / {concentration}")
    print(f"Amount of directions: {num_dir}")
    print(f"Error: {error}")

    if circular == 0:
        print(f"Number of circularization is {circular}, and 0 concatemerization")
    else:
        print(f"Number of circularization is {circular}")
        print(f"Number of concatemerization is {concatemer}")
        print(f"circularization / concatemerization is {circular / concatemer}")
    print(f"average of furthest distance from tail / length = {furthest_avg} / {length}")
    print(f"It takes {t1 - t0} seconds")
    print(f"The program finished at {t1}")
    sys.stdout = output
