import sys

from lib.nucleotides import DNA, RNA
from lib.fasta import read_fasta


def run_dna(sequence):
    '''
    Counting DNA Nucleotides
    Problem
    A string is simply an ordered collection of symbols selected from some
    alphabet and formed into a word; the length of a string is the number of
    symbols that it contains.

    An example of a length 21 DNA string (whose alphabet contains the symbols
    'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

    Given: A DNA string s of length at most 1000 nt.

    Return: Four integers (separated by spaces) counting the respective number
    of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

    Sample Dataset
    AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

    Sample Output
    20 12 17 21
    '''
    return DNA(sequence).count_bases()


def run_rna(sequence):
    '''
    Transcribing DNA into RNA
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
    return DNA(sequence).to_rna()

def run_revc(sequence):
    '''
    Complementing a Strand of DNA
    Problem
    In DNA strings, symbols 'A' and 'T' are complements of each other, as are
    'C' and 'G'.

    The reverse complement of a DNA string s is the string sc formed by
    reversing the symbols of s, then taking the complement of each symbol
    (e.g., the reverse complement of "GTCA" is "TGAC").

    Given: A DNA string s of length at most 1000 bp.

    Return: The reverse complement sc of s.

    Sample Dataset
    AAAACCCGGT

    Sample Output
    ACCGGGTTTT
    '''
    return DNA(sequence).reverse_complement()


def run_gc(fasta):
    '''
    Computing GC Content
    Problem
    The GC-content of a DNA string is given by the percentage of symbols in the
    string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is
    37.5%. Note that the reverse complement of any DNA string has the same
    GC-content.

    DNA strings must be labeled when they are consolidated into a database. A
    commonly used method of string labeling is called FASTA format. In this
    format, the string is introduced by a line that begins with '>', followed
    by some labeling information. Subsequent lines contain the string itself;
    the first line to begin with '>' indicates the label of the next string.

    In Rosalind's implementation, a string in FASTA format will be labeled by
    the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000
    and 9999.

    Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp
    each).

    Return: The ID of the string having the highest GC-content, followed by the
    GC-content of that string. Rosalind allows for a default error of 0.001 in
    all decimal answers unless otherwise stated; please see the note on
    absolute error below.

    Sample Dataset
    >Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT

    Sample Output
    Rosalind_0808
    60.919540
    '''
    max_content, max_dna = 0, None
    for dna in read_fasta(fasta):
        gc = dna.gc_content()
        if gc > max_content:
            max_content = gc
            max_dna = dna
    return '%s\n%f' % (max_dna.name, max_content)


def run_hamm(data):
    ''' Counting point mutations
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
    data = data.split('\n')
    seq, other = DNA(data[0]), DNA(data[1])
    return seq.hamming_distance(other)


def run_subs(data):
    ''' Finding a motif in DNA
    Problem
    Given two strings s and t, t is a substring of s if t is contained as a
    contiguous collection of symbols in s (as a result, t must be no longer
    than s).

    The position of a symbol in a string is the total number of symbols found
    to its left, including itself (e.g., the positions of all occurrences of
    'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at
    position i of s is denoted by s[i].

    A substring of s can be represented as s[j:k], where j and k represent the
    starting and ending positions of the substring in s; for example, if
    s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

    The location of a substring s[j:k] is its beginning position j; note that t
    will have multiple locations in s if it occurs more than once as a
    substring of s (see the Sample below).

    Given: Two DNA strings s and t (each of length at most 1 kbp).

    Return: All locations of t as a substring of s.

    Sample Dataset
    GATATATGCATATACTT
    ATAT
    Sample Output
    2 4 10
    '''
    dna, motif = data.split('\n')
    dna = DNA(dna)
    return ' '.join(str(i + 1) for i in dna.find_motif(motif))


def run_prot(data):
    '''
    Translating RNA into Protein
    Problem
    The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

    The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

    Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

    Return: The protein string encoded by s.

    Sample Dataset
    AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
    Sample Output
    MAMAPRTEINSTRING
    '''
    rna = RNA(data)
    return rna.translate()


problems = {
    'dna': run_dna,
    'rna': run_rna,
    'revc': run_revc,
    'gc': run_gc,
    'hamm': run_hamm,
    'subs': run_subs,
    'prot': run_prot,
}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('''Usage:

python3 %s <problem_code> < dataset.txt > output.txt
''' % sys.argv[0])
        sys.exit(1)

    problem = problems.get(sys.argv[1])
    if not problem:
        print(
            'Couldn\'t find "{}" problem. Available ones:\n{}',
            sys.argv[1],
            '\n'.join(sorted(problems)))
        sys.exit(1)

    inpt = sys.stdin.read().strip()
    print(problem(inpt))
