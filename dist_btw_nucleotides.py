import mpmath as mp

len_of_nucleo = mp.fmul(3.4, mp.power(10, -10))

one_milli = mp.power(10, -3)

one_micro = mp.power(10, -6)

vol_of_standard_reactor = mp.fmul(100, one_micro)

# for reference:
# grams_list = [1e-07, 1e-07, 1e-07, 1e-07, 1e-07, 1e-07, 1e-07, 1e-06, 1e-06, 1e-06, 1e-06, 1e-06, 1e-06, 1e-06, 9.999999999999999e-06, 9.999999999999999e-06, 9.999999999999999e-06, 9.999999999999999e-06, 9.999999999999999e-06, 9.999999999999999e-06, 9.999999999999999e-06, 9.999999999999999e-05, 9.999999999999999e-05, 9.999999999999999e-05, 9.999999999999999e-05, 9.999999999999999e-05, 9.999999999999999e-05, 9.999999999999999e-05, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
# length_list = [500, 1000, 2000, 5000, 10000, 20000, 50000, 500, 1000, 2000, 5000, 10000, 20000, 50000, 500, 1000, 2000, 5000, 10000, 20000, 50000, 500, 1000, 2000, 5000, 10000, 20000, 50000, 500, 1000, 2000, 5000, 10000, 20000, 50000]

num_tails_grams_list = [
    [1.9544436711e+10, 9.7727900978e+09, 4.8865379969e+09, 1.9546495079e+09, 9.7733047227e+08, 4.8866666573e+08, 1.9546700939e+08],
    [1.95444367118e+11, 9.77279009781e+10, 4.88653799692e+10, 1.9546495079e+10, 9.77330472273e+09, 4.88666665729e+09, 1.95467009396e+09],
    [1.9544436711802e+12, 9.772790097806e+11, 4.886537996923e+11, 1.9546495079e+11, 9.773304722725e+10, 4.886666657294e+10, 1.954670093957e+10],
    [1.95444367118024e+13, 9.77279009780647e+12, 4.88653799692398e+12, 1.95464950790043e+12, 9.77330472272514e+11, 4.88666665729379e+11, 1.95467009395707e+11],
    [1.9544436711802406e+14, 9.772790097806469e+13, 4.88653799692398e+13, 1.9546495079004263e+13, 9.77330472272514e+12, 4.88666665729379e+12, 1.954670093957069e+12]
]

# finding the side length (in nucleotides) of the cube in simulated from the vol_of_standard_reactor

vol_standard_in_mtrs_cubed = mp.fmul(vol_of_standard_reactor, one_milli)
side_len_of_sim_cub = mp.cbrt(vol_standard_in_mtrs_cubed)
num_nucleo_side_len = mp.fdiv(side_len_of_sim_cub, len_of_nucleo)

total_vol = mp.power(num_nucleo_side_len, 3)

avg_dist_btw_2_nuc = []

for i in range(len(num_tails_grams_list)):
    avg_dist_btw_2_nuc.append([])
    for num in num_tails_grams_list[i]:
        vol_per_nuc = mp.fdiv(total_vol, num)
        dist_btw_2_nuc = mp.cbrt(vol_per_nuc)
        avg_dist_btw_2_nuc[i].append(float(dist_btw_2_nuc))

with open("data/dist_btw_nucleotides", "w") as file:
    for x in avg_dist_btw_2_nuc:
        file.write(f"{x}\n")

def get_data():
    return avg_dist_btw_2_nuc
