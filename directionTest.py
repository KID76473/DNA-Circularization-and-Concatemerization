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


num_dir = 60  # off if odd
# directions = get_directions(num_dir)
# directions = direction_functions.get_propelled_directions(num_dir, np.array([0, 1, 0]), np.pi / 6)
directions = direction_functions.another_way(num_dir, np.array([0, 1, 0]), np.pi / 2)
# print(directions)
# print(len(directions))
test_directions(directions)
visualize_directions(directions)
