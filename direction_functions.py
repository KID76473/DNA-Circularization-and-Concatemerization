import numpy as np


def get_6_directions():
    return [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]


def get_5_directions(last):
    arr = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    arr = np.delete(arr, last)
    return arr


# set up all directions
def get_directions(num):
    d = np.zeros((num * num, 3))
    angles = np.linspace(0, 2 * np.pi, num, endpoint=False)  # xy
    phi_angles = np.linspace(0, 2 * np.pi, num, endpoint=False)  # z
    for i in range(num):  # angle of xy plane
        for j in range(num):  # angle of z plane
            d[i * num + j, 2] = np.sin(phi_angles[j])
            d[i * num + j, 1] = np.cos(phi_angles[j]) * np.sin(angles[i])
            d[i * num + j, 0] = np.cos(phi_angles[j]) * np.cos(angles[i])
    return d


# generates directions based on last step
def get_propelled_directions(num, last, deg):
    if (last == 0).all():
        theta_angles = np.linspace(0, 2 * np.pi, num, endpoint=False)
        phi_angles = np.linspace(0, 2 * np.pi, num, endpoint=False)
    else:
        phi = np.arcsin(last[2])
        theta = np.arcsin(last[1] / np.cos(phi))
        theta_angles = helper(np.linspace(0, 2 * np.pi, num, endpoint=False), theta - deg, theta + deg)
        phi_angles = helper(np.linspace(0, 2 * np.pi, num, endpoint=False), phi - deg, phi + deg)
    d = []
    for i in range(len(theta_angles)):  # angle of xy plane
        for j in range(len(phi_angles)):  # angle of z plane
            arr = [np.cos(phi_angles[j]) * np.cos(theta_angles[i]),
                   np.cos(phi_angles[j]) * np.sin(theta_angles[i]),
                   np.sin(phi_angles[j])]
            d.append(arr)
    return np.array(d)


# removes propelled angles
def helper(angles, a, b):
    if a < 0 or b >= 2 * np.pi:  # range out of 0 or 2pi
        if a < 0:
            temp = a
            a = b
            b = temp + 2 * np.pi
        elif b >= 2 * np.pi:
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
        i = 0
        while i < len(angles):
            if a < angles[i] < b:
                angles = np.delete(angles, i)
            else:
                i += 1
    return angles
