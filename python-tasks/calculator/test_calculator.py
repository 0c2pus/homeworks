import unittest
from calculator import add_numbers, subtract_numbers, multiply_numbers, divide_numbers


class TestAddNumbers(unittest.TestCase):
    """Test cases for add_numbers function."""
    
    def test_addition(self):
        """Test addition of positive numbers."""
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
    
    
    def test_addition_float(self):
        """Test addition of float numbers."""
        result = add_numbers(2.5, 3.5)
        self.assertEqual(result, 6)
    
    
    def test_addition_negative(self):
        """Test addition of negative numbers."""
        result = add_numbers(-5, 2)
        self.assertEqual(result, -3)
    
    
    def test_addition_zero(self):
        """Test addition of zero."""
        result = add_numbers(2, 0)
        self.assertEqual(result, 2)


class TestSubtractNumbers(unittest.TestCase):
    """Test cases for subtract_numbers function."""
    
    def test_subtraction(self):
        """Test subtraction of positive numbers."""
        result = subtract_numbers(10, 5)
        self.assertEqual(result, 5)
    
    
    def test_subtraction_float(self):
        """Test subtraction of float numbers."""
        result = subtract_numbers(5.5, 2.5)
        self.assertEqual(result, 3)
    
    
    def test_subtraction_negative(self):
        """Test subtraction of negative numbers."""
        result = subtract_numbers(-5, 2)
        self.assertEqual(result, -7)
    
    
    def test_subtraction_zero(self):
        """Test subtraction of zero."""
        result = subtract_numbers(0, 2)
        self.assertEqual(result, -2)


class TestMultiplyNumbers(unittest.TestCase):
    """Test cases for test_multiply function."""
    
    def test_multiply(self):
        """Test multiply of positive numbers."""
        result = multiply_numbers(3, 3)
        self.assertEqual(result, 9)
    
    
    def test_multiply_float(self):
        """Test subtraction of float numbers."""
        result = multiply_numbers(5.5, 2.5)
        self.assertEqual(result, 13.75)
    
    
    def test_multiply_negative(self):
        """Test subtraction of negative numbers."""
        result = multiply_numbers(-2, 2)
        self.assertEqual(result, -4)
    
    
    def test_multiply_zero(self):
        """Test multiply of zero."""
        result = multiply_numbers(0, 2)
        self.assertEqual(result, 0)
    
class TestDivisionNumbers(unittest.TestCase):
    """Test cases for test_division function."""
    
    def test_division(self):
        """Test _division of positive numbers."""
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)
    
    
    def test_division_float(self):
        """Test subtraction of float numbers."""
        result = divide_numbers(5.5, 2.5)
        self.assertEqual(result, 2.2)
    
    
    def test_division_negative(self):
        """Test subtraction of negative numbers."""
        result = divide_numbers(-10, 2)
        self.assertEqual(result, -5)

    
    def test_division_by_error(self):
        """Test _division of zero."""
        result = divide_numbers(5, 0)
        self.assertEqual(result, "Error")
