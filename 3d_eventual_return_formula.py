import math as ma
import matplotlib.pyplot as plt
from decimal import Decimal

leng_start = 0
leng_end = 900

x_vals = []
y_vals = []

output_file = open("eventual_return_formula_output", "a")

#even steps have a chance of returning, odd steps will not return
def eventual_ret_for(steps):
    #link to formula:
    #https://dspace.mit.edu/bitstream/handle/1721.1/100853/18-304-spring-2006/contents/projects/randomwalks.pdf
    n = (int) (steps / 2)
    total_prob = 0
    factor = Decimal((1 / 6) ** steps)
    possible_config_factor = ma.factorial(steps)
    for i in range(0, n):
        for j in range(0, i):
            j_factorial = Decimal(ma.factorial(j))
            k_factorial = Decimal(ma.factorial(i))
            z_val = n - j - i
            if (z_val < 0):
                z_val = 0
            z_factorial = Decimal(ma.factorial(z_val))
            val = j_factorial * k_factorial * z_factorial
            denom = val ** 2
            prob = (possible_config_factor) / (denom)
            total_prob = total_prob + prob
    total_prob = total_prob * factor
    return total_prob

for i in range(leng_start, leng_end):
    x_vals.append(i)
    return_prob = 0
    if (i % 2 == 0): #even
        return_prob = eventual_ret_for(i)
    y_vals.append(return_prob)
    output_file.write(f"length: {i}; return probability: {return_prob} \n")

plt.plot(x_vals, y_vals)
plt.xlabel('length')
plt.ylabel('calculated return probability (circularization)')
plt.title('length vs calculated circularization prob')
plt.grid(True)
plt.show()