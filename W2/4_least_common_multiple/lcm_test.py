
import unittest
import random
from lcm import lcm_naive, lcm

class TestCase(unittest.TestCase):
    """ Tests for lowest common multiple algorithm """

    def setUp(self):
        self.model = lcm_naive
        self.algorithm = lcm


    def test_model_known_input(self):
        self.assertEqual(self.model(6, 8), 24)


    def test_known_input(self):
        self.assertEqual(self.model(6, 8), self.algorithm(6, 8))


    def test_random_inputs(self):
        for _ in range(0, 100):
            i1 = random.randint(0, 1000)
            i2 = random.randint(0, 1000)
            self.assertEqual(self.model(i1, i2), self.algorithm(i1, i2))



############
### MAIN ###
############

if __name__ == "__main__":
    unittest.main()
