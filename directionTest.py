import time
import random
import numpy as np
import matplotlib.pyplot as plt
import direction_functions


# test whether the length is 1 or not and repetition
def test_directions(directions):
    seen = [[]]
    repeated = 0
    for d in directions:  # determine precision
        # print("-------------------------------")
        # print(d, type(d))
        temp = [d[0], d[1], d[2]]
        # print(type(temp))
        if temp not in seen:
            seen.append(temp)
        else:
            # print("!!!repeated!!!")
            # print(f"d is {d}")
            # repeated_directions = seen[seen.index(temp)]
            # print(f"repeated is [{repeated_directions}]")
            # print(f"difference is {d - repeated_directions}")
            repeated += 1
    # print(len(seen))
    print(f"repeated: {repeated}, overall: {len(directions)}, ratio: {repeated / len(directions)}")


# Visualize the directions
def visualize_directions(directions, rand=np.array([0, 0, 0]), out_points=np.array([]), annotate=False):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plotting the direction points
    ax.scatter(directions[:, 0], directions[:, 1], directions[:, 2])
    ax.scatter(rand[0], rand[1], rand[2], color='r')
    if len(out_points) != 0:
        ax.scatter(out_points[:, 0], out_points[:, 1], out_points[:, 2], color='y')

    # Annotating the direction points
    if annotate:
        for i in range(directions.shape[0]):
            ax.text(directions[i, 0], directions[i, 1], directions[i, 2],
                    f'({directions[i, 0]:.2f}, {directions[i, 1]:.2f}, {directions[i, 2]:.2f})',
                    size=10, zorder=1, color='k')
        if (rand != 0).all():
            ax.text(rand[0], rand[1], rand[2],
                    f'({rand[0]:.2f}, {rand[1]:.2f}, {rand[2]:.2f})',
                    size=10, zorder=1, color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_box_aspect([1, 1, 1])
    plt.show()


# with warnings.catch_warnings(record=True) as w:
#     warnings.simplefilter("always")
#     num_dir = 90  # hemispheres are off if num_dir is odd
#     input = direction_functions.get_directions(num_dir)
#     for d in input:
#         # print(d)
#         directions = direction_functions.fibonacci_sphere(d, np.pi / 6, samples=2000)
#         print(directions[random.randint(0, len(directions) - 1)])
#         # print(np.size(directions))
#         # test_directions(directions)
#         print("--------------------------------------")
#     # print(directions)
#     # print(len(directions))
#     for warning in w:
#         print(f"Warning detected: {warning.message}")

# # test distance between two points over sphere
# p1 = np.array([0, 0], dtype='float64')
# p2 = np.array([np.pi / 2, np.pi], dtype='float64')
# print(f"{direction_functions.my_way(p1, p2)} my way")
# print(f"{direction_functions.spherical_distance(p1, p2)} given way")
# print(f"{direction_functions.another_way(p1, p2)} another way")

# # visualization
# # one specific dir
origin = np.array([0, 0, 0])
# last_dir = np.array([0, 0.707, 0.707])
# last_dir = np.array([1 / np.sqrt(3), 1 / np.sqrt(3), 1 / np.sqrt(3)])
# last_dir = np.array([1 / 2, 1 / 3, -1 / 3])
# last_dir = np.array([np.sqrt(2), -np.sqrt(2), 0])
# last_dir = [0.08766495,  0.05693028, -0.9945219]

# choose one random dir
all_dirs = direction_functions.get_directions(360)
rand_dir = all_dirs[np.random.choice(360 ** 2)]
print(f"the last direction is: {rand_dir}")
print("-------------------------------------")

# rand_dir = np.array([0.99558784,  0.03476669, -0.08715574])

p = np.arccos(rand_dir[2])
t = np.arcsin(rand_dir[1] / np.sin(p))
print(f"theta: {t}, phi: {p}")
print(f"to degree: {direction_functions.to_degree([t, p])}")

dir_fib, _, out = direction_functions.fibonacci_sphere(rand_dir, np.pi / 5, samples=2000)
# print(np.shape(dir_lattice), np.shape(dir_fib))
visualize_directions(dir_fib, rand_dir, out)

# # speed
# t0 = time.time()
# last = np.array([0, 0, 0], dtype='float32')
# head = np.array([0, 0, 0], dtype='float32')
# for _ in range(2000):
#     temp, length = direction_functions.fibonacci_sphere(last, np.pi / 5)
#     temp = temp[np.random.choice(length)]
#     head += temp
#     last = temp
#     print(head)
# t1 = time.time()
# print(t1 - t0)
# # 1000: 13s 2.1s with numba
# # 2000: 25s  2.8s with numba
# # 4000: 51s 3.7s with numba
