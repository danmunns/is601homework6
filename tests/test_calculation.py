"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations(num_1, num_2, operation, expected):
    if isinstance(expected, str):  # Check if expected is an exception message
        try:
            calc = Calculation(num_1, num_2, operation)
            calc.perform()  # Perform the calculation to potentially raise the exception
        except (ValueError, ZeroDivisionError) as e:
            assert str(e) == expected, f"Exception message '{str(e)}' does not match expected '{expected}'"
    else:  # Normal case (no exception)
        calc = Calculation(num_1, num_2, operation)
        result = calc.perform()
        assert result == expected, f"Failed {operation.__name__} operation with {num_1} and {num_2}"

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    This test verifies that the __repr__ method of a Calculation instance 
    returns a string that accurately represents the state of the Calculation 
    object, including its operands and operation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The __repr__ method output does \
        not match the expected string."    


def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined 
    and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()  # Attempt to perform the calculation, which should trigger the ValueError.
