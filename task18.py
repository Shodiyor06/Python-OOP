class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"{self.name} — {self.price} so'm")

p1 = Product("Noutbuk", 9500000, "Elektronika")
p2 = Product("Kamera", 4200000, "Foto")
p3 = Product("Kreslo", 1700000, "Mebel")
p4 = Product("Telefon", 6800000, "Elektronika")
p5 = Product("Kiyim", 750000, "Moda")
p6 = Product("Sovutkich", 5100000, "Maishiy texnika")

products = [p1, p2, p3, p4, p5, p6]

most_expensive = products[0]
for product in products:
    if product.price > most_expensive.price:
        most_expensive = product

print(" Eng qimmat mahsulot:")
most_expensive.info()
