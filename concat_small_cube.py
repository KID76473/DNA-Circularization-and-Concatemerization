# documentation:
# calculating the rate of concatemerization by randomly generating a tail in a cube around
# the end point of a 3d random walk
# the dimensions of the cube is dependent on the concentration
# the randomly generated tail can exist on any point in the space
# we say a concat event occured if all pts of the tail and end pt of rand walk are <= 1
# we say a cir event occured if all pts of the start_pos and end pt of rand walk are <=1
# note: this model does not account for the case when the end point is both near the starting_pos and a randomly generated tail

import random as rand
import mpmath as mp 
import time

error = 1

num_trials = 100

concentration = mp.fdiv(1, 5) # 1 molecules per 5 unit^3

domain_space = mp.fdiv(1, concentration)

domain_space_halved = mp.fdiv(domain_space, 2)

len_list = [500, 1000, 1500, 2000]

cir_vals = []
concat_vals = []
concen_vals = []
len_vals = []

start_pos = [0, 0, 0] #[x, y, z]

file_output = open("data/simple_concat", "w")

t0 = time.time()

def random_walk(pos: list, dir: int):
    if dir == 0: #east
        pos[0] += 1
    elif dir == 1: #west
        pos[0] -= 1
    elif dir == 2: #up
        pos[1] += 1
    elif dir == 3: #down
        pos[1] -= 1
    elif dir == 4: #z up
        pos[2] += 1
    elif dir == 5: #z down
        pos[2] -= 1 
    return pos

#list1 and list2 must be of equal length
def list_comp(list1: list, list2: list):
    result = []
    for i in range(0, len(list1)):
        val = abs(list1[i] - list2[i])
        bool = val < error
        result.append(bool)
    return result


for num in len_list:
    total_cir = 0
    total_concat = 0
    for i in range(num_trials + 1):
        pos = [0, 0, 0]

        # 3d rand walk
        for j in range(0, num):
            direction = rand.randint(0, 5)
            pos = random_walk(pos, direction)

        # cir case
        cir_result = list_comp(start_pos, pos)
        if all(cir_result):
            total_cir += 1
            continue

        cube_boundaries = []

        # 0 and 3 for idx = 0, 1 and 4 for idx = 1, 2 and 5 for idx = 2
        for i in range(0, 6):
            idx = i % 3
            if (i % 2 == 0): #even
                val = pos[idx] - domain_space_halved
                cube_boundaries.append(val)
            else:
                val = pos[idx] + domain_space_halved
                cube_boundaries.append(val)

        # generating a random tail
        x_pos = rand.uniform(cube_boundaries[0], cube_boundaries[3])
        y_pos = rand.uniform(cube_boundaries[4], cube_boundaries[1])
        z_pos = rand.uniform(cube_boundaries[2], cube_boundaries[5])
        tail = [x_pos, y_pos, z_pos]
        
        #for debugging
        print(f"pos {pos}")
        print(f"tail {tail}")
        print(f"domain half {domain_space_halved}")
        print(f"0 {cube_boundaries[0]}")
        print(f"3 {cube_boundaries[3]}")

        # concat case
        concat_result = list_comp(pos, tail)

        if all(concat_result):
            total_concat += 1
            #for debugging
            # print("concat")

        # making sure the file is running
        # if i % 100000 == 0:
        #     print(f"length: {num} total_cir: {total_cir} total: {num_trials} \n")
        
    cir_vals.append(total_cir)
    concat_vals.append(total_concat)
    concen_vals.append(concentration)
    len_vals.append(num)
    file_output.write(f"length: {num} total_cir: {total_cir} total_concat: {total_concat} concentration: {concentration} total: {num_trials} \n")


t1 = time.time()

print(f"time taken: {t1 - t0}")
print(f"total_cir {cir_vals}")
print(f"total_concat {concat_vals}")
print(f"conc {concen_vals}")
print(f"len {len_list}")

file_output.write(f"time taken: {t1 - t0}\n")

file_output.close