#!/usr/bin/python3
"""
    Unit test module for max_integer function from 6-max_integer module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        TestCase subclass
    """

    def test_module_docstring(self):
        """ Test module's docstring """
        mod = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod) > 1)

    def test_function_docstring(self):
        """ Test function's docstring """
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_max_interger(self):
        """
            Test for normal case scenarios
            Test cases: empty list, ascending, descending,
                            random, more than one max value
        """
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertAlmostEqual(max_integer([1, 5, 0, 5]), 5)
        self.assertAlmostEqual(max_integer([1, 9, 3, 7]), 9)

    def test_max_integer_raises(self):
        """
            Test for error scnarios
            Test cases: non list data types, list with none integer data types,
                        list with mixed data types
        """
        self.assertRaises(TypeError, max_integer("hello"))
        self.assertRaises(TypeError, max_integer((1, 2)))
        self.assertRaises(TypeError, max_integer(["hello", "hi"]))
        with self.assertRaises(TypeError):
            max_integer([1, "hello"])
        with self.assertRaises(TypeError):
            max_integer(1)
