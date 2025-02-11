"""
This module contains the Calculator class which creates a 
Calculator instance and provides access to underlying operations
and functions.
"""

from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation

# Definition of the Calculator class
class Calculator:
    """
    Creates Calculator class which allows you to perform basic mathematical
    operations on 2 numbers and retrieve history of calculations that have
    been performed.
    """
    # Operation Methods

    @staticmethod
    def _perform_operation(num_1: Decimal, num_2: Decimal, operation: \
                           Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation.create(num_1, num_2, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(num_1: Decimal, num_2: Decimal) -> Decimal:
        """Perform add operation, then return the result."""
        return Calculator._perform_operation(num_1, num_2, add)

    @staticmethod
    def subtract(num_1: Decimal, num_2: Decimal) -> Decimal:
        """Perform subtract operation, then return the result."""
        return Calculator._perform_operation(num_1, num_2, subtract)

    @staticmethod
    def multiply(num_1: Decimal, num_2: Decimal) -> Decimal:
        """Perform multiply operation, then return the result."""
        return Calculator._perform_operation(num_1, num_2, multiply)

    @staticmethod
    def divide(num_1: Decimal, num_2: Decimal) -> Decimal:
        """Perform divide operation, then return the result."""
        return Calculator._perform_operation(num_1, num_2, divide)

    # History Methods

    @staticmethod
    def get_history() -> list[Calculations]:
        """Get history of calculations, then return the result."""
        return Calculations.get_history()
    
    @staticmethod
    def clear_history() -> None:
        """Clear history of calculations, then return the result."""
        return Calculations.clear_history()

    @staticmethod
    def get_latest() -> Calculation:
        """Get latest calculation, then return the result."""
        return Calculations.get_latest()

    @staticmethod
    def find_by_operation(operation_name: str) -> list[Calculation]:
        """Get latest calculation by operation type, then return the result."""
        return Calculations.find_by_operation(operation_name)
