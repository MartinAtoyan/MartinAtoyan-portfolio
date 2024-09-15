from homeworks.projects.Banking_account_project.account.Account import Account


class Customer:
    def __init__(self, name: str,
                 contact_info: str,
                 accounts: list[Account]):
        self.__name = name
        self.__contact_info = contact_info
        self.__accounts = []

    def add_account(self, account: Account) -> None:
        self.__accounts.append(account)
        print(f"You add account {account}")

    def view_accounts(self) -> None:
        for account in self.__accounts:
            print(f"Account number - {account.account_number} \n"
                  f"Account balance - {account.show_balance()} \n"
                  f"Account type - {account.get_account_type()}")