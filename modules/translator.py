"""
translator.py

Translate DNA sequence into protein sequence.
"""

from Bio.Seq import Seq


def translate_dna(sequence):
    """
    Translate DNA sequence into amino acids.

    Returns:
        Protein sequence
    """

    sequence = sequence.upper().replace("\n", "").replace(" ", "")

    try:
        dna = Seq(sequence)
        protein = dna.translate(to_stop=False)
        return str(protein)

    except Exception:
        return "Invalid DNA Sequence"


def get_start_stop_codons(sequence):
    """
    Find start and stop codons.

    Returns:
        Dictionary
    """

    sequence = sequence.upper()

    start_positions = []
    stop_positions = []

    stop_codons = ["TAA", "TAG", "TGA"]

    for i in range(0, len(sequence) - 2):

        codon = sequence[i:i + 3]

        if codon == "ATG":
            start_positions.append(i + 1)

        if codon in stop_codons:
            stop_positions.append(i + 1)

    return {
        "Start Codons": start_positions,
        "Stop Codons": stop_positions
    }