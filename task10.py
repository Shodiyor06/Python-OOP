class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        amount = float(input("Mablag' kiriting: "))
        self.balance += amount
        print(f"{amount} so'm hisobingizga qo'shildi. Jami balans: {self.balance} so'm")

    def withdraw(self):
        amount = float(input("Mablag' yechib oling: "))
        if amount > self.balance:
            print("Balansdan ko'p mablag' yechib bo'lmaydi.")
        else:
            self.balance -= amount
            print(f"{amount} so'm hisobingizdan yechildi. Jami balans: {self.balance} so'm")

bank1 = BankAccount("Ali", 100000)
bank1.deposit()
bank1.withdraw()
print(f"Hisob egasi: {bank1.owner}, Jami balans: {bank1.balance} so'm")