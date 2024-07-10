import matplotlib.pyplot as plt

x_vals = [i for i in range(2,21)]
simulated_concat_vals = []
predicted_concat_vals = []

simulation_file = open("data/big_cube_concat_output_final_loop", "r")
prediction_file = open("data/monte_carlo_out", "r")

for line in simulation_file:
    split_line = line.split()
    if split_line[1] == "loops":
        continue
    else:
        simulated_concat_vals.append(float(split_line[1]))

for line in prediction_file:
    split_line = line.split()
    concen = split_line[1]
    parsed_concen = concen[:-1] # getting rid of last char
    if int(parsed_concen) > 20:
        break
    elif int(parsed_concen) == 1:
        continue
    else:
        predicted_concat_vals.append(float(split_line[3]))

plt.plot(x_vals, simulated_concat_vals, color = "blue", marker = 'o', label = "simulated concat vals")
plt.plot(x_vals, predicted_concat_vals, color = "red", marker = "o", label = "predicted concat vals")

for i in range(0, len(x_vals)):
    plt.annotate(f"{round(predicted_concat_vals[i], 4)}", (x_vals[i], predicted_concat_vals[i]))

plt.yscale('log')
plt.xlabel('Concentration (dist btw 2 tails)')
plt.ylabel('Concatemerization Probability')
plt.title('(None Real World Values) Concat vs Concen')
plt.grid(True)
plt.legend()
plt.show()



# print(x_vals)
# print(simulated_concat_vals)
# print(predicted_concat_vals)