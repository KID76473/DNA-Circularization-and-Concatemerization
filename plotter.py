import numpy as np
import matplotlib.pyplot as plt

# Lists to store cir/num values for each interval
cir_num_500 = []
cir_num_1000 = []
cir_num_1500 = []
cir_num_2000 = []

# Process each file
for i in range(32):
    filename = f"output_thread_{i}.txt"
    with open(filename, 'r') as file:
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

# Calculate the average cir/num for each interval
avg_cir_num_500 = np.mean(cir_num_500)
avg_cir_num_1000 = np.mean(cir_num_1000)
avg_cir_num_1500 = np.mean(cir_num_1500)
avg_cir_num_2000 = np.mean(cir_num_2000)

# Create the plot
x = [500, 1000, 1500, 2000]
y = [avg_cir_num_500, avg_cir_num_1000, avg_cir_num_1500, avg_cir_num_2000]

plt.plot(x, y, marker='o')
plt.xlabel('i')
plt.ylabel('Average cir/num')
plt.title('Average cir/num vs. i')
plt.grid(True)
plt.show()
