class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance > amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("Account has a negative balance")
        return self

    @classmethod
    def all_account_info(cls):
        for account in cls.all_accounts:
            print(f"Account Balance: {account.balance}")




account1 = BankAccount(0.02, 20)
account2 = BankAccount(0.01)

account1.deposit(30).deposit(5).deposit(15).withdraw(20).yield_interest().display_account_info()
account2.deposit(50).deposit(2).withdraw(30).withdraw(2).withdraw(15).withdraw(15).yield_interest().display_account_info()


BankAccount.all_account_info()