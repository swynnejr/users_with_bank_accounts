class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account.deposit(100)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawl(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print(self.account.balance)
        print(self.name)

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # self.name = User

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if self.balance < amount:
            print("We took $5 that you don't even have.")
            self.balance -= (amount + 5)
            return self
        else:
            self.balance -= amount
            return self


    def display_account_info(self):
        print(f'Your balance is: {self.balance}')


    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self