import random as rand
import time

trials = 10000000

lengths = [500, 1000, 1500, 2000, 5000, 10000, 20000, 50000]

dir_list = [-3, -2, -1, 1, 2, 3]

output_file = open("3d_ran_walk_vol_exclu_6_dir.txt", "w")

generated_output_file = open("3d_ran_walk_vol_exlcu_6_dir_paths.txt", "w")

#list1 and list2 must be of equal length
def list_comp(list1: list, list2: list):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

# 6 direction
def rand_walk(pos : list):
    dir = rand.choice(dir_list)
    if dir == -3: #east
        pos[0] += 1
    elif dir == -2: # y up
        pos[1] += 1
    elif dir == -1: #z up
        pos[2] += 1
    elif dir == 3: #west
        pos[0] -= 1
    elif dir == 2: # y down
        pos[1] -= 1
    elif dir == 1: #z down
        pos[2] -= 1 
    return pos

def run(lengths, trials):
    start_pt = (0,0,0)
    output_cir_count = []
    output_failed_gens = []
    output_generated = []

    for num in lengths:
        i = 0
        cir_count = 0
        failed_gens = 0
        generated = []
        #temp = []

        while i < trials:
            pos = start_pt # start
            
            pos_of_existing_nucleos = set()

            for j in range(1, num + 1):
                save_pos = pos
                pos = rand_walk(list(pos))

                counter = 0
                while counter < 100 and tuple(pos) in pos_of_existing_nucleos:
                    pos = rand_walk(list(save_pos))
                    counter += 1

                # no where to ggenerate the next pt (failed attempt)
                if counter >= 100 and tuple(pos) in pos_of_existing_nucleos:
                    i = i - 1
                    failed_gens += 1
                    break

                pos_of_existing_nucleos.add(tuple(pos))
                #temp.append(pos)
                
                # cir event
                if j == num and list_comp(pos, list(start_pt)):
                    cir_count += 1

                # early origin (failed attempt)
                if j != num and list_comp(pos, list(start_pt)):
                    i = i - 1
                    failed_gens += 1
                    break

                if j == num:
                    generated.append(pos)

            if i % 100000 == 0:
                print(f"kkjkj length {num} trial_num {i} cir_count {output_cir_count} failed_gens {output_failed_gens}")

            i += 1
        
        output_cir_count.append(cir_count)
        output_failed_gens.append(failed_gens)
        output_generated.append(generated)

    print(f"length {num} trial_num {i} cir_count {output_cir_count} failed_gens {output_failed_gens}")

    return output_cir_count, output_failed_gens, output_generated

t0 = time.time()

cir_count, failed_gens, generated = run(lengths, trials)

t1 = time.time()

print(f"time {t1 - t0}")
print(cir_count)
print(failed_gens)

output_file.write(f"time {t1 - t0} \n")
output_file.write(f"lengths {lengths} \n")
output_file.write(f"trials {trials} \n")
output_file.write(f"output_cir_count {cir_count} \n")
output_file.write(f"output_failed_gens {failed_gens} \n")
generated_output_file.write(f"generated {generated} \n")

output_file.close()
generated_output_file.close()

