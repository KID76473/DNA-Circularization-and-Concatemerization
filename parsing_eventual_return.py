import matplotlib.pyplot as plt

x_vals =[]
y_vals = []

list = [500, 1000, 1500, 2000]

file = open("data/other_eventual_return_formula_output_3", "r")

for line in file:
    split = line.split()
    x_val = split[1]
    x_val = x_val[:len(x_val) - 1]
    if float(x_val) in list:
        x_vals.append(float(x_val))
        y_val = split[4]
        y_vals.append(float(y_val))

plt.plot(x_vals, y_vals, color='blue', marker='o')

for i in range(0, len(list)):
    plt.annotate(f"{round(y_vals[i], 10)}", (x_vals[i], y_vals[i]))

plt.yscale('log')
plt.xlabel('Length of DNA (nt)')
plt.ylabel('Calculated Return Probability (self-circularization)')
plt.title('Length of DNA vs Calculated Return Probability')
plt.grid(True)
plt.show()
