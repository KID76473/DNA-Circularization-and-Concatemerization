import matplotlib.pyplot as plt


# Function to extract data from the file
def extract_data(filename):
    data = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        current_loop = None
        for line in lines:
            if line.strip().endswith('loops'):
                current_loop = int(line.split()[0])
                data[current_loop] = {}
            elif current_loop is not None:
                parts = line.split(':')
                key = int(parts[0].strip())
                value = float(parts[1].strip())
                data[current_loop][key] = value
    return data


# Function to plot the data of the last loop
def plot_last_loop(data):
    last_loop = max(data.keys())
    x = list(data[last_loop].keys())
    y = list(data[last_loop].values())

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title(f'Probability of Concatemerization vs. Concentration')
    plt.xlabel('Concentration')
    plt.ylabel('Probability of Concatemerization')
    plt.grid(True)
    plt.savefig("big_cube_center_cube")
    plt.show()


filename = 'data/big_cube'
data = extract_data(filename)
plot_last_loop(data)
