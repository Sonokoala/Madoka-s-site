import pandas as pd
import time
import random
import string
import sys
from io import StringIO

# Load the CSV file
csv_path = '/Users/madoka/Desktop/Tafe_Programming/test data_symplelogin.csv'

# Debugging: Print the contents of the CSV file
try:
    df = pd.read_csv(csv_path)
    print("CSV file loaded successfully.")
    print("DataFrame contents:")
    print(df.head())
    print("DataFrame columns:")
    print(df.columns)
    
    # Convert column names to lowercase
    df.columns = df.columns.str.lower()
    print("DataFrame columns after conversion to lowercase:")
    print(df.columns)
except Exception as e:
    print(f"Error loading CSV file: {e}")
    sys.exit(1)

# Convert CSV data to a dictionary for easy lookup
try:
    user_db = {row['username']: row['password'] for _, row in df.iterrows()}
except KeyError as e:
    print(f"KeyError: {e}. Please ensure the CSV file has 'username' and 'password' columns.")
    sys.exit(1)

def login(username, password):
    return user_db.get(username) == password

def register(username, password):
    user_db[username] = password
    with open("accounts.txt", "a") as f:
        f.write(f"{username}:{password}\n")
    return True

def generate_password(length=10, character_types=["numbers", "symbols", "letters"]):
    password = ""
    for _ in range(length):
        char_type = random.choice(character_types)
        if char_type == "numbers":
            password += random.choice(string.digits)
        elif char_type == "symbols":
            password += random.choice(string.punctuation)
        elif char_type == "letters":
            password += random.choice(string.ascii_letters)
    return password

def display_menu():
    print("Menu:")
    print("1. Login")
    print("2. Register")
    print("3. Passwords")
    print("4. View Accounts (Admin Only)")
    print("5. Save")
    print("6. Exit")

def main():
    while True:
        print("Start")
        choice = input("Login or Register? (1/2): ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                print("Successful Login!")
                display_menu()
                while True:
                    option = input("Choose an option: ")
                    if option == "1":
                        username = input("Enter username: ")
                        password = input("Enter password: ")
                        if login(username, password):
                            print("Successful Login!")
                        else:
                            print("Invalid Credentials - Retry?")
                    elif option == "2":
                        register_username = input("Enter username: ")
                        password_choice = input("Choose password option (1/2): ")
                        if password_choice == "1":
                            password = input("Enter password: ")
                        else:
                            try:
                                password_length = int(input("Enter password length (default 10): ") or 10)
                                character_types = input("Choose character types (numbers, symbols, letters) - Optional: ")
                                if character_types:
                                    character_types = character_types.split(",")
                                else:
                                    character_types = ["numbers", "symbols", "letters"]
                                password = generate_password(password_length, character_types)
                            except ValueError as e:
                                print(f"Invalid input: {e}")
                                continue
                        register(register_username, password)
                        print("Registration successful!")
                    elif option == "3":
                        password_choice = input("Choose password option (1/2): ")
                        if password_choice == "1":
                            password = input("Enter password: ")
                        else:
                            try:
                                password_length = int(input("Enter password length (default 10): ") or 10)
                                character_types = input("Choose character types (numbers, symbols, letters) - Optional: ")
                                if character_types:
                                    character_types = character_types.split(",")
                                else:
                                    character_types = ["numbers", "symbols", "letters"]
                                password = generate_password(password_length, character_types)
                            except ValueError as e:
                                print(f"Invalid input: {e}")
                                continue
                        print("Password options")
                    elif option == "4" and username == "admin":
                        with open("accounts.txt", "r") as f:
                            print(f.read())
                    elif option == "5":
                        register_username = input("Enter username: ")
                        password = input("Enter password: ")
                        register(register_username, password)
                        print("Save successful!")
                    elif option == "6":
                        time.sleep(2)
                        print("Exiting...")
                        break
                    else:
                        print("Invalid option")
            else:
                print("Invalid Credentials - Retry?")
        elif choice == "2":
            register_username = input("Enter username: ")
            password_choice = input("Choose password option (1/2): ")
            if password_choice == "1":
                password = input("Enter password: ")
            else:
                try:
                    password_length = int(input("Enter password length (default 10): ") or 10)
                    character_types = input("Choose character types (numbers, symbols, letters) - Optional: ")
                    if character_types:
                        character_types = character_types.split(",")
                    else:
                        character_types = ["numbers", "symbols", "letters"]
                    password = generate_password(password_length, character_types)
                except ValueError as e:
                    print(f"Invalid input: {e}")
                    continue
            register(register_username, password)
            print("Registration successful!")

# Mock input and output
import builtins

class MockInputOutput:
    def __init__(self, inputs):
        self.inputs = inputs
        self.input_index = 0
        self.output = StringIO()

    def input(self, prompt=""):
        if self.input_index < len(self.inputs):
            response = self.inputs[self.input_index]
            self.input_index += 1
            print(f"Input: {response}")  # Debugging statement
            return response
        return ""

    def print(self, *args, **kwargs):
        if 'file' in kwargs:
            self.output.write(' '.join(map(str, args)) + '\n')
        else:
            print(*args)  # Call the original print function directly

    def get_output(self):
        return self.output.getvalue()
# Replace built-in input and print functions
from builtins import input, print
def run_test(inputs):
    original_input = input
    original_print = print
    mock_io = MockInputOutput(inputs)
    builtins.input = mock_io.input
    builtins.print = mock_io.print

    try:
        main()
    finally:
        builtins.input = original_input
        builtins.print = original_print

    return mock_io.get_output()
def new_func():
    original_input = __builtins__.input
    return original_input

# Test cases
def test_login_and_register():
    global user_db
    user_db.clear()  # テストの前にデータベースをリセット

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
    user_db.clear()  # テストの前にデータベースをリセット
    user_db["testuser"] = "testpassword"  # 正しいユーザー情報を設定
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