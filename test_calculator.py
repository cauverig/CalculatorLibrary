import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

"""Unit tests for calculator library"""

import calculator

class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2,2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4,2)

if __name__ == '__main__':
    unittest.main()
