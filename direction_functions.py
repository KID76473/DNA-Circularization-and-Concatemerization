import math
import numpy as np
from numba import njit


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
@njit
def fibonacci_sphere(last, deg, samples=1000):
    remain_all = False  # exclude some directions too closed to last direction
    if (last == 0).all():
        remain_all = True  # remain all direction if it is the first step
    dist = deg  # = 2pi * r * deg / 2pi = deg
    points = []
    phi = math.pi * (math.sqrt(5.) - 1.)  # golden angle in radians
    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = math.sqrt(1 - y * y)  # radius at y
        theta = phi * i  # golden angle increment
        x = math.cos(theta) * radius
        z = math.sin(theta) * radius
        p1 = np.arcsin(z)
        t1 = np.arcsin(y / np.cos(p1))
        p2 = np.arcsin(last[2])
        t2 = np.arcsin(last[1] / np.cos(p2))
        if remain_all or spherical_distance([t1, p1], [t2, p2]) > dist:
            points.append((x, y, z))
    return np.array(points), len(points)


# return the distance over sphere between two points
@njit
def spherical_distance(a, b):
    return 2 * np.arcsin(np.sqrt((np.sin(np.abs(a[1] - b[1]) / 2)) ** 2 + np.cos(a[1]) * np.cos(b[1]) * (np.sin(np.abs(a[0] - b[0]) / 2)) ** 2))
    # lat1, lon1 = a
    # lat2, lon2 = b
    #
    # delta_lat = lat2 - lat1
    # delta_lon = lon2 - lon1
    #
    # sin_lat = np.sin(delta_lat / 2) ** 2
    # sin_lon = np.sin(delta_lon / 2) ** 2
    # cos_lat1 = np.cos(lat1)
    # cos_lat2 = np.cos(lat2)
    #
    # a = sin_lat + cos_lat1 * cos_lat2 * sin_lon
    # c = 2 * np.arcsin(np.sqrt(a))
    # # try:
    # #     if a < 0:
    # #         print("222222222222222222222222222222222222222222222222")
    # #     c = 2 * np.arcsin(np.sqrt(a))
    # # except ValueError as e:
    # #     raise ValueError(f"Invalid input from inner to arcsin: {a}. Details: {e}")
    #
    # return c