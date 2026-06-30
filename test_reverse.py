from modules.reverse_complement import reverse_complement, complement

sequence = "ATGCCGTAGCTA"

print("Original:")
print(sequence)

print("\nComplement:")
print(complement(sequence))

print("\nReverse Complement:")
print(reverse_complement(sequence))