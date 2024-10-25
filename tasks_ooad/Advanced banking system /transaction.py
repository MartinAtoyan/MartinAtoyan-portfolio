#
# class Transaction:
#     def __init__(self, account_number, amount, transaction_type):
#         self.account_number = account_number
#         self.amount = amount
#         self.transaction_type = transaction_type
#
#     @property
#     def account_number(self):
#         return self.__account_number
#
#     @account_number.setter
#     def account_number(self, value):
#         if isinstance(value, int) and value > 0:
#             self.__account_number = value
#         else:
#             raise ValueError
#
#     @property
#     def amount(self):
#         return self.__amount
#
#     @amount.setter
#     def amount(self, value):
#         if isinstance(value, float) and value > 0:
#             self.__amount = value
#         else:
#             raise ValueError
#
#     @property
#     def transaction_type(self):
#         return self.__transaction_type
#
#     @transaction_type.setter
#     def transaction_type(self, value):
#         if isinstance(value, str) and len(value) >= 1:
#             self.__transaction_type = value
#         else:
#             raise ValueError
#
#     def __str__(self):
#         return f"{self.__account_number} : {self.__amount} : {self.__transaction_type}"
#

class Transaction:
    def __init__(self, account_number: int, amount: float, transaction_type: str):
        self.account_number = account_number
        self.amount = amount
        self.transaction_type = transaction_type

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
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        if isinstance(value, float) and value > 0:
            self.__amount = value
        else:
            raise ValueError("Amount must be a positive float.")

    @property
    def transaction_type(self) -> str:
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value: str):
        if isinstance(value, str) and len(value) >= 1:
            self.__transaction_type = value
        else:
            raise ValueError("Transaction type must be a non-empty string.")

    def __str__(self) -> str:
        return (f"Transaction: Account #{self.account_number}, "
                f"Amount: ${self.amount:.2f}, Type: {self.transaction_type}")
