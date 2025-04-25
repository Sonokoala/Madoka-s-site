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

import os
from io import StringIO
import sys
from main import main  # main.pyのmain関数をインポート

# Mock input and output
class MockInputOutput:
    def __init__(self, inputs, original_print):
        self.inputs = inputs
        self.input_index = 0
        self.output = StringIO()
        self.original_print = original_print

    def input(self, prompt=""):
        if self.input_index < len(self.inputs):
            response = self.inputs[self.input_index]
            self.input_index += 1
            return response
        return ""

    def print(self, *args, **kwargs):
        if 'file' in kwargs:
            kwargs['file'] = self.output
        else:
            kwargs['file'] = self.output
        self.original_print(*args, **kwargs)

    def get_output(self):
        return self.output.getvalue()

# Replace built-in input and print functions
def run_test(inputs):
    # Check if __builtins__ is a dict or a module
    if isinstance(__builtins__, dict):
        original_input = __builtins__['input']
        original_print = __builtins__['print']
        mock_io = MockInputOutput(inputs, original_print)
        __builtins__['input'] = mock_io.input
        __builtins__['print'] = mock_io.print
    else:
        original_input = __builtins__.input
        original_print = __builtins__.print
        mock_io = MockInputOutput(inputs, original_print)
        __builtins__.input = mock_io.input
        __builtins__.print = mock_io.print

    try:
        main()
    finally:
        if isinstance(__builtins__, dict):
            __builtins__['input'] = original_input
            __builtins__['print'] = original_print
        else:
            __builtins__.input = original_input
            __builtins__.print = original_print

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
if __name__ == "__main__":
    test_login_and_register()