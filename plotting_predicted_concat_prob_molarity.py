import matplotlib.pyplot as plt

concen_list = [.1, 1, 10, 1, 10]

num_concen = len(concen_list)

length = [500, 1000, 2000, 5000, 10000, 20000, 50000]
num_lens = len(length)

colors = ["red", "blue", "green", "black", "pink"]

concat_prob = [9.918166766452744e-15, 9.918166766452745e-14, 9.918166766452744e-13, 9.918166766452745e-12, 9.918166766452745e-11]

concat_array = []

for i in range(num_concen):
    temp = []
    for j in range(num_lens):
        temp.append(concat_prob[i])
    concat_array.append(temp)

for i in range(num_concen):
    if i < 3:
        string = "pico molar"
    else:
        string = "nano molar" 
    plt.plot(length, concat_array[i], color = colors[i], marker = 'o', label = f"{str(concen_list[i])} {string}")
    for j in range(num_lens - 1, num_lens):
        plt.annotate(f"{round(concat_array[i][j], 15)}", (length[j], concat_array[i][j]), xycoords='data', xytext=(length[j] * 1.00000001, concat_array[i][j] * 1.2))

plt.yscale('log', base = 2)
plt.xlabel('Length (nt)')
plt.ylabel('Predicted concatemerization probablity')
plt.title('Concatemerization probability of various lengths and concentrations (Molarity)')
plt.grid(True)
plt.legend()
plt.show()
