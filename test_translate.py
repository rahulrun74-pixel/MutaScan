from modules.translator import translate_dna, get_start_stop_codons

sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

print("DNA:")
print(sequence)

print("\nProtein:")
print(translate_dna(sequence))

print("\nCodons:")
print(get_start_stop_codons(sequence))