import numpy as np
import matplotlib.pyplot as plt
N = 64
years = 1000
density = 100
Tails = np.zeros((N,N,N,3),dtype = np.int8)
record = np.zeros(years)
Gate = np.ones((N,N,N,3),dtype = np.int8)
count = np.sum(Gate)
for i in range(years):
    Tails += Gate * np.random.choice([-1,1],(N,N,N,3), p=[0.5,0.5])
    delta = ((Tails%density) == 0)
    d = delta[:,:,:,0] * delta[:,:,:,1] * delta[:,:,:,2]
    Gate = (np.ones((N,N,N),dtype = np.int8) - d)[..., np.newaxis]
    record[i] = np.sum(Gate)
    if i%100 == 0:
        print(i,np.sum(Gate))
plt.plot(np.array(range(years)), record)
plt.show()