from modules.needleman_wunsch import needleman_wunsch

seq1 = "ATGCCGA"
seq2 = "ATGTTCGA"

a1, a2, score = needleman_wunsch(seq1, seq2)

print("Alignment Score:", score)
print()
print(a1)
print(a2)