import os
import pkgutil
import importlib
from calculator import Calculator
from app.commands import CommandHandler, CalculatorCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        self.calculator = Calculator()
        self.load_plugins()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        package_dir = os.path.dirname(importlib.import_module(plugins_package).__file__)
        for _, plugin_name, _ in pkgutil.iter_modules([package_dir]):
            plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
            for item_name in dir(plugin_module):
                item = getattr(plugin_module, item_name)
                try:
                    if issubclass(item, CalculatorCommand) and item is not CalculatorCommand:
                        self.command_handler.register_command(plugin_name, item(self.calculator))
                except TypeError:
                    continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            command = input("Enter command (add, subtract, multiply, divide): ").strip()
            if command == "exit":
                break
            num_1 = input("Enter first number: ").strip()
            num_2 = input("Enter second number: ").strip()
            self.command_handler.execute_command(command, num_1, num_2)