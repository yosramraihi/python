class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdram(self,amount):
        if((self.balance - amount) >=0) :
           self.balance -=amount
        else:
           print(f"insufficinent funds: charging 5 free")
           self.balance -=5
        return self
    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self
    def interest(self):
        if self.balance>0 :
            self.balance +=(self.balance * self.int_rate)
        return self 


account=BankAccount(.05,1000)
account2=BankAccount(.02,5000)

account.deposit(10).deposit(20).deposit(40).withdram(600).interest().display_account_info()
account2.deposit(100).deposit(200).deposit(400).withdram(60).interest().display_account_info()
