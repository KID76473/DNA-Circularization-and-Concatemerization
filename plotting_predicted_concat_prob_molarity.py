import matplotlib.pyplot as plt
import math

concen_list = [.1, 1, 10, 1, 10]

num_concen = len(concen_list)

length = [500, 1000, 2000, 5000, 10000, 20000, 50000]
num_lens = len(length)

colors = ["red", "blue", "green", "black", "pink"]

concat_prob = [9.918166766452744e-15, 9.918166766452745e-14, 9.918166766452744e-13, 9.918166766452745e-12, 9.918166766452745e-11]

# log base 2 of concat_prob values
for i in range(len(concat_prob)):
    num = math.log2(concat_prob[i])
    concat_prob[i] = num

concat_array = []

#adding circularization line

calculated_cir_prob_6_dir = [5.89299191739383e-5, 2.08504968733022e-5, 7.37452810116553e-6, 
                             1.86604420114764e-6, 6.59795734661119e-7, 2.33281766771726e-7, 
                             5.90174654293721e-8]

# log base 2 of calculated cir prob 6 dir values
for i in range(len(calculated_cir_prob_6_dir)):
    num = math.log2(calculated_cir_prob_6_dir[i])
    calculated_cir_prob_6_dir[i] = num

for i in range(num_concen):
    temp = []
    for j in range(num_lens):
        temp.append(concat_prob[i])
    concat_array.append(temp)

# print(concat_array)

# assert(0)

for i in range(num_concen):
    if i < 3:
        string = "pico molar"
    else:
        string = "nano molar" 
    plt.plot(length, concat_array[i], color = colors[i], marker = 'o', label = f"{str(concen_list[i])} {string}")
    for j in range(num_lens - 1, num_lens):
        plt.annotate(f"{round(concat_array[i][j], 0)}", (length[j], concat_array[i][j]), xycoords='data', xytext=(length[j] * 1.00000001, concat_array[i][j] + .8))

plt.plot(length, calculated_cir_prob_6_dir, color = 'purple', marker = 'o', label = "6 dir calculated")
for j in range(0, num_lens):
    plt.annotate(f"{round(calculated_cir_prob_6_dir[j], 0)}", (length[j], calculated_cir_prob_6_dir[j]), xycoords='data', xytext=(length[j] * 1.00000001, calculated_cir_prob_6_dir[j] + .8))

# plt.yscale('log', base = 10)
plt.xlabel('Length (nt)')
plt.ylabel('Predicted probablity (no log scale; log 2 before plotting)')
plt.title('Probability of various lengths and concentrations (Molarity)')
plt.grid(True)
plt.legend()
plt.show()
