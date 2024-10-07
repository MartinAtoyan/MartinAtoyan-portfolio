from abc import ABC, abstractmethod


class Order(ABC):
    __slots__ = ("customer", "menu_items")

    def __init__(self, customer, menu_items):
        self.customer = customer
        self.menu_items = menu_items

    @abstractmethod
    def calculate_total_price(self):
        pass

    def get_total_price(self):
        return self.calculate_total_price()

    def __str__(self):
        return f"Customer: {self.customer}, Total Price: ${self.get_total_price():.2f}"


class DineInOrder(Order):
    __slots__ = ("table_number", )

    def __init__(self, customer, menu_items, table_number):
        super().__init__(customer, menu_items)
        self.table_number = table_number

    def calculate_total_price(self):
        base_price = 0
        for item in self.menu_items:
            base_price += item['price']
        service_charge = base_price * 0.1
        return base_price + service_charge

    def __str__(self):
        return f"{super().__str__()}, Table Number: {self.table_number}"




class TakeawayOrder(Order):
    __slots__ = ()

    def calculate_total_price(self):
        total_price = 0
        for item in self.menu_items:
            total_price += item['price']
        return total_price

    def __str__(self):
        return f"{super().__str__()} (Takeaway)"



class DeliveryOrder(Order):
    __slots__ = ("delivery_address", "delivery_fee")

    def __init__(self, customer, menu_items, delivery_address, delivery_fee):
        super().__init__(customer, menu_items)
        self.delivery_address = delivery_address
        self.delivery_fee = delivery_fee

    def calculate_total_price(self):
        base_price = 0
        for item in self.menu_items:
            base_price += item['price']
        return base_price + self.delivery_fee

    def __str__(self):
        return f"{super().__str__()}, Delivery Address: {self.delivery_address}, Delivery Fee: ${self.delivery_fee:.2f}"



if __name__ == "__main__":
    menu_items = [{'name': 'Pizza', 'price': 12.99}, {'name': 'Soda', 'price': 2.50}]

    dine_in_order = DineInOrder('James Doe', menu_items, 5)
    print(dine_in_order)

    takeaway_order = TakeawayOrder('Jane Doe', menu_items)
    print(takeaway_order)

    delivery_order = DeliveryOrder('Alice', menu_items, '123 Main St', 5.00)
    print(delivery_order)
