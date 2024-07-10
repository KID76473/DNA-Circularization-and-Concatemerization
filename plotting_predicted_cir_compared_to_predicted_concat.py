import matplotlib.pyplot as plt

#model 1 is the # tails * sphere / total vol
model1 =  [[3.211628228924419e-11, 1.6091080921329013e-11, 8.053775404841235e-12, 3.211628228924419e-12, 1.6091080921329012e-12, 8.053775404841236e-13, 3.2116282289244193e-13], 
         [3.211628228924419e-10, 1.6091080921329013e-10, 8.053775404841236e-11, 3.211628228924419e-11, 1.6091080921329013e-11, 8.053775404841235e-12, 3.211628228924419e-12], 
         [3.2116282289244193e-09, 1.6091080921329013e-09, 8.053775404841235e-10, 3.211628228924419e-10, 1.6091080921329013e-10, 8.053775404841236e-11, 3.211628228924419e-11], 
         [3.211628228924419e-08, 1.6091080921329013e-08, 8.053775404841235e-09, 3.2116282289244193e-09, 1.6091080921329013e-09, 8.053775404841235e-10, 3.211628228924419e-10],
        [3.2116282289244187e-07, 1.6091080921329012e-07, 8.053775404841235e-08, 3.211628228924419e-08, 1.6091080921329013e-08, 8.053775404841235e-09, 3.2116282289244193e-09]]

calculated_cir_prob_6_dir = [5.89299191739383e-5, 2.08504968733022e-5, 7.37452810116553e-6, 
                             1.86604420114764e-6, 6.59795734661119e-7, 2.33281766771726e-7, 
                             5.90174654293721e-8]

# cir / concat
ratio_list = []

concen_list = [.1, 1, 10, 100, 1000]
concen_length = len(concen_list)

length = [500, 1000, 2000, 5000, 10000, 20000, 50000]
num_lens = len(length)

colors = ["red", "blue", "green", "black", "pink"]

size = len(model1)

fig, ax1 = plt.subplots()

# ax2 = ax1.twinx()

for i in range(0, concen_length):
    temp = []
    for j in range(0, num_lens):
        # ratio = cir prob / concat prob
        ratio = calculated_cir_prob_6_dir[j] / model1[i][j]
        temp.append(ratio)
    ratio_list.append(temp)

for i in range(0, size):
    ax1.plot(length, ratio_list[i], color = colors[i], marker = 'o', label = f"{str(concen_list[i])} ug / mL")
    for j in range(0, num_lens):
        ax1.annotate(f"{round(ratio_list[i][j], 1)}", (length[j], ratio_list[i][j]), xycoords='data', xytext=(length[j] * 1.00000001, ratio_list[i][j] * 1.2))

# ax1.plot(length, calculated_cir_prob_6_dir, color = 'purple', marker = 'o', label = "6 dir calculated")
# for j in range(0, num_lens):
#     ax1.annotate(f"{round(calculated_cir_prob_6_dir[j], 10)}", (length[j], calculated_cir_prob_6_dir[j]), xycoords='data', xytext=(length[j] * 1.00000001, calculated_cir_prob_6_dir[j] * 1.2))

ax1.set_xlabel('length')
ax1.set_yscale('log', base = 2)
ax1.set_ylabel('Ratio between Circularization and Concatemerization', color = 'black')
ax1.tick_params(axis='y', labelcolor = 'black')
ax1.legend(loc = 'upper right')
# ax2.set_ylabel('Predicted circularization probability', color = 'teal')
# ax2.tick_params(axis='y', labelcolor = 'teal')
# ax2.set_yscale('log')
# ax2.legend(loc = 'lower right')
plt.title("Ratio between Circularization and Concatemerization")
plt.grid(True)
plt.show()