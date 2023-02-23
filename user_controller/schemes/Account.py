import user as user
class Account:
    def __init__(self, user, card, balance, cut, card_type):
        self.user = user
        self.card = card
        self.balance = balance
        self.cut = cut
        self.type = card_type


    def get_user_info(self):
        # TODO: Tienes que agreager la opcion de addres y la de phone 
        return self.user.name # self.user.address, self.user.phone
        

    def get_card_info(self):
        return self.card.number, self.card.exp_date, self.card.cvv

    def get_balance(self):
        return self.balance

    def get_cut(self):
        return self.cut

    def get_card_type(self):
        return self.type

    def set_balance(self, new_balance):
        self.balance = new_balance

    def set_cut(self, new_cut):
        self.cut = new_cut
