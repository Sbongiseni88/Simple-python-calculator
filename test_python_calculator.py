import unittest
from unittest.mock import patch
from python_calculator import calculate



class TestCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=['+', '5', '3'])
    def test_addition(self, mock_input):
        result = calculate('+', 5, 3)
        self.assertEqual(result, 8)

    @patch('builtins.input', side_effect=['-', '5', '3'])
    def test_subtraction(self, mock_input):
        result = calculate('-', 5, 3)
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['*', '5', '3'])
    def test_multiplication(self, mock_input):
        result = calculate('*', 5, 3)
        self.assertEqual(result, 15)

    @patch('builtins.input', side_effect=['/', '5', '3'])
    def test_division(self, mock_input):
        result = calculate('/', 5, 3)
        self.assertEqual(result, 1.667)

    @patch('builtins.input', side_effect=['/', '5', '0'])
    def test_divide_by_zero(self, mock_input):
        with self.assertRaises(ZeroDivisionError):
            calculate('/', 5, 0)

    @patch('builtins.input', side_effect=['#', '5', '3'])
    def test_invalid_operator(self, mock_input):
        with self.assertRaises(ValueError):
            calculate('#', 5, 3)

if __name__ == '__main__':
    unittest.main()
