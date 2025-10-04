class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance (default 0)."""
        self.__account_balance = initial_balance  # encapsulated attribute

    def deposit(self, amount):
        """Deposit a positive amount to the account."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw an amount if sufficient funds exist."""
        if amount > self.__account_balance:
            print("Insufficient funds!")
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current balance: ${self.__account_balance:.2f}")
