"""Various stuff tests."""


# !DEV -----------------------
# DEBUG: to be removed before publishing
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/exsextractor')))
# !DEV ----------------------

from src.exsextractor.stuff import (
    int_stuff,
    float_stuff,
    str_stuff,
    bool_stuff,
    list_stuff,
    dict_stuff,
    tuple_stuff,
    set_stuff,
    set_stuff,
    frozenset_stuff,
    bytes_stuff,
    bytearray_stuff,
    memoryview_stuff,
    complex_stuff,
    exception_stuff
)
from src.exsextractor.utils import DictTestCase

import unittest


class NumbersTests(unittest.TestCase):
    def test_int_stuff(self):
        result = int_stuff(1,2)
        self.assertEqual(result,3)
        self.assertNotEqual(result,4)
    
    def test_float_stuff(self):
        result = float_stuff(1.0,2.0)
        self.assertAlmostEqual(result,3.0)
        result = float_stuff(1.5555,1.5556)
        self.assertAlmostEqual(result,3.1111,4)
    
    def test_bool_stuff(self):
        result = bool_stuff(True,False)
        self.assertFalse(result)
        self.assertTrue(not result)
    
    def test_complex_stuff(self):
        result = complex_stuff(1j,2j)
        self.assertEqual(result,1j+2j)

class DictTests(DictTestCase):
    def test_dict_stuff(self):
        result = dict_stuff({"a":1,"b":2},{"c":3,"d":4})
        self.assertDictEqual(result,{"a":1,"b":2,"c":3,"d":4})
        self.assertDictSubsetOf({"a":1,"d":4},result)
        
class SetsTests(unittest.TestCase):
    def test_list_stuff(self):
        result = list_stuff([1,2],[3,4])
        self.assertListEqual(result,[1,2,3,4])
        self.assertIn(3,result)
    
    def test_tuple_stuff(self):
        result = tuple_stuff((1,2),(3,4))
        self.assertTupleEqual(result,(1,2,3,4))
        self.assertIn(3,result)
    
    def test_set_stuff(self):
        result = set_stuff({1,2},{3,4})
        self.assertSetEqual(result,{1,2,3,4})
        self.assertIn(3,result)
    
    def test_frozenset_stuff(self):
        result = frozenset_stuff(frozenset({1,2}),frozenset({3,4}))
        self.assertSetEqual(result,frozenset({1,2,3,4}))
        self.assertIn(3,result)

class StringsAndMemoryTests(unittest.TestCase):
    def test_str_stuff(self):
        result = str_stuff("a","b")
        self.assertEqual(result,"ab")
    
    def test_bytes_stuff(self):
        result = bytes_stuff(b"a",b"b")
        self.assertEqual(result,b"ab")
    
    def test_bytearray_stuff(self):
        result = bytearray_stuff(bytearray(b"a"),bytearray(b"b"))
        self.assertEqual(result,bytearray(b"ab"))
    
    def test_memoryview_stuff(self):
        result = memoryview_stuff(memoryview(b"a"),memoryview(b"b"))
        self.assertEqual(result,memoryview(b"ab"))

class ExceptionTests(unittest.TestCase):
    def test_exception_stuff(self):
        with self.assertRaises(Exception):
            exception_stuff(1)

if __name__ == '__main__':
    unittest.main()
