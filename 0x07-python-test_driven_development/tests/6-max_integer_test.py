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

    def check_empty_list(self):
        """ Pass an empty list """
        self.assertEqual(max_integer([]), None)

    def check_order_list(self):
        """ Pass list with numbers arranged in ascending
            and descending orders
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def random_order_list(self):
        """ Pass list with randomly ordered numbers """
        self.assertEqual(max_integer([1, 9, 3, 7]), 9)

    def multiple_max_list(self):
        """ Pass list with multiple max values """
        self.assertEqual(max_integer([1, 5, 0, 5]), 5)

    def one_element_list(self):
        """ Pass list with one element """
        self.assertEqual(max_integer([2]), 2)

    def positive_and_negative_list(self):
        """ Pass list with positive and negative numbers """
        self.assertEqual(max_integer([1, -9, 3, -7]), 3)

    def negative_numbers_list(self):
        """ Pass list with negative numbers only """
        self.assertEqual(max_integer([-1, -9, -3, -7]), -1)

    def float_list(self):
        """ Pass a list with floats only """
        self.assertEqual(max_integer([1.2, 3.98, 3.89, 1.02]), 3.98)

    def mix_numbers_list(self):
        """ Pass a list with integers and floats """
        self.assertEqual(max_integer([1.2, 4, 3.89, 2, 1.02, 4.01]), 4.01)

    def few_arguments(self):
        """ Pass few arguments """
        self.assertRaises(TypeError, max_integer())

    def many_arguments(self):
        """ Pass many arguments """
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3], 4)

    def none_argument(self):
        """ Pass none as an argument """
        with self.assertRaises(TypeError):
            max_integer(None)

    def non_list_argument(self):
        """ Pass string, tuple and int as parameter """
        self.assertRaises(TypeError, max_integer("hello"))
        self.assertRaises(TypeError, max_integer((1, 2)))
        with self.assertRaises(TypeError):
            max_integer(1)

    def wrong_list(self):
        """ Pass string with elements that are not strings or floats """
        self.assertRaises(TypeError, max_integer(["hello", "hi"]))
        with self.assertRaises(TypeError):
            max_integer([1, 2, "hello"])
