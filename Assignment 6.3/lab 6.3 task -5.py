class BankAccount:
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

# User input to create account
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
account = BankAccount(name, account_number)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid option. Please try again.")