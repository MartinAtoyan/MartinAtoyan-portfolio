


if __name__ == "__main__":
    from account import CheckingAccount, SavingAccount, JointAccount
    from costumer import Customer

    alice = Customer("Alice", "alice@example.com")
    bob = Customer("Bob", "bob@example.com")

    checking = CheckingAccount(123, 1000)
    savings = SavingAccount(456, 5000)

    joint_account = JointAccount(789, 2000, [alice, bob])

    alice.add_account(checking)
    bob.add_account(savings)
    alice.add_account(joint_account)
    bob.add_account(joint_account)

    alice.transfer_funds(123, 456, 300)
