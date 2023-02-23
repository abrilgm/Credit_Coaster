class Payment:
    def __init__(self, payer, payee, amount, currency, description, status, method, fee, reference):
        self.payer = payer
        self.payee = payee
        self.amount = amount
        self.currency = currency
        self.description = description
        self.status = status
        self.method = method
        self.fee = fee
        self.reference = reference

    def get_payer_info(self):
        return self.payer.name, self.payer.email, self.payer.phone

    def get_payee_info(self):
        return self.payee.name, self.payee.email, self.payee.phone

    def get_amount(self):
        return self.amount

    def get_currency(self):
        return self.currency

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_method(self):
        return self.method

    def get_fee(self):
        return self.fee

    def get_reference(self):
        return self.reference

    def set_status(self, new_status):
        self.status = new_status

    def set_method(self, new_method):
        self.method = new_method
