import unittest
from main import run_dna, run_rna, run_revc, run_gc, run_hamm, run_subs
from main import run_prot


class TestAlgorithms(unittest.TestCase):

    def test_dna(self):
        ''' Test for http://rosalind.info/problems/dna/ '''
        data = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
        expected = '20 12 17 21'
        self.assertEqual(run_dna(data), expected)


    def test_rna(self):
        ''' Test for http://rosalind.info/problems/rna/ '''
        data = 'GATGGAACTTGACTACGTAAATT'
        expected = 'GAUGGAACUUGACUACGUAAAUU'
        self.assertEqual(run_rna(data), expected)

    def test_revc(self):
        ''' Test for http://rosalind.info/problems/revc/ '''
        data = 'AAAACCCGGT'
        expected = 'ACCGGGTTTT'
        self.assertEqual(run_revc(data), expected)

    def test_gc(self):
        ''' Test for http://rosalind.info/problems/gc/ '''
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
        ''' Test for http://rosalind.info/problems/hamm/ '''
        data = 'GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT'
        expected = 7
        self.assertEqual(run_hamm(data), expected)

    def test_subs(self):
        ''' Test for http://rosalind.info/problems/subs/ '''
        data = 'GATATATGCATATACTT\nATAT'
        expected = '2 4 10'
        self.assertEqual(run_subs(data), expected)

    def test_prot(self):
        ''' Test for http://rosalind.info/problems/prot/ '''
        data = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
        expected = 'MAMAPRTEINSTRING'
        self.assertEqual(run_prot(data), expected)

if __name__ == '__main__':
    unittest.main()
