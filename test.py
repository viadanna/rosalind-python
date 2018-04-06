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


if __name__ == '__main__':
    unittest.main()
