"""
reverse_complement.py

Generate the reverse complement of a DNA sequence.
"""

from Bio.Seq import Seq


def reverse_complement(sequence):
    """
    Returns the reverse complement of a DNA sequence.
    """

    sequence = sequence.upper().replace("\n", "").replace(" ", "")

    try:
        dna = Seq(sequence)
        return str(dna.reverse_complement())

    except Exception:
        return "Invalid DNA Sequence"


def complement(sequence):
    """
    Returns the complement of a DNA sequence.
    """

    sequence = sequence.upper().replace("\n", "").replace(" ", "")

    try:
        dna = Seq(sequence)
        return str(dna.complement())

    except Exception:
        return "Invalid DNA Sequence"