import os
import matplotlib.pyplot as plt


# Define the function to extract the cir/num value from a line
def extract_cir_num(line):
    parts = line.split(', ')
    cir_num_part = parts[-1]
    cir_num_value = float(cir_num_part.split(': ')[-1])
    return cir_num_value


# Define the filenames and initialize the data structures
filenames = [f'data/circle_thread_no_back_{i}.txt' for i in range(32)]
data = {500: [], 1000: [], 1500: [], 2000: []}

# Read the data from each file
for filename in filenames:
    with open(filename, 'r') as file:
        lines = file.readlines()
        found = {500: False, 1000: False, 1500: False, 2000: False}
        for line in reversed(lines):
            if line.startswith('i: 500') and not found[500]:
                data[500].append(extract_cir_num(line))
                found[500] = True
            elif line.startswith('i: 1000') and not found[1000]:
                data[1000].append(extract_cir_num(line))
                found[1000] = True
            elif line.startswith('i: 1500') and not found[1500]:
                data[1500].append(extract_cir_num(line))
                found[1500] = True
            elif line.startswith('i: 2000') and not found[2000]:
                data[2000].append(extract_cir_num(line))
                found[2000] = True

            # Break the loop if all values are found
            if all(found.values()):
                break

# Calculate the average of cir/num for each i
averages = {i: sum(values) / len(values) for i, values in data.items()}

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(averages.keys(), averages.values(), marker='o', linestyle='-', color='b')
plt.xlabel('i')
plt.ylabel('cir / num')
plt.title('Plot of i vs. cir / num')
plt.grid(True)
plt.xticks([500, 1000, 1500, 2000])

# Add value labels to each point
for i, value in averages.items():
    plt.annotate(f'{value:.2e}', (i, value), textcoords="offset points", xytext=(0, 10), ha='center')

plt.show()
