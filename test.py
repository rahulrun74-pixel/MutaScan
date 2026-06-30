from modules.mutation_detector import detect_mutations

reference = "ATGCCGTAGCTA"
sample = "ATGTCGTTAGTA"

mutations, summary = detect_mutations(reference, sample)

print("\nSummary")
print(summary)

print("\nMutations")

for m in mutations:
    print(m)