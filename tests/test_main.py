#test_main.py

"""
Tests for main.py 
"""

import unittest
from unittest.mock import patch
from io import StringIO
from main import App

class TestMain(unittest.TestCase):
    """
    Tests for main.py
    """
    def setUp(self):
        self.app = App()

    @patch('builtins.input', side_effect=['add', '5', '3', 'exit'])
    @patch('builtins.print')
    def test_main_add(self, mock_print, mock_input):
        """
        Test add operation via REPL loop
        """
        self.app.start()
        mock_print.assert_any_call("The result is: 8")

    @patch('builtins.input', side_effect=['subtract', '10', '4', 'exit'])
    @patch('builtins.print')
    def test_main_subtract(self, mock_print, mock_input):
        """
        Test subtract operation via REPL loop
        """
        self.app.start()
        mock_print.assert_any_call("The result is: 6")

    @patch('builtins.input', side_effect=['multiply', '2', '3', 'exit'])
    @patch('builtins.print')
    def test_main_multiply(self, mock_print, mock_input):
        """
        Test multiply operation via REPL loop
        """
        self.app.start()
        mock_print.assert_any_call("The result is: 6")

    @patch('builtins.input', side_effect=['divide', '10', '2', 'exit'])
    @patch('builtins.print')
    def test_main_divide(self, mock_print, mock_input):
        """
        Test divide operation via REPL loop
        """
        self.app.start()
        mock_print.assert_any_call("The result is: 5")

    @patch('builtins.input', side_effect=['divide', '10', '0', 'exit'])
    @patch('builtins.print')
    def test_main_divide_by_zero(self, mock_print, mock_input):
        """
        Test divide by zero operation via REPL loop
        """
        self.app.start()
        mock_print.assert_any_call("An error occurred: Cannot divide by zero")

    @patch('builtins.input', side_effect=['unknown', '5', '3', 'exit'])
    @patch('builtins.print')
    def test_main_unknown_command(self, mock_print, mock_input):
        """
        Test unknown command via REPL loop
        """
        self.app.start()
        mock_print.assert_any_call("No such command: unknown")

if __name__ == '__main__':
    unittest.main()