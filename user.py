class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, deposit):
        self.balance += deposit
        return self
    def make_withdrawal(self, withdrawal):
        self.balance -= withdrawal
        return self
    def display_user_balance(self):
        return self.balance

    def transfer_money(self, payee, amount):
        self.make_withdrawal(amount)
        payee.make_deposit(amount)

monty = User('monty')
guido = User('guido')
python = User('python')

monty.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(100)

print(monty.display_user_balance())     # 50

guido.make_deposit(50).make_deposit(50).make_withdrawal(100).make_withdrawal(100)

print(guido.display_user_balance())     # -100

python.make_deposit(50).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100)

print(python.display_user_balance())    # -250

monty.transfer_money(python, 50)

print(monty.display_user_balance())     # 50 - 50 = 0
print(python.display_user_balance())    # -250 + 50 = -200
