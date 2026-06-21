class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance



# TODO: Create two accounts
# TODO: Print the information using the mentioned format

b1 = BankAccount("Alice", 1000)
b2 = BankAccount("Bob", 2000)
print(f"Alice's balance: ${b1.balance}")
print(f"Bob's balance: ${b2.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")