# Create a Bank Account in class which includes customer balance, day wise transactions, can transfer 
# money to different person account, interest given to him with a specific percentage



class BankAccount:
    def __init__(self, customer_name, initial_balance=0):
        self.customer_name = customer_name
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: {amount}")
        else:
            print("Insufficient balance.")
    
    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Transfer to {recipient}: {amount}")
            recipient.deposit(amount)
        else:
            print("Insufficient balance.")
    
    def calculate_interest(self, interest_rate):
        interest = self.balance * (interest_rate / 100)
        self.balance += interest
        self.transactions.append(f"Interest: {interest}")
    
    def print_transactions(self):
        print(f"Transaction history for {self.customer_name}:")
        for transaction in self.transactions:
            print(transaction)
    
    def print_balance(self):
        print(f"Current balance for {self.customer_name}: {self.balance}")


account1 = BankAccount("John Doe", 1000)
account2 = BankAccount("Jane Smith", 500)

account1.deposit(500)
account1.withdraw(200)
account1.transfer(300, account2)
account1.calculate_interest(2.5)

account1.print_balance()
account1.print_transactions()

account2.print_balance()
account2.print_transactions()
