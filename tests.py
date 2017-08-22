import unittest

from mastermind import feedback, feedback_list_comprehension
from mastermind_exceptions import MastermindError


class ParentMastermindTestCase(object):

    def test_maker_code_None(self):
        with self.assertRaises(MastermindError):
            self.func(None, ['a', 'b', 'c', 'd'])

    def test_maker_code_invalid(self):
        with self.assertRaises(MastermindError):
            self.func(1, ['a', 'b', 'c', 'd'])

    def test_breaker_code_None(self):
        with self.assertRaises(MastermindError):
            self.func(['a', 'b', 'c', 'd'], None)

    def test_breaker_code_invalid(self):
        with self.assertRaises(MastermindError):
            self.func(['a', 'b', 'c', 'd'], 'asdf')

    def test_different_lengths_entries(self):
        with self.assertRaises(MastermindError):
            self.func(['a', 'b', 'c', 'd'], ['a', 'b'])

    def test_valid_codes(self):
        self.assertEqual(self.func(['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']), ['B', 'B', 'B', 'B'])
        self.assertEqual(self.func(['a', 'b', 'c', 'd'], ['a', 'r', 'd', 'q']), ['B', 'W'])
        self.assertEqual(self.func(['a', 'b', 'c', 'd'], ['b', 'b', 't', 'c']), ['B', 'W'])
        self.assertEqual(self.func(['a', 'b', 'b', 'b'], ['b', 'b', 'c', 'd']), ['B', 'W'])
        self.assertEqual(self.func(['b', 'a', 'b', 'd'], ['a', 'b', 'b', 'a']), ['B', 'W', 'W'])
        self.assertEqual(self.func(['b', 'a', 'b', 'd'], ['a', 'b', 'd', 'b']), ['W', 'W', 'W', 'W'])
        self.assertEqual(self.func(['b', 'a', 'b', 'd'], ['e', 'f', 'g', 'h']), [])


class TestMastermind(unittest.TestCase, ParentMastermindTestCase):
    def setUp(self):
        self.func = feedback


class TestMastermindList(unittest.TestCase, ParentMastermindTestCase):
    def setUp(self):
        self.func = feedback_list_comprehension


if __name__ == '__main__':
    unittest.main()
