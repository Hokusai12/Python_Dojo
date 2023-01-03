class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance):
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




class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
        self.accounts.update({"0": BankAccount(0.02, 0)})

    def make_account(self, balance, int_rate = 0.01):
        self.accounts.update({str(len(self.accounts)): BankAccount(int_rate, balance)})
        print(f"New account {str(len(self.accounts) - 1)} created with a starting balance of {balance} and interest rate of {int_rate} for {self.name}")
        return self

    def make_deposit(self, amount, account):
        self.accounts[account].deposit(amount)
        return self

    def make_withdrawal(self, amount, account):
        self.accounts[account].withdraw(amount)
        return self

    def display_user_balance(self):
        for account in self.accounts:
            print(f"Account {account} Balance: {self.accounts[account].balance}")

    def transfer_money(self, amount, other_user):
        print(f"Transfer of {amount} beginning from {self.name} to {other_user.name}")
        for account in self.accounts:
            if self.accounts[account].balance > amount:
                self.accounts[account].withdraw(amount)
                other_user.accounts["0"].deposit(amount)
                return True
        print("Not enough funds available to complete transfer request")
        return False



user1 = User("Jessica Day", "jess.day@email.com")
user2 = User("Wallace Gromit", "wallaceandgromit@email.com")

user2.make_deposit(200, "0")
user1.transfer_money(300, user2)

print(user1.name)
user1.display_user_balance()
print(user2.name)
user2.display_user_balance()

user1.make_account(400, 0.02).make_deposit(20, "1").transfer_money(225, user2)

print(user1.name)
user1.display_user_balance()
print(user2.name)
user2.display_user_balance()