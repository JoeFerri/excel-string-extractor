"""Various utility functions."""

from unittest import TestCase


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
                mismatched.append('%s, expected: %s, actual: %s' %
                                  (safe_repr(key), safe_repr(value),
                                   safe_repr(dictionary[key])))

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
