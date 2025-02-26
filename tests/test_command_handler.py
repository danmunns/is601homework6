"""
Tests for CommandHandler class
"""

import unittest
from unittest.mock import patch
from io import StringIO
from app.commands import CommandHandler, Command

class TestCommandHandler(unittest.TestCase):
    """
    Tests for CommandHandler class
    """
    def setUp(self):
        self.command_handler = CommandHandler()

    @patch('sys.stdout', new_callable=StringIO)
    def test_execute_command_keyerror(self, mock_stdout):
        """
        Test execute_command with an unknown command to cover KeyError
        """
        self.command_handler.execute_command('unknown', '5', '3')
        self.assertIn("No such command: unknown", mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()