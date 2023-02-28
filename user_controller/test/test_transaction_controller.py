#import unittest
from user_controller.schemes.Account import Account
from user_controller.schemes.card import Card
from user_controller.schemes.transactions import Transaction
from user_controller.controllers.transaction_controller import TransactionController

class TestTransactionController():
    def test_make_purchase(self):
        # Set up test data
        acc = Account(12345, "Ana", "Juarez", 1000.0)
        card_number = "1234567890123456"
        exp_date = "12/23"
        nip = "1234"
        cvv = "123"
        payments_amount = 500.0
        
        # Call the function being tested
        transaction = TransactionController.make_purchase(card_number, exp_date, nip, cvv, payments_amount, acc)
        
        # Assert that the transaction amount matches the payment amount
        self.assertEqual(transaction.amount, payments_amount)
        
        # Assert that the account balance has been updated
        self.assertEqual(acc.balance, 500.0)
        
        # Assert that the card balance has been updated
        self.assertEqual(transaction.card.balance, payments_amount)
