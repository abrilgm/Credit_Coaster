
from Account import Account


class User:
    
    def __init__(self, name: str, birthdate: str, phone: str, age:str):
        self.account = None
        self.name = name
        self.birthdate = birthdate
        self.phone = phone
        self.age = age


    def create_account(self):
         if self.account:
             return
             self.account = Account(self)
    
    
user = User("Name","01-01-01","123123123","23")
user.create_account()
