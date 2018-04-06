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
        return DNA(''.join(
            DNA.complements[base]
            for base in reversed(self.sequence)))

    def to_rna(self):
        ''' Converts bases T to U '''
        return RNA(self.sequence.replace('T', 'U'))

    def gc_content(self):
        ''' Returns the GC content of the DNA sequence '''
        counter = Counter(self.sequence)
        return (counter['G'] + counter['C']) / len(self.sequence) * 100.

    def to_proteins(self):
        ''' Returns possible proteins encoded by DNA sequence '''
        for prot in self.to_rna().to_proteins():
            yield prot
        for prot in self.reverse_complement().to_rna().to_proteins():
            yield prot


codon_table = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L",
    "AUC": "I", "GUC": "V", "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
    "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", "UCG": "S", "CCG": "P",
    "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "*", "CAA": "Q",
    "AAA": "K", "GAA": "E", "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R",
    "AGC": "S", "GGC": "G", "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}


class RNA(Nucleotides):
    ''' Class for RNA nucleotides '''

    def translate(self, stop=False, start=0):
        ''' Translates RNA into a sequence of aminoacids '''
        protein = []
        length = len(self.sequence[start:]) // 3 * 3
        for i in range(0, length, 3):
            aminoacid = codon_table[self.sequence[start + i:start + i + 3]]
            if stop and aminoacid == '*':
                break
            protein.append(aminoacid)
        return ''.join(protein)

    def to_proteins(self):
        ''' Returns possible proteins encoded by RNA sequence '''
        for start in range(3):
            amino = self.translate(start=start)
            for match in re.finditer(r'M', amino):
                start = match.start()
                size = amino[start:].find('*')
                if size > 0:
                    seq = amino[start:start + size]
                    yield Protein(seq)


class Protein(Sequence):

    motif_rx = re.compile(r'{(\w)}')

    def find_motif(self, motif):
        rx = self.motif_rx.sub(r'(?!\1)\\w', motif)  # Convert to regex
        rx = re.compile('(?=({}))'.format(rx))  # Overlapping
        # Return start of match
        return [m.start() + 1 for m in rx.finditer(self.sequence)]
