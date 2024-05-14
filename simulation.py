import time
import numpy as np
import matplotlib.pyplot as plt


# dimension = 3 N = 64 length = 1000 concentration = 10 num_ang = 360
dimension = 3
N = 8  # number of molecules = N^3
length = 1000
concentration = 10  # distance between every pair of adjacent points
heads = np.zeros((N, N, N, dimension))
leftover = np.zeros(length)  # # of dna that does not circularize and concatenate
terminate = np.ones((N, N, N, dimension))
# count = np.sum(terminate)
num_cir = []
num_con = []

num_ang = 9  # number of angles
angles = np.linspace(0, 2 * np.pi, num_ang, endpoint=False)
directions = np.zeros((num_ang ** 2, dimension))
# print(np.shape(directions))
for i in range(num_ang):  # angle of xy plane
    for j in range(num_ang):  # angle of z plane
        directions[i * num_ang + j, 2] = np.sin(angles[j])
        directions[i * num_ang + j, 1] = np.cos(angles[j]) * np.sin(angles[i])
        directions[i * num_ang + j, 0] = np.cos(angles[j]) * np.cos(angles[i])
print(directions)

# for i in range(num_ang ** 2):  # determine precision
#     print(np.abs(directions[i, 0] ** 2 + directions[i, 1] ** 2 + directions[i, 2] ** 2 - 1) < 0.001)

t0 = time.time()

error = 0.00001
for i in range(length):  # length
    # print(i)

    # heads += terminate * np.random.choice([-1, 1], (N, N, N, dimension), p=[0.5, 0.5])  # step further randomly for each one
    # heads += terminate * directions[np.random.choice(range(num_ang ** 2)), :]
    for x in range(N):
        for y in range(N):
            for z in range(N):
                heads[x, y, z] += terminate[x, y, z] * directions[np.random.choice(range(num_ang ** 2))]
    # heads += terminate * np.random.choice(directions, (N, N, N, dimension), p=[1 / num_ang ** 2] * num_ang ** 2)
    # print("-------------------------------")
    # print(f"the {i}th step")
    # print("heads")
    # print(heads)

    # count # of circularization
    circular = (np.abs(heads - np.ones((N, N, N, dimension))) < error)  # true if any dimension is at 100x
    circular = circular[:, :, :, 0] * circular[:, :, :, 1] * circular[:, :, :, 2]  # all dimensions must be at 100 x
    num_cir.append(np.sum(circular))
    # print(f"circular: {np.sum(circular)}")

    # count # of concatemerization
    concatemer = (np.abs(heads % concentration - np.ones((N, N, N, dimension))) < error)
    concatemer = concatemer[:, :, :, 0] * concatemer[:, :, :, 1] * concatemer[:, :, :, 2]
    concatemer = concatemer.astype(float)
    concatemer -= circular.astype(float)
    num_con.append(np.sum(concatemer))
    # print(f"concatemer: {np.sum(concatemer)}")

    # terminate = (np.ones((N, N, N), dtype=np.int8) - circular)[..., np.newaxis]
    terminate = (np.ones((N, N, N), dtype=np.int8) - circular - concatemer)[..., np.newaxis]
    leftover[i] = np.sum(terminate)  # count how may dna do not meet self or others
    # if i % 100 == 0:  # print every 100 length
    #     print(i, np.sum(terminate))

t1 = time.time()

# plt.plot(np.array(range(length)), leftover)
# plt.show()

if num_con[-1] == 0:
    print(f"Number of circularization is {num_cir[-1]}, and 0 concatemerization")
else:
    print(f"Number of circularization is {num_cir[-1]}")
    print(f"Number of concatemerization is {num_con[-1]}")
    print(f"circularization / concatemerization is {num_cir[-1] / num_con[-1]}")
print(f"{t1 - t0} seconds")
