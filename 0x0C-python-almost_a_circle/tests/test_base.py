#!/usr/bin/python3
""" Base class and subclass (Rectagle and Square)
    test module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Tests for Base class
    """

    def test_constructor_arguments(self):
        base0 = Base()
        base0 = Base(1)
        with self.assertRaises(TypeError):
            base0 = Base(1, 3)

    def test_nb_objects(self):
        """ Test private class attribute __nb_objects
        """
        base0 = Base(2)
        base1 = Base(3)
        self.assertTrue(base0._Base__nb_objects ==
                        base1._Base__nb_objects)
        self.assertFalse(hasattr(base0, '__nb_objects'))
        self.assertEqual(base0._Base__nb_objects, 2)

    def test_id(self):
        """ Test object ids and uniqueness
        """
        base0 = Base()
        base1 = Base(2)
        self.assertEqual(base0.id, 2)
        self.assertEqual(base1.id,  2)
        self.assertFalse(base0 is base1)
