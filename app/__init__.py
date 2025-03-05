import os
import pkgutil
import importlib
import sys
from dotenv import load_dotenv
import logging
import logging.config
from calculator import Calculator
from app.commands import CommandHandler, CalculatorCommand

class App:
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        self.command_handler = CommandHandler()
        self.calculator = Calculator()
        self.load_plugins()
    
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

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
        while True:  # REPL Read, Evaluate, Print, Loop
            command = input("Enter calculation type (add, subtract, multiply, divide) or 'exit' to exit: ").strip()
            if command == "exit":
                break
            num_1 = input("Enter first number: ").strip()
            num_2 = input("Enter second number: ").strip()
            self.command_handler.execute_command(command, num_1, num_2)