import math
import random as rand

sphere_radius = 1
num_tails = 10 ** 8

num_trails = 10000

side_len_of_norm_cube = 1.365 * (10 ** 7)
vol_of_cube = side_len_of_norm_cube ** 3
val1 = vol_of_cube / (1.955 * (10 ** 13))
side_len = val1 * (10 ** 8)

def comp_sphere(list: list, radius: int):
    val1 = list[0] ** 2
    val2 = list[1] ** 2
    val3 = list[2] ** 2
    distance = math.sqrt(val1 + val2 + val3)
    if distance <= radius:
        return True
    else:
        return False

def run(num_tails, side_len_halved, radius):
    cir = 0
    for i in range(num_trails):
        for j in range(num_tails):
            tail = [rand.uniform(-side_len_halved, side_len_halved), rand.uniform(-side_len_halved, side_len_halved), rand.uniform(-side_len_halved, side_len_halved)]
            if comp_sphere(tail, radius):
                cir += 1
            if i % 100000 == 0:
                print(f"trial_num {i} tail_num {j} cir {cir}")
    return cir

cir = run(num_tails, side_len / 2, sphere_radius)
file = open("big_cube_concat_24_square", "w")

file.write(f"tail: {num_tails} cir: {cir}")
