class User:
    def __init__(self, user_name, initial_balance, bank):
        self.user_name = user_name
        self.balance = initial_balance
        self.transaction_history = []
        self.loan = 0
        self.bank = bank

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")
        print(f"Deposit of {amount} successful. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal: -{amount}')
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient funds. Unable to withdraw.")

    def transfer(self, receiver_name, amount):
        receiver = self.bank.find_user(receiver_name)

        if receiver is not None:
            if self.balance >= amount:
                self.balance -= amount
                receiver.balance += amount
                self.transaction_history.append(f'Transferred {amount} to {receiver_name}')
                receiver.transaction_history.append(f'Received {amount} from {self.user_name}')
                print(f"Transfer of {amount} to {receiver_name} successful.")
                print(f"Your new balance: {self.balance}")
                print(f"{receiver_name}'s new balance: {receiver.balance}")
            else:
                print("Insufficient funds. Unable to transfer")
        else:
            print("Receiver not found")

    def check_balance(self):
        print(f"Balance of {self.user_name} is {self.balance}")

    def check_transaction_history(self):
        print(f"Transaction history of {self.user_name}: {self.transaction_history}")

    def take_loan(self, loan_amount):
        if self.bank.is_loan_enabled():
            if self.loan == 0:
                self.loan = loan_amount
                self.balance += loan_amount
                self.transaction_history.append(f"Loan taken: +{loan_amount}")
                print(f"Loan of {loan_amount} granted. New balance is {self.balance}")
            else:
                print(f"{self.user_name} already has an existing loan.")
        else:
            print("Loan feature is not enabled.")
