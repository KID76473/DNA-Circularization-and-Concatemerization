import random as rand
import time

# random walk
# calculate the distance from the end point to the origin (circularzation)
# claculate distance from end point to an evenly distrubuted point based on 

num_trials = 125000000

len_list = [500, 1000, 2000, 5000, 10000, 20000, 50000]

avg_distance_btw_2_tails = 953.715332748677  # unit is length of nucleotide, this distance is for 300 ug/mL

len_vals = []
cir_vals = []
concat_vals = []

file_output = open("random_walk_even_distr_output.txt", "w")

t0 = time.time()

def random_walk(pos, dir):
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

def helper(pos, value) -> bool:
    for num in pos:
        if abs(num) % value > 1:
            return False
    return True

def helper2(pos) -> bool:
    for num in pos:
        if abs(num) > 1:
            return False
    return True

for num in len_list:
    total_cir = 0
    total_concat = 0
    for i in range(num_trials):
        pos = [0, 0, 0]

        # random walk
        for j in range(0, num):
            direction = rand.randint(0, 5)
            pos = random_walk(pos, direction)

        # final position of the random walk
        if helper2(pos):
            total_cir += 1
        elif helper(pos, avg_distance_btw_2_tails):
            total_concat += 1
        
        if i % 100000 == 0: #making sure the file is running
            print(f"length: {num} distance: {avg_distance_btw_2_tails} total_cir: {total_cir} total_concat: {total_concat} total: {num_trials} \n")
        
    len_vals.append(num)
    cir_vals.append(total_cir)
    concat_vals.append(total_concat)
    file_output.write(f"length: {num} distance: {avg_distance_btw_2_tails} total_cir: {total_cir} total_concat: {total_concat} total: {num_trials} \n")

t1 = time.time()

print(f"time taken: {t1 - t0}")
file_output.write(f"time taken: {t1 - t0}\n")

file_output.close

print(len_vals)
print(avg_distance_btw_2_tails)
print(cir_vals)
print(concat_vals)