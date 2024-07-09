# assuming a 3d random walk is a 3d normal distribution
# with mean = 0
# variance = 1
# covar = n * (variance ** 2) * I, where n is the # of steps, I is the identity matrix

import numpy as np
import random as rand
import math

# General algorithm:
# generating a head
# generate a tail using np multi normal
# make sure it's not outside the cube, if it is, reroll
# run through the list of heads
# if it is near enoguh to another head: concat
# if it is near enough to own head: cir
# if a head got cir'ed remove it from the list
# if a head got concat'ed remove it from the list
# remove tail as well
# Note: There's a chance a tail or head can directly spawn on an existing head or tail

cir = 0
concat = 0

trials = 1
sphere_radius = 1

# # adjusted_big_cube_vol = mp.power(10, 14)
# adjusted_vol_no_mp = 10 ** 14

# # adjusted_big_cue_side_len = mp.cbrt(adjusted_big_cube_vol)
# adjusted_big_cube_sidelen_no_mp = math.cbrt(adjusted_vol_no_mp)

num_steps = [500, 1000, 2000, 5000, 10000, 20000, 50000]
variance = 1

# number of molecules to simulate:

# idx 0 corresponds to point_one, idx 1 corresponds to one, ...
adjusted_big_cube_vol_list = [10 ** 14, 10 ** 13, 10 ** 12, 10 ** 11, 10 **10]

point_one = [768.4669673998093, 384.25596399823985, 192.13360256693767, 76.8547900261919, 38.42761985159409, 19.2138661359149, 7.68555994485739]
one = [768.4669673998092, 384.25596399823985, 192.13360256693767, 76.85479002619189, 38.42761985159407, 19.2138661359149, 7.685559944857391]
ten = [768.4669673998093, 384.25596399823985, 192.13360256693764, 76.85479002619188, 38.42761985159408, 19.213866135914895, 7.685559944857391] 
one_hundred = [768.4669673998093, 384.2559639982398, 192.13360256693764, 76.85479002619188, 38.42761985159408, 19.2138661359149, 7.68555994485739] 
one_thousand = [768.4669673998094, 384.2559639982399, 192.1336025669377, 76.85479002619189, 38.42761985159408, 19.2138661359149, 7.685559944857394]

# all concentrations in a 10^14 nucleodtide ^ 3 reactor
# point_one = [768.4669673998093, 384.25596399823985, 192.13360256693767, 76.8547900261919, 38.42761985159409, 19.2138661359149, 7.68555994485739]
# one = [7684.669673998092, 3842.5596399823985, 1921.3360256693766, 768.5479002619189, 384.2761985159408, 192.13866135914895, 76.85559944857391]
# ten = [76846.69673998094, 38425.59639982399, 19213.360256693762, 7685.479002619189, 3842.7619851594077, 1921.3866135914895, 768.5559944857391]
# one_hundred = [768466.9673998093, 384255.96399823984, 192133.60256693762, 76854.79002619188, 38427.61985159408, 19213.866135914897, 7685.55994485739]
# one_thousand = [7684669.673998093, 3842559.639982399, 1921336.0256693768, 768547.9002619189, 384276.1985159408, 192138.66135914897, 76855.59944857394]

tails_list = [point_one, one, ten, one_hundred, one_thousand]

file = open("concat_snapshot_model_output", "a")

# returns true if position one is outside position two
def position_comparison(pos_one: list, boundary):
    size = len(pos_one)
    for i in range(0, size):
        if abs(pos_one[i]) >= boundary:
            return True
    return False

def comp_sphere(pos_one: list, pos_two: list, radius: int):
    val1 = (pos_one[0] - pos_two[0]) ** 2
    val2 = (pos_one[1] - pos_two[1]) ** 2
    val3 = (pos_one[2] - pos_two[2]) ** 2
    distance = math.sqrt(val1 + val2 + val3)
    if distance <= radius:
        return True
    else:
        return False

def run(simulated_tails, trials, cube_vol):
    size = len(simulated_tails)
    cir_output = []
    concat_output = []
    adjusted_big_cue_side_len = math.cbrt(cube_vol)
    adjusted_big_cue_side_len_halved = adjusted_big_cue_side_len / 2
    for i in range(size):
        cir = 0
        concat = 0
        tails_count = simulated_tails[i]
        covar = num_steps[i] * np.identity(3) * (variance ** 2)
        for j in range(trials):
            rng = np.random.default_rng()
            heads = []
            tails = []
            for k in range(tails_count):
                # generating random head
                head = [rand.uniform(-adjusted_big_cue_side_len_halved, adjusted_big_cue_side_len_halved), rand.uniform(-adjusted_big_cue_side_len_halved, adjusted_big_cue_side_len_halved), rand.uniform(-adjusted_big_cue_side_len_halved, adjusted_big_cue_side_len_halved)]
                                
                # generating random tail (treating random walk as a trivariate distribution)
                tail = rng.multivariate_normal(head, covar, size=1, method='cholesky')
                
                while position_comparison(tail[0], adjusted_big_cue_side_len_halved):
                    tail = rng.multivariate_normal(head, covar, size=1, method='cholesky')

                heads.append(head)
                tails.append(tail[0])
                
                print(f"heads {heads}\n")
                print(f"tails {tails} \n")

                # checking if interaction happened:
                
                size_heads = len(heads)
                size_tails = len(tails)

                for r in range(size_heads):
                    for s in range(size_tails):
                        # circularization:
                        if r == (size_heads - 1) and r == s:
                            if comp_sphere(tails[s], heads[r], sphere_radius):
                                cir += 1
                                heads.pop()
                                tails.pop()
                                print("cir")

                        # concat:
                        elif comp_sphere(tails[s], heads[r], sphere_radius):
                            concat += 1
                            del heads[r]
                            del tail[s]
                            print("concat")

        cir_output.append(cir)
        concat_output.append(concat)
    return cir_output, concat_output


temp = [10]

temp_cir, temp_concat = run(temp, trials, adjusted_big_cube_vol_list[4])
print(f"cir: {temp_cir} \n")
print(f"concat: {temp_concat} \n")

assert(0)

size = len(tails_list)

for i in range(size):
    temp_cir, temp_concat = run(tails_list[i], trials, adjusted_big_cube_vol_list[i])
    file.write(f"list_num: {i} cir: {temp_cir} concat: {temp_concat}")

file.close()

# covar = num_steps * np.identity(3) * (variance ** 2)

# pts = np.random.multivariate_normal(mean, covar, size=10000000)
# #print(pts)
# for i in range(len(pts)):
#     if all(np.less_equal(np.abs(pts[i]), origin)):
#         cir += 1

# fig = plt.figure()
# ax = fig.add_subplot(projection = '3d')

# ax.scatter(pts[:,0], pts[:, 1], pts[:, 2], '.')

# plt.show()