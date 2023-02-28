from user_controller.schemes.user import User

class UserController:
    @staticmethod
    def create_user(name, birthdate, phone, age):
        """Create a new User instance with the given attributes."""
        user = User(name=name, birthdate=birthdate, phone=phone, age=age)
        return user

    @staticmethod
    def create_user_with_account(name, birthdate, phone, age):
        """Create a new User instance with an associated Account instance."""
        user = User(name=name, birthdate=birthdate, phone=phone, age=age)
        account = account(user=user)
        user.account = account
        return user

    @staticmethod
    def get_user_by_phone(users, phone):
        """Retrieve a User instance by phone number."""
        user = next((user for user in users if user.phone == phone), None)
        return user

    @staticmethod
    def update_user_phone(user, new_phone):
        """Update the phone number of a User instance."""
        if user is not None:
            user.phone = new_phone
            return True
        else:
            return False
