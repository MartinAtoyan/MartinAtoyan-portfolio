import abc

class Account(abc.ABC):
    def __init__(self, account_number: int, balance: float, account_type: str):
        if account_number > 0:
            self.account_number = account_number
        else:
            print("Account id must be positive number")

        self.__balance = balance

        if type(account_type) is str:
            self.__account_type = account_type

    @abc.abstractmethod
    def deposit(self, amount: float) -> None:
        ...

    @abc.abstractmethod
    def withdraw(self, amount: float) -> None:
        ...

    @abc.abstractmethod
    def transfer(self, destination: "Account", amount: float ) -> None:
        ...

    @abc.abstractmethod
    def show_balance(self) -> None:
        ...

    @abc.abstractmethod
    def get_account_type(self) -> str:
        ...


class CheckingAccount(Account):
    def __int__(self, account_number: int, balance: float):
        super().__init__(account_number, balance, "check")
        self.overdraft_limit = 500.0
        self.__total = self.__balance + self.overdraft_limit

    def deposit(self, amount: float) -> None:
        self.__balance += amount
        print(f"Your deposit is {amount}. Your balance {self.__balance}")

    def withdraw(self, amount: float) -> None:
        if self.__balance > amount:
            self.__balance -= amount
            print(f"You withdrew {amount}")
        elif self.__total > amount:
            self.__total -= amount
            print(f"You withdrew with overdraft.")
        else:
            print(f"You can't withdraw from your balance {amount}. Your total balance less then withdraw amount")


    def transfer(self, to_account: "Account", amount: float) -> None:
        if self.__balance > amount:
            self.__balance -= amount
            to_account.deposit(amount)
            print(f"You transferred {amount}")
        elif self.__total > amount:
            self.__total -= amount
            to_account.deposit(amount)
            print(f"You transferred with overdraft.")
        else:
            print(f"You can't transfer. Transfer amount is more than total balance.")


    def show_balance(self) -> None:
        print(f"Your balance is {self.__balance} \n Your total balance is {self.__total}")


    def get_account_type(self) -> str:
        return self.__account_type



class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: float, interest_rate: float):
        super().__init__(account_number, balance, "Savings")
        self.interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        self.__balance += amount
        print(f"Deposited {amount}. Balance is {self.__balance}.")

    def withdraw(self, amount: float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. Balance is {self.__balance}.")
        else:
            print("Insufficient balance.")

    def transfer(self, to_account: 'Account', amount: float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
            to_account.deposit(amount)
            print(f"Transferred {amount} to account {to_account.account_number}.")
        else:
            print("Insufficient balance.")

    def show_balance(self) -> None:
        print(f"Current balance: {self.__balance}")

    def get_account_type(self) -> str:
        return self.__account_type


class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, joint_owners: list):
        super().__init__(account_number, balance, "Joint")
        self.__joint_owners = joint_owners

    def deposit(self, amount: float) -> None:
        self.__balance += amount
        print(f"Deposited {amount}. Balance is {self.__balance}.")

    def withdraw(self, amount: float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. Balance is {self.__balance}.")
        else:
            print("Insufficient balance.")

    def transfer(self, destination: 'Account', amount: float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
            destination.deposit(amount)
            print(f"Transferred {amount} to account {destination.account_number}.")
        else:
            print("Amount is less than your balance.")

    def show_balance(self) -> None:
        print(f"Balance: {self.__balance}")

    def get_account_type(self) -> str:
        return self.__account_type

    def add_owner(self, customer_name: str) -> None:
        self.__joint_owners.append(customer_name)
        print(f"Added {customer_name} as a joint owner.")



class TransactionManager(abc.ABC):
    @abc.abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        ...

    @abc.abstractmethod
    def show_transaction_history(self) -> None:
        ...


