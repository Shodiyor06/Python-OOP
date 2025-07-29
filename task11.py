class Book:
    def __init__(self, title, author, is_read):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print(f"{self.title} kitobi o'qildi.")
    def status(self):
        if self.is_read:
            print(f"{self.title} kitobi o'qilgan.")
        else:
            print(f"{self.title} kitobi hali o'qilmagan.")
book1 = Book("Yulduzlar ostida", "O'tkir Hoshimov", False)
book1.mark_as_read()
book1.status()