import mpmath as mp
import random as rand
import time

mp.dps = 1000

# universal consts

ava_num = mp.fmul(6.02, mp.power(10, 23))

liter_to_meter_cubed = mp.power(10, -3)

avg_dNTP_mass = 615.96

nucleo_binding_fac = 36.04

len_one_nucleo = mp.fmul(3.4, mp.power(10, -10))

one_nano_gram = mp.power(10, -9)

one_micro_gram = mp.power(10, -6)

# simulation consts

sphere_radius = 1

num_trials = 1

# molarity
num_moles_ds_DNA_list = [one_nano_gram, mp.fmul(50, one_nano_gram), mp.fmul(100, one_nano_gram)]
num_liters_list = [1, 1, 1]

molarity_concen_list = []
molarity_factor_list = []

size = len(num_moles_ds_DNA_list)

for i in range(size):
    molarity_concen = mp.fdiv(num_moles_ds_DNA_list[i], num_liters_list[i])
    molarity_factor = mp.fdiv(ava_num, liter_to_meter_cubed)
    molarity_concen_list.append(molarity_concen)
    molarity_factor_list.append(molarity_factor)

# grams
num_grams_list = [one_micro_gram, mp.fmul(50, one_micro_gram), mp.fmul(100, one_micro_gram)]
num_bp_list = [500, 500, 500]

grams_concen_list = []
grams_factor_list = []

size = len(num_grams_list)

for i in range(size):
    num_grams = num_grams_list[i]
    num_bp = num_bp_list[i]
    grams_concen = mp.fdiv(num_grams, mp.fmul(liter_to_meter_cubed, num_bp))
    grams_factor = mp.fdiv(ava_num, mp.fadd(mp.fmul(liter_to_meter_cubed, avg_dNTP_mass), nucleo_binding_fac))
    grams_concen_list.append(grams_concen)
    grams_factor_list.append(grams_factor)


# cube approximation of a nucleotide
num_nucleo_side_length = 50000

num_nucleotides_tube = mp.fmul(5.84, mp.power(10, 7))

num_nucleo_side_len_halved = num_nucleo_side_length / 2 # change here

cube_side_len = mp.fmul(num_nucleo_side_length, len_one_nucleo)

vol_cube = mp.power(cube_side_len, 3)

vol_of_quarter_test_tube = mp.fmul(7.85398163, mp.power(10, -6))

vol = vol_cube # change here

# num of tail calculations

num_tails_molarity_list = []

num_tails_grams_list = []

size = len(molarity_concen_list)

for i in range(0, size):
    molarity_conc = molarity_concen_list[i]
    molarity_factor = molarity_factor_list[i]
    num_tails_molarity = mp.fmul(mp.fmul(molarity_conc, molarity_factor), vol)
    num_tails_molarity_list.append(int(mp.floor(num_tails_molarity)))

size = len(grams_concen_list)

for i in range(size):
    grams_concen = grams_concen_list[i]
    grams_factor = grams_factor_list[i]
    num_tails_grams = mp.fmul(mp.fmul(grams_concen, grams_factor), vol)
    num_tails_grams_list.append(int(mp.floor(num_tails_grams)))

print(num_tails_molarity_list)
print(num_tails_grams_list)


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
    distance = mp.cbrt(val2)
    if distance <= radius:
        return True
    else:
        return False

# monte carlo simulation with a unit cube around the origin and a big cube around the origin


def monte_carlo_simulation(radius: int, num_trials: int, num_tails_list: list):
    output = []
    for i in range(len(num_tails_list)):
        num_concatemerized = 0
        round_num_tails = num_tails_list[i]
        for j in range(num_trials):
            for k in range(int(round_num_tails)):
                randomly_generated_tail_loc = [rand.uniform(-num_nucleo_side_len_halved, num_nucleo_side_len_halved), rand.uniform(-num_nucleo_side_len_halved, num_nucleo_side_len_halved), rand.uniform(-num_nucleo_side_len_halved, num_nucleo_side_len_halved)]
                # if all(comp_cube(randomly_generated_tail_loc, radius)):
                #     num_concatemerized += 1
                with open("file.txt", 'a') as file:
                    file.write(str(randomly_generated_tail_loc) + "\n")
                if comp_sphere(randomly_generated_tail_loc, radius):
                    num_concatemerized += 1
        output.append(num_concatemerized)
    return output

x_vals = num_grams_list

t0 = time.time()

y_vals = monte_carlo_simulation(sphere_radius, num_trials, num_tails_grams_list)
print(y_vals)

t1 = time.time()

print(f"time: {t1 - t0}")
