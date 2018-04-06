from collections import Counter
import re


class Sequence(object):
    def __init__(self, sequence, name=None):
        self.name = name
        self.sequence = sequence


class Nucleotides(Sequence):
    ''' Common class for nucleotides '''
    bases = ""

    def count_bases(self):
        ''' Count the number of bases '''
        count = Counter(self.sequence)
        return ' '.join([
            str(count[b]) for b in self.bases])

    def hamming_distance(self, nucleotide):
        ''' Calculate the Hamming distance '''
        return sum([
            1 for i in range(len(self.sequence))
            if self.sequence[i] != nucleotide.sequence[i]])

    def find_motif(self, motif):
        ''' Find initial positions of given motif '''
        positions = []
        for i in range(len(self.sequence) - len(motif)):
            if self.sequence[i:i + len(motif)] == motif:
                positions.append(i)
        return positions


class DNA(Nucleotides):
    ''' Class for DNA nucleotides '''
    bases = 'ACGT'
    complements = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A',
    }

    def reverse_complement(self):
        ''' Returns a string containing the reverse complement '''
        return ''.join(
            DNA.complements[base]
            for base in reversed(self.sequence))

    def to_rna(self):
        ''' Converts bases T to U '''
        return self.sequence.replace('T', 'U')

    def gc_content(self):
        ''' Returns the GC content of the DNA sequence '''
        counter = Counter(self.sequence)
        return (counter['G'] + counter['C']) / len(self.sequence) * 100.


codon_table = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L",
    "AUC": "I", "GUC": "V", "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
    "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", "UCG": "S", "CCG": "P",
    "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q",
    "AAA": "K", "GAA": "E", "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R",
    "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}


class RNA(Nucleotides):
    ''' Class for RNA nucleotides '''

    def translate(self):
        ''' Translates RNA into a sequence of aminoacids '''
        protein = []
        for i in range(0, len(self.sequence), 3):
            aminoacid = codon_table[self.sequence[i:i + 3]]
            if aminoacid == 'Stop':
                break
            protein.append(aminoacid)
        return ''.join(protein)


class Protein(Sequence):

    motif_rx = re.compile(r'{(\w)}')

    def find_motif(self, motif):
        rx = self.motif_rx.sub(r'(?!\1)\\w', motif)  # Convert to regex
        rx = re.compile('(?=({}))'.format(rx))  # Overlapping
        # Return start of match
        return [m.start() + 1 for m in rx.finditer(self.sequence)]
