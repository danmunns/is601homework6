"""
This module contains the calculation class which creates
a calculation instance that can be passed along to the requested operation
and saved in the calculations history.
"""

# pylint: disable=unused-import
from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

# Definition of the Calculation class with type annotations for improved readability and safety
class Calculation:
    """
    Creates a calculation object which can be passed to the appropriate 
    mathematical operation and added to calculations history.
    """
    def __init__(self, num_1: Decimal, num_2: Decimal, operation: \
                 Callable[[Decimal, Decimal], Decimal]):
        self.num_1 = num_1
        self.num_2 = num_2
        self.operation = operation

    # Static method to create a new instance of Calculation
    @staticmethod    
    def create(num_1: Decimal, num_2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Create calculation instance and return object."""
        return Calculation(num_1, num_2, operation)

    # Method to perform the calculation stored in this object
    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        return self.operation(self.num_1, self.num_2)

    # Special method to provide a string representation of the Calculation instance
    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.num_1}, {self.num_2}, {self.operation.__name__})"
