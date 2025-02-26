from app.commands import CommandHandler
from app.commands.add import AddCommand 
from app.commands.subtract import SubtractCommand 
from app.commands.multiply import MultiplyCommand 
from app.commands.divide import DivideCommand
from calculator import Calculator

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        self.calculator = Calculator()
        self.register_commands()

    def register_commands(self):
        # Register commands here
        self.command_handler.register_command("add", AddCommand(self.calculator))
        self.command_handler.register_command("subtract", SubtractCommand(self.calculator))
        self.command_handler.register_command("multiply", MultiplyCommand(self.calculator))
        self.command_handler.register_command("divide", DivideCommand(self.calculator))

    def start(self):
        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            command = input("Enter command (add, subtract, multiply, divide): ").strip()
            if command == "exit":
                break
            num_1 = input("Enter first number: ").strip()
            num_2 = input("Enter second number: ").strip()
            self.command_handler.execute_command(command, num_1, num_2)