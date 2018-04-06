'''
Open Reading Frames
http://rosalind.info/problems/orf/

Problem

Either strand of a DNA double helix can serve as the coding strand for RNA
transcription. Hence, a given DNA string implies six total reading frames, or
ways in which the same region of DNA can be translated into amino acids: three
reading frames result from reading the string itself, whereas three more result
from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends
by stop codon, without any other stop codons in between. Thus, a candidate
protein string is derived by translating an open reading frame into amino acids
until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from
ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
'''
from lib.fasta import read_fasta


def run_orf(data):
    return '\n'.join(set(
        p.sequence
        for dna in read_fasta(data)
        for p in dna.to_proteins()))
