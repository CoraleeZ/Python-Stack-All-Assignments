class BankAccount:
    def __init__(self,amount=0,interest_rate=0.01):
        self.account_balance=amount
        self.interest_rate=interest_rate
    def deposit(self, amount):
        if(amount<0):
            print('amount should be a positive number')
            return false
        else:
            self.account_balance+=amount
        return self
    def withdraw(self, amount):
        if(amount<0):
            print('amount should be a positive number')
        elif(amount>self.account_balance):
            print('Insufficient funds: Charging a $5 fee')
            self.account_balance-=5
        else:
            self.account_balance-=amount
        return self
    def display_account_info(self):
        print("Balance: $"+str(self.account_balance))
        return self
    def yield_interest(self):
        if(self.account_balance>0):
            self.account_balance+=self.account_balance*self.interest_rate
        return self

account1=BankAccount(500,0.02)
account2=BankAccount(300,0.03)

account1.deposit(20).deposit(10).deposit(30).withdraw(10).yield_interest().display_account_info()
account2.deposit(30).deposit(40).withdraw(10).withdraw(20).withdraw(5).yield_interest().display_account_info()