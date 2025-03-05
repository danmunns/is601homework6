"""
Tests for app module
"""

import unittest
from unittest.mock import patch
import logging
from app import App

class TestApp(unittest.TestCase):
    """
    Tests for App class
    """
    def setUp(self):
        self.app = App()

    def test_register_commands(self):
        """
        Test that commands are registered correctly
        """
        self.assertIn("add", self.app.command_handler.commands)
        self.assertIn("subtract", self.app.command_handler.commands)
        self.assertIn("multiply", self.app.command_handler.commands)
        self.assertIn("divide", self.app.command_handler.commands)

    @patch('builtins.input', side_effect=['add', '5', '3', 'exit'])
    @patch('builtins.print')
    def test_start_add_command(self, mock_print, mock_input):
        """
        Test the REPL loop for add command
        """
        self.app.start()
        mock_print.assert_any_call("The result is: 8")

    @patch('builtins.input', side_effect=['subtract', '10', '4', 'exit'])
    @patch('builtins.print')
    def test_start_subtract_command(self, mock_print, mock_input):
        """
        Test the REPL loop for subtract command
        """
        self.app.start()
        mock_print.assert_any_call("The result is: 6")

    @patch('builtins.input', side_effect=['multiply', '2', '3', 'exit'])
    @patch('builtins.print')
    def test_start_multiply_command(self, mock_print, mock_input):
        """
        Test the REPL loop for multiply command
        """
        self.app.start()
        mock_print.assert_any_call("The result is: 6")

    @patch('builtins.input', side_effect=['divide', '10', '2', 'exit'])
    @patch('builtins.print')
    def test_start_divide_command(self, mock_print, mock_input):
        """
        Test the REPL loop for divide command
        """
        self.app.start()
        mock_print.assert_any_call("The result is: 5")

if __name__ == '__main__':
    unittest.main()