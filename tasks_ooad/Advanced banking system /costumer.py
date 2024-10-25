# class Costumer:
#     def __init__(self, name, contact_info):
#         self.name = name
#         self.contact_info = contact_info
#         self.accounts = {}
#
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if isinstance(value, str) and len(value) > 1:
#             self.__name = value
#         else:
#             raise ValueError("Name must be string and greater than 1.")
#
#     @property
#     def contact_info(self):
#         return self.__contact_info
#
#     @contact_info.setter
#     def contact_info(self, value):
#         if isinstance(value, str) and len(value) > 1:
#             self.__contact_info = value
#         else:
#             raise TypeError("Contact info must be string.")
#
#     def add_account(self, account):
#         self.accounts[account.account_number] = account
#
#     def get_account(self, account_number):
#         return self.accounts.get(account_number)
#
#     def transfer_funds(self, from_account, to_account, amount):
#         if from_account in self.accounts and to_account in self.accounts:
#
#             start = self.accounts[from_account]
#             finish = self.accounts[to_account]
#             start.withdraw(amount)
#             finish.deposit(amount)
#
#         else:
#             raise ValueError("One or both accounts not found")

from typing import Dict
from account import Account  # Assuming you have an `Account` class

class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.accounts: Dict[int, Account] = {}

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 1:
            self.__name = value
        else:
            raise ValueError("Name must be a string with more than one character.")

    @property
    def contact_info(self) -> str:
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value: str):
        if isinstance(value, str) and len(value) > 1:
            self.__contact_info = value
        else:
            raise ValueError("Contact info must be a string with more than one character.")

    def add_account(self, account: Account):
        if isinstance(account, Account):
            self.accounts[account.account_number] = account
        else:
            raise TypeError("Only instances of Account can be added.")

    def get_account(self, account_number: int) -> Account:
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError(f"No account found with number {account_number}.")
        return account

    def transfer_funds(self, from_account_number: int, to_account_number: int, amount: float):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        try:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f"Transferred ${amount} from account {from_account_number} to {to_account_number}.")
        except ValueError as e:
            raise ValueError(f"Transfer failed: {str(e)}")
