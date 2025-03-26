import unittest
import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from src.calculator import Calculator

# filepath: test/test_calculator_tests.py

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)
        self.assertEqual(Calculator.subtract(0, 1), -1)
        self.assertEqual(Calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertEqual(Calculator.multiply(-1, 1), -1)
        self.assertEqual(Calculator.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(Calculator.divide(6, 3), 2)
        self.assertEqual(Calculator.divide(-6, 3), -2)
        self.assertEqual(Calculator.divide(5, 2), 2.5)

        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(5, 0)

if __name__ == "__main__":
    unittest.main()