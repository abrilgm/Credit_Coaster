
from user_controller.schemes.Account import Account
from user_controller.schemes.card import Card
from user_controller.schemes.transactions import Transaction

class TransactionController:
    
    @staticmethod
    def make_purchase(card_number: str, exp_date: str, nip: str, cvv: str, payments_amount: float, acc: Account):
        # Create card object
        purchase_card = Card(card_number, exp_date, nip, cvv)
        
        # Validate NIP
        if not purchase_card.verify_nip(nip):
            raise ValueError("NIP incorrecto")
        
        # Validate amount < limit
        if acc.balance < payments_amount:
            raise ValueError("Fondos insuficientes")
        
        # Charge amount to card
        purchase_card.charge(payments_amount)
        
        # Subtract amount from account balance
        acc.withdraw(payments_amount)
        
        # Create transaction
        tran = Transaction(purchase_card, payments_amount)
        
        # Return transaction
        return tran

    

