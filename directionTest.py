import numpy as np
import matplotlib.pyplot as plt

# set up all directions
def get_directions(num):
    directions = np.zeros((num * num, dimension))
    angles = np.linspace(0, 2 * np.pi, num, endpoint=False)  # xy
    phi_angles = np.linspace(0, 2 * np.pi, num, endpoint=False)  # z
    for i in range(num):  # angle of xy plane
        for j in range(num):  # angle of z plane
            directions[i * num + j, 2] = np.sin(phi_angles[j])
            directions[i * num + j, 1] = np.cos(phi_angles[j]) * np.sin(angles[i])
            directions[i * num + j, 0] = np.cos(phi_angles[j]) * np.cos(angles[i])
    return directions

# test whether the length is 1 or not
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
            print("!!!repeated!!!")
            print(f"d is {d}")
            repeated_directions = seen[seen.index(temp)]
            print(f"repeated is [{repeated_directions}]")
            print(f"difference is {d - repeated_directions}")
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
    plt.show()


num_dir = 360
dimension = 3
directions = get_directions(num_dir)
test_directions(directions)
visualize_directions(directions)
