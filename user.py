class User:

    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name, self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

Michael = User('Michael Stinko', 'mystink@email.stench')
Anna = User('Anna Banana', 'abanana@fruity.com')
Beef = User('Beef Testosterone', 'btest@meat.net')
Bonk = User('Bonk on the Head', 'bonk@bonk.bonk')

Beef.make_deposit(42)
Beef.make_deposit(20)
Beef.make_deposit(8)
Beef.make_withdrawal(10)
Beef.display_user_balance()
Bonk.make_deposit(1000)
Bonk.make_withdrawal(100)
Bonk.make_withdrawal(8)
Bonk.make_withdrawal(25)
Bonk.display_user_balance()
Bonk.transfer_money(Beef, 300)
Beef.display_user_balance()
Bonk.display_user_balance()