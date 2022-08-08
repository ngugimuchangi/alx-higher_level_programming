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
    def setUp(self):
        """ Test setup
        """
        self.base0 = Base()
        self.base1 = Base()
        self.base2 = Base(1)
        self.base3 = Base(4)

    def test_arguments(self):
        with self.assertRaises(TypeError):
            self.base4 = Base(1, 3)

    def test_nb_objects(self):
        """ Test private class attribute __nb_objects
        """
        self.assertTrue(self.base0._Base__nb_objects ==
                        self.base3._Base__nb_objects)
        self.assertFalse(hasattr(self.base0, '__nb_objects'))
        self.assertEqual(self.base0._Base__nb_objects, 6)

    def test_id(self):
        """ Test object ids and uniqueness
        """
        self.assertEqual(self.base0.id, 3)
        self.assertEqual(self.base1.id, 4)
        self.assertEqual(self.base2.id,  1)
        self.assertEqual(self.base3.id,  4)
        self.assertFalse(self.base0 is self.base2)

    def tearDown(self):
        """ Cleanup actions
        """
        del self.base0
        del self.base1
        del self.base2
        del self.base3
