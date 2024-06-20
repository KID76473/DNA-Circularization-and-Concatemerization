import numpy as np
import matplotlib.pyplot as plt
import sys

radius = 1 #closeness of DNA spheres where concatemerization happens
conc_start = 1 #smaller the conc val (denoting the distance between 2 DNA spheres) the greater the concentration
conc_end = 1000

output_filename = open("monte_carlo_out", "a")

x_vals = []
y_vals = []

for conc in range(conc_start, conc_end + 1):
    #monte carlo formula based on conc of DNA spheres
    num = 4 * np.pi * radius ** 3 
    denom = 3 * conc ** 3
    concat_val = num / denom
    output_filename.write(f"conc: {conc}; concat_value: {concat_val} \n")
    x_vals.append(conc)
    y_vals.append(concat_val)

plt.plot(x_vals, y_vals)
plt.xlabel('concentration')
plt.ylabel('concatemerization value (monte carlo)')
plt.title('concat. val vs. concentration')
plt.grid(True)
plt.show()
