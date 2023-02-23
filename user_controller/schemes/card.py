class Card:
    def __init__(self, number, exp_date, cvv, nip):
        self.number = number
        self.exp_date = exp_date
        self.cvv = cvv
        self.nip = nip

    def get_number(self):
        return self.number

    def get_exp_date(self):
        return self.exp_date

    def get_cvv(self):
        return self.cvv

    def verify_nip(self, nip):
        return self.nip == nip
