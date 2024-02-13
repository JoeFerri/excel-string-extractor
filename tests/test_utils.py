"""Various utils tests."""


from src.exsextractor.utils import (
    safe_repr,
    DictTestCase,
    nargs_range,
    bool_parser,
    pair_parser
)
import unittest

# !DEV -----------------------
# DEBUG: to be removed before publishing
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/exsextractor')))
# !DEV ----------------------


# TODO:


if __name__ == '__main__':
    unittest.main()
