import numpy as np


heads = np.load('heads.npy')
print(heads[0, 0, 0])

furthest = np.load('furthest.npy')
print(furthest[0, 0, 0])

cir = np.load('circularization.npy')
print(f"circularization: {cir}")

con = np.load('concatemerization.npy')
print(f"concatemerization: {con}")
