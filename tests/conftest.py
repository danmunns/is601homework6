# conftest.py

"""
This module generates random test data and passes it to certain tests.
"""
# pylint: disable=comparison-with-callable

from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide


fake = Faker()

def generate_test_data(num_records):
    """Generates random data for tests using Faker"""

    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_int(min=0, max=15))
        b = Decimal(fake.random_int(min=0, max=15)) if _ % 10 != 3 else \
            Decimal(fake.random_int(min=0, max=0))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        try:
            expected = operation_func(a, b)  # Calculate expected result first
        except (ZeroDivisionError, ValueError) as e:
            expected = str(e) # Store the exception message

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Enables user input to number of test records generated"""
    parser.addoption("--num_records", action="store", default=5, type=int, \
                     help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Pass Faker data to tests that use the appropriate variables"""
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"num_1", "num_2", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        
        # Adjust the parameterization to include both operation_name and operation for broad 
        # compatibility. Ensure 'operation_name' is used for identifying the operation in Calculator 
        # class tests'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames \
                                else op_func, expected) for a, b, op_name, op_func, expected \
                                    in parameters]
        metafunc.parametrize("num_1,num_2,operation,expected", modified_parameters)