"""
This module contains tests for the Calculator class.
"""
from decimal import Decimal
from calculator import Calculator
from test_calculations import setup_calculations

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(2,2) == 0

def test_divide():
    '''Test that division function works '''    
    assert Calculator.divide(2,2) == 1

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculator.multiply(2,2) == 4

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    assert len(Calculator.get_history()) == 2

