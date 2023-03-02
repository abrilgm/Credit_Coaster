#import unittest
from controllers.card_controller import CardController
from schemes.card import Card

class TestCardController():

    def setUp(self):
        # Create a sample Card instance
        self.card = Card("1234567890123456", "01/23", "123", "4567")

    def test_verify_nip(self):
        # Verify that a correct NIP returns True
        self.assertTrue(CardController.verify_nip(self.card, "4567"))

        # Verify that an incorrect NIP returns False
        self.assertFalse(CardController.verify_nip(self.card, "1111"))