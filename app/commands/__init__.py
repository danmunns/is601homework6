from decimal import Decimal, InvalidOperation
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, num_1, num_2):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, num_1, num_2):
        try:
            self.commands[command_name].execute(num_1, num_2)
        except KeyError:
            print(f"No such command: {command_name}")

class CalculatorCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, num_1, num_2):
        try:
            num_1_decimal = Decimal(num_1)
            num_2_decimal = Decimal(num_2)
            result = self.calculate(num_1_decimal, num_2_decimal)
            print(f"The result is: {result}")
        except InvalidOperation:
            print(f"Invalid number input: {num_1} or {num_2} is not a valid number.")
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero")
        except Exception as e:
            print(f"An error occurred: {e}")