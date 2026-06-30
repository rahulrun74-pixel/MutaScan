"""
needleman_wunsch.py

Global Sequence Alignment
Needleman-Wunsch Algorithm
"""

MATCH = 1
MISMATCH = -1
GAP = -1


def needleman_wunsch(seq1, seq2):
    """
    Returns:
        aligned_seq1
        aligned_seq2
        alignment_score
    """

    m = len(seq1)
    n = len(seq2)

    # Score matrix
    score = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialization
    for i in range(m + 1):
        score[i][0] = i * GAP

    for j in range(n + 1):
        score[0][j] = j * GAP

    # Fill score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                diagonal = score[i - 1][j - 1] + MATCH
            else:
                diagonal = score[i - 1][j - 1] + MISMATCH

            up = score[i - 1][j] + GAP
            left = score[i][j - 1] + GAP

            score[i][j] = max(diagonal, up, left)

    # Traceback
    aligned1 = ""
    aligned2 = ""

    i = m
    j = n

    while i > 0 and j > 0:

        current = score[i][j]

        if seq1[i - 1] == seq2[j - 1]:
            diag = score[i - 1][j - 1] + MATCH
        else:
            diag = score[i - 1][j - 1] + MISMATCH

        if current == diag:
            aligned1 = seq1[i - 1] + aligned1
            aligned2 = seq2[j - 1] + aligned2
            i -= 1
            j -= 1

        elif current == score[i - 1][j] + GAP:
            aligned1 = seq1[i - 1] + aligned1
            aligned2 = "-" + aligned2
            i -= 1

        else:
            aligned1 = "-" + aligned1
            aligned2 = seq2[j - 1] + aligned2
            j -= 1

    while i > 0:
        aligned1 = seq1[i - 1] + aligned1
        aligned2 = "-" + aligned2
        i -= 1

    while j > 0:
        aligned1 = "-" + aligned1
        aligned2 = seq2[j - 1] + aligned2
        j -= 1

    return aligned1, aligned2, score[m][n]