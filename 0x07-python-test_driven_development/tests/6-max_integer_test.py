#!/usr/bin/python3
"""Unittests for max_integer([...])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    def test_max_integer(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 5, 2, 7, 3]), 7)

        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -5, -2, -7, -3]), -1)

        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

        """Test with a list containing a single element"""
        self.assertEqual(max_integer([42]), 42)

        """Test with a list containing duplicate integers"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

        """Test with a large list of integers"""
        self.assertEqual(max_integer(list(range(1000000))), 999999)

        """Test with a list containing mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_max_integer_with_duplicates(self):

        """Test with a list containing duplicate integers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 4, 3, 2, 1]), 4)

    def test_max_integer_with_strings(self):

        """Test with a list containing strings"""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')


if __name__ == '__main__':
    unittest.main()
