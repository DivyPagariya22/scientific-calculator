import unittest
import math
from calculator import square_root, factorial, natural_log, power

# Functions to be tested
def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if not isinstance(x, int):
        raise ValueError("Factorial is only defined for integers.")
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

# Unit Test Class
class TestScientificCalculator(unittest.TestCase):
    
    # Square Root Tests
    def test_square_root_positive(self):
        self.assertEqual(square_root(16), 4)
        
    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0)
        
    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-9)
    
    # Factorial Tests
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-3)
    
    def test_factorial_non_integer(self):
        with self.assertRaises(ValueError):
            factorial(5.5)
    
    # Natural Log Tests
    def test_natural_log_positive(self):
        self.assertAlmostEqual(natural_log(math.e), 1)
    
    def test_natural_log_one(self):
        self.assertEqual(natural_log(1), 0)
    
    def test_natural_log_zero(self):
        with self.assertRaises(ValueError):
            natural_log(0)
    
    def test_natural_log_negative(self):
        with self.assertRaises(ValueError):
            natural_log(-5)
    
    # Power Function Tests
    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)
    
    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -2), 0.25)
    
    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)
    
    def test_power_zero_base(self):
        self.assertEqual(power(0, 5), 0)

if __name__ == "__main__":
    unittest.main()

# python -m unittest test_calculator.py
