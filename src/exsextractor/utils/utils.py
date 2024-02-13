"""Various utility functions."""

from unittest import TestCase

import argparse
import re


_MAX_LENGTH = 80


def safe_repr(obj, short=False):
    # Python\Python311\Lib\unittest\util.py
    try:
        result = repr(obj)
    except Exception:
        result = object.__repr__(obj)
    if not short or len(result) < _MAX_LENGTH:
        return result
    return result[:_MAX_LENGTH] + ' [truncated]...'


class DictTestCase (TestCase):

    def assertDictSubsetOf(self, subset, dictionary, msg=None):
        # Python\Python311\Lib\unittest\case.py
        """
            Checks whether dictionary is a superset of subset.

            Old assertDictContainsSubset() was renamed to assertDictSubsetIn().
            The assertDictContainsSubset() method was deprecated because
            it was misimplemented with the arguments in the wrong order.
            This created hard-to-debug optical illusions where tests like
            TestCase().assertDictContainsSubset({'a':1, 'b':2}, {'a':1}) would fail.

            (Contributed by Raymond Hettinger.)

            see: https://docs.python.org/3/whatsnew/3.2.html#unittest
        """

        self.assertIsInstance(subset, dict, 'First argument is not a dictionary')
        self.assertIsInstance(dictionary, dict, 'Second argument is not a dictionary')
        """Checks whether dictionary is a superset of subset."""
        missing = []
        mismatched = []
        for key, value in subset.items():
            if key not in dictionary:
                missing.append(key)
            elif value != dictionary[key]:
                mismatched.append(
                    '%s, expected: %s, actual: %s' %
                    (safe_repr(key), safe_repr(value), safe_repr(dictionary[key]))
                )

        if not (missing or mismatched):
            return

        standardMsg = ''
        if missing:
            standardMsg = 'Missing: %s' % ','.join(safe_repr(m) for m in missing)
        if mismatched:
            if standardMsg:
                standardMsg += '; '
            standardMsg += 'Mismatched values: %s' % ','.join(mismatched)

        self.fail(self._formatMessage(msg, standardMsg))


def nargs_range(nmin: int, nmax: int) -> argparse.Action:
    """https://stackoverflow.com/a/4195302"""
    class NArgsRange (argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            if not nmin <= len(values) <= nmax:
                msg = 'argument "{f}" requires between {nmin} and {nmax} arguments'.format(
                    f=self.dest, nmin=nmin, nmax=nmax)
                raise argparse.ArgumentError(self, msg)
            setattr(args, self.dest, values)
    return NArgsRange


def bool_parser(s: str) -> bool | str:
    if s.lower() == 'true':
        return True
    elif s.lower() == 'false':
        return False
    return s


def pair_parser(sep: str = '=', escaped_sep: str = '%') -> callable:
    def parser(s: str) -> tuple[str, str]:
        pattern_str = f'{escaped_sep}{sep}'
        pattern = rf'(?<!{escaped_sep}){sep}'
        parts = re.split(pattern, s)

        if len(parts) == 2:
            s1 = parts[0].replace(pattern_str, sep)
            s2 = parts[1].replace(pattern_str, sep)
            return s1, s2
        else:
            raise ValueError("Invalid format: unable to split the string using the provided separator and escape separator")
    return parser
