import mpmath as mp
import math

cir = 0
concat = 0

ten_to_the_seven = mp.power(10, 7)
big_cube_vol = mp.power(mp.fmul(1.365, ten_to_the_seven), 3)

adjusted_big_cube_vol = 10 ** 14
adjusted_big_cue_side_len = math.cbrt(adjusted_big_cube_vol)

# number of molecules to simulate:

point_one = [19544436711.802406, 9772790097.806469, 4886537996.92398, 1954649507.9004269, 977330472.2725142, 488666665.72937894, 195467009.39570683]
one = [195444367118.02405, 97727900978.0647, 48865379969.2398, 19546495079.004265, 9773304722.72514, 4886666657.29379, 1954670093.9570687]
ten = [1954443671180.2407, 977279009780.647, 488653799692.39795, 195464950790.04263, 97733047227.2514, 48866666572.9379, 19546700939.570686]
one_hundred = [19544436711802.406, 9772790097806.469, 4886537996923.9795, 1954649507900.4263, 977330472272.5142, 488666665729.37897, 195467009395.70682]
one_thousand = [195444367118024.1, 97727900978064.7, 48865379969239.805, 19546495079004.266, 9773304722725.14, 4886666657293.79, 1954670093957.069]

tails_list = [point_one, one, ten, one_hundred, one_thousand]

adjusted_vol_list = []

adjusted_tails_list = []

file = open("adjusted_tails_calculations", "w")

size = len(tails_list)

for i in range(size):
    temp_adjusted_vol_list = []
    temp = []
    tails = tails_list[i]
    mulitple = 1
    if i >= 1:
        mulitple = 10
    adjusted_big_cube_vol = adjusted_big_cube_vol / mulitple
    for tail in tails:
        count = 1
        temp_adjusted_vol = adjusted_big_cube_vol
        adjusted_tail_count = mp.fmul(mp.fdiv(tail, big_cube_vol), adjusted_big_cube_vol)

        while adjusted_tail_count > 10:
            temp_adjusted_vol = adjusted_big_cube_vol / (10 * count)
            adjusted_tail_count = mp.fmul(mp.fdiv(tail, big_cube_vol), temp_adjusted_vol)
            count += 1

        temp_adjusted_vol_list.append(temp_adjusted_vol)
        temp.append(float(adjusted_tail_count))
    
    adjusted_tails_list.append(temp)
    adjusted_vol_list.append(temp_adjusted_vol_list)

file.write(f"adjusted_tail_counts: {adjusted_tails_list} \n")
file.write(f"adjusted_vol: {adjusted_vol_list}")