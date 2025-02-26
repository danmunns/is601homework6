from app.commands import Command

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