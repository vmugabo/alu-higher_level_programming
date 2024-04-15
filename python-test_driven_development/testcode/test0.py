import unittest
from add_integer import add_integer

class TestAddInteger(unittest.TestCase):

    def test_add_integer(self):
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(1.5, 2.5), 3)
        self.assertEqual(add_integer(1), 99)  # default value for b is 98

    def test_non_numeric_a(self):
        with self.assertRaises(TypeError):
            add_integer('a', 2)

    def test_non_numeric_b(self):
        with self.assertRaises(TypeError):
            add_integer(1, 'b')

if __name__ == '__main__':
    unittest.main()