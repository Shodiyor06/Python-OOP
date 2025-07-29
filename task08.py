class Product:

    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
    def show_in_stock(self):
        if self.in_stock:
            print(f'{self.name} omborda mavjud')
        else:
            print("mavjud emas")
meva = Product('olma', 13000, 'meva', True)
meva.show_in_stock()