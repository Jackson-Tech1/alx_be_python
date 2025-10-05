class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with optional starting balance (default=0)."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit amount into account. Returns True if successful."""
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds. Returns True if successful."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def
