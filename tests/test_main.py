#test_main.py

"""
Tests for main.py 
"""

import pytest
import sys
from io import StringIO
from main import main,calculate_and_print  # Ensure this import matches your project structure

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

def test_main_correct_usage(monkeypatch, capsys):
    # Simulate command-line arguments
    monkeypatch.setattr(sys, 'argv', ['main.py', '10', '5', 'add'])
    main()
    captured = capsys.readouterr()
    assert "The result of 10 add 5 is equal to 15" in captured.out

def test_main_incorrect_number_of_arguments(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['main.py', '10', '5'])  # Missing argument
    with pytest.raises(SystemExit) as e:  # Expect sys.exit()
        main()
    assert e.value.code == 1  # Check exit code
    captured = capsys.readouterr()
    assert "Usage: python main.py <number1> <number2> <operation>" in captured.out