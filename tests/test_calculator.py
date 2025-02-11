"""
This module contains tests for the Calculator class.
"""
# pylint: disable=unused-import
from decimal import Decimal
from calculator import Calculator
from tests.test_calculations import setup_calculations

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4, "Add operation failed"

def test_subtraction():
    '''Test that subtraction function works '''    
    assert Calculator.subtract(2,2) == 0, "Subtract operation failed"

def test_divide():
    '''Test that division function works '''    
    assert Calculator.divide(2,2) == 1, "Divide operation failed"

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculator.multiply(2,2) == 4, "Multiply operation failed"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    assert len(Calculator.get_history()) == 2, "History does not contain \
        the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """Test retrieving the last calculation."""
    latest = Calculator.get_latest()
    assert latest.num_1 == Decimal('20') and latest.num_2 == Decimal('3'), "Did not \
        get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    """Test retrieving the last calculation by operation type."""
    add_operations = Calculator.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations \
        with add operation"
    subtract_operations = Calculator.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of \
        calculations with subtract operation"
