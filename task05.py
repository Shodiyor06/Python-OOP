class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

product1 = Product("Laptop", 1500, "Electronics", True)
product2 = Product("Chair", 85, "Furniture", True)  
product3 = Product("Notebook", 3, "Stationery", False)
print(product1.name)
print(product1.price)
print(product1.category)
print(product1.in_stock)

print(product2.name)
print(product2.price)
print(product2.category)
print(product2.in_stock)

print(product3.name)
print(product3.price)
print(product3.category)
print(product3.in_stock)