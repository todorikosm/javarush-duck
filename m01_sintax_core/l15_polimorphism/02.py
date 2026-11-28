class Product:
    all = []
    total_discount = 25

    @classmethod
    def total_price(cls):
        # cls.all и Product.cls - это одно и то же
        return sum([p.get_price() * p.quantity for p in cls.all])

    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount
        self.quantity = 4
        Product.all.append(self)

    def get_price(self):
        discount = max(Product.total_discount, self.discount)
        return round(self.price * (1 - discount / 100), 2)

    def __str__(self):
        return self.name


product_1 = Product("велосипед", 100000, 30)
product_2 = Product("ролики", 30000, 25)
product_3 = Product("лыжи", 45000, 20)

print(*Product.all)
print(Product.total_price())
