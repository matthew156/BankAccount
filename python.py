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
        if self.balance < 0:
            self.balance -= 5
            print('Insufficient funds, charging a $5 fee...')
        return self    
    def display_account_info(self):
        print(f'Your Account Balance is: {self.balance}')
    def yield_interest(self):
        self.balance *= + (self.int_rate * 0.01)
        return self        


peter = Bankaccount('Peter', 'peter@fakeemail.com', 15, 1000)

lois = Bankaccount('Lois', 'peter@fakeemail.com', 15, 1000)

hank = Bankaccount('Hank', 'peter@fakeemail.com', 15, 100)

peter.deposit(2000).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()

lois.deposit(2000).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()


hank.withdraw(105)
hank.display_account_info()