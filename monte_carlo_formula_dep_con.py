import numpy as np
import sys

radius = 1 #closeness of DNA spheres where concatemerization happens
conc_start = 1
conc_end = 200

output_filename = open("monte_carlo_out", "a")

for conc in range(conc_start, conc_end + 1):
    #monte carlo formula based on conc of DNA spheres
    num = 4 * np.pi * radius ** 3 
    denom = 3 * conc ** 3
    output_filename.write(f"conc: {conc}; concat_value: {num / denom} \n")