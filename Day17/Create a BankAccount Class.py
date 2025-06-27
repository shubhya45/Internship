# Create a BankAccount Class
# Attributes:

# account_holder, balance.

# Methods:

# deposit(amount) — Adds money.

# withdraw(amount) — Subtracts money if available.

# display_balance() — Shows the balance.

# Test it: Create an account, deposit money, withdraw money, and display the balance.

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance= balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"the amount after deposit: {self.balance}")
    def withdraw(self,amount):
        self.balance-=amount
        print(f"the amount after withdraw: {self.balance} ")
    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"current balance: {self.balance}")
b1=BankAccount("Shubham",5000)
b1.deposit(4000)
b1.withdraw(500)
b1.display_balance()
    
        