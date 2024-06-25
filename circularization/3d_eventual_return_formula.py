import mpmath as mp
import matplotlib.pyplot as plt

#assuming 6 directions of movement
#eventual return to the origin point

leng_start = 0
leng_end = 2000

direction = mp.fdiv(1, 6)

x_vals = []
y_vals = []

mp.dps = 10000

output_file = open("data/eventual_return_formula_output_1", "a")

#even steps have a chance of returning, odd steps will not return
def eventual_ret_for(steps):
    #link to formula:
    #https://dspace.mit.edu/bitstream/handle/1721.1/100853/18-304-spring-2006/contents/projects/randomwalks.pdf
    n = steps // 2
    total_prob = 0
    factor = mp.power(direction, steps)
    possible_config_factor = mp.factorial(steps)
    for i in range(0, n + 1):
        for j in range(0, i + 1):
            z_val = n - j - i
            if (z_val >= 0):
                j_factorial = mp.factorial(j)
                k_factorial = mp.factorial(i)
                z_factorial = mp.factorial(z_val)
                val_1 = mp.fmul(j_factorial, k_factorial)
                val_2 = mp.fmul(val_1, z_factorial)
                denom = mp.power(val_2, 2)
                prob = mp.fdiv(possible_config_factor, denom)
                total_prob = mp.fadd(total_prob, prob)
    total_prob = mp.fmul(total_prob, factor)
    return total_prob

for i in range(leng_start, leng_end + 2, 2): # + 2 to include the upper bound
    x_vals.append(i)
    return_prob = eventual_ret_for(i)
    y_vals.append(return_prob)
    output_file.write(f"length: {i}; return probability: {return_prob} \n")

output_file.close

plt.plot(x_vals, y_vals)
plt.xlabel('length')
plt.ylabel('calculated return probability (circularization)')
plt.title('length vs calculated circularization prob')
plt.grid(True)
plt.show()