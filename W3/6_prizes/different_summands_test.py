
import unittest
import random
from different_summands import optimal_summands, fast_optimal_summands

class TestCase(unittest.TestCase):
    """ Tests for Different Prizes """

    def setUp(self):
        self.model = optimal_summands
        self.algorithm = fast_optimal_summands


    def test_model(self):
        self.assertEqual(len(optimal_summands(500)), 31)

    def test1(self):
        self.assertEqual(len(fast_optimal_summands(1)), len(optimal_summands(1)))

    def test2(self):
        self.assertEqual(len(fast_optimal_summands(2)), len(optimal_summands(2)))

    def test500(self):
        self.assertEqual(len(fast_optimal_summands(500)), len(optimal_summands(500)))

    def test1M(self):
        self.assertEqual(len(fast_optimal_summands(1000000)), len(optimal_summands(1000000)))



############
### MAIN ###
############

if __name__ == "__main__":
    unittest.main()
