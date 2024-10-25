# from abc import ABC, abstractmethod
# from typing import List
# from transaction import Transaction
# from costumer import Costumer
#
# class Account(ABC):
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#         self.account_type = None
#         self.transactions = []
#
#     @property
#     def account_number(self):
#         return self.__account_number
#
#     @account_number.setter
#     def account_number(self, value):
#         if isinstance(value, str) and len(value) > 0:
#             self.__account_number = value
#         else:
#             raise ValueError("Account number must be a positive integer.")
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, value):
#         if isinstance(value, float) and value >= 0:
#             self.__balance = value
#         else:
#             raise ValueError("Balance must be a non-negative float.")
#
#     @abstractmethod
#     def withdraw(self, value):
#         pass
#
#     def deposit(self, value):
#         if isinstance(value, float) and value > 0:
#             self.balance += value
#             transaction = Transaction(self.account_number, value, "deposit")
#             self.transactions.append(transaction)
#         else:
#             raise ValueError("Deposit value must be a positive float.")
#
# class SavingAccount(Account):
#     def __init__(self, account_number, balance):
#         super().__init__(account_number, balance)
#         self.withdraw_count = 0
#         self.withdraw_limit = 100
#         self.account_type = "Saving"
#
#     def withdraw(self, value):
#         if value <= self.balance and self.withdraw_count < self.withdraw_limit:
#             self.balance -= value
#             transaction = Transaction(self.account_number, value, "withdraw")
#             self.transactions.append(transaction)
#             self.withdraw_count += 1
#         else:
#             raise ValueError("value must be smaller than your balance and check your limit")
#
#
# class IndividualAccount(Account):
#     def __init__(self, account_number, balance):
#         super().__init__(account_number, balance)
#         self.account_type = "Individual"
#
#     def withdraw(self, value):
#         if value < self.balance:
#             self.balance -= value
#             transaction = Transaction(self.account_number, value, "withdraw")
#             self.transactions.append(transaction)
#         else:
#             raise ValueError("value > balance.")
#
#
# class CheckingAccount(Account):
#     def __init__(self, account_number, balance):
#         super().__init__(account_number, balance)
#         self.account_type = "Checking"
#
#     def withdraw(self, value):
#         if value < self.balance:
#             self.balance -= value
#             transaction = Transaction(self.account_number, value, "withdraw")
#             self.transactions.append(transaction)
#         else:
#             raise ValueError("value smaller than your balance")
#
#
# class JointAccount(CheckingAccount):
#     def __init__(self, account_number, balance, costumers: List["Costumer"]):
#         super().__init__(account_number, balance)
#         self.costumers = costumers
#         self.account_type = "Joint"
#
#     @property
#     def costumers(self):
#         return self.__costumers
#
#     @costumers.setter
#     def costumers(self, value):
#         if all(isinstance(cos, Costumer) for cos in value):
#             self.__costumers = value
#         else:
#             raise ValueError("All elements must be Account type.")
#

from abc import ABC, abstractmethod
from typing import List
from transaction import Transaction
from costumer import Customer

class Account(ABC):
    def __init__(self, account_number: int, balance: float):
        self.account_number = account_number
        self.balance = balance
        self.account_type = None
        self.transactions: List[Transaction] = []

    @property
    def account_number(self) -> int:
        return self.__account_number

    @account_number.setter
    def account_number(self, value: int):
        if isinstance(value, int) and value > 0:
            self.__account_number = value
        else:
            raise ValueError("Account number must be a positive integer.")

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        if isinstance(value, float) and value >= 0:
            self.__balance = value
        else:
            raise ValueError("Balance must be a non-negative float.")

    @abstractmethod
    def withdraw(self, value: float):
        pass

    def deposit(self, value: float):
        if isinstance(value, float) and value > 0:
            self.balance += value
            transaction = Transaction(self.account_number, value, "deposit")
            self.transactions.append(transaction)
        else:
            raise ValueError("Deposit value must be a positive float.")


class SavingAccount(Account):
    def __init__(self, account_number: int, balance: float):
        super().__init__(account_number, balance)
        self.withdraw_count = 0
        self.withdraw_limit = 100
        self.account_type = "Saving"

    def withdraw(self, value: float):
        if value <= self.balance and self.withdraw_count < self.withdraw_limit:
            self.balance -= value
            transaction = Transaction(self.account_number, value, "withdraw")
            self.transactions.append(transaction)
            self.withdraw_count += 1
        else:
            raise ValueError("Withdrawal failed: Insufficient balance or limit reached.")


class IndividualAccount(Account):
    def __init__(self, account_number: int, balance: float):
        super().__init__(account_number, balance)
        self.account_type = "Individual"

    def withdraw(self, value: float):
        if value <= self.balance:
            self.balance -= value
            transaction = Transaction(self.account_number, value, "withdraw")
            self.transactions.append(transaction)
        else:
            raise ValueError("Withdrawal failed: Insufficient balance.")


class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float):
        super().__init__(account_number, balance)
        self.account_type = "Checking"

    def withdraw(self, value: float):
        if value <= self.balance:
            self.balance -= value
            transaction = Transaction(self.account_number, value, "withdraw")
            self.transactions.append(transaction)
        else:
            raise ValueError("Withdrawal failed: Insufficient balance.")


class JointAccount(CheckingAccount):
    def __init__(self, account_number: int, balance: float, customers: List[Customer]):
        super().__init__(account_number, balance)
        self.customers = customers
        self.account_type = "Joint"

    @property
    def customers(self) -> List[Customer]:
        return self.__customers

    @customers.setter
    def customers(self, value: List[Customer]):
        if all(isinstance(cust, Customer) for cust in value):
            self.__customers = value
        else:
            raise ValueError("All elements must be Customer instances.")
