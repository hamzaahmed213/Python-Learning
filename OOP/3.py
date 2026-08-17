# Create a BankAccount class with:

# name
# balance

# Create methods:

# deposit(amount)
# withdraw(amount)
# display_balance()

class bankaccount:
    def __init__(self, name, balance = 0):
        self.name = name 
        self.balance = balance
    
    def deposit(self, amount):
        print(f"Amount Deposit:{amount}")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not Insuffient Balance")
        else:
            print(f"Amount Withdrawn: {amount}")
            self.balance -= amount

    def display_balance(self):
        print(f"Balance is: {self.balance}")




print("Welcome To Our Bank")
name = input("Enter Your Name: ")
account = bankaccount(name)
while True:
    choice = int(input("Choose:\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit\n"))
    if choice == 1:
        amount = int(input("Enter The Amount"))
        account.deposit(amount)
    elif choice == 2:
        amount = int(input("Enter The Amount"))
        account.withdraw(amount)
    elif choice == 3:
        account.display_balance()
    elif choice == 4:
        print("Thank you for banking with us!")
        break
    else:
        print("invalid choice")
       