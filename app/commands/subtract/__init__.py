from app.commands import CalculatorCommand

class SubtractCommand(CalculatorCommand):
    def calculate(self, num_1, num_2):
        return self.calculator.subtract(num_1, num_2)