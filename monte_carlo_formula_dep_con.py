import numpy as np
import sys

radius = 1 #closeness of DNA spheres where concatemerization happens
conc_start = 1
conc_end = 200

output_filename = open("monte_carlo_out", "a")

for conc in range(conc_start, conc_end + 1):
    #monte carlo formula based on conc of DNA spheres
    #link to formula: 
    #https://dspace.mit.edu/bitstream/handle/1721.1/100853/18-304-spring-2006/contents/projects/randomwalks.pdf
    num = 4 * np.pi * radius ** 3 
    denom = 3 * conc ** 3
    output_filename.write(f"conc: {conc}; concat_value: {num / denom} \n")

