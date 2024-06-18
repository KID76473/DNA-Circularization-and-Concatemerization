import numpy as np

radius = 1 #closeness of DNA spheres where concatemerization happens
conc_start = 1
conc_end = 100

for conc in range(conc_start, conc_end + 1):
    #monte carlo formula based on conc of DNA spheres
    num = 4 * np.pi * radius ** 3 
    denom = 3 * conc ** 3
    print(f"conc: {conc}; concat_value: {num / denom}")