import numpy as np
import matplotlib.pyplot as plt

n = 10000
length = 10
scatter = [[], []]

for _ in range(n):
    tail = [0, 0]
    for _ in range(length):
        if np.random.choice([1, -1]) == 1:
            tail[0] += np.random.choice([1, -1])
        else:
            tail[1] += np.random.choice([1, -1])
    # print(tail)
    scatter[0].append(tail[0])
    scatter[1].append(tail[1])

plt.scatter(scatter[0], scatter[1])
plt.scatter(0, 0, c='#FF0000')
scale = 20
plt.xlim([-scale, scale])
plt.ylim([-scale, scale])
plt.show()
