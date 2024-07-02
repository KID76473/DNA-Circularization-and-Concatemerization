import matplotlib.pyplot as plt
import mpmath as mp

x_vals =[]
calculated_cir_vals = []

x_vals2 = [500, 1000, 1500, 2000]
simulated_cir_vals_6_directions = [5962/ 100000000, 2127 / 100000000, 1068 / 100000000, 726 / 100000000]
simulated_cir_vals_360_sq_directions = [float(6.428571428571429e-05), float(2.316326530612245e-05), float(1.316326530612245e-05), float(8.061224489795918e-06)]

# i: 500, head: [-27.93062734  16.80206253 -15.2447046 ], cir: 1260.0, cir / num: 6.428571428571429e-05
# i: 1000, head: [-39.54447639  16.40907344 -22.19282782], cir: 454.0, cir / num: 2.316326530612245e-05
# i: 1500, head: [-25.89273202  22.09586016 -41.67371645], cir: 258.0, cir / num: 1.316326530612245e-05
# i: 2000, head: [-24.06138657  17.01622523 -47.10633122], cir: 158.0, cir / num: 8.061224489795918e-06

print(simulated_cir_vals_360_sq_directions)

file = open("data/other_eventual_return_formula_output_3", "r")

for line in file:
    split = line.split()
    x_val = split[1]
    x_val = x_val[:len(x_val) - 1]
    if float(x_val) in x_vals2:
        x_vals.append(float(x_val))
        y_val = split[4]
        calculated_cir_vals.append(float(y_val))

plt.plot(x_vals, calculated_cir_vals, color='blue', marker='o', label = "calculated")

plt.plot(x_vals2, simulated_cir_vals_6_directions, color="red", marker='o', label = "6 dir simulated")

plt.plot(x_vals2, simulated_cir_vals_360_sq_directions, color='green', marker='o', label = "360 dir simulated" )

for i in range(0, 4):
    plt.annotate(f"{round(simulated_cir_vals_360_sq_directions[i], 8)}", (x_vals2[i], simulated_cir_vals_360_sq_directions[i]))
    # plt.annotate(f"{round(simulated_cir_vals[i], 8)}", (x_vals2[i], simulated_cir_vals[i]))


plt.yscale('log')
plt.xlabel('Length')
plt.ylabel('Circularization Probability')
plt.title('DNA Length vs Circularization Probability')
plt.grid(True)
plt.legend()
plt.show()
