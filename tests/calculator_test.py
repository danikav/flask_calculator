import unittest
from modules.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(15, self.calculator.add(10, 5))


    def test_subtract(self):
        self.assertEqual(5, self.calculator.subtract(10, 5))

    def test_multiply(self):
        self.assertEqual(50, self.calculator.multiply(10, 5))

    def test_divide(self):
        self.assertEqual(2, self.calculator.divide(10, 5))