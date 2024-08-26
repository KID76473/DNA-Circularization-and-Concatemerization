import numpy as np
import scipy


def sphere_volume(r: float) -> float:
    return 4 * np.pi * r ** 3 / 3


def container_volume(h: float) -> float:
    return np.pi * 0.0088 ** 2 * h


radius = 1  # radius of error
height = 0.05  # 0.15m at max
# V = container_volume(height)
V = 0.1  # mL
molar_mass = 487  # g / # of molecules
num_tails_grams_list = [
    [1.9544436711e+10, 9.7727900978e+09, 4.8865379969e+09, 1.9546495079e+09, 9.7733047227e+08, 4.8866666573e+08, 1.9546700939e+08],
    [1.95444367118e+11, 9.77279009781e+10, 4.88653799692e+10, 1.9546495079e+10, 9.77330472273e+09, 4.88666665729e+09, 1.95467009396e+09],
    [1.9544436711802e+12, 9.772790097806e+11, 4.886537996923e+11, 1.9546495079e+11, 9.773304722725e+10, 4.886666657294e+10, 1.954670093957e+10],
    [1.95444367118024e+13, 9.77279009780647e+12, 4.88653799692398e+12, 1.95464950790043e+12, 9.77330472272514e+11, 4.88666665729379e+11, 1.95467009395707e+11],
    [1.9544436711802406e+14, 9.772790097806469e+13, 4.88653799692398e+13, 1.9546495079004263e+13, 9.77330472272514e+12, 4.88666665729379e+12, 1.954670093957069e+12]
]
length_list = [500, 1000, 2000, 5000, 10000, 20000, 50000]


# fixed length
# calculate concentration
result_concentration = []
for l in length_list:
    sigma_sq = l * (1 / 3) ** 2
    fun = lambda x: x ** 2 * np.exp(- x ** 2 / (2 * sigma_sq)) / (2 * np.pi * sigma_sq) ** (3 / 2)
    integral = scipy.integrate.quad(fun, 0, 1)
    # print(integral[0])
    n = V * integral[0] / (4 * np.pi * radius ** 3 / 3)
    result_concentration.append(n * molar_mass / V)

print("Concentration in molar per mL:")
print(result_concentration)

# fixed concentration
# calculate length

