import numpy as np
import matplotlib.pyplot as plt


# Lists to store cir/num values for each interval
cir_num_500 = []
cir_num_1000 = []
cir_num_1500 = []
cir_num_2000 = []

num_500 = []
num_1000 = []
num_1500 = []
num_2000 = []

# Process each file
for i in range(32):
    cir_filename = f"data/output_thread_{i}.txt"  # circularization
    con_filename = f"data/concat_thread_{i}.txt"  # concatemerization
    with open(cir_filename, 'r') as file:
        lines = file.readlines()
        # Extract the relevant lines (last 4-5 lines)
        for line in lines[-8:]:
            if "i: 500" in line:
                cir_num_500.append(float(line.split()[-1]))
            elif "i: 1000" in line:
                cir_num_1000.append(float(line.split()[-1]))
            elif "i: 1500" in line:
                cir_num_1500.append(float(line.split()[-1]))
            elif "i: 2000" in line:
                cir_num_2000.append(float(line.split()[-1]))
    with open(con_filename, 'r') as file:
        lines = file.readlines()
        # Extract the relevant lines (last 4-5 lines)
        for line in lines[-8:]:
            if "i: 500" in line:
                num_500.append(float(line.split()[-1]))
            elif "i: 1000" in line:
                num_1000.append(float(line.split()[-1]))
            elif "i: 1500" in line:
                num_1500.append(float(line.split()[-1]))
            elif "i: 2000" in line:
                num_2000.append(float(line.split()[-1]))

# Calculate the average cir/num for each interval
avg_cir_num_500 = np.mean(cir_num_500)
avg_cir_num_1000 = np.mean(cir_num_1000)
avg_cir_num_1500 = np.mean(cir_num_1500)
avg_cir_num_2000 = np.mean(cir_num_2000)

avg_num_500 = np.mean(num_500) - avg_cir_num_500
avg_num_1000 = np.mean(num_1000) - avg_cir_num_1000
avg_num_1500 = np.mean(num_1500) - avg_cir_num_1500
avg_num_2000 = np.mean(num_2000) - avg_cir_num_2000

# Create the plot
x = [500, 1000, 1500, 2000]
y_cir = [avg_cir_num_500, avg_cir_num_1000, avg_cir_num_1500, avg_cir_num_2000]
y_con = [avg_num_500, avg_num_1000, avg_num_1500, avg_num_2000]

plt.plot(x, y_cir, marker='o', color='blue', label='circularization')
plt.plot(x, y_con, marker='o', color='red', label='Concatemerization')
for i in range(len(x)):
    plt.annotate(y_cir[i], (x[i], y_cir[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(y_con[i], (x[i], y_con[i]), textcoords="offset points", xytext=(0,-10), ha='center')
plt.xlabel('Steps')
plt.ylabel('Probability of Circularization and Concatemerization')
plt.title('Probability of Circularization and Concatemerizationvs. Steps')
plt.grid(True)
plt.legend()
plt.show()
