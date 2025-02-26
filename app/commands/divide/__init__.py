from app.commands import CalculatorCommand

class DivideCommand(CalculatorCommand):
    def calculate(self, num_1, num_2):
        return self.calculator.divide(num_1, num_2)