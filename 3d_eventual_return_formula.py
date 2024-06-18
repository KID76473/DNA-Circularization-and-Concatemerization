import math as ma

#even steps have a chance of returning, odd steps will not return
def eventual_ret_for(steps):
    n = steps / 2
    prob = 0
    factor = (1 / 6) ** steps
    possible_config_factor = ma.factorial(steps)
    for i in range(0, n):
        for j in range(0, i):
            j_factorial = ma.factorial(j)
            k_factorial = ma.factorial(i)
            z_factorial = ma.factorial(n - j - i)
            val = (possible_config_factor) / ((j_factorial * k_factorial * z_factorial) ** 2)
            prob = prob + (factor * val)
    return prob