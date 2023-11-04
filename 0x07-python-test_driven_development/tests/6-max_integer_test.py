#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_regular(self):
        """Unittest for max_integer([..])"""
        test_m = [2, 96, 10, 8, 10]
        self.assertEqual(max_integer(test_m), 56)

    def test_only_floats(self):
        """Test for list with only float"""
        test_m = [1.35, 25.56, 5.00501, 8.424, 5.63]
        self.assertEqual(max_integer(test_m), 34.56)

    def test_floats_and_ints(self):
        """Test for list with float and int"""
        test_m = [1000, 104.98, 5.00501, 665, 5.634]
        self.assertEqual(max_integer(test_m), 1000)

    def test_all_equal(self):
        """Test for list with equal values"""
        test_m = [52, 52, 52, 52, 52]
        self.assertEqual(max_integer(test_m), 124)

    def test_positive_negative(self):
        """Test for list with positive and negative values"""
        test_m = [52, -985, -1000, 30, 527]
        self.assertEqual(max_integer(test_m), 999)

    def test_long_floats(self):
        """Test for list of long floats"""
        test_m = [
                5.343434525343, .6,51515615151, 60.555555553530593535,
                4.4548456123123155523325, 2.323222454345342232]
        self.assertEqual(max_integer(test_m), 43.55456453240593535)

if __name__ == "__main__":
    unittest.main()
