import numpy as np
import matplotlib.pyplot as plt


heads = np.load('heads.npy')
furthest = np.load('furthest.npy')
cir = np.load('circularization.npy')
con = np.load('concatemerization.npy')

num = 10
print(f"circularization: {cir}")
print(f"concatemerization: {con}")

label = []
for i in range(num):
    label.append([cir[i], con[i]])

fig, ax = plt.subplots()

plt.plot(range(24, 24 + num), [1] * num, color='red')
plt.scatter(range(24, 24 + num), cir / con)
plt.xlabel("Distance between DNA Molecule(10 simulations for every distance)")
plt.ylabel("Ratio of Circularization / Concatemerization")
ax.set_title("Ratio of Circularization / Concatemerization \nover 10 Simulations for each distance from 24 to 34")

for i, l in enumerate(label):
    ax.text(24 + i, cir[i] / con[i], l)

plt.grid(True)
plt.show()
