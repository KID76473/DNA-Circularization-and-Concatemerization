import numpy as np
from numba import jit

point_one_avg_dist_btw_2_nuc = [5068.117754597808, 6385.303716748203, 8044.900114186083, 10918.5454132389,
                                    13756.478370729503, 17332.059770040003, 23523.210422361073]
one_avg_dist_btw_2_nuc = [2352.4118777175854, 2963.7954430884633, 3734.1118537536295, 5067.939846938371,
                              6385.191639541378, 8044.829509212695, 10918.507082715489]
ten_avg_dist_btw_2_nuc = [1091.8928703672013, 1375.671983375185, 1733.221188384396, 2352.32930029704,
                              2963.743421457293, 3734.0790818280216, 5067.9220554854255]
one_hundred_avg_dist_btw_2_nuc = [506.8117754597808, 638.5303716748203, 804.4900114186083, 1091.8545413238903,
                                      1375.6478370729503, 1733.2059770040003, 2352.3210422361076]
one_thous_avg_dist_btw_2_nuc = [235.24118777175855, 296.37954430884633, 373.41118537536295, 506.7939846938371,
                                    638.5191639541378, 804.4829509212694, 1091.850708271549]

concens = [point_one_avg_dist_btw_2_nuc, one_avg_dist_btw_2_nuc, ten_avg_dist_btw_2_nuc, one_hundred_avg_dist_btw_2_nuc, one_thous_avg_dist_btw_2_nuc]


# @jit
def func(concentrations: list):
    N = 64
    dimensions = 3

    num = 1000000
    concat = np.zeros(19)
    error = 1

    with open("../data/big_cube_real_world_values", 'w') as f:
        f.write("Started running\n")

    i = 0
    while i < num:
        for c in range(len(concentrations)):
            positions = np.random.uniform(0, concentrations[c], size=(N, N, N, dimensions))
            concat[c] += np.sum((positions < error).all(axis=-1))
        n = 10000
        # write the result to file every 100000 loops
        if i % n == 0:
            write_file(i, concat, concentrations)
            # print(f"{i} loops")
            # print(str(concat / i) + "\n")
        i += 1
    file = open("../data/big_cube_real_world_values", 'a')
    file.write("---------")


def write_file(i, concat, concentrations):
    with open("../data/big_cube_real_world_values", 'a') as f:
        f.write(f"{i} loops\n")
        # f.write(str(positions) + "\n")
        for c in range(len(concentrations)):
            f.write(str(concentrations[c]) + ": " + str(concat[c] / ((i + 1) * 64 ^ 3)) + "\n")


for concs in concens:
    func(concs)
