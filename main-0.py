from bank_account import BankAccount

def run_tests():
    print("Running BankAccount tests...\n")

    # Test 1: Deposit
    account = BankAccount(100)
    account.deposit(50)
    expected = 150
    result = account.get_balance()
    print("Deposit Test:", "✅ PASS" if result == expected else f"❌ FAIL (Got {result}, Expected {expected})")

    # Test 2: Withdrawal with sufficient funds
    account = BankAccount(100)
    success = account.withdraw(20)
    expected = 80
    result = account.get_balance()
    print("Withdrawal Test:", "✅ PASS" if success and result == expected else f"❌ FAIL (Got {result}, Expected {expected})")

    # Test 3: Withdrawal more than available
    account = BankAccount(100)
    success = account.withdraw(200)
    expected = 100
    result = account.get_balance()
    print("Overdraft Test:", "✅ PASS" if not success and result == expected else f"❌ FAIL (Got {result}, Expected {expected})")

    # Test 4: Display balance
    account = BankAccount(123.45)
    print("Display Balance Test: Expected output: Current Balance: $123.45")
    print("Actual output: ", end="")
    account.display_balance()
