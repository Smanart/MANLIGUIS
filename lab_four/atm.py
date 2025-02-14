class Customer:
    def __init__(self, name: str, pin: str, account_number: str):
        self.name = name
        self.pin = pin
        self.account_number = account_number

    def __str__(self):
        return f"Customer: {self.name}, Account: {self.account_number}"

class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account: {self.account_number}, Balance: {self.balance}"

class BankServer:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: BankAccount):
        self.accounts[account.account_number] = account

    def get_account(self, account_number: str):
        return self.accounts.get(account_number)

    def __str__(self):
        return f"BankServer with {len(self.accounts)} accounts"

class ATM:
    def __init__(self, bank_server: BankServer):
        self.bank_server = bank_server

    def authenticate(self, customer: Customer):
        account = self.bank_server.get_account(customer.account_number)
        if account and customer.pin == "8877":
            return account
        return None

    def display_menu(self):
        print("Welcome to ATM!")
        print("Click 1: Check Balance")
        print("Click 2: Withdraw")
        print("Click 3: Deposit")
        print("Click 4: Exit")

    def withdraw(self, account: BankAccount, amount: float):
        if account.withdraw(amount):
            print(f"Withdrawal successful. Current Balance: {account.get_balance()}")
        else:
            print("Insufficient funds or invalid amount.")

    def deposit(self, account: BankAccount, amount: float):
        if account.deposit(amount):
            print(f"Deposit successful. Current Balance: {account.get_balance()}")
        else:
            print("Invalid deposit amount.")

    def main(self):
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        account_number = input("Enter your account number: ")

        customer = Customer(name, pin, account_number)
        account = self.authenticate(customer)

        if not account:
            print("Authentication failed. Invalid PIN or account number.")
            return

        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Your balance: {account.get_balance()}")
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(account, amount)
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                self.deposit(account, amount)
            elif choice == "4":
                print("Exiting ATM. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":

    bank_server = BankServer()

    bank_account = BankAccount("12345678", 10000)
    bank_server.add_account(bank_account)

    atm = ATM(bank_server)

    atm.main()