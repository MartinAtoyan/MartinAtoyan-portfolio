class Product:
    def __init__(self, product_id: int, product_name: str, quantity_in_stock: int):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def set_product_id(self, product_id: int):
        self.__product_id = product_id

    def set_product_name(self, product_name: str):
        self.__product_name = product_name

    def set_product_quantity(self, quantity: int):
        self.__quantity_in_stock = quantity

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_product_quantity(self):
        return self.__quantity_in_stock

    def add_to_stock(self, quantity):
        if quantity >= 1:
            self.__quantity_in_stock += quantity

    def reduce_stock(self, quantity):
        if 0 < quantity <= self.__quantity_in_stock:
            self.__quantity_in_stock -= quantity



