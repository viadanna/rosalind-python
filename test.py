import unittest
from problems.dna import run_dna
from problems.rna import run_rna
from problems.revc import run_revc
from problems.gc import run_gc
from problems.hamm import run_hamm
from problems.subs import run_subs
from problems.prot import run_prot
from problems.fib import run_fib
from problems.iprb import run_iprb
from problems.fibd import run_fibd
from problems.mrna import run_mrna
from problems.iev import run_iev
from problems.cons import run_cons


class TestAlgorithms(unittest.TestCase):

    def test_dna(self):
        ''' http://rosalind.info/problems/dna/ '''
        data = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
        expected = '20 12 17 21'
        self.assertEqual(run_dna(data), expected)


    def test_rna(self):
        ''' http://rosalind.info/problems/rna/ '''
        data = 'GATGGAACTTGACTACGTAAATT'
        expected = 'GAUGGAACUUGACUACGUAAAUU'
        self.assertEqual(run_rna(data), expected)

    def test_revc(self):
        ''' http://rosalind.info/problems/revc/ '''
        data = 'AAAACCCGGT'
        expected = 'ACCGGGTTTT'
        self.assertEqual(run_revc(data), expected)

    def test_gc(self):
        ''' http://rosalind.info/problems/gc/ '''
        data = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''
        expected = '''Rosalind_0808
60.919540'''
        self.assertEqual(run_gc(data), expected)

    def test_hamm(self):
        ''' http://rosalind.info/problems/hamm/ '''
        data = 'GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT'
        expected = 7
        self.assertEqual(run_hamm(data), expected)

    def test_subs(self):
        ''' http://rosalind.info/problems/subs/ '''
        data = 'GATATATGCATATACTT\nATAT'
        expected = '2 4 10'
        self.assertEqual(run_subs(data), expected)

    def test_prot(self):
        ''' http://rosalind.info/problems/prot/ '''
        data = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
        expected = 'MAMAPRTEINSTRING'
        self.assertEqual(run_prot(data), expected)

    def test_fib(self):
        ''' http://rosalind.info/problems/fib/ '''
        data = '5 3'
        expected = 19
        self.assertEqual(run_fib(data), expected)

    def test_iprb(self):
        ''' http://rosalind.info/problems/iprb/ '''
        data = '2 2 2'
        expected = '0.78333'
        self.assertEqual('{:.5f}'.format(run_iprb(data)), expected)

    def test_fibd(self):
        ''' http://rosalind.info/problems/fibd/ '''
        data = '6 3'
        expected = 4
        self.assertEqual(run_fibd(data), expected)

    def test_mrna(self):
        ''' http://rosalind.info/problems/mrna/ '''
        data = 'MA'
        expected = 12
        self.assertEqual(run_mrna(data), expected)

    def test_iev(self):
        ''' http://rosalind.info/problems/iev/ '''
        data = '1 0 0 1 0 1'
        expected = 3.5
        self.assertEqual(run_iev(data), expected)

    def test_cons(self):
        ''' http://rosalind.info/problems/cons/ '''
        data = '''>Rosalind_1
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
ATGGCACT'''
        expected = '''ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6'''
        self.assertEqual(run_cons(data), expected)


if __name__ == '__main__':
    unittest.main()
