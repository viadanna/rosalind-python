'''
Finding a Protein Motif
http://rosalind.info/problems/mprt/

Problem

To allow for the presence of its varying forms, a protein motif is represented
by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino
acid except X." For example, the N-glycosylation motif is written as
N{P}[ST]{P}.

You can see the complete description and features of a particular protein by
its access ID "uniprot_id" in the UniProt database, by inserting the ID number
into http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following
http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at
http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given
access ID followed by a list of locations in the protein string where the motif
can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
'''
from urllib import request
from lib.fasta import read_fasta
from lib.nucleotides import Protein

source = 'http://www.uniprot.org/uniprot/{}.fasta'


def fetch(url):
    ''' Fetch protein sequence fasta from UniProt '''
    req = request.Request(url, None, headers={
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; \
Win64; x64; Trident/5.0'})
    fasta = request.urlopen(req).read().decode("utf-8").strip()
    for prot in read_fasta(fasta, Protein):
        # Odd way to deal with a generator
        return prot


def run_mprt(uids):
    ''' Returns IDs and positions of N-glyn for given protein IDs '''
    res = ''
    for uid in uids.split():
        prot = fetch(source.format(uid))
        pos = prot.find_motif('N{P}[ST]{P}')
        if pos:
            res = '{}\n{}\n{}'.format(res, uid, ' '.join(str(p) for p in pos))
    return res.strip()
