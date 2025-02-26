from app.commands import Command

class SubtractCommand(Command):
    def __init__(self, calculator, num_1, num_2):
        self.calculator = calculator
        self.num_1 = num_1
        self.num_2 = num_2

    def execute(self):
        result = self.calculator.subtract(self.num_1, self.num_2)
        print(f"Result: {result}")