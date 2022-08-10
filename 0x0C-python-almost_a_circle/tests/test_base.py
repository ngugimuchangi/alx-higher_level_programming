#!/usr/bin/python3
""" Base class and subclass (Rectagle and Square)
    test module
"""
import unittest
import inspect
from os import remove
from json import dumps
from csv import DictReader
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Tests for Base class
    """
    def tearDown(self):
        """ Clean up action at the end of each test
        """
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(cls):
        """ Clean up actions at the end of the class
        """
        test_files = ["Base.json", "Rectangle.json", "Rectangle.csv",
                      "Square.json", "Square.csv"]
        for i in test_files:
            remove(i)

    def test_base_doc_strings(self):
        """ Check base class documentation
        """
        self.assertTrue(len(Base.__doc__) > 20)
        self.assertTrue(len(Base.__init__.__doc__) > 20)
        self.assertTrue(len(Base.to_json_string.__doc__) > 20)
        self.assertTrue(len(Base.from_json_string.__doc__) > 20)
        self.assertTrue(len(Base.create.__doc__) > 20)
        self.assertTrue(len(Base.save_to_file.__doc__) > 20)
        self.assertTrue(len(Base.load_from_file.__doc__) > 20)
        self.assertTrue(len(Base.save_to_file_csv.__doc__) > 20)
        self.assertTrue(len(Base.load_from_file_csv.__doc__) > 20)
        self.assertTrue(len(Base.draw.__doc__) > 20)

    def test_inheritance(self):
        """ Test inheritances of Base class and subclasses
        """
        base0 = Base(3)
        r0 = Rectangle(1, 2, 3, 4, 5)
        s0 = Square(1, 2, 3, 4)
        self.assertIsInstance(base0, object)
        self.assertIsInstance(base0, Base)
        self.assertIsInstance(r0, object)
        self.assertIsInstance(r0, Base)
        self.assertIsInstance(r0, Rectangle)
        self.assertIsInstance(s0, object)
        self.assertIsInstance(s0, Base)
        self.assertIsInstance(s0, Rectangle)
        self.assertIsInstance(s0, Square)
        self.assertNotIsInstance(r0, Square)
        self.assertNotIsInstance(base0, Rectangle)
        self.assertNotIsInstance(base0, Square)

    def test_constructor_arguments(self):
        """ Test constructor arguments for self
        """
        base0 = Base()
        base0 = Base(89)

        with self.assertRaises(TypeError):
            base0 = Base(1, 3)

    def test_nb_objects(self):
        """ Test private class attribute __nb_objects
        """
        base0 = Base()
        base1 = Base(2)
        base3 = Base()
        base4 = Base(5)
        base5 = Base()

        self.assertTrue(base0._Base__nb_objects ==
                        base5._Base__nb_objects)
        self.assertFalse(hasattr(base0, '__nb_objects'))
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_id(self):
        """ Test automatic assigning of id
        """
        base0 = Base()
        base1 = Base()
        base2 = Base(2)
        base3 = Base()
        base4 = Base(12)

        self.assertEqual(base0.id, 1)
        self.assertEqual(base3.id,  3)
        self.assertEqual(base4.id,  12)
        self.assertEqual(base1.id, base2.id)
        self.assertFalse(base1 is base2)

    def test_to_json_string(self):
        """ Test to dictionary for rectangles
        """
        r0 = Rectangle(1, 2, 3, 4, 5)
        r1 = Rectangle(1, 3, 4, 7, 9)
        s0 = Square(1, 2, 3, 4)
        s1 = Square(4, 3, 2, 1)

        dict_list0 = [r0.to_dictionary(), r1.to_dictionary()]
        dict_list1 = [s0.to_dictionary(), s1.to_dictionary()]
        dict_list2 = [r1.to_dictionary(), s1.to_dictionary()]

        self.assertEqual(Base.to_json_string("hello"), None)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(dict_list0), dumps(dict_list0))
        self.assertEqual(Base.to_json_string(dict_list1), dumps(dict_list1))
        self.assertEqual(Base.to_json_string(dict_list2), dumps(dict_list2))

        self.assertEqual(Rectangle.to_json_string(dict_list0),
                         dumps(dict_list0))
        self.assertEqual(Square.to_json_string(dict_list1), dumps(dict_list1))

    def test_from_json_string(self):
        """ Test method that converts json string to python object
        """
        r0 = Rectangle(1, 2, 3, 4, 5)
        json_str = r0.to_json_string([r0.to_dictionary()])
        new_object = r0.from_json_string(json_str)

        self.assertTrue(new_object == [r0.to_dictionary()])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('1'), 1)

    def test_create(self):
        """ Test method for creating new rectangle and square instances
        """
        r0 = Rectangle(1, 2, 3, 4, 5)
        s0 = Square(4, 3, 2, 1)

        r_dict = r0.to_dictionary()
        s_dict = s0.to_dictionary()

        r1 = Rectangle.create(**r_dict)
        r2 = Rectangle.create(**{'id': 4})
        r3 = Rectangle.create(**{'id': 4, 'width': 4})
        r4 = Rectangle.create(**{'id': 4, 'width': 4, 'height': 3})
        r5 = Rectangle.create(**{'id': 4, 'width': 4, 'height': 3, 'x': 3})

        s1 = Square.create(**s_dict)
        s2 = Square.create(**{'id': 2})
        s3 = Square.create(**{'id': 2, 'size': 9})
        s4 = Square.create(**{'id': 2, 'size': 9, 'x': 3})

        with self.assertRaises(NameError):
            Base.create(**r0_dict)

        with self.assertRaises(NameError):
            Base.create(**s0_dict)

        self.assertTrue(str(r1) == str(r0))
        self.assertTrue(str(r2) == "[Rectangle] (4) 0/0 - 1/2")
        self.assertTrue(str(r3) == "[Rectangle] (4) 0/0 - 4/2")
        self.assertTrue(str(r4) == "[Rectangle] (4) 0/0 - 4/3")
        self.assertTrue(str(r5) == "[Rectangle] (4) 3/0 - 4/3")

        self.assertTrue(str(s1) == str(s0))
        self.assertTrue(str(s2) == "[Square] (2) 0/0 - 1")
        self.assertTrue(str(s3) == "[Square] (2) 0/0 - 9")
        self.assertTrue(str(s4) == "[Square] (2) 3/0 - 9")

        self.assertFalse(r1 is r0)
        self.assertFalse(s1 is s0)

    def test_save_to_file(self):
        """ Test method that saves objects to json files
        """
        r0 = Rectangle(10, 7, 2, 8, 1)
        r1 = Rectangle(2, 4, 3, 4, 5)
        s0 = Square(1, 2, 3, 4)
        s1 = Square(4, 3, 2, 1)

        exp_str0 = dumps([r0.to_dictionary(), r1.to_dictionary()])
        exp_str1 = dumps([s0.to_dictionary(), s1.to_dictionary()])
        exp_str2 = dumps([r0.to_dictionary(), s1.to_dictionary()])

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="UTF8") as f:
            json_str = f.read()
        self.assertTrue(json_str == "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="UTF8") as f:
            json_str = f.read()
        self.assertTrue(json_str == "[]")

        Rectangle.save_to_file([r0, r1])
        with open("Rectangle.json", "r") as f:
            json_str = f.read()
        self.assertTrue(json_str == exp_str0)

        Rectangle.save_to_file([s0, s1])
        with open("Rectangle.json", "r") as f:
            json_str = f.read()
        self.assertTrue(json_str == exp_str1)

        Rectangle.save_to_file([r0, s1])
        with open("Rectangle.json", "r") as f:
            json_str = f.read()
        self.assertFalse(json_str == exp_str2)

        Square.save_to_file(None)
        with open("Square.json", "r", encoding="UTF8") as f:
            json_str = f.read()
        self.assertTrue(json_str == "[]")

        Square.save_to_file([])
        with open("Square.json", "r", encoding="UTF8") as f:
            json_str = f.read()
        self.assertTrue(json_str == "[]")

        Square.save_to_file([s0, s1])
        with open("Square.json", "r", encoding="UTF8") as f:
            json_str = f.read()
        self.assertTrue(json_str == exp_str1)

        Square.save_to_file([r0, r1])
        with open("Square.json", "r") as f:
            json_str = f.read()
        self.assertFalse(json_str == exp_str0)

        Square.save_to_file([r0, s1])
        with open("Square.json", "r") as f:
            json_str = f.read()
        self.assertFalse(json_str == exp_str2)

        Base.save_to_file([r0, r1])
        with open("Base.json", "r") as f:
            json_str = f.read()
        self.assertTrue(json_str == exp_str0)

        Base.save_to_file([s0, s1])
        with open("Base.json", "r", encoding="UTF8") as f:
            json_str = f.read()
        self.assertTrue(json_str == exp_str1)

        Square.save_to_file([r0, r1])
        with open("Rectangle.json", "r") as f:
            json_str = f.read()
        self.assertFalse(json_str == exp_str0)

    def test_load_from_file(self):
        """ Test method for creating rectangle and square instances from files
        """
        r0 = Rectangle(10, 7, 2, 8, 1)
        r1 = Rectangle(2, 4, 3, 4, 5)
        s0 = Square(1, 2, 3, 4)
        s1 = Square(4, 3, 2, 1)

        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

        Rectangle.save_to_file([r0, r1])
        obj_list = Rectangle.load_from_file()
        self.assertTrue(type(obj_list is list))
        self.assertTrue(all(type(i) is Rectangle for i in obj_list))
        self.assertTrue(str(r0) == str(obj_list[0]))
        self.assertTrue(str(r1) == str(obj_list[1]))
        self.assertFalse(r0 is obj_list[0])
        self.assertFalse(r1 is obj_list[1])

        Square.save_to_file([s0, s1])
        obj_list = Square.load_from_file()
        self.assertTrue(type(obj_list is list))
        self.assertTrue(all(type(i) is Square for i in obj_list))
        self.assertTrue(str(s0) == str(obj_list[0]))
        self.assertTrue(str(s1) == str(obj_list[1]))
        self.assertFalse(s0 is obj_list[0])
        self.assertFalse(s1 is obj_list[1])

    def test_save_to_csv(self):
        """ Test method for saving instances to csv files
        """
        r0 = Rectangle(10, 7, 2, 8, 1)
        r1 = Rectangle(2, 4, 3, 4, 5)
        s0 = Square(1, 2, 3, 4)
        s1 = Square(4, 3, 2, 1)

        dict0 = [r0.to_dictionary(), r1.to_dictionary()]
        dict1 = [s0.to_dictionary(), s1.to_dictionary()]

        exp_res0 = [{i: str(row[i]) for i in row} for row in dict0]
        exp_res1 = [{i: str(row[i]) for i in row} for row in dict1]

        Rectangle.save_to_file_csv([r0, r1])
        with open("Rectangle.csv", "r", encoding="UTF8") as f:
            content = [row for row in DictReader(f)]
        self.assertTrue(content == exp_res0)

        Square.save_to_file_csv([s0, s1])
        with open("Square.csv", "r", encoding="UTF8") as f:
            content = [row for row in DictReader(f)]
        self.assertTrue(content == exp_res1)

    def test_load_from_csv(self):
        """ Test method to for creating instances from data in csv files
        """
        r0 = Rectangle(10, 7, 2, 8, 1)
        r1 = Rectangle(2, 4, 3, 4, 5)
        s0 = Square(1, 2, 3, 4)
        s1 = Square(4, 3, 2, 1)

        self.assertEqual(Rectangle.load_from_file_csv(), [])
        Rectangle.save_to_file_csv([r0, r1])
        obj_list = Rectangle.load_from_file_csv()
        self.assertTrue(type(obj_list is list))
        self.assertTrue(all(type(i) is Rectangle for i in obj_list))
        self.assertTrue(str(r0) == str(obj_list[0]))
        self.assertTrue(str(r1) == str(obj_list[1]))
        self.assertFalse(r0 is obj_list[0])
        self.assertFalse(r1 is obj_list[1])

        self.assertEqual(Square.load_from_file_csv(), [])
        Square.save_to_file_csv([s0, s1])
        obj_list = Square.load_from_file_csv()
        self.assertTrue(type(obj_list is list))
        self.assertTrue(all(type(i) is Square for i in obj_list))
        self.assertTrue(str(s0) == str(obj_list[0]))
        self.assertTrue(str(s1) == str(obj_list[1]))
        self.assertFalse(s0 is obj_list[0])
        self.assertFalse(s1 is obj_list[1])
