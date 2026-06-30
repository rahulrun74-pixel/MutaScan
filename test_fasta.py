from modules.fasta_reader import read_fasta

sequence = read_fasta("test.fasta")

print(sequence)
print(len(sequence))