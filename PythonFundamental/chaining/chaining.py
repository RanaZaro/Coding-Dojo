class User:		# declare a class and give it name User
    def __init__(self,name,email,amount):
        self.name = name
        self.email = "email"
        self.account_balance =amount
    def make_withdrawal(self, amount):
        self.account_balance= self.account_balance-amount
        return self
        
    def display_user_balance(self):
        print(self.name,self.account_balance)
    def transfer_money(self, other_user, amount):
        other_user.account_balance=other_user.account_balance+amount
        self.account_balance=self.account_balance-amount
        return self
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

rana=User("rana","rana.com",1000)
dana=User("dana","rana.com",50)
thabet=User("thabet","rana.com",500)
#2

rana.display_user_balance()
rana.make_deposit(50).make_deposit(100)
rana.make_withdrawal(100).make_withdrawal(100)

#3


dana.display_user_balance()
dana.make_withdrawal(20).make_withdrawal(30)

#4

thabet.display_user_balance()
dana.transfer_money(thabet,100).transfer_money(rana,10)







