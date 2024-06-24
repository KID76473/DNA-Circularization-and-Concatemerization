import matplotlib.pyplot as plt

x_vals =[]
y_vals = []

file = open("data/other_eventual_return_formula_output_3", "r")

for line in file:
    split = line.split()
    x_val = split[1]
    x_val = x_val[:len(x_val) - 1]
    x_vals.append(float(x_val))
    y_val = split[4]
    y_vals.append(float(y_val))

plt.plot(x_vals, y_vals)
plt.yscale('log')
plt.xlabel('length')
plt.ylabel('calculated return probability (circularization)')
plt.title('length vs calculated circularization prob')
plt.grid(True)
plt.show()
