import sys
import time
import numpy as np
import matplotlib.pyplot as plt


# set up all directions
def get_directions(num):
    directions = np.zeros((num_dir ** 2, dimension))
    angles = np.linspace(0, 2 * np.pi, num, endpoint=False)
    # print(np.shape(directions))
    for i in range(num):  # angle of xy plane
        for j in range(num):  # angle of z plane
            directions[i * num + j, 2] = np.sin(angles[j])
            directions[i * num + j, 1] = np.cos(angles[j]) * np.sin(angles[i])
            directions[i * num + j, 0] = np.cos(angles[j]) * np.cos(angles[i])
    # print(np.shape(directions))
    return directions


# test whether the length is 1 or not
def test_directions(num, directions):
    for i in range(num):  # determine precision
        print(np.abs(directions[i, 0] ** 2 + directions[i, 1] ** 2 + directions[i, 2] ** 2 - 1) < 0.001)


def simulate(dimension, N, length, concentration, error, num_dir, print_log, save_output):
    directions = get_directions(num_dir)
    heads = np.zeros((N, N, N, dimension))
    furthest = np.zeros((N, N, N, dimension))
    furthest_avg = 0
    t0 = time.time()

    for i in range(length):  # length
        # # directions self-propelled
        # random_directions = np.zeros((N, N, N, dimension))
        # for x in range(N):
        #     for y in range(N):
        #         for z in range(N):
        #             temp_directions = directions.copy()
        #             np.random.shuffle(temp_directions)
        #             for direction in temp_directions:
        #                 # print(is_within_expel(last_dir[x, y, z], direction, expel))
        #                 if not is_within_expel(last_dir[x, y, z], direction, expel):
        #                     random_directions[x, y, z] = direction
        #                     last_dir[x, y, z] = direction  # Update last_dir with the chosen direction
        #                     break
        # heads += random_directions

        # any direction
        random_directions = directions[np.random.choice(num_dir ** 2, size=(N, N, N))]
        heads += random_directions

        # record if heads reach the furthest distance from tail
        heads_squared_dist = np.sum(heads ** 2, axis=-1)
        furthest_squared_dist = np.sum(furthest ** 2, axis=-1)
        mask = heads_squared_dist > furthest_squared_dist
        furthest[mask] = heads[mask]

        if print_log:
            print("-------------------------------")
            print(f"the {i}th step")
            print(time.time())
            print(f"heads: {heads}")

    t1 = time.time()

    np.save('heads.npy', heads)
    np.save('furthest.npy', furthest)

    for x in range(N):
        for y in range(N):
            for z in range(N):
                furthest_avg += (furthest[x, y, z, 0] ** 2 + furthest[x, y, z, 1] ** 2 + furthest[
                    x, y, z, 2] ** 2) ** 1 / 2
    furthest_avg /= N ** 3

    circular = np.sum((np.abs(heads) < error).all(axis=-1))
    concatemer = np.sum((np.abs(heads) % concentration < error).all(axis=-1)) - circular

    if save_output:
        output = sys.stdout
        with open('output.txt', 'w') as f:
            sys.stdout = f
            print(f"The program started running at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t0))}")
            print(f"Dimension: {dimension}")
            print(f"Length of one axis: {N}, and number of molecule: {N ** 3}")
            print(f"Length of DNA: {length}")
            print(f"Each extension | distance between two adjacent molecules | radius of error:")
            print(f" 1 | {concentration} | {error}")
            print(f"Number of directions: {num_dir}")

            if concatemer == 0:
                print(f"Number of circularization is {circular}, and 0 concatemerization")
            else:
                print(f"Number of circularization is {circular}")
                print(f"Number of concatemerization is {concatemer}")
                print(f"circularization / concatemerization is {circular / concatemer}")
            print(f"Rate of circularization: {circular / (N ** 3)}")
            print(
                f"Rate of concatemerization: {concatemer / (N ** 3)}, which should be {4 * np.pi * error ** 3 / (concentration ** 3 * 3)}")
            print(f"average of furthest distance from tail / length = {furthest_avg} / {length}")
            print(f"It takes {t1 - t0} seconds")
            print(f"The program finished at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t1))}")
            sys.stdout = output

    return circular, concatemer, furthest_avg


# 3mm test tube, 3.5nm each step
# dimension = 3 N = 64 length = 1000 concentration = 10 num_dir = 360 error = 0.0001

# # check validity
# dimension = 3
# N = 3  # number of molecules = N^3
# length = 2
# concentration = 2  # distance between every pair of adjacent points
# error = 1
# num_dir = 360  # number of angles
# directions = np.zeros((num_dir ** 2, dimension))
# heads = np.zeros((N, N, N, dimension))
# furthest = np.zeros((N, N, N, dimension))
# print_log = 0
# save_output = 1

# test
dimension = 3
N = 64  # number of molecules = N^3
length = 1000
concentration = 29  # distance between every pair of adjacent points
error = 1
num_dir = 360  # number of angles
print_log = 0  # print out heads every loop
save_output = 0  # save output in output.txt

# test_directions(num_dir, get_directions(num_dir))

num = 100
array_cir = np.zeros(num)
array_con = np.zeros(num)
for i in range(num):
    print(i)
    array_cir[i], array_con[i], _ = simulate(dimension, N, length, concentration, error, num_dir, print_log, save_output)
plt.figure(figsize=(10, 5))
plt.plot(array_cir, label='Circularization', color='blue')
plt.plot(array_con, label='Concatemerization', color='red')
plt.xlabel('Simulation Index')
plt.ylabel('Count')
plt.title('Circularization and Concatemerization over 100 Simulations')
plt.legend()
plt.grid(True)
plt.show()
