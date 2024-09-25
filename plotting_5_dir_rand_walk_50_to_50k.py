import matplotlib.pyplot as plt

# trial: 157600000 

length = [500, 1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000] 

cir = [5077 / 157600000, 1800 / 157600000, 608 / 157600000, 155 / 157600000, 57 / 157600000, 25 / 157600000, 17 / 157600000, 2 / 157600000, 3 / 157600000]

for i in range(len(cir)):
    plt.annotate(f"{round(cir[i], 15)}", (length[i], cir[i]), xycoords='data', xytext=(length[i] * 1.00000001, cir[i] * 1.00001))

plt.plot(length, cir)
plt.grid(True)
plt.show()