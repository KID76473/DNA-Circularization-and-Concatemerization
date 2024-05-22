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
# last_dir = np.zeros([N, N, N, 2])
# expel = 0  # angle of area that next extension will not be

# test
dimension = 3
N = 32  # number of molecules = N^3
length = 10000
concentration = 2  # distance between every pair of adjacent points
heads = np.zeros((N, N, N, dimension))
furthest = np.zeros((N, N, N, dimension))
error = 0.5
num_dir = 90  # number of angles
furthest_avg = 0
last_dir = np.zeros([N, N, N, 3])
expel = np.pi / 4  # angle of area that next extension will not be

# set up all directions
angles = np.linspace(0, 2 * np.pi, num_dir, endpoint=False)
directions = np.zeros((num_dir ** 2, dimension))
# print(np.shape(directions))
for i in range(num_dir):  # angle of xy plane
    for j in range(num_dir):  # angle of z plane
        directions[i * num_dir + j, 2] = np.sin(angles[j])
        directions[i * num_dir + j, 1] = np.cos(angles[j]) * np.sin(angles[i])
        directions[i * num_dir + j, 0] = np.cos(angles[j]) * np.cos(angles[i])
# print(np.shape(directions))

# # test whether the length is 1 or not
# for i in range(num_dir ** 2):  # determine precision
#     print(np.abs(directions[i, 0] ** 2 + directions[i, 1] ** 2 + directions[i, 2] ** 2 - 1) < 0.001)

def is_within_expel(last_direction, direction, expel):
    if not (last_direction == 0).all():
        dot_product = np.dot(last_direction, direction)
        norms_product = np.linalg.norm(last_direction) * np.linalg.norm(direction)

        # Ensure norms_product is not zero to avoid division by zero
        if norms_product == 0:
            return False

        # Calculate the cosine of the angle and clamp it to the range [-1, 1]
        cos_angle = dot_product / norms_product
        cos_angle = np.clip(cos_angle, -1.0, 1.0)

        # Calculate the angle
        angle = np.arccos(cos_angle)

        return np.abs(angle) <= expel
    else:
        return False

t0 = time.time()

for i in range(length):  # length
    # too slow
    random_directions = np.zeros((N, N, N, dimension))
    for x in range(N):
        for y in range(N):
            for z in range(N):
                temp_directions = directions.copy()
                np.random.shuffle(temp_directions)
                for direction in temp_directions:
                    # print(is_within_expel(last_dir[x, y, z], direction, expel))
                    if not is_within_expel(last_dir[x, y, z], direction, expel):
                        random_directions[x, y, z] = direction
                        last_dir[x, y, z] = direction  # Update last_dir with the chosen direction
                        break
    heads += random_directions

    # # new
    # let heads move
    # random_directions = np.zeros((N, N, N, 2))
    # for x in range(N):
    #     for y in range(N):
    #         for z in range(N):
    #             temp = directions.copy()
    #             temp = np.where(temp != last_dir[x, y, z])
    #             # out of bound error needs to be solved
    #             start = np.where(directions == last_dir - expel)
    #             start = start[0] * num_dir ** 2 + start[1] * num_dir + start[2]
    #             end = np.where(directions == last_dir + expel)
    #             end = end[0] * num_dir ** 2 + end[1] * num_dir + end[2]
    #             for j in range(start, end):
    #                 temp.delete(np.where(directions == directions[j]))
    #             heads += temp[np.random.choice(len(temp), size=(N, N, N, 3))]
    # last_dir = random_directions

    # # old
    # random_directions = directions[np.random.choice(num_dir ** 2, size=(N, N, N))]
    # heads += random_directions

    # record if heads reach the furthest distance from tail
    heads_squared_dist = np.sum(heads ** 2, axis=-1)
    furthest_squared_dist = np.sum(furthest ** 2, axis=-1)
    mask = heads_squared_dist > furthest_squared_dist
    furthest[mask] = heads[mask]

    print("-------------------------------")
    print(f"the {i}th step")
    print(time.time())
    # print(f"heads: {heads}")

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
