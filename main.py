#main.py

from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation
from calculator import Calculator

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Commands
class AddCommand(Command):
    def __init__(self, calculator, num_1, num_2):
        self.calculator = calculator
        self.num_1 = num_1
        self.num_2 = num_2

    def execute(self):
        result = self.calculator.add(self.num_1, self.num_2)
        print(f"Result: {result}")

class SubtractCommand(Command):
    def __init__(self, calculator, num_1, num_2):
        self.calculator = calculator
        self.num_1 = num_1
        self.num_2 = num_2

    def execute(self):
        result = self.calculator.subtract(self.num_1, self.num_2)
        print(f"Result: {result}")

class MultiplyCommand(Command):
    def __init__(self, calculator, num_1, num_2):
        self.calculator = calculator
        self.num_1 = num_1
        self.num_2 = num_2

    def execute(self):
        result = self.calculator.multiply(self.num_1, self.num_2)
        print(f"Result: {result}")

class DivideCommand(Command):
    def __init__(self, calculator, num_1, num_2):
        self.calculator = calculator
        self.num_1 = num_1
        self.num_2 = num_2

    def execute(self):
        try:
            result = self.calculator.divide(self.num_1, self.num_2)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

# Invoker
class CalculatorInvoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        self.history.append(command)
        command.execute()

# REPL
def repl(calculator):
    invoker = CalculatorInvoker()

    while True:
        command_input = input("Enter command (add, subtract, multiply, divide) and two values, or 'exit' to quit: ").split()
        if not command_input:
            continue
        if command_input[0] == 'exit':
            break
        if len(command_input) > 3:
            print("Error: Too many arguments. Please enter a command followed by two numeric values.")
            continue
        
        try:
            command, num_1, num_2 = command_input[0], Decimal(command_input[1]), Decimal(command_input[2])
        except (IndexError, InvalidOperation):
            print("Invalid input. Please enter a command followed by two numeric values.")
            continue

        try:
            if command == 'add':
                invoker.execute_command(AddCommand(calculator, num_1, num_2))
            elif command == 'subtract':
                invoker.execute_command(SubtractCommand(calculator, num_1, num_2))
            elif command == 'multiply':
                invoker.execute_command(MultiplyCommand(calculator, num_1, num_2))
            elif command == 'divide':
                invoker.execute_command(DivideCommand(calculator, num_1, num_2))
            else:
                print("Unknown command")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator = Calculator()
    repl(calculator)