class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm qo'shildi. Joriy balans: {self.balance} so'm.")
        else:
            print("Iltimos, musbat summani kiriting.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Joriy balans: {self.balance} so'm.")
        else:
            print("Yechildi operatsiyasi amalga oshmadi. Balans yetarli emas yoki noto'g'ri summa kiritildi.")
    def show_balance(self):
        print(f"Hisobingizdagi joriy balans: {self.balance} so'm.")
bank1 = Bank("Ali", 100000)
bank2 = Bank("Vali", 200000)
bank3 = Bank("Salim", 30000)
bank1.deposit(50000)
bank1.withdraw(20000)
bank1.show_balance()
bank2.deposit(10000)
bank2.withdraw(15000)
bank2.show_balance()
bank3.deposit(1000)
bank3.withdraw(5000)
bank3.show_balance()