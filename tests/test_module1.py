import unittest
from numersis.module1 import function1

class TestFunction1(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(function1(2, 3), 5)

if __name__ == "__main__":
    unittest.main()