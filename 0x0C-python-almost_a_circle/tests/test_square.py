#!/usr/bin/python3
""" Rectangle class test module
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ Tests for Rectangle class
    """

    def test_constructor_arguments(self):
        """ Test few and too many arguments
        """
        with self.assertRaises(TypeError):
            s0 = Square()
        with self.assertRaises(TypeError):
            s0 = Square(1, 2, 3, 4, 5)

    def test_size_validation(self):
        """ Test for size value validation
        """
        s0 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError) as e:
            s0.size = None
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            s0.size = "hello"
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            s0.size = 1.2
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            s0.size = 0
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            s0.size = -1
        self.assertEqual("width must be > 0", str(e.exception))

    def test_area(self):
        """ Test for area method
        """
        s0 = Square(2, 3, 2, 1)
        s1 = Square(4, 7, 3)
        self.assertEqual(s0.area(), 4)
        self.assertEqual(s1.area(), 16)

    def test_display(self):
        """ Test for output of display function
        """
        s0 = Square(2, 2, 2, 1)
        s1 = Square(4, 0, 0, 2)
        s_capture = io.StringIO()
        sys.stdout = s_capture
        s0.display()
        self.assertEqual(s_capture.getvalue(), "\n\n  ##\n  ##\n")
        s_capture.truncate(0)
        s_capture.seek(0)
        s1.display()
        self.assertEqual(s_capture.getvalue(), "####\n####\n####\n####\n")

    def test_str(self):
        """ Test magic method __str__
        """
        s0 = Square(2, 3, 2, 9)
        s1 = Square(1, 3, 2, 3)
        self.assertEqual(str(s0), "[Square] (9) 3/2 - 2")
        self.assertEqual(str(s1), "[Square] (3) 3/2 - 1")

    def test_update_with_args(self):
        """ Test for update method with non-keyword
            arguments
        """
        s0 = Square(2, 2, 1, 4)
        self.assertEqual(str(s0), "[Square] (4) 2/1 - 2")

        s0.update()
        self.assertEqual(str(s0), "[Square] (4) 2/1 - 2")

        s0.update(9, 12, 7, 0)
        self.assertEqual(str(s0), "[Square] (9) 7/0 - 12")

        s0.update(2, 6)
        self.assertEqual(str(s0), "[Square] (2) 7/0 - 6")

        s0.update(1, 9, 3, 4, 5)
        self.assertEqual(str(s0), "[Square] (1) 3/4 - 9")

    def test_update_with_kwargs(self):
        """ Test for update method with keyword arguments
        """
        sorted_dict = {'id': 3, 'size': 8, 'x': 3, 'y': 1}
        random_dict = {'size':  9, 'x': 0, 'id': 10, 'y': 5}
        long_dict = {'width': 0, 'x': 3, 'height': 9,
                     'id': 4, 'y': 1, 'size': 7}
        short_dict = {'id': 3, 'x': 7}

        s0 = Square(2, 3, 2, 1)
        self.assertEqual(str(s0), "[Square] (1) 3/2 - 2")

        s0.update(**{})
        self.assertEqual(str(s0), "[Square] (1) 3/2 - 2")

        s0.update(**sorted_dict)
        self.assertEqual(str(s0), "[Square] (3) 3/1 - 8")

        s0.update(**random_dict)
        self.assertEqual(str(s0), "[Square] (10) 0/5 - 9")

        s0.update(**long_dict)
        self.assertEqual(str(s0), "[Square] (4) 3/1 - 7")

        s0.update(**short_dict)
        self.assertEqual(str(s0), "[Square] (3) 7/1 - 7")

    def test_args_and_kwargs(self):
        """ Test when args and kwargs are both present
        """
        kwargs = {'id': 3, 'size': 10, 'x': 3, 'y': 1}

        s0 = Square(3, 2, 1, 4)
        self.assertEqual(str(s0), "[Square] (4) 2/1 - 3")

        s0.update(9, 12, 7, 4, **kwargs)
        self.assertEqual(str(s0), "[Square] (9) 7/4 - 12")

    def test_dictionary(self):
        """ Test to_dictionary method
        """
        s0 = Square(3, 2, 1, 4)
        self.assertEqual(s0.to_dictionary(),
                         {'id': 4, 'size': 3, 'x': 2, 'y': 1})
