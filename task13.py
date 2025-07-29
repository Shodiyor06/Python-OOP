class Book:
    def __init__(self, title, author, is_read):
        self.title = title
        self.author = author
        self.is_read = is_read
    def mark_as_read(self):
        pass
    def status(self):
        if self.is_read:
            print(f"{self.title} kitobi o'qilgan.")
        else:
            print(f"{self.title} kitobi hali o'qilmagan.")
book1 = Book("Yulduzlar ostida", "O'tkir Hoshimov", False)
book2 = Book("O'tgan kunlar", "Abdulla Qodiriy", True)
book3 = Book("Alisher Navoiy", "Abdurauf Fitrat", False)
book4 = Book("Shum bola", "O'tkir Hoshimov", True)
book1.status()
book2.status()
book3.status()
book4.status()