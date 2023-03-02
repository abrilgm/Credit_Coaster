#import unittest
from datetime import date
from user_controller.schemes.user import User
from user_controller.schemes.Account import Account
from user_controller.controllers.user_controller import UserController

class TestUserController():
    def setUp(self):
        self.user = User(name="John Doe", birthdate=date(1990, 1, 1), phone="555-1234", age=31)
        self.account = Account(user=self.user)
        self.user.account = self.account
        self.users = [self.user]

    def test_create_user(self):
        name = "Jane Smith"
        birthdate = date(1995, 5, 5)
        phone = "555-4321"
        age = 26
        new_user = UserController.create_user(name, birthdate, phone, age)
        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.name, name)
        self.assertEqual(new_user.birthdate, birthdate)
        self.assertEqual(new_user.phone, phone)
        self.assertEqual(new_user.age, age)

    def test_create_user_with_account(self):
        name = "Jane Smith"
        birthdate = date(1995, 5, 5)
        phone = "555-4321"
        age = 26
        new_user = UserController.create_user_with_account(name, birthdate, phone, age)
        self.assertIsInstance(new_user, User)
        self.assertIsInstance(new_user.account, Account)
        self.assertEqual(new_user.name, name)
        self.assertEqual(new_user.birthdate, birthdate)
        self.assertEqual(new_user.phone, phone)
        self.assertEqual(new_user.age, age)

    def test_get_user_by_phone(self):
        phone = "555-1234"
        user = UserController.get_user_by_phone(self.users, phone)
        self.assertEqual(user, self.user)

    def test_update_user_phone(self):
        new_phone = "555-5678"
        result = UserController.update_user_phone(self.user, new_phone)
        self.assertTrue(result)
        self.assertEqual(self.user.phone, new_phone)

    def test_update_user_phone_invalid_user(self):
        new_phone = "555-5678"
        result = UserController.update_user_phone(None, new_phone)
        self.assertFalse(result)

#if __name__ == '__main__':
 #   unittest.main()
