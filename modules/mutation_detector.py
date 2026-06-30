"""
mutation_detector.py

Detect mutations using Needleman-Wunsch alignment.
"""

from modules.needleman_wunsch import needleman_wunsch


def detect_mutations(reference, sample):

    aligned_ref, aligned_sample, score = needleman_wunsch(reference, sample)

    mutations = []

    substitution = 0
    insertion = 0
    deletion = 0

    position = 0

    for r, s in zip(aligned_ref, aligned_sample):

        if r != "-":
            position += 1

        if r == s:
            continue

        if r == "-":

            insertion += 1

            mutations.append({
                "Position": position,
                "Reference": "-",
                "Sample": s,
                "Mutation": "Insertion"
            })

        elif s == "-":

            deletion += 1

            mutations.append({
                "Position": position,
                "Reference": r,
                "Sample": "-",
                "Mutation": "Deletion"
            })

        else:

            substitution += 1

            mutations.append({
                "Position": position,
                "Reference": r,
                "Sample": s,
                "Mutation": "Substitution"
            })

    summary = {
        "Reference Length": len(reference),
        "Sample Length": len(sample),
        "Substitution": substitution,
        "Insertion": insertion,
        "Deletion": deletion,
        "Total": substitution + insertion + deletion,
        "Alignment Score": score
    }

    return aligned_ref, aligned_sample, mutations, summary