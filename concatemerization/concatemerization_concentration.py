import numpy as np
import matplotlib.pyplot as plt

# Initialize a list to store the last arrays
last_arrays = []

# Loop through all files named concat_thread_x_concentration.txt
for i in range(32):
    filename = f'data/concat_thread_{i}_concentration.txt'

    with open(filename, 'r') as file:
        lines = file.readlines()

        # Reverse lines and find the last array by checking lines with 'loops cons:'
        for line in reversed(lines):
            if 'loops cons:' in line:
                # Extract the numerical values from the line
                array_str = line.split('cons: ')[-1].strip('[]').split()
                array_values = np.array([float(x) for x in array_str])

                # # Ensure the array has 48 values
                # if len(array_values) == 48:
                #     last_arrays.append(array_values)
                # break

# Write each array into a file called test_output.txt
with open('data/test_output', 'w') as f:
    for i, array in enumerate(last_arrays):
        f.write(f'Array {i}: {array.tolist()}\n')

# Calculate the average of the last arrays
average_array = np.mean(last_arrays, axis=0)

# Plot the average array
plt.plot(average_array)
plt.xlabel('Index')
plt.ylabel('Average Value')
plt.title('Average of the Last Arrays from Each File')
plt.grid(True)
plt.show()
