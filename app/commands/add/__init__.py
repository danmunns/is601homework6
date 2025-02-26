from app.commands import Command

class AddCommand(Command):
    def __init__(self, calculator, num_1, num_2):
        self.calculator = calculator
        self.num_1 = num_1
        self.num_2 = num_2

    def execute(self):
        result = self.calculator.add(self.num_1, self.num_2)
        print(f"Result: {result}")