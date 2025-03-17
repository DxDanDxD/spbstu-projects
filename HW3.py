class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @staticmethod
    def validate_amount(amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма должна быть положительным числом.")
        return True

    @classmethod
    def create_with_zero_balance(cls, account_number):
        return cls(account_number)

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount

    def withdraw(self, amount):
        if self.validate_amount(amount):
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                raise ValueError("Недостаточно средств на счете.")

    def get_balance(self):
        return self.__balance

    import secrets
    import string

    class User:
        def __init__(self, username, password):
            self.__username = username
            self.__password = password

        @staticmethod
        def is_password_strong(password):
            return len(password) >= 6

        @classmethod
        def create_with_default_password(cls, username):
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet) for _ in range(12))
            return cls(username, password)

        def change_password(self, new_password):
            if self.is_password_strong(new_password):
                self.__password = new_password
            else:
                raise ValueError("Пароль должен содержать не менее 6 символов.")

        def get_username(self):
            return self.__username


from datetime import datetime

class Book:
    def __init__(self, title, author, year=None):
        self.__title = title
        self.__author = author
        self.__year = year if year is not None else 2024

    @staticmethod
    def validate_year(year):
        current_year = datetime.now().year
        if not isinstance(year, int) or year > current_year:
            raise ValueError("Год издания должен быть целым числом и не в будущем.")
        return True

    @classmethod
    def create_with_default_year(cls, title, author):
        return cls(title, author)

    def get_info(self):
        return f"Книга: {self.__title}, Автор: {self.__author}, Год издания: {self.__year}"