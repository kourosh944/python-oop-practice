class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        print("The deposit has been made.")
        
    def add_interest(self):
        self.balance = self.balance + (self.balance * self.interest_rate)

KB = SavingsAccount("kourosh",1000,0.1)
KB.deposit(200)
KB.add_interest()
print(KB.balance)
