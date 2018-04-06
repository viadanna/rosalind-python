'''
Consensus and Profile
http://rosalind.info/problems/cons/

Problem

A matrix is a rectangular table of values divided into rows and columns. An m×n
matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate
the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n.
Their profile matrix is a 4×n matrix P in which P1,j represents the number of
times that 'A' occurs in the jth position of one of the strings, P2, j
represents the number of times that C occurs in the jth position, and so on
(see below).

A consensus string c is a string of length n formed from our collection by
taking the most common symbol at each position; the jth symbol of c therefore
corresponds to the symbol having the maximum value in the j-th column of the
profile matrix. Of course, there may be more than one most common symbol,
leading to multiple possible consensus strings.

DNA Strings

A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T

Profile

A   5 1 0 0 5 5 0 0
C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6

Consensus	A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''
from collections import defaultdict
from lib.fasta import read_fasta


def run_cons(fasta):
    # Read data
    seqs = read_fasta(fasta)
    profile = []

    # Calculate profile
    for seq in seqs:
        for i, base in enumerate(seq.sequence):
            if len(profile) == i:
                profile.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
            profile[i][base] += 1

    # Find consensus sequence
    consensus = ""
    transpose = defaultdict(list)
    for position in profile:
        best = ('*', -1)
        for base, count in position.items():
            transpose[base].append(count)
            if best[1] < count:
                best = (base, count)
        consensus = "{}{}".format(
            consensus,
            best[0])

    # Prepare output
    for base in 'ACGT':
        consensus = '{}\n{}: {}'.format(
            consensus,
            base,
            ' '.join(str(count) for count in transpose[base]))
    return consensus
