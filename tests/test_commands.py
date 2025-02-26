"""
Tests for command classes
"""

import unittest
from unittest.mock import patch
from io import StringIO
from app.commands.add import AddCommand 
from app.commands.subtract import SubtractCommand 
from app.commands.multiply import MultiplyCommand 
from app.commands.divide import DivideCommand
from calculator import Calculator

class TestCalculatorCommands(unittest.TestCase):
    """
    Tests for calculator command classes
    """
    def setUp(self):
        self.calculator = Calculator()

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_command(self, mock_stdout):
        """
        Test AddCommand
        """
        command = AddCommand(self.calculator)
        command.execute('5', '3')
        self.assertIn("The result is: 8", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_subtract_command(self, mock_stdout):
        """
        Test SubtractCommand
        """
        command = SubtractCommand(self.calculator)
        command.execute('10', '4')
        self.assertIn("The result is: 6", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_multiply_command(self, mock_stdout):
        """
        Test MultiplyCommand
        """
        command = MultiplyCommand(self.calculator)
        command.execute('2', '3')
        self.assertIn("The result is: 6", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_divide_command(self, mock_stdout):
        """
        Test DivideCommand
        """
        command = DivideCommand(self.calculator)
        command.execute('10', '2')
        self.assertIn("The result is: 5", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_divide_by_zero(self, mock_stdout):
        """
        Test DivideCommand with division by zero
        """
        command = DivideCommand(self.calculator)
        command.execute('10', '0')
        self.assertIn("An error occurred: Cannot divide by zero", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_number_input_add(self, mock_stdout):
        """
        Test invalid number input for add command
        """
        command = AddCommand(self.calculator)
        command.execute('a', '3')
        self.assertIn("Invalid number input: a or 3 is not a valid number.", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_number_input_subtract(self, mock_stdout):
        """
        Test invalid number input for subtract command
        """
        command = SubtractCommand(self.calculator)
        command.execute('a', '3')
        self.assertIn("Invalid number input: a or 3 is not a valid number.", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_number_input_multiply(self, mock_stdout):
        """
        Test invalid number input for multiply command
        """
        command = MultiplyCommand(self.calculator)
        command.execute('a', '3')
        self.assertIn("Invalid number input: a or 3 is not a valid number.", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_number_input_divide(self, mock_stdout):
        """
        Test invalid number input for divide command
        """
        command = DivideCommand(self.calculator)
        command.execute('a', '3')
        self.assertIn("Invalid number input: a or 3 is not a valid number.", mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()