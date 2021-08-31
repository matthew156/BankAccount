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
        return f'Your Account Balance is: {self.balance}'
    def yield_interest(self):
        self.balance *= + (self.int_rate * 0.01)
        return self        

class User:
    def __init__(self, name) :
        self.name = name
        self.money = 0
        self.account = Bankaccount(name='Hank', email='fakeemail@gmail.com', int_rate=5, balance=0)
    def display_user_balance(self):
        self.account.display_account_info()
    

user1 =User('user1')

user1.account.deposit(100)
user1.account.withdraw(50)
user1.account.display_account_info()