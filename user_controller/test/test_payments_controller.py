#import unittest
from schemes.payments import Payment
from schemes.user import User
from controllers.payments_controller import PaymentController

class TestPaymentsController():
    def setUp(self):
        self.user1 = User("John Doe", "01-01-1990", "555-5555", 30)
        self.user2 = User("Jane Smith", "05-15-1995", "444-4444", 25)
        self.payment1 = Payment(self.user1, self.user2, 100, "USD", "Test payment", "pending", "credit card", 5, "ABC123")
        self.payment2 = Payment(self.user2, self.user1, 50, "USD", "Test payment", "pending", "paypal", 2.5, "XYZ789")
        self.controller = PaymentController()

    def test_create_payment(self):
        self.assertEqual(len(self.controller.get_all_payments()), 0)
        self.controller.create_payment(self.payment1)
        self.assertEqual(len(self.controller.get_all_payments()), 1)
        self.assertEqual(self.controller.get_payment_by_reference("ABC123"), self.payment1)
        self.controller.create_payment(self.payment2)
        self.assertEqual(len(self.controller.get_all_payments()), 2)
        self.assertEqual(self.controller.get_payment_by_reference("XYZ789"), self.payment2)

    def test_update_payment(self):
        self.controller.create_payment(self.payment1)
        self.assertEqual(self.controller.get_payment_by_reference("ABC123").get_status(), "pending")
        self.controller.update_payment_status("ABC123", "approved")
        self.assertEqual(self.controller.get_payment_by_reference("ABC123").get_status(), "approved")
        self.assertEqual(self.controller.get_payment_by_reference("ABC123").get_method(), "credit card")
        self.controller.update_payment_method("ABC123", "bank transfer")
        self.assertEqual(self.controller.get_payment_by_reference("ABC123").get_method(), "bank transfer")

    def test_delete_payment(self):
        self.controller.create_payment(self.payment1)
        self.controller.create_payment(self.payment2)
        self.assertEqual(len(self.controller.get_all_payments()), 2)
        self.controller.delete_payment("ABC123")
        self.assertEqual(len(self.controller.get_all_payments()), 1)
        self.assertEqual(self.controller.get_payment_by_reference("ABC123"), None)