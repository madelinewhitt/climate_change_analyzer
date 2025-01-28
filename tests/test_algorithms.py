import unittest
from src.algorithms import add


class TestAddFunction(unittest.TestCase):
    def test_add(self):
        result = add(1,3)
        self.assertEqual(result, 4)

if __name__ == 'main':
    unittest.main()
