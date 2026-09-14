class insufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.amount=amount
        self.balance=amount+self.balance
        return f"Your account is credited with {amount}. your is new balance is {self.balance}."
    def withdraw(self,amount):
        if amount>self.balance:
            raise insufficientFundsError(f"The {amount} cannot be withdrawn, Available balance {self.balance}")
        self.balance=self.balance-amount
        return f"Your account is Debited with {amount}. your is new balance is {self.balance}"

#---------------------------------------concept 2 (inheritance)----------------------------------------------
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)   # runs BankAccount's __init__ first
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance
        

# account=BankAccount("Darshan",100)
saving=SavingsAccount("Darshan",100,0.05)
print(saving.owner)
print(saving.deposit(100))
try:
    print(saving.withdraw(5000))
except insufficientFundsError as e:
    print(f"Transaction failed: {e}")

print(saving.add_interest())