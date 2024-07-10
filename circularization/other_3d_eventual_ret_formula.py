import mpmath as mp
import time
import matplotlib.pyplot as plt

#assuming 6 directions of movement
#eventual return to the origin point

length = [50000]
direction = mp.fdiv(1, 6)

x_vals = []
y_vals = []

mp.dps = 10000

output_file = open("other_eventual_return_formula_output_4", "a")

#even steps have a chance of returning, odd steps will not return
def eventual_ret_for(steps):
    #formula:
    #https://math.dartmouth.edu/~prob/prob/prob.pdf pg 486
    #https://sites.math.washington.edu/~morrow/336_19/papers19/Legrand.pdf
    n = steps // 2
    total_prob = 0
    factor = mp.power(direction, steps)
    possible_config_factor = mp.factorial(steps)
    for i in range(0, n + 1):
        for j in range(0, n + 1):
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
        if i % 100 == 0:
            print(i)
    total_prob = mp.fmul(total_prob, factor)
    return total_prob

t0 = time.time()

for num in length: # + 2 to include the upper bound
    x_vals.append(num)
    return_prob = eventual_ret_for(num)
    y_vals.append(return_prob)
    output_file.write(f"length: {num}; return probability: {return_prob} \n")

t1 = time.time()

print(f"time: {t1 - t0}")

plt.plot(x_vals, y_vals)
plt.xlabel('length')
plt.ylabel('calculated return probability (circularization)')
plt.title('length vs calculated circularization prob')
plt.grid(True)
plt.show()