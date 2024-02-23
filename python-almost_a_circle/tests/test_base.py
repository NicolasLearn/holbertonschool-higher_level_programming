#!/usr/bin/python3
"""Unittest for the module Base, class Base"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests to the Base class. Tasks 0
    """
    def setUp(self):
        """Update for each test"""
        Base._Base__nb_objects = 0
        pass

    def test_is_instance(self):
        """Test if b is a right instance"""
        b = Base()
        self.assertIsInstance(b, Base)

    def test_private_attribute(self):
        """Tests if nb_objects is private class attribute."""
        b = Base()
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
        self.assertTrue(b.id, 1)

    def test_initialization_of_attribute(self):
        """Test if nb_objects initializes to zero."""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        """Tests Base() instantiation."""

        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        id_int = 74
        b3 = Base(id_int)
        self.assertEqual(b3.id, id_int)

        id_str = "b4"
        b4 = Base(id_str)
        self.assertEqual(b4.id, id_str)

    def test_constructor(self):
        """Tests constructor initialization"""
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "Base.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "Base.__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    """Tests to_json_string, tasks 15
    """
    def test_to_json_string(self):
        """Tests to_json_string() signature:"""

        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "Base.to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        d = [{'x': 10, 'y': 20, 'width': 30, 'id': 55,
             'height': 40}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))

        d = [{"test": 74}]
        self.assertEqual(Base.to_json_string(d), '[{"test": 74}]')

        d = [{"test": 74}, {"abc": 123}, {123: "abc"}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"test": 74}, {"abc": 123}, {"123": "abc"}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 10, 'y': 20, 'width': 30, 'id': 55,
             'height': 40}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))

        d = [{}]
        self.assertEqual(Base.to_json_string(d), '[{}]')

        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d), '[{}, {}]')

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    """Tests to save_to_file, tasks 16
    """
    def tests_save_to_file(self):
        """Tests save_to_file() method."""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    """Tests to from_json_string, tasks 17
    """
    def test_test_from_json_string(self):
        """Tests to_json_string() signature:"""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "Base.from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 10, "y": 20, "width": 30, "id": 55, "height": 40}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 10, 'y': 20, 'width': 30, 'id': 55,
             'height': 40}]
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"Test": 74}, {"abc": 123}, {"zero": 0}]
        s = '[{"Test": 74}, {"abc": 123}, {"zero": 0}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"Test": 74}]
        s = '[{"Test": 74}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 10, 'y': 20, 'width': 30, 'id': 55,
             'height': 40}]
        s = '[{"x": 10, "y": 20, "width": 30, "id": 55, \
"height": 40}]'
        self.assertEqual(Base.from_json_string(s), d)

        list_in = [
            {'id': 74, 'width': 10, 'height': 5},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list_out = Rectangle.from_json_string(
            Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)

    """Tests to create, tasks 18
    """
    def test_create(self):
        """Tests create() method."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    """Tests to load_from_file, tasks 19
    """
    def test_load_from_file(self):
        """Tests load_from_file() method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))


if __name__ == "__main__":
    unittest.main()
