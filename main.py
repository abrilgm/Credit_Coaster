# Importar las clases necesarias
from user_controller.schemes.user import User
from user_controller.schemes.card import Card
from user_controller.schemes.Account import Account
from user_controller.schemes.transactions import Transaction
from user_controller.schemes.payments import Payment

# Solicitar información del usuario
print('Bienvenido a la aplicación de tarjeta de crédito')
name = input('Por favor ingrese su nombre: ')
email = input('Por favor ingrese su correo electrónico: ')
phone = input('Por favor ingrese su número de teléfono: ')

# Crear objeto de la clase User con la información del usuario
user = User(name, phone, birthdate=str, age=str)

# Solicitar información de la tarjeta
print('Por favor ingrese la información de su tarjeta de crédito')
number = input('Número de la tarjeta: ')
expiration_date = input('Fecha de expiración (MM/YY): ')
cvv = input('CVV: ')
nip = input('NIP: ')

# Crear objeto de la clase Card con la información de la tarjeta
card = Card(number, expiration_date, cvv, nip)

# Solicitar información de la cuenta
print('Por favor ingrese la información de su cuenta')
balance = float(input('Saldo actual: '))
cut = float(input('Límite de crédito: '))
card_type = input('Tipo de tarjeta: ')

# Crear objeto de la clase Account con la información de la cuenta
account = Account(user, card, balance, cut, card_type)

# Solicitar información de la transacción
print('Por favor ingrese la información de la transacción')
t_type = input('Tipo de transacción: ')
description = input('Descripción: ')
status = input('Estado: ')
source = input('Origen: ')
destination = input('Destino: ')
location = input('Ubicación: ')


# Crear objeto de la clase Transaction con la información de la transacción
transaction = Transaction(t_type, description, status, source, destination, location)

# Solicitar información del pago
print('Por favor ingrese la información del pago')
payer = input('Pagador: ')
payee = input('Beneficiario: ')
amount = float(input('Monto: '))
currency = input('Divisa: ')
description = input('Descripción: ')
status = input('Estado: ')
method = input('Método de pago: ')
fee = float(input('Comisión: '))
reference = input('Referencia: ')

# Crear objeto de la clase Payment con la información del pago
payment = Payment(payer, payee, amount, currency, description, status, method, fee, reference)

# Imprimir información de la cuenta, tarjeta, transacción y pago
print('Información de la cuenta:')
print(account.get_info())
print('Información de la tarjeta:')
print(card.get_info())
print('Información de la transacción:')
print(transaction.get_info())
print('Información del pago:')
print(payment.get_info())

