"""
This module contains mathematical operations for the calculator.
"""

from decimal import Decimal

def add(num_1: Decimal, num_2: Decimal) -> Decimal:
    """
    Addition function
    """
    return num_1 + num_2

def subtract(num_1: Decimal, num_2: Decimal) -> Decimal:
    """
    Subtraction function
    """
    return num_1 - num_2

def multiply(num_1: Decimal, num_2: Decimal) -> Decimal:
    """
    Multiplication function
    """
    return num_1 * num_2

def divide(num_1: Decimal, num_2: Decimal) -> Decimal:
    """
    Division function
    """
    if num_2 == 0:
        raise ValueError("Cannot divide by zero")
    return num_1 / num_2
