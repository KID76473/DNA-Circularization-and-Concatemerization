import numpy as np

def distance_calculator(pos_one: list, pos_two: list):
    val1 = (pos_one[0] - pos_two[0]) ** 2
    val2 = (pos_one[1] - pos_two[1]) ** 2
    val3 = (pos_one[2] - pos_two[2]) ** 2
    distance = np.sqrt(val1 + val2 + val3)
    return distance

length = 500
covar = length * np.identity(3)

rng = np.random.default_rng()
point = rng.multivariate_normal([0,0,0], covar, size = 1, method='cholesky')

distance = distance_calculator(point[0], [0,0,0])

print(f"point {point} \n")
print(f"distance from origin {distance}")
print(f"sqrt(3) = {np.sqrt(3)}")
print(f"factor {distance / np.sqrt(3)}")


