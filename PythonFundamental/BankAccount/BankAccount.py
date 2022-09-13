class BankAccount:
    def __init__(self, int_rate=.08, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self

    def displayAccountInfo(self):
        print(f"Balance: ${self.balance}")

    def yieldInterest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
       
        return self


account1 = BankAccount()
account1.displayAccountInfo()


account1.deposit(100).deposit(50).deposit(70).withdraw(
    100).yieldInterest().displayAccountInfo()



account2 = BankAccount()
account2.displayAccountInfo()   

account2.deposit(100).deposit(30).withdraw(50).withdraw(20).withdraw(
    50).withdraw(40).yieldInterest().displayAccountInfo()