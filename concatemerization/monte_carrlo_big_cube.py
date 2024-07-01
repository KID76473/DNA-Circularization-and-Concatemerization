import numpy as np


N = 64
dimensions = 3
concentrations = np.arange(2, 21, 19)
positions = np.zeros((N, N, N, dimensions))
num = 100000000000
concat = np.zeros(19)
error = 1

with open("../data/big_cube", 'w') as f:
    f.write("Started running\n")

i = 0
while i < num:
    for c in range(len(concentrations)):
        positions = np.random.uniform(concentrations[c] * 10, size=(N, N, N, dimensions))
        concat[c] = np.sum((positions < error).all(axis=-1))
    n = 10000
    # write the result to file every 100000 loops
    if i % n == 0:
        with open("../data/big_cube", 'a') as f:
            f.write(f"{i} loops\n")
            f.write(str(positions) + "\n")
    i += 1
concat /= i
print(concat)
