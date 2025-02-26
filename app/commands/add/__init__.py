from app.commands import CalculatorCommand

class AddCommand(CalculatorCommand):
    def calculate(self, num_1, num_2):
        return self.calculator.add(num_1, num_2)