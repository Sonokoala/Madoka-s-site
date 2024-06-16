# test_user_manager.py

import unittest
from user_manager import UserManager
import string

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()

    def test_register_new_user(self):
        result = self.user_manager.register("newuser", "newpassword123")
        self.assertEqual(result, "Registration successful")

    def test_register_existing_user(self):
        self.user_manager.register("user1", "password123")
        result = self.user_manager.register("user1", "newpassword123")
        self.assertEqual(result, "Username already exists")

    def test_register_short_password(self):
        result = self.user_manager.register("newuser", "short")
        self.assertEqual(result, "Password too short")

    def test_login_success(self):
        self.user_manager.register("user1", "password123")
        result = self.user_manager.login("user1", "password123")
        self.assertEqual(result, "Login successful")

    def test_login_invalid_username(self):
        result = self.user_manager.login("invaliduser", "password123")
        self.assertEqual(result, "Invalid username or password")

    def test_login_invalid_password(self):
        self.user_manager.register("user1", "password123")
        result = self.user_manager.login("user1", "wrongpassword")
        self.assertEqual(result, "Invalid username or password")

    def test_generate_password_default(self):
        password = self.user_manager.generate_password()
        self.assertTrue(len(password) >= 8)

    def test_generate_password_custom_length(self):
        password = self.user_manager.generate_password(length=12)
        self.assertTrue(len(password) == 12)

    def test_generate_password_no_special_chars(self):
        password = self.user_manager.generate_password(use_special_chars=False)
        self.assertTrue(all(c in string.ascii_letters + string.digits for c in password))

    def test_generate_password_short_length(self):
        result = self.user_manager.generate_password(length=5)
        self.assertEqual(result, "Password length too short")

if __name__ == '__main__':
    unittest.main()
