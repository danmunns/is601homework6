"""
Tests for command classes
"""

import unittest
from unittest.mock import patch
from io import StringIO
from app.commands import CommandHandler
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
        self.command_handler = CommandHandler()

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_command(self, mock_stdout):
        """
        Test AddCommand
        """
        self.command_handler.register_command("add", AddCommand(self.calculator))
        self.command_handler.execute_command('add', '5', '3')
        self.assertIn("The result is: 8", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_subtract_command(self, mock_stdout):
        """
        Test SubtractCommand
        """
        self.command_handler.register_command("subtract", SubtractCommand(self.calculator))
        self.command_handler.execute_command('subtract', '10', '4')
        self.assertIn("The result is: 6", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_multiply_command(self, mock_stdout):
        """
        Test MultiplyCommand
        """
        self.command_handler.register_command("multiply", MultiplyCommand(self.calculator))
        self.command_handler.execute_command('multiply', '2', '3')
        self.assertIn("The result is: 6", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_divide_command(self, mock_stdout):
        """
        Test DivideCommand
        """
        self.command_handler.register_command("divide", DivideCommand(self.calculator))
        self.command_handler.execute_command('divide', '10', '2')
        self.assertIn("The result is: 5", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_divide_by_zero(self, mock_stdout):
        """
        Test DivideCommand with division by zero
        """
        self.command_handler.register_command("divide", DivideCommand(self.calculator))
        self.command_handler.execute_command('divide', '10', '0')
        self.assertIn("An error occurred: Cannot divide by zero", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_unknown_command(self, mock_stdout):
        """
        Test unknown command
        """
        self.command_handler.execute_command('unknown', '5', '3')
        self.assertIn("No such command: unknown", mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()