# user_manager.py

import random
import string

class UserManager:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            return "Username already exists"
        if len(password) < 6:
            return "Password too short"
        self.users[username] = password
        return "Registration successful"

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return "Login successful"
        return "Invalid username or password"

    def generate_password(self, length=8, use_special_chars=True):
        if length < 6:
            return "Password length too short"
        chars = string.ascii_letters + string.digits
        if use_special_chars:
            chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))