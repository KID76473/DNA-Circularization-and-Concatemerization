import matplotlib.pyplot as plt

#model 1 is the # tails * sphere / total vol
model1 =  [[3.211628228924419e-11, 1.6091080921329013e-11, 8.053775404841235e-12, 3.211628228924419e-12, 1.6091080921329012e-12, 8.053775404841236e-13, 3.2116282289244193e-13], 
         [3.211628228924419e-10, 1.6091080921329013e-10, 8.053775404841236e-11, 3.211628228924419e-11, 1.6091080921329013e-11, 8.053775404841235e-12, 3.211628228924419e-12], 
         [3.2116282289244193e-09, 1.6091080921329013e-09, 8.053775404841235e-10, 3.211628228924419e-10, 1.6091080921329013e-10, 8.053775404841236e-11, 3.211628228924419e-11], 
         [3.211628228924419e-08, 1.6091080921329013e-08, 8.053775404841235e-09, 3.2116282289244193e-09, 1.6091080921329013e-09, 8.053775404841235e-10, 3.211628228924419e-10],
        [3.2116282289244187e-07, 1.6091080921329012e-07, 8.053775404841235e-08, 3.211628228924419e-08, 1.6091080921329013e-08, 8.053775404841235e-09, 3.2116282289244193e-09]]

#model 2 is the 1 - (1 - prob of 1 tail in head sphere)^number of tails)

model2 =  [[3.2116309611751603e-11, 1.609112842970717e-11, 8.05377986523581e-12, 3.211653165635653e-12, 1.6091572518917019e-12, 8.053557820630886e-13, 3.211875210240578e-13], 
           [3.211628740729111e-10, 1.6091084020786184e-10, 8.05377986523581e-11, 3.2116309611751603e-11, 1.609112842970717e-11, 8.05377986523581e-12, 3.211653165635653e-12], 
           [3.2116281856175988e-09, 1.609108069011711e-09, 8.053775424343712e-10, 3.211628740729111e-10, 1.6091084020786184e-10, 8.05377986523581e-11, 3.2116309611751603e-11], 
           [3.21162823002652e-08, 1.6091080912161715e-08, 8.053775424343712e-09, 3.2116281856175988e-09, 1.609108069011711e-09, 8.053775424343712e-10, 3.211628740729111e-10], 
           [3.2116282289162967e-07, 1.6091080923263945e-07, 8.053775402139252e-08, 3.21162823002652e-08, 1.6091080912161715e-08, 8.053775424343712e-09, 3.2116281856175988e-09]]

# simulated_cir_vals_6_directions = [5962 / 100000001, 2127 / 100000001, 1068 / 100000001, 726 / 100000001]

concen_list = [.1, 1, 10, 100, 1000]

length = [500, 1000, 2000, 5000, 10000, 20000, 50000]
len_s = [500, 1000, 1500, 2000]
num_lens = len(length)

colors = ["red", "blue", "green", "black", "pink"]

size = len(model1)

fig, ax1 = plt.subplots()

#ax2 = ax1.twinx()

for i in range(0, size):
    ax1.plot(length, model1[i], color = 'blue', marker = 'o', label = f"{str(concen_list[i])} ug / mL")
    ax1.plot(length, model2[i], color = 'red', marker = 'o', label = f"{str(concen_list[i])} ug / mL")
    for j in range(0, num_lens):
        ax1.annotate(f"{round(model1[i][j], 13)}", (length[j], model1[i][j]), xycoords='data', xytext=(length[j] * 1.00000001, model1[i][j] * 1.2))
        ax1.annotate(f"{round(model2[i][j], 13)}", (length[j], model2[i][j]), xycoords='data', xytext=(length[j] * 1.00000001, model2[i][j] * 1.2))

# ax2.plot(len_s, simulated_cir_vals_6_directions, color = 'purple', marker = 'o', label = "6 dir simulated")

ax1.set_xlabel('length')
ax1.set_yscale('log', base = 2)
ax1.set_ylabel('Predicted concatemerization probablity', color = 'brown')
ax1.tick_params(axis='y', labelcolor = 'brown')
ax1.legend(loc = 'upper right')
# ax2.set_ylabel('Predicted circularization probability', color = 'teal')
# ax2.tick_params(axis='y', labelcolor = 'teal')
# ax2.set_yscale('log')
# ax2.legend(loc = 'lower right')
plt.title("Concatemerization probability of various lengths and concentrations (Comparing 2 formulas)")
plt.grid(True)
plt.show()