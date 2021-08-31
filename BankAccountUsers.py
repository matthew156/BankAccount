class Bankaccount:
    def __init__(self, name, email, int_rate, balance):
        self.name = name
        self.email = email
        self.int_rate = int_rate
        self.balance = balance
        self.money = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self    
    def display_account_info(self):
        print(f'Your Account Balance is: {self.balance}')
    def yield_interest(self):
        self.balance *= + (self.int_rate * 0.01)
        return self        

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bankaccount(int_rate=0.02, balance=0)
    
    def updated_deposit(self):
        self.account.deposit(100)
        return self
    def updated_withdraw(self):
        self.account.withdraw(100)
        return self
    def updated_display_user_balance(self):
        self.account.display_account_info

peter = User('Peter', 'peter@fakeemail.com')

print(peter.updated_deposit)