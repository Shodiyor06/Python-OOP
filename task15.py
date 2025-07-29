class Product:

    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
    
p1 = Product('olma', 13000, 'meva', True)
p2 = Product('banan', 12000, 'meva', False)
p3 = Product('kartoshka', 8000, 'sabzavot', True)
p4 = Product('pomidor', 10000, 'sabzavot', True)
p5 = Product('qovoq', 15000, 'sabzavot', False)
p6 = Product('uzum', 20000, 'meva', True)

products = [p1, p2, p3, p4, p5, p6]

total = 0
for product in products:
    if product.in_stock:
        total += product.price

print(f"Ombordagi mahsulotlar narxi: {total:.2f}")
