class RangeDescriptor:
    def __init__(self, min_v, max_v):
        self.min = min_v
        self.max = max_v

    def __set__(self, instance, value):
        if self.min < value < self.max:
            self.price = value
        else:
            raise ValueError(f"Price must be between {self.min} and {self.max}")


class Product:
    price = RangeDescriptor(20, 600)
    def __init__(self, name, price):
        self.name = name
        self.product_price = price



# p1 = Product("box", 30)
# p1.price = 50
# print(p1.name)
# print(p1.product_price)
# p1.price = 650

