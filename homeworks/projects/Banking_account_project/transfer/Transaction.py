from datetime import datetime
from typing import Optional

from homeworks.projects.Banking_account_project.account.Account import Account


class Transaction:
    def __init__(self, from_account: Account,
                 to_account: Optional['Account'],
                 amount: float,
                 transaction_type: str,
                 timestamp: datetime):
        self.__from_account = from_account
        self.__to_account = to_account
        self.__amount = amount
        self.__transaction_type = transaction_type
        self.__timestamp = datetime.now()

    def log(self) -> None:
        print(f"Transaction: {self.__transaction_type}, "
              f"Amount: {self.__amount}, "
              f"From: {self.__from_account}, "
              f"To: {self.__to_account}, "
              f"Date: {self.__timestamp}")

