
import unittest
import random
from merge_sort import merge_sort
from quick_sort import randomized_quick_sort

class TestCase(unittest.TestCase):
    """ Tests for  """

    def setUp(self):
        self.model = merge_sort
        self.algorithm = randomized_quick_sort
        self.sample1 = '5 2 3 9 2 2'
        self.sample2 = '10 1 2 3 4 5 6 7 8 9 10'
        self.sample3 = '14 1 2 3 4 4 3 2 2 2 1 1 5 3 8'


    def convert_input(self, s):
        n, *a = list(map(int, s.split()))
        return n, a


    def generate_random_sequence(self, nmin=1, nmax=10000, arange=(1, 1000000000)):
        n = random.randint(nmin, nmax)
        a = []
        for i in range(0, n):
            a.append(random.randint(arange[0], arange[1]))
        return n, a


    def test_model(self):
        n, a = self.convert_input(self.sample1)
        self.assertEqual(self.model(a), [2, 2, 2, 3, 9])


    def test_sample1(self):
        n, a = self.convert_input(self.sample1)
        self.assertEqual(self.model(a), self.algorithm(a, 0, n-1))


    def test_sample2(self):
        n, a = self.convert_input(self.sample2)
        self.assertEqual(self.model(a), self.algorithm(a, 0, n-1))


    def test_sample3(self):
        n, a = self.convert_input(self.sample3)
        self.assertEqual(self.model(a), self.algorithm(a, 0, n-1))

    def test_random(self):
        n, a = self.generate_random_sequence()
        self.assertEqual(self.model(a), self.algorithm(a, 0, n-1))



############
### MAIN ###
############

if __name__ == "__main__":
    unittest.main()
