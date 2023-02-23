
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