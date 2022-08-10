#!/usr/bin/python3
""" Rectangle class test module
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests for Rectangle class
    """

    def tearDown(self):
        """ Clean up action at the end of every test
        """
        Base._Base__nb_objects = 0

    def test_rectangle_doc_strings(self):
        """ Check base class documentation
        """
        self.assertTrue(len(Rectangle.__doc__) > 20)
        self.assertTrue(len(Rectangle.__init__.__doc__) > 20)
        self.assertTrue(len(Rectangle.__str__.__doc__) > 20)
        self.assertTrue(len(Rectangle.area.__doc__) > 20)
        self.assertTrue(len(Rectangle.display.__doc__) > 20)
        self.assertTrue(len(Rectangle.update.__doc__) > 20)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 20)

    def test_constructor_arguments(self):
        """ Test few and too many arguments
        """
        r0 = Rectangle(1, 2)
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)

        with self.assertRaises(TypeError):
            r5 = Rectangle()
        with self.assertRaises(TypeError):
            r5 = Rectangle(1)
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_validation(self):
        """ Test for width value validation
        """
        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(None, 2, 0, 0, 1)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r0 = Rectangle("1", 2, 0, 0, 1)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(1.2, 2, 0, 0, 1)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r0 = Rectangle(0, 2, 0, 0, 1)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r0 = Rectangle(-1, 2, 0, 0, 1)
        self.assertEqual("width must be > 0", str(e.exception))

    def test_height_validation(self):
        """ Test for height value validation
        """
        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(1, None, 0, 0, 1)
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(2, "2", 0, 0, 1)
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(2, 1.2, 0, 0, 1)
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r0 = Rectangle(2, 0, 0, 0, 1)
        self.assertEqual("height must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r0 = Rectangle(1, -2, 0, 0, 1)
        self.assertEqual("height must be > 0", str(e.exception))

    def test_x_validation(self):
        """ Test for x value validation
        """
        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(1, 2, None, 0, 1)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(1, 2, "0", 0, 1)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(1, 2, 0.1, 0, 1)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r0 = Rectangle(1, 2, -1, 0, 1)
        self.assertEqual("x must be >= 0", str(e.exception))

    def test_y_validation(self):
        """ Test for x value validation
        """
        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(1, 2, 1, None, 1)
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(1, 2, 0, "0", 1)
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            r0 = Rectangle(1, 2, 0, 0.1, 1)
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            r0 = Rectangle(1, 2, 0, -1, 1)
        self.assertEqual("y must be >= 0", str(e.exception))

    def test_area(self):
        """ Test for area method
        """
        r0 = Rectangle(2, 3, 2, 1, 1)
        r1 = Rectangle(14, 7, 3, 0, 7)
        self.assertEqual(r0.area(), 6)
        self.assertEqual(r1.area(), 98)

    def test_display(self):
        """ Test for output of display function
        """
        r0 = Rectangle(2, 3, 2, 1, 4)
        r1 = Rectangle(2, 3, 2, 0, 3)
        r2 = Rectangle(2, 3, 0, 1, 3)
        r3 = Rectangle(3, 4, 0, 0, 3)
        r_capture = io.StringIO()
        sys.stdout = r_capture
        r0.display()
        self.assertEqual(r_capture.getvalue(), "\n  ##\n  ##\n  ##\n")

        r_capture.truncate(0)
        r_capture.seek(0)
        r1.display()
        self.assertEqual(r_capture.getvalue(), "  ##\n  ##\n  ##\n")

        r_capture.truncate(0)
        r_capture.seek(0)
        r2.display()
        self.assertEqual(r_capture.getvalue(), "\n##\n##\n##\n")

        r_capture.truncate(0)
        r_capture.seek(0)
        r3.display()
        self.assertEqual(r_capture.getvalue(), "###\n###\n###\n###\n")

    def test_str(self):
        """ Test magic method __str__
        """
        r0 = Rectangle(2, 3, 2, 1, 2)
        r1 = Rectangle(1, 3, 2, 2, 3)
        self.assertEqual(str(r0), "[Rectangle] (2) 2/1 - 2/3")
        self.assertEqual(str(r1), "[Rectangle] (3) 2/2 - 1/3")

    def test_update_with_args(self):
        """ Test for update method with non-keyword
            arguments
        """
        r0 = Rectangle(2, 3, 2, 1, 4)
        self.assertEqual(str(r0), "[Rectangle] (4) 2/1 - 2/3")

        r0.update()
        self.assertEqual(str(r0), "[Rectangle] (4) 2/1 - 2/3")

        r0.update(9, 12, 7, 0, 4)
        self.assertEqual(str(r0), "[Rectangle] (9) 0/4 - 12/7")

        r0.update(2)
        self.assertEqual(str(r0), "[Rectangle] (2) 0/4 - 12/7")

        r0.update(3, 6)
        self.assertEqual(str(r0), "[Rectangle] (3) 0/4 - 6/7")

        r0.update(4, 7, 6)
        self.assertEqual(str(r0), "[Rectangle] (4) 0/4 - 7/6")

        r0.update(2, 6, 7, 3)
        self.assertEqual(str(r0), "[Rectangle] (2) 3/4 - 6/7")

        r0.update(1, 9, 3, 4, 1, 5, 7)
        self.assertEqual(str(r0), "[Rectangle] (1) 4/1 - 9/3")

    def test_update_with_kwargs(self):
        """ Test for update method with keyword arguments
        """
        sorted_dict = {'id': 3, 'width': 10, 'height': 8, 'x': 3, 'y': 1}
        random_dict = {'width': 9, 'x': 0, 'height': 19, 'id': 10, 'y': 5}
        long_dict = {'width': 7, 'x': 3, 'height': 9, 'id': 4,
                     'y': 1, 'unknown': 0}
        short_dict0 = {'id': 3}
        short_dict1 = {'id': 4, 'width': 10}
        short_dict2 = {'id': 3, 'width': 12, 'height': 7}
        short_dict3 = {'id': 4, 'width': 7, 'height': 12, 'x': 5}

        r0 = Rectangle(2, 3, 2, 1, 4)
        self.assertEqual(str(r0), "[Rectangle] (4) 2/1 - 2/3")

        r0.update(**{})
        self.assertEqual(str(r0), "[Rectangle] (4) 2/1 - 2/3")

        r0.update(**sorted_dict)
        self.assertEqual(str(r0), "[Rectangle] (3) 3/1 - 10/8")

        r0.update(**random_dict)
        self.assertEqual(str(r0), "[Rectangle] (10) 0/5 - 9/19")

        r0.update(**long_dict)
        self.assertEqual(str(r0), "[Rectangle] (4) 3/1 - 7/9")

        r0.update(**short_dict0)
        self.assertEqual(str(r0), "[Rectangle] (3) 3/1 - 7/9")

        r0.update(**short_dict1)
        self.assertEqual(str(r0), "[Rectangle] (4) 3/1 - 10/9")

        r0.update(**short_dict2)
        self.assertEqual(str(r0), "[Rectangle] (3) 3/1 - 12/7")

        r0.update(**short_dict3)
        self.assertEqual(str(r0), "[Rectangle] (4) 5/1 - 7/12")

    def test_args_and_kwargs(self):
        """ Test when args and kwargs are both present
        """
        kwargs = {'id': 3, 'width': 10, 'height': 8, 'x': 3, 'y': 1}

        r0 = Rectangle(2, 3, 2, 1, 4)
        self.assertEqual(str(r0), "[Rectangle] (4) 2/1 - 2/3")

        r0.update(9, 12, 7, 0, 4, **kwargs)
        self.assertEqual(str(r0), "[Rectangle] (9) 0/4 - 12/7")

    def test_to_dictionary(self):
        """ Test to_dictionary method
        """
        r0 = Rectangle(2, 3, 2, 1, 4)
        self.assertEqual(r0.to_dictionary(),
                         {'id': 4, 'width': 2, 'height': 3, 'x': 2, 'y': 1})
