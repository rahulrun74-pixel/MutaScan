"""
gc_content.py

Calculate GC content and nucleotide composition.
"""


def calculate_gc(sequence):
    """
    Calculate GC percentage.

    Returns:
        float
    """

    sequence = sequence.upper().replace("\n", "").replace(" ", "")

    if len(sequence) == 0:
        return 0

    gc = sequence.count("G") + sequence.count("C")

    return round((gc / len(sequence)) * 100, 2)


def nucleotide_count(sequence):
    """
    Count each nucleotide.

    Returns:
        dictionary
    """

    sequence = sequence.upper()

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
        "N": sequence.count("N"),
        "Length": len(sequence)
    }