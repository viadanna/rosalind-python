'''
Transcribing DNA into RNA
http://rosalind.info/problems/rna/

Problem

An RNA string is a string formed from the alphabet containing 'A', 'C',
'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed
RNA string u is formed by replacing all occurrences of 'T' in t with 'U'
in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT

Sample Output
GAUGGAACUUGACUACGUAAAUU
'''
from lib.sequences import DNA


def run_rna(sequence):
    ''' Converts a DNA string into RNA '''
    return DNA(sequence).to_rna().sequence
