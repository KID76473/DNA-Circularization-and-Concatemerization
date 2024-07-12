import warnings
warnings.filterwarnings('always', category=RuntimeWarning)
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
def visualize_directions(directions):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(directions[:, 0], directions[:, 1], directions[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_box_aspect([1, 1, 1])
    plt.show()


with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    num_dir = 90  # hemispheres are off if num_dir is odd
    input = direction_functions.get_directions(num_dir)
    for d in input:
        # print(d)
        directions = direction_functions.fibonacci_sphere(np.array([0, 0.707, 0.707]), np.pi / 6, samples=2000)
        # print(directions[random.randint(0, length - 1)])
        # print(np.size(directions))
        # test_directions(directions)
        print("--------------------------------------")
    # print(directions)
    # print(len(directions))
    for warning in w:
        print(f"Warning detected: {warning.message}")

# directions = direction_functions.fibonacci_sphere(np.array([0, 0.707, 0.707]), np.pi / 6, samples=2000)
# # print(np.shape(directions))
# visualize_directions(directions)
