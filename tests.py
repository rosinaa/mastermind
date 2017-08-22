import unittest

from mastermind import feedback
from mastermind_exceptions import MastermindError


class TestMastermind(unittest.TestCase):

	def test_maker_code_None(self):
		with self.assertRaises(MastermindError):
			feedback(None, ['a', 'b', 'c', 'd'])

	def test_maker_code_invalid(self):
		with self.assertRaises(MastermindError):
			feedback(1, ['a', 'b', 'c', 'd'])

	def test_breaker_code_None(self):
		with self.assertRaises(MastermindError):
			feedback(['a', 'b', 'c', 'd'], None)

	def test_breaker_code_invalid(self):
		with self.assertRaises(MastermindError):
			feedback(['a', 'b', 'c', 'd'], 'asdf')

	def test_different_lengths_entries(self):
		with self.assertRaises(MastermindError):
			feedback(['a', 'b', 'c', 'd'], ['a', 'b'])

	def test_valid_codes(self):
		self.assertEqual(feedback(['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']), ['B', 'B', 'B', 'B'])
		self.assertEqual(feedback(['a', 'b', 'c', 'd'], ['a', 'r', 'd', 'q']), ['B', 'W'])
		self.assertEqual(feedback(['a', 'b', 'c', 'd'], ['b', 'b', 't', 'c']), ['B', 'W'])
		self.assertEqual(feedback(['a', 'b', 'b', 'b'], ['b', 'b', 'c', 'd']), ['B', 'W'])
		self.assertEqual(feedback(['b', 'a', 'b', 'd'], ['a', 'b', 'b', 'a']), ['B', 'W', 'W'])
		self.assertEqual(feedback(['b', 'a', 'b', 'd'], ['a', 'b', 'd', 'b']), ['W', 'W', 'W', 'W'])
		self.assertEqual(feedback(['b', 'a', 'b', 'd'], ['e', 'f', 'g', 'h']), [])


if __name__ == '__main__':
    unittest.main()
