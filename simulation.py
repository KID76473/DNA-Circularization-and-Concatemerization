import time
import numpy as np
import matplotlib.pyplot as plt


# dimension = 3 N = 64 length = 1000 concentration = 10 num_dir = 360 error = 0.0001
dimension = 3
N = 3  # number of molecules = N^3
length = 1000
concentration = 2  # distance between every pair of adjacent points
heads = np.zeros((N, N, N, dimension))
leftover = np.zeros(length)  # # of dna that does not circularize and concatenate
terminate = np.ones((N, N, N, dimension))
# count = np.sum(terminate)
num_cir = []
num_con = []
error = 0.01
num_dir = 4  # number of angles

# set up all directions
angles = np.linspace(0, 2 * np.pi, num_dir, endpoint=False)
directions = np.zeros((num_dir ** 2, dimension))
# print(np.shape(directions))
for i in range(num_dir):  # angle of xy plane
    for j in range(num_dir):  # angle of z plane
        directions[i * num_dir + j, 2] = np.sin(angles[j])
        directions[i * num_dir + j, 1] = np.cos(angles[j]) * np.sin(angles[i])
        directions[i * num_dir + j, 0] = np.cos(angles[j]) * np.cos(angles[i])
# print(len(directions))

# test whether the length is 1 or not
# for i in range(num_dir ** 2):  # determine precision
#     print(np.abs(directions[i, 0] ** 2 + directions[i, 1] ** 2 + directions[i, 2] ** 2 - 1) < 0.001)

t0 = time.time()

for i in range(2):  # length
    # heads += terminate * np.random.choice([-1, 1], (N, N, N, dimension), p=[0.5, 0.5])  # step further randomly for each one
    # heads += terminate * directions[np.random.choice(range(num_dir ** 2)), :]
    for x in range(N):
        for y in range(N):
            for z in range(N):
                heads[x, y, z] += terminate[x, y, z] * directions[np.random.choice(range(num_dir ** 2))]
    # heads += terminate * np.random.choice(directions, (N, N, N, dimension), p=[1 / num_dir ** 2] * num_dir ** 2)
    print("-------------------------------")
    print(f"the {i}th step")
    print(f"heads: {heads}")

    # count # of circularization
    circular = (np.abs(heads) < error)  # true if any dimension is around zero within error
    # print(f"circular: {circular}")
    circular = circular[:, :, :, 0] * circular[:, :, :, 1] * circular[:, :, :, 2]  # all dimensions must be true
    num_cir.append(np.sum(circular))
    # print(f"circular: {num_cir[i]}")
    print(f"circular: {circular.astype(int)}")

    # count # of concatemerization including circularization
    concatemer = (np.abs(heads % concentration) < error)
    concatemer = concatemer[:, :, :, 0] * concatemer[:, :, :, 1] * concatemer[:, :, :, 2]
    # record all terminated molecules
    terminate = (np.ones((N, N, N), dtype=np.int8) - concatemer)[..., np.newaxis]
    leftover[i] = np.sum(terminate)  # count how may dna do not meet self or others
    # remove circularization from concatemerization
    concatemer = concatemer.astype(np.int8) - circular.astype(np.int8)
    num_con.append(np.sum(concatemer))
    # print(f"concatemer: {num_con[i]}")
    print(f"concatemer: {concatemer}")

    # if i % 100 == 0:  # print every 100 length
    #     print(i, np.sum(terminate))

t1 = time.time()

# plt.plot(np.array(range(length)), leftover)
# plt.show()

print("-------------------------------")
print(f"Dimension: {dimension}")
print(f"Number of molecule: {N ** 3}")
print(f"Length of DNA: {length}")
print(f"Concentration(space between adjacent molecules): {concentration}")
print(f"Number of directions: {num_dir}")
print(f"Error: {error}")

if num_con[-1] == 0:
    print(f"Number of circularization is {num_cir[-1]}, and 0 concatemerization")
else:
    print(f"Number of circularization is {num_cir[-1]}")
    print(f"Number of concatemerization is {num_con[-1]}")
    print(f"circularization / concatemerization is {num_cir[-1] / num_con[-1]}")
print(f"It takes {t1 - t0} seconds")
