from Bank import Bank

def main():
    # Create a bank
    my_bank = Bank("My Bank")

    # Create users and accounts
    user1 = my_bank.create_account("Alice", 1000)
    user2 = my_bank.create_account("Bob", 500)

    # Perform transactions
    user1.deposit(200)
    user1.withdraw(100)
    user1.transfer("Bob", 50)

    user2.deposit(300)
    user2.transfer("Alice", 25)

    # Check balances and transaction history
    user1.check_balance()
    user1.check_transaction_history()

    user2.check_balance()
    user2.check_transaction_history()

    # Enable loan feature and take a loan
    my_bank.toggle_loan_feature(True)
    user1.take_loan(500)

    # Check total bank balance and total loan amount
    print(f"Total Bank Balance: {my_bank.check_total_balance()}")
    print(f"Total Loan Amount: {my_bank.check_total_loan_amount()}")

if __name__ == "__main__":
    main()
