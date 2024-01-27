from User import User

class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True
    
    def create_account(self, user_name, initial_balance):
        user = User(user_name, initial_balance, self)
        self.users.append(user)
        self.total_balance += initial_balance
        return user        

    def check_total_balance(self):
        return self.total_balance

    def check_total_loan_amount(self):
        return self.total_loan_amount

    def toggle_loan_feature(self, enable):
        self.loan_enabled = enable
    
    def is_loan_enabled(self):
        return self.loan_enabled

    def find_user(self, user_name):
        for user in self.users:
            if user.user_name == user_name:
                return user
        return None