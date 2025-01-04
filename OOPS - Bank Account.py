#Implement a BankAccount class with deposit, withdraw, and balance display methods.
class BankAccount:
    def __init__(self,owner, balance = 0):
        self.owner = owner
        self. balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient funds for withdrawal.")
    def display_balance(self):
        print(f"Current balance: ${self.balance}")
account = BankAccount("Jahnavi", 5000)
account.display_balance()
account.deposit(500)
account.withdraw(2000)
account.withdraw(500)
account.display_balance()