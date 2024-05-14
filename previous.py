import time
import numpy as np
import matplotlib.pyplot as plt


dimension = 3
N = 64
length = 1000
density = 10
tails = np.zeros((N, N, N, dimension), dtype=np.int8)
leftover = np.zeros(length)  # # of dna that does not circularize and concatenate
terminate = np.ones((N, N, N, dimension), dtype=np.int8)
# count = np.sum(terminate)
num_cir = []
num_con = []

t0 = time.time()

for i in range(length):  # length
    # print(i)

    tails += terminate * np.random.choice([-1, 1], (N, N, N, dimension), p=[0.5, 0.5])  # step further randomly for each one
    # print("-------------------------------")
    # print(f"the {i}th step")
    # print("tails")
    # print(tails)

    # count # of circularization
    circular = (tails == 0)  # true if any dimension is at 100x
    circular = circular[:, :, :, 0] * circular[:, :, :, 1] * circular[:, :, :, 2]  # all dimensions must be at 100 x
    num_cir.append(np.sum(circular))
    # print(f"circular: {np.sum(circular)}")

    # count # of concatemerization
    concatemer = ((tails % density) == 0)
    concatemer = concatemer[:, :, :, 0] * concatemer[:, :, :, 1] * concatemer[:, :, :, 2]
    concatemer = concatemer.astype(int)
    concatemer -= circular.astype(int)
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