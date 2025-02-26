from app.commands import CalculatorCommand

class MultiplyCommand(CalculatorCommand):
    def calculate(self, num_1, num_2):
        return self.calculator.multiply(num_1, num_2)