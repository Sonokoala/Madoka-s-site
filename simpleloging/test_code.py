# main.py

def main():
    print("Start")
    while True:
        choice = input("Login or Register? (1/2): ")
        if choice == "1":
            print("Login")
            # Login process
            username = input("Enter username: ")
            password = input("Enter password: ")
            # Here you would normally check the credentials
            print(f"Logged in as {username}")
            break
        elif choice == "2":
            print("Register")
            # Registration process
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            # Here you would normally save the credentials
            print(f"Registered new user {username}")
            break
        else:
            print("Invalid choice, please enter 1 or 2.")

# test_simple_login.py

import os
from io import StringIO
import sys
from main import main  # Adjust the import if your main script has a different name

# Mock input and output
class MockInputOutput:
    def __init__(self, inputs):
        self.inputs = inputs
        self.input_index = 0
        self.output = StringIO()

    def input(self, prompt=""):
        if self.input_index < len(self.inputs):
            response = self.inputs[self.input_index]
            self.input_index += 1
            return response
        return ""

    def print(self, *args, **kwargs):
        print(*args, **kwargs, file=self.output)

    def get_output(self):
        return self.output.getvalue()

# Replace built-in input and print functions
import builtins

def run_test(inputs):
    original_input = builtins.input
    original_print = builtins.print
    mock_io = MockInputOutput(inputs)
    builtins.input = mock_io.input
    builtins.print = mock_io.print

    try:
        main()
    finally:
        builtins.input = original_input
        builtins.print = original_print

    return mock_io.get_output()
# Test cases
def test_login_and_register():
    # Test registration
    inputs = [
        "2",  # Register
        "testuser",  # Username
        "testpassword",  # Password
        "1",  # Login
        "testuser",  # Username
        "testpassword",  # Password
    ]
    output = run_test(inputs)
    print("Test Registration and Login Output:")
    print(output)

    # Test login with invalid credentials
    inputs = [
        "1",  # Login
        "wronguser",  # Username
        "wrongpassword",  # Password
    ]
    output = run_test(inputs)
    print("Test Invalid Login Output:")
    print(output)

# Run tests
test_login_and_register()
