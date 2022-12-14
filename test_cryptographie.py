import unittest
from cryptographie import alphabet,crypter

class TestCrypto(unittest.TestCase):
	def test_alphabet(self):
		self.assertAlmostEqual(alphabet("B"),"BCDEFGHIJKLMNOPQRSTUVWXYZA")
		self.assertAlmostEqual(alphabet("E"),"EFGHIJKLMNOPQRSTUVWXYZABCD")
		self.assertAlmostEqual(alphabet("J"),"JKLMNOPQRSTUVWXYZABCDEFGHI")
	def test_crypter(self):
		self.assertAlmostEqual(crypter("CRYPTOGRAPHIE","eneam",['EFGHIJKLMNOPQRSTUVWXYZABCD', 'NOPQRSTUVWXYZABCDEFGHIJKLM', 'EFGHIJKLMNOPQRSTUVWXYZABCD', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'MNOPQRSTUVWXYZABCDEFGHIJKL']),"GECPFSTVABLVI")
		self.assertAlmostEqual(crypter("CRYPTOLOGIE","eneam",['EFGHIJKLMNOPQRSTUVWXYZABCD', 'NOPQRSTUVWXYZABCDEFGHIJKLM', 'EFGHIJKLMNOPQRSTUVWXYZABCD', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'MNOPQRSTUVWXYZABCDEFGHIJKL']),"GECPFSYSGUI")
		self.assertAlmostEqual(crypter("CRYPTANALYSE","eneam",['EFGHIJKLMNOPQRSTUVWXYZABCD', 'NOPQRSTUVWXYZABCDEFGHIJKLM', 'EFGHIJKLMNOPQRSTUVWXYZABCD', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'MNOPQRSTUVWXYZABCDEFGHIJKL']),"GECPFEAELKWR")
		self.assertAlmostEqual(crypter("COOL'COOL","eneam",['EFGHIJKLMNOPQRSTUVWXYZABCD', 'NOPQRSTUVWXYZABCDEFGHIJKLM', 'EFGHIJKLMNOPQRSTUVWXYZABCD', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'MNOPQRSTUVWXYZABCDEFGHIJKL']),"GBSL'GBSL")
		self.assertAlmostEqual(crypter("COOL COOL","eneam",['EFGHIJKLMNOPQRSTUVWXYZABCD', 'NOPQRSTUVWXYZABCDEFGHIJKLM', 'EFGHIJKLMNOPQRSTUVWXYZABCD', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'MNOPQRSTUVWXYZABCDEFGHIJKL']),"GBSL GBSL")


