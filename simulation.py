import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import direction_functions


def simulate(dimension, N, length, concentration, error, num_dir, print_log, save_output):
    directions = direction_functions.get_directions(num_dir)
    heads = np.zeros((N, N, N, dimension))
    furthest = np.zeros((N, N, N, dimension))
    furthest_avg = 0
    t0_func = time.time()

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

    t1_func = time.time()

    for x in range(N):
        for y in range(N):
            for z in range(N):
                furthest_avg += (furthest[x, y, z, 0] ** 2 + furthest[x, y, z, 1] ** 2 + furthest[
                    x, y, z, 2] ** 2) ** 1 / 2
    furthest_avg /= N ** 3

    circular = np.sum((np.abs(heads) < error).all(axis=-1))
    concatemer = np.sum((np.abs(heads) % concentration < error).all(axis=-1)) - circular

    if save_output:
        np.save('./data/heads.npy', heads)
        np.save('./data/furthest.npy', furthest)
        output = sys.stdout
        with open('data/output.txt', 'w') as f:
            sys.stdout = f
            print(f"The program started running at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t0_func))}")
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
            # print(f"Rate of circularization: {circular / (N ** 3)}")
            # print(f"Rate of concatemerization: {concatemer / (N ** 3)} ")
            print(f"connected / not connect: {(circular + concatemer) / N ** 3}, which should be {4 * np.pi * error ** 3 / (concentration ** 3 * 3)}")
            print(f"average of furthest distance from tail / length = {furthest_avg} / {length}")
            print(f"It takes {t1_func - t0_func} seconds")
            print(f"The program finished at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t1_func))}")
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
length = 2000
concentration = 29  # distance between every pair of adjacent points
error = 1
num_dir = 360  # number of angles
print_log = 0  # print out heads every loop
save_output = 1  # save output in output.txt

# test_directions(num_dir, get_directions(num_dir))

# simulate(dimension, N, length, concentration, error, num_dir, print_log, save_output)

# increasing distance and fixed DNA length
t0 = time.time()
save_summary = 1
num = 10
start = 35
array_cir = np.zeros(num)
array_con = np.zeros(num)
for j in range(num):
    # print(j)
    concentration = start + j
    for i in range(num):
        temp1, temp2, _ = simulate(dimension, N, length, concentration, error, num_dir, print_log, save_output)
        array_cir[j] += temp1
        array_con[j] += temp2
        print(str(j) + str(i) + ": " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    array_cir[j] /= num
    array_con[j] /= num

# # increasing DNA length and fixed distance
# t0 = time.time()
# save_summary = 1
# num = 10
# array_cir = np.zeros(num)
# array_con = np.zeros(num)
# for j in range(num):
#     # print(j)
#     length = 1000 + j * 1000
#     for i in range(num):
#         temp1, temp2, _ = simulate(dimension, N, length, concentration, error, num_dir, print_log, save_output)
#         array_cir[j] += temp1
#         array_con[j] += temp2
#         print(str(j) + str(i) + ": " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     array_cir[j] /= num
#     array_con[j] /= num

label = []
for i in range(num):
    label.append([array_cir[i], array_con[i]])

if save_summary:
    np.save('./data/circularization.npy', array_cir)
    np.save('./data/concatemerization.npy', array_con)
    print("Data saved")

fig, ax = plt.subplots(figsize=(6, 6))

# plt.subplot(2, 1, 1)
# plt.plot(array_avg)
# plt.xlabel('Simulation Index')
# plt.title('Average Furthest Distance over 100 Simulations with 29 units distance')
# plt.legend()

# plt.subplot(2, 1, 2)
plt.plot(range(start, start + num), [1] * num, color='red')
plt.scatter(range(start, start + num), array_cir / array_con)
for i, l in enumerate(label):
    ax.text(start + i, array_cir[i] / array_con[i], l)
ax.set_title(f"Ratio of Circularization / Concatemerization \nover 100 Simulations for each distance from {start} to {start + 10}")
# ax.set_title("Ratio of Circularization / Concatemerization \nover 100 Simulations for each DNA length from 1k to 10k")
plt.grid(True)

plt.tight_layout()
plt.show()
