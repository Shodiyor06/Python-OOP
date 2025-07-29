class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} balansi: {self.balance}")

    def get_balance(self):
        return self.balance

acc1 = BankAccount("Ali", 1200)
acc2 = BankAccount("Laylo", 850)
acc3 = BankAccount("Shodiyor", 2000)
acc4 = BankAccount("Kamola", 450)
acc5 = BankAccount("Anvar", 1750)

accounts = [acc1, acc2, acc3, acc4, acc5]

total = 0
for acc in accounts:
    total += acc.get_balance()

print(f"Jami balans: {total}")
