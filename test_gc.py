from modules.gc_content import calculate_gc, nucleotide_count

sequence = "ATGCCGTAGCTA"

print("GC Content:", calculate_gc(sequence), "%")
print()

counts = nucleotide_count(sequence)

for base, value in counts.items():
    print(base, ":", value)