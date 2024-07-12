# assuming a 3d random walk is a 3d normal distribution
# with mean = 0
# variance = 1
# covar = n * I, where n is the # of steps, I is the identity matrix

import numpy as np
import random as rand
import math
from numba import njit
import time

# General algorithm:
# generating a head
# generate a tail using np multi normal
# make sure it's inside the cube
# run through the list of heads
# if it is near enoguh to another head: concat
# if it is near enough to own head: cir
# if a head got cir'ed remove it from the list
# if a head got concat'ed remove it from the list
# remove tail as well
# Note: There's a chance a tail or head can directly spawn on an existing head or tail

trials = 1
sphere_radius = 1

num_steps = [500, 1000, 2000, 5000, 10000, 20000, 50000]
variance = 1

# number of molecules to simulate:

adjusted_number_of_tails_list = [9.605837092497614, 9.606399099955997, 9.606680128346882, 7.685479002619189, 3.8427619851594077, 1.9213866135914897, 7.685559944857391]

point_one_cube_vol = [1250000000000.0, 2500000000000.0, 5000000000000.0, 10000000000000.0, 10000000000000.0, 10000000000000.0, 100000000000000.0]
one_cube_vol = [125000000000.0, 250000000000.0, 500000000000.0, 1000000000000.0, 1000000000000.0, 1000000000000.0, 10000000000000.0]
ten_cube_vol = [12500000000.0, 25000000000.0, 50000000000.0, 100000000000.0, 100000000000.0, 100000000000.0, 1000000000000.0]
one_hundred_cube_vol = [1250000000.0, 2500000000.0, 5000000000.0, 10000000000.0, 10000000000.0, 10000000000.0, 100000000000.0]
one_thousand_cube_vol = [125000000.0, 250000000.0, 500000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 10000000000.0]

cube_vol_list = [point_one_cube_vol, one_cube_vol, ten_cube_vol, one_hundred_cube_vol, one_thousand_cube_vol]

file = open("concat_snapshot_model_output.txt", "w")

# returns true if position one is outside position two
@njit
def position_comparison(pos_one: list, boundary):
    size = len(pos_one)
    for i in range(0, size):
        if abs(pos_one[i]) >= boundary:
            return True
    return False

@njit
def list_equality(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

@njit
def comp_sphere(pos_one: list, pos_two: list, radius: int):
    val1 = (pos_one[0] - pos_two[0]) ** 2
    val2 = (pos_one[1] - pos_two[1]) ** 2
    val3 = (pos_one[2] - pos_two[2]) ** 2
    distance = np.sqrt(val1 + val2 + val3)
    if distance <= radius:
        return True
    else:
        return False


def run(simulated_vols, trials, tails_list):
    size = len(simulated_vols)
    cir_output = []
    concat_output = []
    for i in range(size):
        adjusted_big_cue_side_len = math.cbrt(simulated_vols[i])
        adjusted_big_cue_side_len_halved = adjusted_big_cue_side_len / 2
        shadow_realm = [-adjusted_big_cue_side_len, adjusted_big_cue_side_len, adjusted_big_cue_side_len]
        cir_event = 0
        concat_event = 0
        tails_count = round(tails_list[i])
        covar = num_steps[i] * np.identity(3)
        #print(f"boundary {adjusted_big_cue_side_len_halved}")
        for j in range(trials):
            rng = np.random.default_rng()
            heads = []
            tails = []
            for k in range(tails_count):
                # generating random head
                head = [rand.uniform(-adjusted_big_cue_side_len_halved, adjusted_big_cue_side_len_halved), 
                        rand.uniform(-adjusted_big_cue_side_len_halved, adjusted_big_cue_side_len_halved), 
                        rand.uniform(-adjusted_big_cue_side_len_halved, adjusted_big_cue_side_len_halved)]
                                
                # generating random tail (treating random walk as a trivariate distribution)
                tail = rng.multivariate_normal(head, covar, size = 1, method='cholesky')
                
                while position_comparison(tail[0], adjusted_big_cue_side_len_halved):
                    tail = rng.multivariate_normal(head, covar, size = 1, method='cholesky')

                heads.append(head)
                tails.append(tail[0])

                # print(f"head {heads} \n tail {tails}")

                # checking if interaction happened:
                
                size_heads = len(heads)
                size_tails = len(tails)

                for r in range(size_heads):

                    # this head had already had an event, it will not be able to have another event with another tail
                    if list_equality(shadow_realm, heads[r]):
                        continue
                    
                    for s in range(size_tails):

                        #this tail already had an event, it will not have another event
                        if list_equality(shadow_realm, tails[s]):
                            continue

                        # circularization:
                        if r == (size_heads - 1) and r == s:
                            if comp_sphere(tails[s], heads[r], sphere_radius):
                                # print(f"circularized! head {heads[r]} \n tail {tails[s]}")
                                cir_event += 1
                                tails[s] = shadow_realm
                                heads[r] = shadow_realm

                        # concat:
                        elif comp_sphere(tails[s], heads[r], sphere_radius):
                            # print(f"concatemerized! head {heads[r]} \n tail {tails[s]}")
                            concat_event += 1
                            tails[s] = shadow_realm
                            heads[r] = shadow_realm
            
            if j % 100000 == 0:
                print(j, cir_output, concat_output)
            # print(f"cir_count {cir_event} concat_count {concat_event} \n heads {heads} tails {tails}")
            # print("------")

        cir_output.append(cir_event)
        concat_output.append(concat_event)
    return cir_output, concat_output

size = len(cube_vol_list)

t0 = time.time()

for i in range(size):
    temp_cir, temp_concat = run(cube_vol_list[i], trials, adjusted_number_of_tails_list)
    print(i, temp_cir, temp_concat)
    file.write(f"list_num: {i} cir: {temp_cir} concat: {temp_concat} \n")

t1 = time.time()

print(f"time {t1 - t0}")

file.write(f"time {t1 - t0}")

file.close()
