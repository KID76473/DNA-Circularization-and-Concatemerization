import numpy as np
import matplotlib.pyplot as plt


concentrations = np.load("./data/dist_btw_nucleotides.npy")
c_len = len(concentrations)
length_index = 5
length_list = [500, 1000, 2000, 5000, 10000, 20000, 50000]
length = length_list[length_index]
array_cir = np.load('./data/circularization.npy')
array_con = np.load('./data/concatemerization.npy')

label = []
for i in range(c_len):
    label.append([array_cir[i], array_con[i]])

fig, ax = plt.subplots(figsize=(6, 6))

# plt.subplot(2, 1, 1)
# plt.plot(array_avg)
# plt.xlabel('Simulation Index')
# plt.title('Average Furthest Distance over 100 Simulations with 29 units distance')
# plt.legend()

# plt.subplot(2, 1, 2)
plt.plot(concentrations[:, length_index], [1] * c_len, color='red')
if 0 in array_con:
    plt.scatter(concentrations[:, length_index], array_cir, c='blue', label='cir')
    plt.scatter(concentrations[:, length_index], array_con, c='black', label='con')
else:
    plt.scatter(concentrations[:, length_index], array_cir / array_con)
    for i, l in enumerate(label):
        ax.text(concentrations[i][length_index], array_cir[i] / array_con[i], l)
ax.set_title(f"Ratio of Cir / Con \nover 100 Simulations for length = {length}nu")
# ax.set_title("Ratio of Circularization / Concatemerization \nover 100 Simulations for each DNA length from 1k to 10k")
plt.grid(True)

plt.tight_layout()
plt.legend()
plt.show()
