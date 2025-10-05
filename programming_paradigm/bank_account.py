# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional balance (default = 0)."""
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money if balance is sufficient.
        Returns True if successful, otherwise False.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${int(self.__account_balance)}")

