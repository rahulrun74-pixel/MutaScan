"""
alignment_viewer.py

Creates a visual match line for DNA sequence alignment.
"""

def build_alignment(aligned_ref, aligned_sample):
    """
    Builds a match/mismatch visualization string.

    Returns:
        marker string:
        | = match
        * = mismatch
        (space) = gap
    """

    if not aligned_ref or not aligned_sample:
        return ""

    marker = []

    for r, s in zip(aligned_ref, aligned_sample):

        # Gap handling
        if r == "-" or s == "-":
            marker.append(" ")

        # Match
        elif r == s:
            marker.append("|")

        # Mismatch (substitution)
        else:
            marker.append("*")

    return "".join(marker)