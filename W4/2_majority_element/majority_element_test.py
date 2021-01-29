
import unittest
import random
from majority_element import get_majority_element_naive, get_majority_element_fast

class TestCase(unittest.TestCase):
    """ Tests for  """

    def setUp(self):
        self.model = get_majority_element_naive
        self.algorithm = get_majority_element_fast
        self.samples = []
        self.samples.append('5 2 3 9 2 2')
        self.samples.append('4 1 2 3 4')


    def test_model(self):
        n, *a = list(map(int, self.samples[0].split()))
        self.assertEqual(self.model(a, 0, n), 2)


    def test_sample0(self):
        n, *a = list(map(int, self.samples[0].split()))
        self.assertEqual(self.model(a, 0, n), self.algorithm(a, 0, n))


    def test_sample1(self):
        n, *a = list(map(int, self.samples[1].split()))
        self.assertEqual(self.model(a, 0, n), self.algorithm(a, 0, n))


############
### MAIN ###
############

if __name__ == "__main__":
    unittest.main()
