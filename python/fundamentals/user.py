class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account=BankAccount(amount=0,interest_rate=0.01)
    # adding the deposit method
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print('User: '+self.name+', Balance: $'+str(self.account.account_balance))
        return self
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

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

peter=User('Peter','peter@gmail.com')
john=User('john','john@gmail.com')
anna=User('Anna','anna@gmail.com')

peter.make_deposit(100).make_deposit(20).make_withdrawal(30).display_user_balance()

# peter.make_deposit(100)
# peter.make_deposit(20)
# peter.make_withdrawal(30)
# print(peter.account_balance)


john.make_deposit(300).make_deposit(12).make_withdrawal(200).make_withdrawal(100).display_user_balance()

anna.make_deposit(50).make_withdrawal(5).make_withdrawal(6).make_withdrawal(4).display_user_balance()

anna.transfer_money(peter,20).display_user_balance()
peter.display_user_balance()