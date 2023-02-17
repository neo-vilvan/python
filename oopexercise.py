import tkinter as tk

class Bank:
    def __init__(self):
        self.customers = []

    def create_customer(self, name, age, address):
        customer = Customer(name, age, address)
        self.customers.append(customer)

    def create_account(self, index):
        self.customers[index].create_account()

    def deposit(self, index, amount):
        self.customers[index].deposit(amount)

    def withdraw(self, index, amount):
        self.customers[index].withdraw(amount)

    def get_balance(self, index):
        return self.customers[index].get_balance()

class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.accounts = [Account()]

    def create_account(self):
        account = Account()
        self.accounts.append(account)

    def deposit(self, amount):
        self.accounts[0].deposit(amount)

    def withdraw(self, amount):
        self.accounts[0].withdraw(amount)

    def get_balance(self):
        return self.accounts[0].balance

class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

class BankGUI:
    def __init__(self, master):
        self.bank = Bank()

        self.master = master
        master.title("Bank Application")

        self.create_customer_button = tk.Button(master, text="Create Customer", command=self.create_customer)
        self.create_customer_button.pack()

        self.customer_index_label = tk.Label(master, text="Customer Index:")
        self.customer_index_label.pack()
        self.customer_index_entry = tk.Entry(master)
        self.customer_index_entry.pack()

        self.create_account_button = tk.Button(master, text="Create Account", command=self.create_account)
        self.create_account_button.pack()

        self.deposit_label = tk.Label(master, text="Deposit Amount:")
        self.deposit_label.pack()
        self.deposit_entry = tk.Entry(master)
        self.deposit_entry.pack()

        self.deposit_button = tk.Button(master, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_label = tk.Label(master, text="Withdrawal Amount:")
        self.withdraw_label.pack()
        self.withdraw_entry = tk.Entry(master)
        self.withdraw_entry.pack()

        self.withdraw_button = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.balance_button = tk.Button(master, text="Check Balance", command=self.check_balance)
        self.balance_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def create_customer(self):
        self.customer_window = tk.Toplevel(self.master)

        self.name_label = tk.Label(self.customer_window, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.customer_window)
        self.name_entry.pack()

        self.age_label = tk.Label(self.customer_window, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self.customer_window)
        self.age_entry.pack()

        self.address_label = tk.Label(self.customer_window, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(self.customer_window)
        self.address_entry.pack()

        self.submit_button = tk.Button(self.customer_window
