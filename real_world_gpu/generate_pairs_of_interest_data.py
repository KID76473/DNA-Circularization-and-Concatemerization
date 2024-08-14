import sys

try:
    len_of_sticky_end = int(sys.argv[1])
    len_of_strand_exclude_sticky = int(sys.argv[2])
    tot_len = int(sys.argv[3])
    num_molecules = round(float(sys.argv[4]))
    output_file_name = str(sys.argv[5])
except:
    print("Usage: %s <%s> <%s> <%s> <%s> <%s>" % (sys.argv[0], "len_of_sticky_end", "len_of_strand_exclude_sticky", "tot_len", "num_molecules", "output_file_name"), file=sys.stderr)
    sys.exit(1)

num_strands = num_molecules * 2

output_file = open(output_file_name, "w")

output_file.write("{ \n")
output_file.write("order_parameter = bond \n")

#output file name, overwritten by input if name is specified in input instead
output_file.write("name = h_bonds \n")

strand_counter = 1
pair_counter = 1

def populater(strand_num, tot_strands, first_nt_num, pair_counter, adjuster):
    for i in range(strand_num // 2, tot_strands // 2):
        if i == (strand_num // 2):
            sec_nt_num = first_nt_num + tot_len - adjuster
        output_file.write(f"pair{pair_counter} = {first_nt_num}, {sec_nt_num} \n")
        pair_counter += 1
        sec_nt_num_copy = sec_nt_num - 1
        for _ in range(0, len_of_sticky_end - 1):
            output_file.write(f"pair{pair_counter} = {first_nt_num}, {sec_nt_num_copy} \n")
            sec_nt_num_copy = sec_nt_num_copy - 1
            pair_counter += 1
        sec_nt_num += 2 * len_of_strand_exclude_sticky
    return pair_counter

while strand_counter < num_strands:
    first_nucleo_num = ((strand_counter - 1) * len_of_strand_exclude_sticky)
    adjuster = 0
    for i in range(1, len_of_sticky_end + 1):
        adjuster = i
        pair_counter = populater(strand_counter, num_strands, first_nucleo_num, pair_counter, adjuster)
        first_nucleo_num += 1
    strand_counter += 1


output_file.write("}")

output_file.close()