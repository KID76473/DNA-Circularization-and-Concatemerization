import sys

try:
    strand_length = int(sys.argv[1])
    input_file_name = sys.argv[2]
    output_file_name = sys.argv[3]
    num_molecules = float(sys.argv[4])
    size_of_box = float(sys.argv[5])
    position = sys.argv[6]
except:
    print("Usage: %s <%s> <%s> <%s> <%s> <%s> <%s>" % (sys.argv[0], "strand_length", "input_file_name", "output_file_name", "num_molecules", "size_of_box", "position"), file=sys.stderr)
    sys.exit(1)

total_steps = 100000 # 1e5

tot_cir = 0
tot_concat = 0
true_cir = 0
true_concat = 0
failed_cir = 0
failed_concat = 0

input_file = open(input_file_name, "r")
input_file_last_trial_hb = open(f"{position}last_h_bonds.txt", "w")

save = False
for line in input_file:
    split_line = line.split()
    if len(split_line) == 0:
        continue
    if save == True:
        input_file_last_trial_hb.write(f"{line}")
    elif len(split_line) == 2 or int(split_line[2]) != total_steps:
        continue
    else: # we are at the last trial
        save = True

input_file.close()
input_file_last_trial_hb.close()

diction = {}

new_input = open(f"{position}last_h_bonds.txt", "r")

for line in new_input:
    split_line = line.split()
    strand_one = (int(split_line[0]) // strand_length) + 1
    strand_two = (int(split_line[1]) // strand_length) + 1
    if (strand_one, strand_two) not in diction.keys():
        diction[(strand_one, strand_two)] = 1
    else:
        diction[(strand_one, strand_two)] += 1
        assert(diction[(strand_one, strand_two)] < 5)

new_input.close()

for key, value in diction.items():
    polarity_of_first_val = key[0] % 2
    if polarity_of_first_val == 1 and (key[0] + 1) == key[1]:
        if value == 4:
            true_cir += 1
        else: 
            failed_cir += 1
        tot_cir += 1
    else:
        if value == 4:
            true_concat += 1
        else:
            failed_concat += 1
        tot_concat += 1

output_file = open(output_file_name, "w")

output_file.write(f"{input_file_name} \n")

output_file.write(f"{strand_length} {num_molecules} {size_of_box} \n")

output_file.write(f"tot_cir {tot_cir} true_cir {true_cir} failed_cir {failed_cir} \n")

output_file.write(f"tot_concat {tot_concat} true_concat {true_concat} failed_concat {failed_concat} \n")

output_file.close()

print(tot_cir, true_cir, failed_cir, tot_concat, true_concat, failed_concat)
