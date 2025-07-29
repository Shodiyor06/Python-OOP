class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        if self.is_read:
            print(f"{self.title} — Oqilgan")
        else:
            print(f"{self.title} — Oqilmagan")

book1 = Book("Alkimyogar", "Paulo Coelho")
book2 = Book("Otkan kunlar", "Abdulla Qodiriy")
book3 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev")
book4 = Book("Hayvonlar fermasi", "George Orwell")
book5 = Book("Qor", "Orhan Pamuk")

books = [book1, book2, book3, book4, book5]

book2.mark_as_read()
book4.mark_as_read()

print(" Barcha kitoblar holati:")
for book in books:
    book.status()

print("\n Oqilgan kitoblar:")
for book in books:
    if book.is_read:
        print(book.title)
