import math
from numba import njit
import numpy as np
import haversine


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
def fibonacci_sphere(last, deg, samples=1000):
    remain_all = False  # exclude some directions too closed to last direction
    if (last == 0).all():
        remain_all = True  # remain all direction if it is the first step
    dist = deg  # = 2pi * r * deg / 2pi = deg
    points = []
    out = []
    phi = math.pi * (math.sqrt(5.) - 1.)  # golden angle in radians

    p2 = np.arccos(last[2])
    # t2 = np.arcsin(last[1] / np.sin(p2))
    t2 = np.arctan2(last[1], last[0])
    pos2 = to_degree([t2, p2])

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = math.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        p1 = np.arccos(z)
        # t1 = np.arcsin(y / np.sin(p1))
        t1 = np.arctan2(y, x)
        pos1 = to_degree([t1, p1])

        if remain_all or haversine.haversine(pos1, pos2) / 6371.008 > dist:
            points.append([x, y, z])
        #     print(f"in: {pos1, [x, y, z]}")
        # else:
        #     out.append([x, y, z])
        #     print("!!!!!!!!!!!!!!!!!!!!")
        #     print(f"out: {pos1, [x, y, z]}")
        # print(f"hav | deg: {haversine.haversine(pos1, pos2) / 6371.008} | {deg}")
        # print("------------------------")

    return np.array(points), len(points), np.array(out)


# Convert radian to degree. Return [lat, lon] which equals to [phi, theta]
def to_degree(rad):  # rad[0] is theta, and rad[1] is phi
    if rad[0] < 0:
        rad[0] += 2 * np.pi
    elif rad[0] > 2 * np.pi:
        rad[0] -= 2 * np.pi
    if rad[1] < 0:
        rad[1] += np.pi
    elif rad[1] > np.pi:
        rad[1] -= np.pi
    lat = rad[1] * 180 / np.pi - 90
    lon = rad[0] * 180 / np.pi - 180
    return [lat, lon]
