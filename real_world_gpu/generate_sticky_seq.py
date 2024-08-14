import subprocess
import sys

try:
    #argv[0] is path to this file
    sticky_seq_file_name = str(sys.argv[1])
    number_of_molecules = round(float(sys.argv[2]))
    arg_one_side_len_box = str(sys.argv[3])
    top_seq = str(sys.argv[4])
    bot_sticky_end = str(sys.argv[5])
    top_file_name = str(sys.argv[6])
    init_file_name = str(sys.argv[7])
except:
    print("Usage: %s <%s> <%s> <%s> <%s> <%s> <%s> <%s>" % (sys.argv[0], "sticky_seq_file_name", "number_of_molecules", "side_len_of_box", "top_seq", "bot_sticky_seq", "top_file_name", "init_config_file_name"), file=sys.stderr)
    sys.exit(1)

sequence_file = open(sticky_seq_file_name, "w")

print(len(top_seq))

# generating the seq file

input_line = "STICKY" + " " + str(len(bot_sticky_end)) + " " + top_seq + " " + bot_sticky_end + "\n"

for _ in range(number_of_molecules):
    sequence_file.write(input_line)

sequence_file.close()

# generating the initial positional data file and top file from the seq file
generate_sa_path = "/groups/KaihangWang_Group/jzhou2/cuda_oxDNA/oxDNA/utils/real_world_modified_generate-sa.py"
arg_two_seq_file_path = f"/groups/KaihangWang_Group/jzhou2/cuda_oxDNA/oxDNA/examples/real_world_gpu/{sticky_seq_file_name}"

print(arg_two_seq_file_path)

# the following works though
subprocess.run([generate_sa_path + " " + arg_one_side_len_box + " " + arg_two_seq_file_path + " " + top_file_name + " " + init_file_name], shell=True)