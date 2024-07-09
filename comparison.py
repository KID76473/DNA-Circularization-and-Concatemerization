import numpy as np
import mpmath as mp


mp.dps = 50
edge = mp.mpf(1.365e7)
v_all = mp.power(edge, 3)
v_sphere = mp.fmul(mp.mpf(4), mp.pi / mp.mpf(3))
length = [500, 1000, 2000, 5000, 10000, 20000, 50000]
data = np.array([
    [1.95E+10, 9.77E+09, 4.89E+09, 1.95E+09, 9.77E+08, 4.89E+08, 1.95E+08],
    [1.95E+11, 9.77E+10, 4.89E+10, 1.95E+10, 9.77E+09, 4.89E+09, 1.95E+09],
    [1.95E+12, 9.77E+11, 4.89E+11, 1.95E+11, 9.77E+10, 4.89E+10, 1.95E+10],
    [1.95E+13, 9.77E+12, 4.89E+12, 1.95E+12, 9.77E+11, 4.89E+11, 1.95E+11],
    [1.95E+14, 9.77E+13, 4.89E+13, 1.95E+13, 9.77E+12, 4.89E+12, 1.95E+12]
])

model1, model2 = [], []

for i in range(len(data)):
    temp1, temp2 = [], []
    for j in range(len(data[i])):
        temp1.append(mp.fdiv(mp.fmul(data[i][j], v_sphere), v_all))
        temp2.append(1 - (mp.power(1 - mp.fdiv(v_sphere, v_all), data[i][j])))
    model1.append(temp1)
    model2.append(temp2)

print(model1)
print(model2)
