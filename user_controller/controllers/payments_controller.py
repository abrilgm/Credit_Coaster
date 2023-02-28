from user_controller.schemes.payments import Payment

class PaymentController:
    @staticmethod
    def create_payment(payer, payee, amount, currency, description, method):
        """Create a new Payment instance with the given attributes."""
        payment = Payment(payer=payer, payee=payee, amount=amount, currency=currency,
                          description=description, status="Pending", method=method, fee=0, reference="")
        return payment

    @staticmethod
    def get_payment_by_reference(payments, reference):
        """Retrieve a Payment instance by its reference number."""
        payment = next((payment for payment in payments if payment.get_reference() == reference), None)
        return payment

    @staticmethod
    def update_payment_status(payment, new_status):
        """Update the status of a Payment instance."""
        if payment is not None:
            payment.set_status(new_status)
            return True
        else:
            return False

    @staticmethod
    def update_payment_method(payment, new_method):
        """Update the method of a Payment instance."""
        if payment is not None:
            payment.set_method(new_method)
            return True
        else:
            return False
