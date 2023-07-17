#!/usr/bin/python3
"""
Testing Base class
"""
import json
import unittest
from models import base
from models import rectangle



class TestBase(unittest.TestCase):
    """Testing Base class"""

    def test_doc_module(self):
        """checking the module docstring"""
        doc_str = base.Base.__doc__
        self.assertGreater(len(doc_str), 1)

    def test_doc_class(self):
        """checking the class docstring""" 
        self.assertGreater(len(base.Base.__doc__), 1)

    def test_doc_instantation(self):
        """Checking the init method docstring""" 
        self.assertGreater(len(base.Base.__init__.__doc__), 1)

    def test_basics(self):
        """Basic tests"""
        self.base = base.Base(1)
        self.assertEqual(self.base.id, 1)
        self.new_obj = base.Base(5)
        self.assertEqual(self.new_obj.id, 5)

    def test_extra_args(self):
        """Validate behavior when passing extra arguments"""
        try:
            base.Base(32, 25)
        except TypeError:
            pass
        else:
            raise AssertionError
        try:
            base.Base("string", 30, 6)
        except TypeError:
            pass
        else:
            raise AssertionError

    def test_json(self):
        """ Testing json function"""
        self.b1 = base.Base()
        dict_0 = {"key0": 0, "key1": 1}
        list_dict = [dict_0]
        json_dict = self.b1.to_json_string(list_dict)
        self.assertFalse(isinstance(json_dict, dict))
        self.assertTrue(isinstance(json_dict, str))
        """Testing a list of dictionaries"""
        dict_1 = {"key2": 2, "key3": 3}
        list_dict = [dict_0, dict_1]
        json_dict = self.b1.to_json_string(list_dict)
        self.assertFalse(isinstance(json_dict, dict))
        self.assertTrue(isinstance(json_dict, str))

    def test_json_to_file(self):
        """Test the function 'json_to_file' for JSON serialization"""
        self.rect_1 = rectangle.Rectangle(3, 6)
        self.rect_1.save_to_file([self.rect_1])
        data = ""
        try:
            f = open("Rectangle.json", "r")
            data = f.read()
        finally:
            if f:
                f.close()
        self.assertEqual(len(data), 52)

        self.rect_2 = rectangle.Rectangle(5, 8)
        self.rect_2.save_to_file([self.rect_1, self.rect_2])
        data = ""
        try:
            f = open("Rectangle.json", "r")
            data = f.read()
        finally:
            if f:
                f.close()
        self.assertEqual(len(data), 104)

    def test_empty_string(self):
        """Test case for converting an empty list to JSON string"""
        json_string = base.Base.to_json_string([])
        self.assertEqual(json_string, [])
        self.assertTrue(isinstance(json_string, str))

    def test_None_to_json(self):
        """Test case for converting None to JSON string"""
        json_string = base.Base.to_json_string(None)
        self.assertEqual(json_string, [])
        self.assertTrue(isinstance(json_string, str))

    def test_create_class_from_dict(self):
        """Test case for creating an instance from a dictionary"""
        self.rectangle = rectangle.Rectangle(8, 2, 1)
        self.rectangle_dict = self.rectangle.to_dictionary()

    def test_from_json(self):
        """ Testing from jsomn function"""
        self.rectangle = rectangle.Rectangle(3, 5)
        list_dict = [self.rectangle.to_dictionary()]
        json_list_input = self.rectangle.to_json_string(list_dict)
        from_json = self.rectangle.from_json_string(json_list_input)
        self.assertFalse(isinstance(from_json, dict))
        self.assertTrue(isinstance(from_json, list))
        self.assertFalse(isinstance(from_json[0], list))
        self.assertTrue(isinstance(from_json[0], dict))
        self.assertEqual(self.rectangle.from_json_string(None), [])
        self.assertEqual(self.rectangle.from_json_string("[]"), [])

    if __name__ == '__main__':
        unittest.main()
