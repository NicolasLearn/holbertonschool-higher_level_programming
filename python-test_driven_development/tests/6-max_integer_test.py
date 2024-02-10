#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def tests_valid_output(self):
        self.assertEqual(max_integer([2, 5, 1, 3]), 5)
        self.assertEqual(max_integer([1, 5, 1, 1]), 5)
        self.assertEqual(max_integer([-1000, 3, 1, 50, 0]), 50)
        self.assertEqual(max_integer([-20, -2, -0.5, -500]), -0.5)
        self.assertEqual(max_integer([0.3, 0.6, 0.5, 0.2, -1000]), 0.6)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-2, True]), True)
        self.assertEqual(max_integer([False, True]), True)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer((5, 4.5, -10, 8)), 8)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer("abcde"), "e")
        self.assertEqual(max_integer(["Alpha", "Bravo", "Charlie", "123"]), "Charlie")
    
    def test_error_output(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, 5.5)
        self.assertRaises(TypeError, max_integer, -5)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, [2j, 3])
        self.assertRaises(TypeError, max_integer, [-2, "3"])
        self.assertRaises(TypeError, max_integer, ["False", True])
        self.assertRaises(TypeError, max_integer, {5, 4.5, -10, 8})
        self.assertRaises(KeyError, max_integer, {1: 2, 3: 4})

if __name__ == "__main__":
    unittest.main()
