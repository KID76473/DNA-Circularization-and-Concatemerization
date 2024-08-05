import numpy as np
import matplotlib.pyplot as plt


# heads = np.load('data/heads.npy')
# furthest = np.load('data/furthest.npy')
# cir = np.load('data/circularization.npy')
# con = np.load('data/concatemerization.npy')
#
# num = 10
# print(f"circularization: {cir}")
# print(f"concatemerization: {con}")
#
# label = []
# for i in range(num):
#     label.append([cir[i], con[i]])
#
# fig, ax = plt.subplots(figsize=(6, 6))
#
# plt.plot(range(24, 24 + num), [1] * num, color='red')
# plt.scatter(range(24, 24 + num), cir / con)
# plt.xlabel("Distance between DNA Molecule(10 simulations for every distance)")
# plt.ylabel("Ratio of Circularization / Concatemerization")
# # ax.set_title("Ratio of Circularization / Concatemerization \nover 100 Simulations for each distance from 24 to 34")
# ax.set_title("Ratio of Circularization / Concatemerization \nover 100 Simulations for each DNA length from 1k to 10k")
#
# for i, l in enumerate(label):
#     ax.text(24 + i, cir[i] / con[i], l)
#
# plt.grid(True)
# plt.show()

direction_set = np.load('./data/direction_set.npy', allow_pickle=True)
indices = np.load('./data/indices.npy')
# print(np.shape(direction_set))
print(direction_set)
print(indices)
index = np.where(indices == [0, 1, 0])
print(index)
