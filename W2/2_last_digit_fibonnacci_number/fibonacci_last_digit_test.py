
import unittest
import random
from fibonacci_last_digit import get_fibonacci_last_digit_naive, get_fibonacci_last_digit



class FibonacciLastDigit(unittest.TestCase):
    """ Tests for Fibonacci last digit method """

    def setUp(self):
        self.model = get_fibonacci_last_digit_naive
        self.algorithm = get_fibonacci_last_digit


    def test_zeroth_input(self):
        self.assertEqual(self.algorithm(0), 0)


    def test_first_input(self):
        self.assertEqual(self.algorithm(1), 1)


    def test_model_known_input(self):
        self.assertEqual(self.model(331), 9)


    def test_known_inputs(self):
        for i in range(0, 20):
            self.assertEqual(self.model(i), self.algorithm(i))


    def test_random_inputs(self):
        for _ in range(0, 100):
            i = random.randint(0, 100000)
            self.assertEqual(self.model(i), self.algorithm(i))



############
### MAIN ###
############

if __name__ == "__main__":
    unittest.main()
