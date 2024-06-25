import matplotlib.pyplot as plt

x_vals =[]
y_vals = []

list = [500, 1000, 1500, 2000]

file = open("data/monte_carlo_out", "r")

for line in file:
    split = line.split()
    x_val = split[1]
    x_val = x_val[:len(x_val) - 1]
    if float(x_val) in list:
        x_vals.append(float(x_val))
        y_val = split[3]
        y_vals.append(float(y_val))

plt.plot(x_vals, y_vals, color='blue', marker='o')

for i in range(0, len(list)):
    plt.annotate(f"{round(y_vals[i], 12)}", (x_vals[i], y_vals[i]))

plt.yscale('log')
plt.xlabel('Concentration of DNA (distance)')
plt.ylabel('Calculated Concatemerization Probability')
plt.title('Concentration of DNA vs Calculated Concat. Probability')
plt.grid(True)
plt.show()
