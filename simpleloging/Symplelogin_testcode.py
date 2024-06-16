Python 3.13.0a6 (v3.13.0a6:57aee2a02c, Apr  9 2024, 09:56:43) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... import string
... 
... class UserManager:
...     def __init__(self):
...         self.users = {}
... 
...     def register(self, username, password):
...         if username in self.users:
...             return "Username already exists"
...         if len(password) < 6:
...             return "Password too short"
...         self.users[username] = password
...         return "Registration successful"
... 
...     def login(self, username, password):
...         if username in self.users and self.users[username] == password:
...             return "Login successful"
...         return "Invalid username or password"
... 
...     def generate_password(self, length=8, use_special_chars=True):
...         if length < 6:
...             return "Password length too short"
...         chars = string.ascii_letters + string.digits
...         if use_special_chars:
...             chars += string.punctuation
...         return ''.join(random.choice(chars) for _ in range(length))
... 
... # インスタンスを作成
