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
    temp = False
    if (last == 0).all():
        temp = True
    else:
        phi = np.arcsin(last[2])
        print(last[1] / np.cos(phi))
        theta = np.arcsin(last[1] / np.cos(phi))
        curvy_radius = deg  # = 2pi * r * deg / 2pi = deg
    theta_angles = np.linspace(0, np.pi, num, endpoint=False)
    phi_angles = np.linspace(0, 2 * np.pi, num, endpoint=False)
    d = []
    for i in range(len(theta_angles)):  # angle of xy plane
        for j in range(len(phi_angles)):  # angle of z plane
            if temp or spherical_distance([theta, phi], [theta_angles[i], phi_angles[j]]) > curvy_radius:
                arr = [np.cos(phi_angles[j]) * np.cos(theta_angles[i]),
                       np.cos(phi_angles[j]) * np.sin(theta_angles[i]),
                       np.sin(phi_angles[j])]
                d.append(arr)
    return np.array(d), len(d)


# return the distance over sphere between two points
def spherical_distance(a, b):
    return 2 * np.arcsin(np.sqrt((np.sin(np.abs(a[1] - b[1]) / 2)) ** 2 + np.cos(a[1]) * np.cos(b[1]) * (np.sin(np.abs(a[0] - b[0]) / 2)) ** 2))
