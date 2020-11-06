
import unittest
import random
from gcd import gcd_naive, gcd

class TestCase(unittest.TestCase):
    """ Tests for greatest common divisor algorithm """

    def setUp(self):
        self.model = gcd_naive
        self.algorithm = gcd


    def test_model_known_input(self):
        self.assertEqual(self.model(18, 35), 1)


    def test_known_input(self):
        self.assertEqual(self.model(18, 35), self.algorithm(18, 35))


    def test_random_inputs(self):
        for _ in range(0, 100):
            i1 = random.randint(0, 100000)
            i2 = random.randint(0, 100000)
            self.assertEqual(self.model(i1, i2), self.algorithm(i1, i2))



############
### MAIN ###
############

if __name__ == "__main__":
    unittest.main()
