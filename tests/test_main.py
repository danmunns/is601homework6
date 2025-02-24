#test_main.py

"""
Tests for main.py 
"""

import unittest
from unittest.mock import patch
import subprocess  # For running main.py as a subprocess
import sys
from io import StringIO
import pytest
from main import main,calculate_and_print  # Ensure this import matches your project structure

print("sys.path:", sys.path)

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    """
    Tests for calculate and print function in main.py
    """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

class TestMain(unittest.TestCase):

    @patch('sys.argv', ['script_name', '5', '2', 'add'])  # Mock command-line arguments
    def test_main_add(self):
        # Redirect stdout to capture the output
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            main()
            self.assertEqual(stdout.getvalue().strip(), "The result of 5 add 2 is equal to 7")

    @patch('sys.argv', ['script_name', '10', '0', 'divide'])
    def test_main_divide_by_zero(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            main()
            self.assertEqual(stdout.getvalue().strip(), "An error occurred: Cannot divide by zero")

    @patch('sys.argv', ['script_name', 'a', '2', 'add'])
    def test_main_invalid_input(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            main()
            self.assertEqual(stdout.getvalue().strip(), "Invalid number input: a or 2 is not a valid number.")

    @patch('sys.argv', ['script_name', '5', '2', 'invalid_op'])
    def test_main_invalid_operation(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            main()
            self.assertEqual(stdout.getvalue().strip(), "Unknown operation: invalid_op")

    @patch('sys.argv', ['script_name', '5', '2'])  # Incorrect number of arguments
    def test_main_incorrect_arguments(self):
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            with self.assertRaises(SystemExit) as context: # Expect sys.exit(1)
                main()
            self.assertEqual(context.exception.code, 1) # Check the exit code
            self.assertIn("Usage: python main.py <number1> <number2> <operation>", stdout.getvalue().strip())

    def test_main_entry_point(self):  # Test the if __name__ == '__main__' block
        # Run main.py as a subprocess and capture its output
        process = subprocess.run([sys.executable, 'main.py', '5', '2', 'add'],  # Use sys.executable
                               capture_output=True, text=True, check=True) # check=True raises exception on non-zero exit code
        self.assertEqual(process.stdout.strip(), "The result of 5 add 2 is equal to 7")

    def test_main_entry_point_incorrect_args(self):
        process = subprocess.run([sys.executable, 'main.py', '5', '2'], capture_output=True, text=True, check=False)
        self.assertIn("Usage: python main.py <number1> <number2> <operation>", process.stdout)
        self.assertEqual(process.returncode, 1)

if __name__ == '__main__':
    unittest.main()