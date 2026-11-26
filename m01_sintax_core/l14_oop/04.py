# Банкир.

# Создайте класс BankAccount с конструктором, который принимает параметры account_number и initial_balance.
# Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), который снимает средства со счета.
# Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.

# Напишите тут ваш код

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount
        return self.initial_balance

    def withdraw(self, amount):
        if amount <= self.initial_balance:
            self.initial_balance = self.initial_balance - amount
        else:
            print("Недостаточно средств на счете")
        return self.initial_balance


bank_account = BankAccount(22, 1000)
print(bank_account.deposit(77))
print(bank_account.withdraw(66))
