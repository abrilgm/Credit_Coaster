#import unittest
from controllers.account_controller import AccountController
from schemes.user import User
from schemes.card import Card
from schemes.Account import Account

class AccountControllerTest():
    def setUp(self):
        self.user = User("John Doe", "01-01-1990", "555-5555", "31")
        self.card = Card("1234 5678 9012 3456", "01/23", "123", "0000")
        self.account = Account(self.user, self.card, 1000, 15, "Visa")
        self.controller = AccountController()

    def test_create_account(self):
        self.assertIsNone(self.user.account)
        self.controller.create_account(self.user)
        self.assertIsNotNone(self.user.account)

    def test_get_user_info(self):
        self.assertEqual(self.controller.get_user_info(self.account), "John Doe")

    def test_get_card_info(self):
        expected_card_info = ("1234 5678 9012 3456", "01/23", "123")
        self.assertEqual(self.controller.get_card_info(self.account), expected_card_info)

    def test_get_balance(self):
        self.assertEqual(self.controller.get_balance(self.account), 1000)

    def test_set_balance(self):
        self.controller.set_balance(self.account, 500)
        self.assertEqual(self.controller.get_balance(self.account), 500)

    def test_get_cut(self):
        self.assertEqual(self.controller.get_cut(self.account), 15)

    def test_set_cut(self):
        self.controller.set_cut(self.account, 30)
        self.assertEqual(self.controller.get_cut(self.account), 30)

    def test_get_card_type(self):
        self.assertEqual(self.controller.get_card_type(self.account), "Visa")

#if __name__ == '__main__':
#    unittest.main()
