import matplotlib.pyplot as plt
import mpmath as mp

x_vals =[]
calculated_cir_vals = []

x_vals2 = [500, 1000, 1500, 2000]
simulated_cir_vals = [5962/ 100000000, 2127 / 100000000, 1068 / 100000000, 726 / 100000000]

print(simulated_cir_vals)

list = [500, 1000, 1500, 2000]

file = open("data/other_eventual_return_formula_output_3", "r")

for line in file:
    split = line.split()
    x_val = split[1]
    x_val = x_val[:len(x_val) - 1]
    if float(x_val) in list:
        x_vals.append(float(x_val))
        y_val = split[4]
        calculated_cir_vals.append(float(y_val))

plt.plot(x_vals, calculated_cir_vals, color='blue', marker='o', label = "calculated")

plt.plot(x_vals2, simulated_cir_vals, color="red", marker='o', label = "simulated")

for i in range(0, len(list)):
    plt.annotate(f"{round(calculated_cir_vals[i], 8)}", (x_vals[i], calculated_cir_vals[i]))
    # plt.annotate(f"{round(simulated_cir_vals[i], 8)}", (x_vals2[i], simulated_cir_vals[i]))


plt.yscale('log')
plt.xlabel('Length')
plt.ylabel('Circularization Probability')
plt.title('DNA Length vs Circularization Probability')
plt.grid(True)
plt.legend()
plt.show()
