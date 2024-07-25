micro = 10 ** -6
milli = 10 ** -3

vol_standard_reactor = 100 * micro # liters

avogradros_num = 6.022 * (10 ** 23)

avg_molecular_weight_of_a_bp = 615.96 # g/mol

mass_to_adjust_nt_bonds = 36.04 # g/mol

grams_of_interst = [.1 * micro, micro, 10 * micro, 100 * micro, 1000 * micro] # grams

DNA_lengths_of_interest = [500, 1000, 2000, 5000, 10000, 20000, 50000] # nt

output_num_simulated_tails = []

output_file = open("no_mp_math_real_wlrd_concs_to_num_sim_tails.txt", "w")

for grams in grams_of_interst:
    temp = []
    
    for nt in DNA_lengths_of_interest:
        num_moles_of_dsDNA = (grams / ((nt * avg_molecular_weight_of_a_bp) + mass_to_adjust_nt_bonds))
        num_molecules_of_dsDNA = num_moles_of_dsDNA * avogradros_num
        concentration_in_molecules_per_liter = num_molecules_of_dsDNA / milli # assumes 1 mL
        num_simulated_tails = concentration_in_molecules_per_liter * vol_standard_reactor
        temp.append(num_simulated_tails)
    output_num_simulated_tails.append(temp)

output_file.write(f"reference lengths {DNA_lengths_of_interest} \n")

for i in range(len(grams_of_interst)):
    output_file.write(f"{grams_of_interst[i]} grams/mL {output_num_simulated_tails[i]} \n")