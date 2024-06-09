import time

def login(username, password):
    # Validate username and password
    # Replace with actual validation logic
    if username == "admin" and password == "password":
        return True
    return False

def register(username, password):
    # Save to accounts.txt
    with open("accounts.txt", "a") as f:
        f.write(f"{username}:{password}\n")
    return True

def generate_password(length=10, character_types=["numbers", "symbols", "letters"]):
    # Generate password logic
    import random
    import string
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
                            password_length = int(input("Enter password length (default 10): "))
                            character_types = input("Choose character types (numbers, symbols, letters) - Optional: ")
                            password = generate_password(password_length, character_types.split(","))
                        register(register_username, password)
                        print("Registration successful!")
                    elif option == "3":
                        password_choice = input("Choose password option (1/2): ")
                        if password_choice == "1":
                            password = input("Enter password: ")
                        else:
                            password_length = int(input("Enter password length (default 10): "))
                            character_types = input("Choose character types (numbers, symbols, letters) - Optional: ")
                            password = generate_password(password_length, character_types.split(","))
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
                password_length = int(input("Enter password length (default 10): "))
                character_types = input("Choose character types (numbers, symbols, letters) - Optional: ")
                password = generate_password(password_length, character_types.split(","))
            register(register_username, password)
            print("Registration successful!")

if __name__ == "__main__":
    main()
