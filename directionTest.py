import numpy as np
import matplotlib.pyplot as plt


# set up all directions
def get_directions(num):
    d = np.zeros((num * num, dimension))
    angles = np.linspace(0, 2 * np.pi, num, endpoint=False)  # xy
    phi_angles = np.linspace(0, 2 * np.pi, num, endpoint=False)  # z
    for i in range(num):  # angle of xy plane
        for j in range(num):  # angle of z plane
            d[i * num + j, 2] = np.sin(phi_angles[j])
            d[i * num + j, 1] = np.cos(phi_angles[j]) * np.sin(angles[i])
            d[i * num + j, 0] = np.cos(phi_angles[j]) * np.cos(angles[i])
    return d


def get_propelled_directions(num, last, deg):
    phi = np.arcsin(last[2])
    theta = np.arcsin(last[1] / np.cos(phi))
    # print(theta, phi, deg)
    theta_angles = helper(np.linspace(0, 2 * np.pi, num, endpoint=False), theta - deg, theta + deg)
    phi_angles = helper(np.linspace(0, 2 * np.pi, num, endpoint=False), phi - deg, phi + deg)
    d = []
    print(len(theta_angles), len(phi_angles))
    for i in range(len(theta_angles)):  # angle of xy plane
        for j in range(len(phi_angles)):  # angle of z plane
            arr = [np.cos(phi_angles[j]) * np.cos(theta_angles[i]),
                   np.cos(phi_angles[j]) * np.sin(theta_angles[i]),
                   np.sin(phi_angles[j])]
            d.append(arr)
    return np.array(d)


def helper(angles, a, b):
    if a < 0:
        print("a < 0")
        temp = a
        a = b
        b = temp + 2 * np.pi
        i = 0
        while i < len(angles):
            if a > angles[i] or angles[i] > b:
                angles = np.delete(angles, i)
            else:
                i += 1
    elif b >= 2 * np.pi:
        print("b > 2pi")
        temp = b
        b = a
        a = 2 * np.pi - temp
        i = 0
        while i < len(angles):
            if a > angles[i] or angles[i] > b:
                angles = np.delete(angles, i)
            else:
                i += 1
    else:
        print("in the range")
        print(a, b)
        i = 0
        while i < len(angles):
            print(angles[i])
            if a < angles[i] < b:
                angles = np.delete(angles, i)
            else:
                i += 1
    return angles


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
    plt.show()


num_dir = 30
dimension = 3
# directions = get_directions(num_dir)
directions = get_propelled_directions(num_dir, [0, 1, 0], np.pi / 2)
# print(directions)
test_directions(directions)
# print(len(directions))
visualize_directions(directions)
