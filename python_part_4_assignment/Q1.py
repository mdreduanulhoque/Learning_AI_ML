"""
Q1. Create a BankAccount class with attributes account number, owner name,
and balance.
Add methods to deposit, withdraw, and check balance.
"""

class BankAccount:
    def __init__(self, account_num, owner_name, balance):
        self.account_num = account_num
        self.owner_name = owner_name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount {amount} has been added to your account.\nNew Balance {self.__balance}")

    def withdraw(self, amount):
        if(self.__balance - amount >= 0):
            self.__balance -= amount
            print(f"Amount {amount} has been withdrawed from your account.\nNew balance is {self.__balance}")
        else:
            print(f"Insufficient Balance.\nCurrent balance is {self.__balance}")

    def check_balance(self):
        print(f"Current Balance is {self.__balance}")

a1 = BankAccount(account_num=15987, owner_name="lomy", balance=9100)
a1.check_balance()

a1.deposit(amount=9000)

a1.withdraw(amount=5000)