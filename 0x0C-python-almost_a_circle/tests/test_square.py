#!/usr/bin/python3
""" Rectangle class test module
"""
import unittest
import io
import sys
from models.base import Base
from models.square import Square


class TestSqauare(unittest.TestCase):
    """ Tests for Square class
    """
    def tearDown(self):
        """ Clean up action at the end of each test
        """
        Base._Base__nb_objects = 0

    def test_square_doc_strings(self):
        """ Check class and methods documentation
        """
        self.assertTrue(len(Square.__doc__) > 20)
        self.assertTrue(len(Square.__init__.__doc__) > 20)
        self.assertTrue(len(Square.__str__.__doc__) > 20)
        self.assertTrue(len(Square.area.__doc__) > 20)
        self.assertTrue(len(Square.display.__doc__) > 20)
        self.assertTrue(len(Square.update.__doc__) > 20)
        self.assertTrue(len(Square.to_dictionary.__doc__) > 20)

    def test_constructor_arguments(self):
        """ Test few and too many arguments
            and right number of arguments
        """
        s0 = Square(1)
        s1 = Square(1, 2)
        s2 = Square(1, 2, 3)
        s3 = Square(1, 2, 3, 4)

        with self.assertRaises(TypeError):
            s4 = Square()
        with self.assertRaises(TypeError):
            s4 = Square(1, 2, 3, 4, 5)

    def test_size_validation(self):
        """ Test for size value validation
        """
        with self.assertRaises(TypeError) as e:
            s0 = Square(None, 2, 3, 4)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            s0 = Square("1", 2, 3, 4)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            s0 = Square(1.2, 2, 3, 4)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            s0 = Square(0, 1, 2, 3)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            s0 = Square(-1, 2, 3, 4)
        self.assertEqual("width must be > 0", str(e.exception))

    def test_x_validation(self):
        """ Test for x value validation
        """
        with self.assertRaises(TypeError) as e:
            s0 = Square(1, None, 0, 1)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            s0 = Square(1, "0", 0, 1)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            s0 = Square(1, 0.1, 0, 1)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            s0 = Square(1, -1, 0, 1)
        self.assertEqual("x must be >= 0", str(e.exception))

    def test_y_validation(self):
        """ Test for x value validation
        """
        with self.assertRaises(TypeError) as e:
            s0 = Square(1, 1, None, 1)
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            s0 = Square(1, 0, "0", 1)
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            s0 = Square(1, 0, 0.1, 1)
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            s0 = Square(1, 0, -1, 1)
        self.assertEqual("y must be >= 0", str(e.exception))

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

        s0.update(2)
        self.assertEqual(str(s0), "[Square] (2) 2/1 - 2")

        s0.update(2, 6)
        self.assertEqual(str(s0), "[Square] (2) 2/1 - 6")

        s0.update(3, 4, 6)
        self.assertEqual(str(s0), "[Square] (3) 6/1 - 4")

        s0.update(9, 12, 7, 0)
        self.assertEqual(str(s0), "[Square] (9) 7/0 - 12")

        s0.update(1, 9, 3, 4, 5)
        self.assertEqual(str(s0), "[Square] (1) 3/4 - 9")

    def test_update_with_kwargs(self):
        """ Test for update method with keyword arguments
        """
        sorted_dict = {'id': 3, 'size': 8, 'x': 3, 'y': 1}
        random_dict = {'size':  9, 'x': 0, 'id': 10, 'y': 5}
        long_dict = {'width': 0, 'x': 3, 'height': 9,
                     'id': 4, 'y': 1, 'size': 7}
        short_dict0 = {'id': 3}
        short_dict1 = {'id': 5, 'size': 9}
        short_dict2 = {'id': 7, 'size': 12, 'x': 1}

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

        s0.update(**short_dict0)
        self.assertEqual(str(s0), "[Square] (3) 3/1 - 7")

        s0.update(**short_dict1)
        self.assertEqual(str(s0), "[Square] (5) 3/1 - 9")

        s0.update(**short_dict2)
        self.assertEqual(str(s0), "[Square] (7) 1/1 - 12")

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
