'''
Counting point mutations
http://rosalind.info/problems/hamm/

Problem

Given two strings s and t of equal length, the Hamming distance between s
and t, denoted dH(s,t), is the number of corresponding symbols that differ
in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7
'''
from lib.sequences import DNA


def run_hamm(data):
    ''' Calculates the Hamming distance between two strings '''
    seq, other = data.split('\n')
    seq, other = DNA(seq), DNA(other)
    return seq.hamming_distance(other)
