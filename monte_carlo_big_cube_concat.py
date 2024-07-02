import mpmath as mp
import random as rand

mp.dps = 100

# universal consts

ava_num = mp.fmul(6.02, mp.power(10, 23))

liter_to_meter_cubed = mp.power(10, -3)

avg_dNTP_mass = 615.96

nucleo_binding_fac = 36.04

len_one_nucleo = mp.fmul(3.4, mp.power(10, -10))

# molarity
num_moles_ds_DNA = mp.power(10, -9)
num_liters = 1

molarity_concen = mp.fdiv(num_moles_ds_DNA, num_liters)
molarity_factor = mp.fdiv(ava_num, liter_to_meter_cubed)

# grams
num_grams = mp.power(10, -6)
num_bp = 2000

grams_concen = mp.fdiv(num_grams, mp.fmul(liter_to_meter_cubed, num_bp))
grams_factor = mp.fdiv(ava_num, mp.fadd(mp.fmul(liter_to_meter_cubed, avg_dNTP_mass), nucleo_binding_fac))


# cube approximation of a nucleotide
num_nucleo_side_length = 50000

num_nucleo_side_len_halved = num_nucleo_side_length / 2

cube_side_len = mp.fmul(num_nucleo_side_length, len_one_nucleo)

vol_cube = mp.power(cube_side_len, 3)

# num of tail calculations

num_tails_molarity = mp.fmul(mp.fmul(molarity_concen, molarity_factor), vol_cube)
print(molarity_concen)
print(molarity_factor)
print(vol_cube)
print(num_tails_molarity)

num_tails_grams = mp.fmul(mp.fmul(grams_concen, grams_factor), vol_cube)

rounded_nums_tails_molarity = mp.floor(num_tails_molarity)

rounded_nums_tails_grams = mp.floor(num_tails_grams)

print(int(rounded_nums_tails_molarity))
print(num_tails_grams)

def comp(list1: list, radius: int):
    result = []
    for i in range(0, len(list1)):
        bool = abs(list1[i]) <= radius
        result.append(bool)
    return result

# monte carlo simulation with a unit sphere around the origin and a big cube around the origin

sphere_radius = 1

num_trials = 10

num_concatemerized = 0

for i in range(num_trials):
    for j in range(int(rounded_nums_tails_molarity)):
        randomly_generated_tail_loc = [rand.uniform(-num_nucleo_side_len_halved, num_nucleo_side_len_halved), rand.uniform(-num_nucleo_side_len_halved, num_nucleo_side_len_halved), rand.uniform(-num_nucleo_side_len_halved, num_nucleo_side_len_halved)]
        if all(comp(randomly_generated_tail_loc, sphere_radius)):
            num_concatemerized += 1