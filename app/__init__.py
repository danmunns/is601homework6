import pkgutil
import importlib
from calculator import Calculator
from app.commands import CommandHandler, Command

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        self.calculator = Calculator()
        self.load_plugins()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
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