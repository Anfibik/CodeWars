"""https://www.codewars.com/kata/5a03af9606d5b65ff7000009/train/python"""


class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, money):
        if money > self.balance:
            raise ValueError()
        self.balance -= money
        return f"{self.name} has {self.balance}."

    def check(self, user_name, vol_money):
        if user_name.checking_account and user_name.balance > vol_money:
            self.balance += vol_money
            user_name.balance -= vol_money
            return f"{self.name} has {self.balance} and {user_name.name} has {user_name.balance}."
        raise ValueError()

    def add_cash(self, vol_cash):
        self.balance += vol_cash
        return f"{self.name} has {self.balance}."


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

print(Jeff.withdraw(50))
print(Joe.check(Jeff, 50))
print(Jeff.check(Joe, 80))
print(Joe.checking_account)
print(Jeff.check(Joe, 80))
print(Joe.check(Jeff, 100))
print(Jeff.add_cash(20.00))