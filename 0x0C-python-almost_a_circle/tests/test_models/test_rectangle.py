#!/usr/bin/python3
""" Rectangle class test module
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestTriangle(unittest.TestCase):
    """ Tests for Rectangle class
    """

    def setUp(self):
        """ Test setup
        """
        self.r0 = Rectangle(2, 3, 2, 1, None)
        self.r1 = Rectangle(3, 4, 0, 0, None)
        self.r2 = Rectangle(1, 3, 2, 2, 3)
        self.r3 = Rectangle(14, 7, 3, 0, 7)

    def test_constructor_arguments(self):
        """ Test few and too many arguments
        """
        with self.assertRaises(TypeError):
            self.r4 = Rectangle()
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(1)
        with self.assertRaises(TypeError):
            self.r4 = Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_validation(self):
        """ Test for width value validation
        """
        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(None, 2, 0, 0, 1)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r4 = Rectangle("hello", 2, 0, 0, 1)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(1.2, 2, 0, 0, 1)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(0, 2, 0, 0, 1)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(-1, 2, 0, 0, 1)
        self.assertEqual("width must be > 0", str(e.exception))

    def test_height_validation(self):
        """ Test for height value validation
        """
        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(1, None, 0, 0, 1)
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(2, "2", 0, 0, 1)
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(2, 1.2, 0, 0, 1)
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(2, 0, 0, 0, 1)
        self.assertEqual("height must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(1, -2, 0, 0, 1)
        self.assertEqual("height must be > 0", str(e.exception))

    def test_x_validation(self):
        """ Test for x value validation
        """
        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(1, 2, None, 0, 1)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(1, 2, "0", 0, 1)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(1, 2, 0.1, 0, 1)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(1, 2, -1, 0, 1)
        self.assertEqual("x must be >= 0", str(e.exception))

    def test_x_validation(self):
        """ Test for x value validation
        """
        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(1, 2, 1, None, 1)
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(1, 2, 0, "0", 1)
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(1, 2, 0, 0.1, 1)
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(1, 2, 0, -1, 1)
        self.assertEqual("y must be >= 0", str(e.exception))

    def test_area(self):
        """ Test for area method
        """
        self.assertEqual(self.r0.area(), 6)
        self.assertEqual(self.r3.area(), 98)

    def test_display(self):
        """ Test for output of display function
        """
        r_capture = io.StringIO()
        sys.stdout = r_capture
        self.r0.display()
        self.assertEqual(r_capture.getvalue(), "\n  ##\n  ##\n  ##\n")
        r_capture.truncate(0)
        r_capture.seek(0)
        self.r1.display()
        self.assertEqual(r_capture.getvalue(), "###\n###\n###\n###\n")

    def test_str(self):
        """ Test magic method __str__
        """
        self.assertEqual(str(self.r0), "")
        self.assertEqual(str(self.r2), "")

    def test_update_with_args(self):
        """ Test for update method with non-keyword
            arguments
        """
        self.r0.update(1, 5, 4, 3, 5) 
        self.assertEqual(str(self.r0), "")
        self.r1.update(1, 5, 4, 3, 5) 
        self.assertEqual(str(self.r0), "")

    def test_update_with_kwargs(self):
        pass


    def test_update_validation(self):
        """ Test for validation during when update values
        """
        pass

    def tearDown(self):
        """ Clean up action at the end of the tests
        """
        del self.r0
        del self.r1
        del self.r2
        del self.r3
