# Create a parent class BankAccount with account_holder and balance attributes. Add deposit(amount) and 
# withdraw(amount) methods to add and remove money from the account.
# Create a child class SavingsAccount that inherits from BankAccount and has an additional
# interest_rate attribute. Add an add_interest() method that increases the balance according to
# the interest rate. Use super() where appropriate.

class bankaccount:
    def __init__(self):
        self.name = "Hamza Ahmed" 
        self.balance = 10000 
        


    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} Is Credited in Your Account")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance -= amount
            print(f"{amount} is debited from your account")

class savingsacc(bankaccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 5
    def add_interest(self):
        interest = self.balance* (self.interest_rate / 100)
        self.balance += interest

        print(f"Balance after interest is {self.balance}")

acc = savingsacc()
acc.deposit(50000)
acc.withdraw(39000)
acc.deposit(1200)
acc.withdraw(5000)

acc.add_interest()
