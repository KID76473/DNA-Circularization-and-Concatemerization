import glob

# Initialize sums for circularization and concatemerization
total_circularization = 0.0
total_concatemerization = 0.0
total_molucules = 0

# Loop through all test_model_hd_ti.txt files
num = 16
for i in range(num):  # Assuming i ranges from 0 to 31
    file_name = f'./test_model_output/test_model_hd_t{i}.txt'

    with open(file_name, 'r') as file:
        # Read the last three lines
        lines = file.readlines()[-4:]

        # Extract and sum the circularization and concatemerization values
        circularization = float(lines[1].split(":")[1].strip())
        concatemerization = float(lines[2].split(":")[1].strip())
        molecules = int(lines[3].split(":")[1].strip())

        total_circularization += circularization
        total_concatemerization += concatemerization
        total_molucules += molecules

print(f"Total circularization: {total_circularization}")
print(f"Total concatemerization: {total_concatemerization}")
print(f"Total molecules: {total_molucules}")
