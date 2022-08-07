class Bank:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("Amount Deposited:",amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("In You Withdrew:", amount)
        else:
            print(" Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
S= Bank()
S.deposit()
S.withdraw()
S.display()