
class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        
        if self.balance <0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5

        else :
            self.balance -= amount

        return self

    def displayAccountInfo(self):
        print(f"Balance: ${self.balance}")

    def yieldInterest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
       
        return self
        
class User:		# declare a class and give it name User
    def __init__(self,name,email,amount):
        self.name = name
        self.email = "email"
        self.account =BankAccount(0.5,1000)
    print( self.account)


    def make_withdrawal(self, amount):
        self.account.withdraw(1000)
        
    def display_user_balance(self):
       self.account.displayAccountInfo()
   
    def make_deposit(self, amount):	
        self.account.deposit(100)






