import unittest

from simplecalss import add

class simplecalssTest(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(add(1,1), 2)


if __name__ == '__main__':
    unittest.main()