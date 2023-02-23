
from user_controller.schemes.Account import Account
from user_controller.schemes.card import Card
from user_controller.schemes.transactions import Transaction


class TransactionController:
    
    @staticmethod
    def make_purchase(card: Card, amount, nip, acc: Account):
        # TODO
        # Validar NIP
        if not card.verify_nip(nip):
            raise ValueError("Nip incorrecto")
        # Validar monto < limite
        if acc.balance < amount:
            raise ValueError("Fondos insuficientes")
        
        # Crear transaccion
        tran = Transaction()
        
        # Restar/sum balance
        # Regresar la transaccion
        return tran
    

class TransactionController:
    
    @staticmethod
    def make_purchase(card: number, exp_date, nip,cvv pay: payments , acc: Account):
        # Get card details
        card_number = input("Ingrese el número de tarjeta: ")
        card_name = input("Ingrese el nombre en la tarjeta: ")
        card_expiry = input("Ingrese la fecha de vencimiento (MM/YY): ")
        card_cvv = input("Ingrese el código CVV: ")
        payments_amount = input("Ingrese el monto a pagar")
        
        # Create card object
        purchase_card = Card(card_number, card_name, card_expiry, card_cvv)
        
        # Validate NIP
        if not purchase_card.verify_nip(nip):
            raise ValueError("NIP incorrecto")
        
        # Validate amount < limit
        if acc.balance < amount:
            raise ValueError("Fondos insuficientes")
        
        # Charge amount to card
        purchase_card.charge(amount)
        
        # Subtract amount from account balance
        acc.withdraw(amount)
        
        # Create transaction
        tran = Transaction(purchase_card, amount)
        
        # Return transaction
        return tran
