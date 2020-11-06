
import unittest
from fibonacci import fibonacci_recursive, fibonacci_loop



class RecursiveFibonacci(unittest.TestCase):
    """ Tests for recursive Fibonacci method """

    def test_zeroth_input(self):
        self.assertEqual(fibonacci_recursive(0), 0)

    def test_first_input(self):
        self.assertEqual(fibonacci_recursive(1), 1)

    def test_known_input(self):
        self.assertEqual(fibonacci_recursive(19), 4181)



class LoopFibonacci(unittest.TestCase):
    """ Tests for loop Fibonacci method """

    def test_zeroth_input(self):
        self.assertEqual(fibonacci_loop(0), 0)

    def test_first_input(self):
        self.assertEqual(fibonacci_loop(1), 1)

    def test_known_input(self):
        self.assertEqual(fibonacci_recursive(19), fibonacci_loop(19))

    def test_known_inputs(self):
        for i in range(0, 20):
            self.assertEqual(fibonacci_recursive(i), fibonacci_loop(i))



############
### MAIN ###
############

if __name__ == "__main__":
    unittest.main()
