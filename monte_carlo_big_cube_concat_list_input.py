import mpmath as mp
import random as rand
import time

mp.dps = 1000

# universal consts

ava_num = mp.fmul(6.02, mp.power(10, 23))

avg_dNTP_mass = 615.96

nucleo_binding_fac = 36.04

len_of_nucleo = mp.fmul(3.4, mp.power(10, -10))

one_milli = mp.power(10, -3)

one_micro = mp.power(10, -6)

vol_of_standard_reactor = mp.fmul(100, one_micro)

# simulation consts

sphere_radius = 1

num_trials = 10000

# grams / Liter
input_num_grams_list = [mp.fmul(.1, one_micro), one_micro, mp.fmul(10, one_micro), mp.fmul(100, one_micro), mp.fmul(1000, one_micro)]
input_num_bp_list = [500, 1000, 2000, 5000, 10000, 20000, 50000]

num_grams = len(input_num_grams_list)
num_bp = len(input_num_bp_list)

grams_concentration_list = []
grams_list = []

num_bp_list = [input_num_bp_list * 5][0]

for i in range(0, num_grams):
    for j in range(0, num_bp):
        concentration = input_num_grams_list[i] / one_milli
        grams_list.append(float(input_num_grams_list[i]))
        grams_concentration_list.append(float(concentration))


# molarity
molarity_list = []


# calculating input molarity from lengths and grams/Liter concentration
for i in range(0, num_grams):
    for j in range(0, num_bp):
        grams = input_num_grams_list[i]
        denominator = mp.fadd(mp.fmul(input_num_bp_list[j], avg_dNTP_mass), nucleo_binding_fac)
        moles = mp.fdiv(grams, denominator)
        molarity = mp.fdiv(moles, one_milli)
        molarity_list.append(float(molarity))

# num of tail calculations (same in number in both lists)

num_tails_grams_list = []

num_tails_molarity_list = []

for i in range(0, num_grams):
    for j in range(0, num_bp):
        grams = input_num_grams_list[i]

        denominator = mp.fadd(mp.fmul(input_num_bp_list[j], avg_dNTP_mass), nucleo_binding_fac)
        
        num_moles = mp.fdiv(grams, denominator)
        
        num_molecules = mp.fmul(num_moles, ava_num)
        
        concentration = mp.fdiv(num_molecules, one_milli)
        
        num_simulated_tails = mp.fmul(concentration, vol_of_standard_reactor)
        
        num_tails_grams_list.append(float(num_simulated_tails))

for num in molarity_list:
    num_simulated_tails_molarity = mp.fmul(mp.fmul(num, ava_num), vol_of_standard_reactor)
    num_tails_molarity_list.append(float(num_simulated_tails_molarity))

# finding the side length (in nucleotides) of the cube in simulated from the vol_of_standard_reactor

vol_standard_in_mtrs_cubed = mp.fmul(vol_of_standard_reactor, one_milli)
side_len_of_sim_cub = mp.cbrt(vol_standard_in_mtrs_cubed)
num_nucleo_side_len = mp.fdiv(side_len_of_sim_cub, len_of_nucleo)
num_nucleo_side_len_halved = num_nucleo_side_len / 2

# unit shape comparisons

def comp_cube(list: list, radius: int):
    result = []
    size = len(list)
    for i in range(0, size):
        bool = abs(list[i]) <= radius
        result.append(bool)
    return result


def comp_sphere(list: list, radius: int):
    val1 = mp.fadd(mp.power(list[0], 2), mp.power(list[1], 2))
    val2 = mp.fadd(val1, mp.power(list[2], 2))
    distance = mp.sqrt(val2)
    if distance <= radius:
        return True
    else:
        return False

# monte carlo simulation with a unit shape around the origin and a big cube around the origin

output_file = open("real_world_big_cube_concat_00_10k_trials", "a")

def monte_carlo_simulation(radius: int, num_trials: int, num_tails_list: list, file):
    output = []
    size = len(num_tails_list)
    for i in range(0, 1):
        num_concatemerized = 0
        round_num_tails = int(num_tails_list[i])
        print(round_num_tails)
        for j in range(num_trials):
            for k in range(round_num_tails):
                randomly_generated_tail_loc = [rand.uniform(-num_nucleo_side_len_halved, num_nucleo_side_len_halved), rand.uniform(-num_nucleo_side_len_halved, num_nucleo_side_len_halved), rand.uniform(-num_nucleo_side_len_halved, num_nucleo_side_len_halved)]
                # if all(comp_cube(randomly_generated_tail_loc, radius)):
                #     num_concatemerized += 1
                # with open("file.txt", 'a') as file:
                #     file.write(str(randomly_generated_tail_loc) + "\n")
                if comp_sphere(randomly_generated_tail_loc, radius):
                    num_concatemerized += 1
                if k % 100000 == 0:
                    file.write(round_num_tails, j, k, num_concatemerized)
        output.append(num_concatemerized)
        file.write(round_num_tails, num_concatemerized, num_trials)
    return output

x_vals = input_num_grams_list

t0 = time.time()

y_vals = monte_carlo_simulation(sphere_radius, num_trials, num_tails_grams_list, output_file)

t1 = time.time()

print(f"time: {t1 - t0}")
print(f"x_vals {x_vals} \n")
print(f"y_vals {y_vals}")